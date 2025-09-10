# http parameter pollution

> http parameter pollution (hpp) is a web attack evasion technique that allows an attacker to craft a http request in order to manipulate web logics or retrieve hidden information. this evasion technique is based on splitting an attack vector between multiple instances of a parameter with the same name (?param1=value&param1=value). as there is no formal way of parsing http parameters, individual web technologies have their own unique way of parsing and reading url parameters with the same name. some taking the first occurrence, some taking the last occurrence, and some reading it as an array. this behavior is abused by the attacker in order to bypass pattern-based security mechanisms. 

## summary

* [tools](#tools)
* [methodology](#methodology)
    * [parameter pollution table](#parameter-pollution-table)
    * [parameter pollution payloads](#parameter-pollution-payloads)
* [references](#references)


## tools

* **burp suite**: manually modify requests to test duplicate parameters.
* **owasp zap**: intercept and manipulate http parameters.


## methodology

http parameter pollution (hpp) is a web security vulnerability where an attacker injects multiple instances of the same http parameter into a request. the server's behavior when processing duplicate parameters can vary, potentially leading to unexpected or exploitable behavior.

hpp can target two levels:

* client-side hpp: exploits javascript code running on the client (browser).
* server-side hpp: exploits how the server processes multiple parameters with the same name.


**examples**:

```ps1
/app?debug=false&debug=true
/transfer?amount=1&amount=5000
```


### parameter pollution table

when ?par1=a&par1=b

| technology                                      | parsing result           | outcome (par1=) |
| ----------------------------------------------- | ------------------------ | --------------- |
| asp.net/iis                                     | all occurrences          | a,b             |
| asp/iis                                         | all occurrences          | a,b             |
| golang net/http - `r.url.query().get("param")`  | first occurrence         | a               |
| golang net/http - `r.url.query()["param"]`      | all occurrences in array | ['a','b']       |
| ibm http server                                 | first occurrence         | a               |
| ibm lotus domino                                | first occurrence         | a               |
| jsp,servlet/tomcat                              | first occurrence         | a               |
| mod_wsgi (python)/apache                        | first occurrence         | a               |
| nodejs                                          | all occurrences          | a,b             |
| perl cgi/apache                                 | first occurrence         | a               |
| perl cgi/apache                                 | first occurrence         | a               |
| php/apache                                      | last occurrence          | b               |
| php/zues                                        | last occurrence          | b               |
| python django                                   | last occurrence          | b               |
| python flask                                    | first occurrence         | a               |
| python/zope                                     | all occurrences in array | ['a','b']       |
| ruby on rails                                   | last occurrence          | b               |


### parameter pollution payloads

* duplicate parameters:
    ```ps1
    param=value1&param=value2
    ```

* array injection:
    ```ps1
    param[]=value1
    param[]=value1&param[]=value2
    param[]=value1&param=value2
    param=value1&param[]=value2
    ```

* encoded injection:
    ```ps1
    param=value1%26other=value2
    ```

* nested injection:
    ```ps1
    param[key1]=value1&param[key2]=value2
    ```

* json injection:
    ```ps1
    {
        "test": "user",
        "test": "admin"
    }
    ```


## references

- [how to detect http parameter pollution attacks - acunetix - january 9, 2024](https://www.acunetix.com/blog/whitepaper-http-parameter-pollution/)
- [http parameter pollution - itamar verta - december 20, 2023](https://www.imperva.com/learn/application-security/http-parameter-pollution/)
- [http parameter pollution in 11 minutes - pwnfunction - january 28, 2019](https://www.youtube.com/watch?v=qvzbl8yxvx0&ab_channel=pwnfunction)