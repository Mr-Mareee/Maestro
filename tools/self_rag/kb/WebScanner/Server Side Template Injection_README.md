# server side template injection

> template injection allows an attacker to include template code into an existing (or not) template. a template engine makes designing html pages easier by using static template files which at runtime replaces variables/placeholders with actual values in the html pages


## summary

- [tools](#tools)
- [methodology](#methodology)
    - [identify the vulnerable input field](#identify-the-vulnerable-input-field)
    - [inject template syntax](#inject-template-syntax)
    - [enumerate the template engine](#enumerate-the-template-engine)
    - [escalate to code execution](#escalate-to-code-execution)
- [labs](#labs)
- [references](#references)


## tools

* [hackmanit/tinja](https://github.com/hackmanit/tinja) - an effiecient ssti + csti scanner which utilizes novel polyglots
  ```bash
  tinja url -u "http://example.com/?name=kirlia" -h "authentication: bearer ey..."
  tinja url -u "http://example.com/" -d "username=kirlia"  -c "phpsessid=abc123..."
  ```

* [epinna/tplmap](https://github.com/epinna/tplmap) - server-side template injection and code injection detection and exploitation tool
  ```powershell
  python2.7 ./tplmap.py -u 'http://www.target.com/page?name=john*' --os-shell
  python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=*&comment=supercomment&link"
  python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=injecthere*&comment=a&link" --level 5 -e jade
  ```

* [vladko312/sstimap](https://github.com/vladko312/sstimap) - automatic ssti detection tool with interactive interface based on [epinna/tplmap](https://github.com/epinna/tplmap)
  ```powershell
  python3 ./sstimap.py -u 'https://example.com/page?name=john' -s
  python3 ./sstimap.py -u 'https://example.com/page?name=vulnerable*&message=my_message' -l 5 -e jade
  python3 ./sstimap.py -i -a -m post -l 5 -h 'authorization: basic bg9naw46c2vjcmv0x3bhc3n3b3jk'
  ```


## methodology

### identify the vulnerable input field

the attacker first locates an input field, url parameter, or any user-controllable part of the application that is passed into a server-side template without proper sanitization or escaping. 

for example, the attacker might identify a web form, search bar, or template preview functionality that seems to return results based on dynamic user input.

**tip**: generated pdf files, invoices and emails usually use a template. 


### inject template syntax

the attacker tests the identified input field by injecting template syntax specific to the template engine in use. different web frameworks use different template engines (e.g., jinja2 for python, twig for php, or freemarker for java). 

common template expressions:

* `{{7*7}}` for jinja2 (python).
* `#{7*7}` for thymeleaf (java).

find more template expressions in the page dedicated to the technology (php, python, etc).


[image extracted text: [image not found]]


in most cases, this polyglot payload will trigger an error in presence of a ssti vulnerability:

```ps1
${{<%[%'"}}%\.
```

the [hackmanit/template injection table](https://github.com/hackmanit/template-injection-table) is an interactive table containing the most efficient template injection polyglots along with the expected responses of the 44 most important template engines.


### enumerate the template engine

based on the successful response, the attacker determines which template engine is being used. this step is critical because different template engines have different syntax, features, and potential for exploitation. the attacker may try different payloads to see which one executes, thereby identifying the engine.

* **python**: django, jinja2, mako, ...
* **java**: freemarker, jinjava, velocity, ...
* **ruby**: erb, slim, ...

[the post "template-engines-injection-101" from @0xawali](https://medium.com/@0xawali/template-engines-injection-101-4f2fe59e5756) summarize the syntax and detection method for most of the template engines for javascript, python, ruby, java and php and how to differentiate between engines that use the same syntax.


### escalate to code execution

once the template engine is identified, the attacker injects more complex expressions, aiming to execute server-side commands or arbitrary code. 


## labs

* [root me - java - server-side template injection](https://www.root-me.org/en/challenges/web-server/java-server-side-template-injection)
* [root me - python - server-side template injection introduction](https://www.root-me.org/en/challenges/web-server/python-server-side-template-injection-introduction)
* [root me - python - blind ssti filters bypass](https://www.root-me.org/en/challenges/web-server/python-blind-ssti-filters-bypass)


## references

- [a pentester's guide to server side template injection (ssti) - busra demir - december 24, 2020](https://www.cobalt.io/blog/a-pentesters-guide-to-server-side-template-injection-ssti)
- [gaining shell using server side template injection (ssti) - david valles - august 22, 2018](https://medium.com/@david.valles/gaining-shell-using-server-side-template-injection-ssti-81e29bb8e0f9)
- [template engines injection 101 - mahmoud m. awali - november 1, 2024](https://medium.com/@0xawali/template-engines-injection-101-4f2fe59e5756)
- [template injection on hardened targets - lucas 'bitk' philippe - september 28, 2022](https://youtu.be/m0b_ka0omfw)