# web cache deception

> web cache deception (wcd) is a security vulnerability that occurs when a web server or caching proxy misinterprets a client's request for a web resource and subsequently serves a different resource, which may often be more sensitive or private, after caching it.


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [caching sensitive data](#caching-sensitive-data)
    * [caching custom javascript](#caching-custom-javascript)
* [cloudflare caching](#cloudflare-caching)
* [labs](#labs)
* [references](#references)


## tools

* [portswigger/param-miner](https://github.com/portswigger/param-miner) - web cache poisoning burp extension


## methodology

example of web cache deception: 

imagine an attacker lures a logged-in victim into accessing `http://www.example.com/home.php/non-existent.css`

1. the victim's browser requests the resource `http://www.example.com/home.php/non-existent.css`
2. the requested resource is searched for in the cache server, but it's not found (resource not in cache). 
3. the request is then forwarded to the main server. 
4. the main server returns the content of `http://www.example.com/home.php`, most probably with http caching headers that instruct not to cache this page. 
5. the response passes through the cache server. 
6. the cache server identifies that the file has a css extension. 
7. under the cache directory, the cache server creates a directory named home.php and caches the imposter "css" file (non-existent.css) inside it. 
8. when the attacker requests `http://www.example.com/home.php/non-existent.css`, the request is sent to the cache server, and the cache server returns the cached file with the victim's sensitive `home.php` data.


[image extracted text: victim
exa_
get
http:iiwwwexample comhhome
hplnon-existent.css
content of http:ilwww example comlhome-php
proxy server
main server
php
attacker
get
http: ilwwwexample: =
comhome ,
content =
'phplnon-=
http ilwww.€
existentcss
mple.
comlhomephp
-existentcss
phplnon-
omlhome 
comhome.
xample -
example:
http: ilwww
http: ilwww
get
of victim'$
conte !]



### caching sensitive data

**example 1** - web cache deception on paypal home page

1. normal browsing, visit home : `https://www.example.com/myaccount/home/`
2. open the malicious link : `https://www.example.com/myaccount/home/malicious.css`
3. the page is displayed as /home and the cache is saving the page
4. open a private tab with the previous url : `https://www.example.com/myaccount/home/malicious.css`
5. the content of the cache is displayed

video of the attack by omer gil - web cache deception attack in paypal home page
[
[image extracted text: [image not found]]
](https://vimeo.com/249130093)

**example 2** - web cache deception on openai

1. attacker crafts a dedicated .css path of the `/api/auth/session` endpoint.
2. attacker distributes the link
3. victims visit the legitimate link.
4. response is cached.
5. attacker harvests jwt credentials.


### caching custom javascript

1. find an un-keyed input for a cache poisoning
    ```js
    values: user-agent
    values: cookie
    header: x-forwarded-host
    header: x-host
    header: x-forwarded-server
    header: x-forwarded-scheme (header; also in combination with x-forwarded-host)
    header: x-original-url (symfony)
    header: x-rewrite-url (symfony)
    ```
2. cache poisoning attack - example for `x-forwarded-host` un-keyed input (remember to use a buster to only cache this webpage instead of the main page of the website)
    ```js
    get /test?buster=123 http/1.1
    host: target.com
    x-forwarded-host: test"><script>alert(1)</script>

    http/1.1 200 ok
    cache-control: public, no-cache
    [..]
    <meta property="og:image" content="https://test"><script>alert(1)</script>">
    ```


## tricks

the following url format are a good starting point to check for "cache" feature.

* `https://example.com/app/conversation/.js?test`
* `https://example.com/app/conversation/;.js`
* `https://example.com/home.php/non-existent.css`


## cloudflare caching

cloudflare caches the resource when the `cache-control` header is set to `public` and `max-age` is greater than 0. 

- the cloudflare cdn does not cache html by default
- cloudflare only caches based on file extension and not by mime type: [cloudflare/default-cache-behavior](https://developers.cloudflare.com/cache/about/default-cache-behavior/)


in cloudflare cdn, one can implement a `cache deception armor`, it is not enabled by default.
when the `cache deception armor` is enabled, the rule will verify a url's extension matches the returned `content-type`.

cloudflare has a list of default extensions that gets cached behind their load balancers.

|       |      |      |      |      |       |      |
|-------|------|------|------|------|-------|------|
| 7z    | csv  | gif  | midi | png  | tif   | zip  |
| avi   | doc  | gz   | mkv  | ppt  | tiff  | zst  |
| avif  | docx | ico  | mp3  | pptx | ttf   | css  |
| apk   | dmg  | iso  | mp4  | ps   | webm  | flac |
| bin   | ejs  | jar  | ogg  | rar  | webp  | mid  |
| bmp   | eot  | jpg  | otf  | svg  | woff  | pls  |
| bz2   | eps  | jpeg | pdf  | svgz | woff2 | tar  |
| class | exe  | js   | pict | swf  | xls   | xlsx |


exceptions and bypasses:

* if the returned content-type is application/octet-stream, the extension does not matter because that is typically a signal to instruct the browser to save the asset instead of to display it.
* cloudflare allows .jpg to be served as image/webp or .gif as video/webm and other cases that we think are unlikely to be attacks.
* [bypassing cache deception armor using .avif extension file - fixed](https://hackerone.com/reports/1391635)


## labs 

* [portswigger labs for web cache deception](https://portswigger.net/web-security/all-labs#web-cache-poisoning)


## references

- [cache deception armor - cloudflare - may 20, 2023](https://developers.cloudflare.com/cache/cache-security/cache-deception-armor/)
- [exploiting cache design flaws - portswigger - may 4, 2020](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws)
- [exploiting cache implementation flaws - portswigger - may 4, 2020](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws)
- [how i test for web cache vulnerabilities + tips and tricks - bombon (0xbxmbn) - july 21, 2022](https://bxmbn.medium.com/how-i-test-for-web-cache-vulnerabilities-tips-and-tricks-9b138da08ff9)
- [openai account takeover - nagli (@naglinagli) - march 24, 2023](https://twitter.com/naglinagli/status/1639343866313601024)
- [practical web cache poisoning - james kettle (@albinowax) - august 9, 2018](https://portswigger.net/blog/practical-web-cache-poisoning)
- [shockwave identifies web cache deception and account takeover vulnerability affecting openai's chatgpt - nagli (@naglinagli) - july 15, 2024](https://www.shockwave.cloud/blog/shockwave-works-with-openai-to-fix-critical-chatgpt-vulnerability)
- [web cache deception attack - omer gil - february 27, 2017](http://omergil.blogspot.fr/2017/02/web-cache-deception-attack.html)
- [web cache deception attack leads to user info disclosure - kunal pandey (@kunal94) - february 25, 2019](https://medium.com/@kunal94/web-cache-deception-attack-leads-to-user-info-disclosure-805318f7bb29)
- [web cache entanglement: novel pathways to poisoning - james kettle (@albinowax) - august 5, 2020](https://portswigger.net/research/web-cache-entanglement)
- [web cache poisoning - portswigger - may 4, 2020](https://portswigger.net/web-security/web-cache-poisoning)