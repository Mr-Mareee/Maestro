# insecure direct object references

> insecure direct object references (idor) is a security vulnerability that occurs when an application allows users to directly access or modify objects (such as files, database records, or urls) based on user-supplied input, without sufficient access controls. this means that if a user changes a parameter value (like an id) in a url or api request, they might be able to access or manipulate data that they aren’t authorized to see or modify.


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [numeric value parameter](#numeric-value-parameter)
    * [common identifiers parameter](#common-identifiers-parameter) 
    * [weak pseudo random number generator](#weak-pseudo-random-number-generator) 
    * [hashed parameter](#hashed-parameter)
    * [wildcard parameter](#wildcard-parameter)
    * [idor tips](#idor-tips)
* [labs](#labs)
* [references](#references)


## tools

- [portswigger/bapp store > authz](https://portswigger.net/bappstore/4316cc18ac5f434884b2089831c7d19e)
- [portswigger/bapp store > authmatrix](https://portswigger.net/bappstore/30d8ee9f40c041b0bfec67441aad158e)
- [portswigger/bapp store > autorize](https://portswigger.net/bappstore/f9bbac8c4acf4aefa4d7dc92a991af2f)


## methodology

idor stands for insecure direct object reference. it's a type of security vulnerability that arises when an application provides direct access to objects based on user-supplied input. as a result, attackers can bypass authorization and access resources in the system directly, potentially leading to unauthorized information disclosure, modification, or deletion.

**example of idor**

imagine a web application that allows users to view their profile by clicking a link `https://example.com/profile?user_id=123`:

```php
<?php
    $user_id = $_get['user_id'];
    $user_info = get_user_info($user_id);
    ...
```

here, `user_id=123` is a direct reference to a specific user's profile. if the application doesn't properly check that the logged-in user has the right to view the profile associated with `user_id=123`, an attacker could simply change the `user_id` parameter to view other users' profiles:

```ps1
https://example.com/profile?user_id=124
```


[image extracted text: [image not found]]



### numeric value parameter

increment and decrement these values to access sensitive information.

* decimal value: `287789`, `287790`, `287791`, ...
* hexadecimal: `0x4642d`, `0x4642e`, `0x4642f`, ...
* unix epoch timestamp: `1695574808`, `1695575098`, ...

**examples** 

* [hackerone - idor to view user order information - meals](https://hackerone.com/reports/287789)
* [hackerone - delete messages via idor - naaash](https://hackerone.com/reports/697412)

### common identifiers parameter

some identifiers can be guessed like names and emails, they might grant you access to customer data.

* name: `john`, `doe`, `john.doe`, ...
* email: `john.doe@mail.com`
* base64 encoded value: `am9obi5kb2vabwfpbc5jb20=`

**examples** 

* [hackerone - insecure direct object reference (idor) - delete campaigns - datph4m](https://hackerone.com/reports/1969141)


### weak pseudo random number generator

* uuid/guid v1 can be predicted if you know the time they were created: `95f6e264-bb00-11ec-8833-00155d01ef00`
* mongodb object ids are generated in a predictable manner: `5ae9b90a2c144b9def01ec37`
    * a 4-byte value representing the seconds since the unix epoch
    * a 3-byte machine identifier
    * a 2-byte process id
    * a 3-byte counter, starting with a random value

**examples** 

* [hackerone - idor allowing to read another user's token on the social media ads service - a_d_a_m](https://hackerone.com/reports/1464168)
* [idor through mongodb object ids prediction](https://techkranti.com/idor-through-mongodb-object-ids-prediction/)


### hashed parameter

sometimes we see websites using hashed values to generate a random user id or token, like `sha1(username)`, `md5(email)`, ...

* md5: `098f6bcd4621d373cade4e832627b4f6`
* sha1: `a94a8fe5ccb19ba61c4c0873d391e987982fbbd3`
* sha2: `9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08`

**examples** 

* [idor with predictable hmac generation - dicectf 2022 - cryptocat](https://youtu.be/og5_5teg6m0)


### wildcard parameter

send a wildcard (`*`, `%`, `.`, `_`) instead of an id, some backend might respond with the data of all the users.

* `get /api/users/* http/1.1`
* `get /api/users/% http/1.1`
* `get /api/users/_ http/1.1`
* `get /api/users/. http/1.1`


**examples** 

* [todo](#)


### idor tips

* change the http request: `post → put`
* change the content type: `xml → json`
* transform numerical values to arrays: `{"id":19} → {"id":[19]}`
* use parameter pollution: `user_id=hacker_id&user_id=victim_id`


## labs

- [portswigger - insecure direct object references](https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references)


## references

- [from christmas present in the blockchain to massive bug bounty - jesse lakerveld - march 21, 2018](http://web.archive.org/web/20180401130129/https://www.vicompany.nl/magazine/from-christmas-present-in-the-blockchain-to-massive-bug-bounty)
- [how-to: find idor (insecure direct object reference) vulnerabilities for large bounty rewards - sam houton - november 9, 2017](https://www.bugcrowd.com/blog/how-to-find-idor-insecure-direct-object-reference-vulnerabilities-for-large-bounty-rewards/)
- [hunting insecure direct object reference vulnerabilities for fun and profit (part-1) - mohammed abdul raheem - february 2, 2018](https://codeburst.io/hunting-insecure-direct-object-reference-vulnerabilities-for-fun-and-profit-part-1-f338c6a52782)
- [idor - how to predict an identifier? bug bounty case study - bug bounty reports explained - september 21, 2023](https://youtu.be/wx5tws0dres)
- [insecure direct object reference prevention cheat sheet - owasp - july 31, 2023](https://www.owasp.org/index.php/insecure_direct_object_reference_prevention_cheat_sheet)
- [insecure direct object references (idor) - portswigger - december 25, 2019](https://portswigger.net/web-security/access-control/idor)
- [testing for idors - portswigger - october 29, 2024](https://portswigger.net/burp/documentation/desktop/testing-workflow/access-controls/testing-for-idors)
- [testing for insecure direct object references (otg-authz-004) - owasp - august 8, 2014](https://www.owasp.org/index.php/testing_for_insecure_direct_object_references_(otg-authz-004))
- [the rise of idor - hackerone - april 2, 2021](https://www.hackerone.com/company-news/rise-idor)
- [web to app phone notification idor to view everyone's airbnb messages - brett buerhaus - march 31, 2017](http://buer.haus/2017/03/31/airbnb-web-to-app-phone-notification-idor-to-view-everyones-airbnb-messages/)