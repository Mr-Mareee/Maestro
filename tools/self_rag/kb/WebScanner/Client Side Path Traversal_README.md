# client side path traversal

> client-side path traversal (cspt), sometimes also referred to as "on-site request forgery," is a vulnerability that can be exploited as a tool for csrf or xss attacks.  

> it takes advantage of the client side's ability to make requests using fetch to a url, where multiple "../" characters can be injected. after normalization, these characters redirect the request to a different url, potentially leading to security breaches.  

> since every request is initiated from within the frontend of the application, the browser automatically includes cookies and other authentication mechanisms, making them available for exploitation in these attacks.


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [cspt to xss](#cspt-to-xss)
    * [cspt to csrf](#cspt-to-xss)
* [labs](#labs)
* [references](#references)


## tools

* [doyensec/csptburpextension](https://github.com/doyensec/csptburpextension) - cspt is an open-source burp suite extension to find and exploit client-side path traversal.


## methodology

### cspt to xss


[image extracted text: [image not found]]


a post-serving page calls the fetch function, sending a request to a url with attacker-controlled input which is not properly encoded in its path, allowing the attacker to inject `../` sequences to the path and make the request get sent to an arbitrary endpoint. this behavior is referred to as a cspt vulnerability.

**example**:

* the page `https://example.com/static/cms/news.html` takes a `newsitemid` as parameter
* then fetch the content of `https://example.com/newitems/<newsitemid>`
* a text injection was also discovered in `https://example.com/pricing/default.js` via the `cb` parameter
* final payload is `https://example.com/static/cms/news.html?newsitemid=../pricing/default.js?cb=alert(document.domain)//`


### cspt to csrf

a cspt is redirecting legitimate http requests, allowing the front end to add necessary tokens for api calls, such as authentication or csrf tokens. this capability can potentially be exploited to circumvent existing csrf protection measures.

|                                             | csrf               | cspt2csrf          |
| ------------------------------------------- | -----------------  | ------------------ |
| post csrf ?                                 | :white_check_mark: | :white_check_mark: |
| can control the body ?                      | :white_check_mark: | :x:                |
| can work with anti-csrf token ?             | :x:                | :white_check_mark: |
| can work with samesite=lax ?                | :x:                | :white_check_mark: |
| get / patch / put / delete csrf ?           | :x:                | :white_check_mark: |
| 1-click csrf ?                              | :x:                | :white_check_mark: |
| does impact depend on source and on sinks ? | :x:                | :white_check_mark: |


real-world scenarios:

* 1-click cspt2csrf in rocket.chat
* cve-2023-45316: cspt2csrf with a post sink in mattermost : `/<team>/channels/channelname?telem_action=under_control&forcerhsopen&telem_run_id=../../../../../../api/v4/caches/invalidate`
* cve-2023-6458: cspt2csrf with a get sink in mattermost
* [client side path manipulation - erasec.be](https://www.erasec.be/blog/client-side-path-manipulation/): cspt2csrf `https://example.com/signup/invite?email=foo%40bar.com&invitecode=123456789/../../../cards/123e4567-e89b-42d3-a456-556642440000/cancel?a=`
* [cve-2023-5123 : cspt2csrf in grafana’s json api plugin](https://medium.com/@maxime.escourbiac/grafana-cve-2023-5123-write-up-74e1be7ef652) 


## labs

* [doyensec/csptplayground](https://github.com/doyensec/csptplayground) - csptplayground is an open-source playground to find and exploit client-side path traversal (cspt).
* [root me - cspt - the ruler](https://www.root-me.org/en/challenges/web-client/cspt-the-ruler)


## references

- [exploiting client-side path traversal to perform cross-site request forgery - introducing cspt2csrf - maxence schmitt - 02 jul 2024](https://blog.doyensec.com/2024/07/02/cspt2csrf.html)
- [exploiting client-side path traversal - csrf is dead, long live csrf - whitepaper - maxence schmitt - 02 jul 2024](https://www.doyensec.com/resources/doyensec_cspt2csrf_whitepaper.pdf)
- [exploiting client-side path traversal - csrf is dead, long live csrf - owasp global appsec 2024 - maxence schmitt - june 24 2024](https://www.doyensec.com/resources/doyensec_cspt2csrf_owasp_appsec_lisbon.pdf)
- [leaking jupyter instance auth token chaining cve-2023-39968, cve-2024-22421 and a chromium bug - davwwwx - 30-08-2023](https://blog.xss.am/2023/08/cve-2023-39968-jupyter-token-leak/)
- [on-site request forgery - dafydd stuttard - 03 may 2007](https://portswigger.net/blog/on-site-request-forgery)
- [bypassing wafs to exploit cspt using encoding levels - matan berson - 2024-05-10](https://matanber.com/blog/cspt-levels)
- [automating client-side path traversals discovery - vitor falcao - october 3, 2024](https://vitorfalcao.com/posts/automating-cspt-discovery/)
- [cspt the eval villain way! - dennis goodlett - december 3, 2024](https://blog.doyensec.com/2024/12/03/cspt-with-eval-villain.html)
- [bypassing file upload restrictions to exploit client-side path traversal - maxence schmitt - january 9, 2025](https://blog.doyensec.com/2025/01/09/cspt-file-upload.html)