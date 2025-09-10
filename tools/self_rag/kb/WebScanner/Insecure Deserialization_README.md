# insecure deserialization

> serialization is the process of turning some object into a data format that can be restored later. people often serialize objects in order to save them to storage, or to send as part of communications. deserialization is the reverse of that process -- taking data structured from some format, and rebuilding it into an object - owasp


## summary

* [deserialization identifier](#deserialization-identifier)
* [pop gadgets](#pop-gadgets)
* [labs](#labs)
* [references](#references)


## deserialization identifier

check the following sub-sections, located in other chapters :

* [java deserialization : ysoserial, ...](java.md)
* [php (object injection) : phpggc, ...](php.md)
* [ruby : universal rce gadget, ...](ruby.md)
* [python : pickle, ...](python.md)
* [yaml : pyyaml, ...](yaml.md)
* [.net : ysoserial.net, ...](dotnet.md)

| object type     | header (hex) | header (base64) |
|-----------------|--------------|-----------------|
| java serialized | ac ed        | ro              |
| .net viewstate  | ff 01        | /w              |
| python pickle   | 80 04 95     | gasv            |
| php serialized  | 4f 3a        | tz              |


## pop gadgets

> a pop (property oriented programming) gadget is a piece of code implemented by an application's class, that can be called during the deserialization process.

pop gadgets characteristics:
* can be serialized
* has public/accessible properties
* implements specific vulnerable methods
* has access to other "callable" classes


## labs

* [portswigger - modifying serialized objects](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-modifying-serialized-objects)
* [portswigger - modifying serialized data types](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-modifying-serialized-data-types)
* [portswigger - using application functionality to exploit insecure deserialization](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-using-application-functionality-to-exploit-insecure-deserialization)
* [portswigger - arbitrary object injection in php](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-arbitrary-object-injection-in-php)
* [portswigger - exploiting java deserialization with apache commons](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-exploiting-java-deserialization-with-apache-commons)
* [portswigger - exploiting php deserialization with a pre-built gadget chain](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-exploiting-php-deserialization-with-a-pre-built-gadget-chain)
* [portswigger - exploiting ruby deserialization using a documented gadget chain](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-exploiting-ruby-deserialization-using-a-documented-gadget-chain)
* [portswigger - developing a custom gadget chain for java deserialization](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-developing-a-custom-gadget-chain-for-java-deserialization)
* [portswigger - developing a custom gadget chain for php deserialization](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-developing-a-custom-gadget-chain-for-php-deserialization)
* [portswigger - using phar deserialization to deploy a custom gadget chain](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-using-phar-deserialization-to-deploy-a-custom-gadget-chain)
* [nickstadb - deserlab](https://github.com/nickstadb/deserlab)


## references

- [exploitdb introduction - abdelazim mohammed(@intx0x80) - may 27, 2018](https://www.exploit-db.com/docs/english/44756-deserialization-vulnerability.pdf)
- [exploiting insecure deserialization vulnerabilities - portswigger - july 25, 2020](https://portswigger.net/web-security/deserialization/exploiting)
- [instagram's million dollar bug - wesley wineberg - december 17, 2015](http://www.exfiltrated.com/research-instagram-rce.php)