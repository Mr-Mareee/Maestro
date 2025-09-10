# regular expression

> regular expression denial of service (redos) is a type of attack that exploits the fact that certain regular expressions can take an extremely long time to process, causing applications or services to become unresponsive or crash. 


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [evil regex](#evil-regex)
    * [backtrack limit](#backtrack-limit)
* [references](#references)


## tools

* [tjenkinson/redos-detector](https://github.com/tjenkinson/redos-detector) - a cli and library which tests with certainty if a regex pattern is safe from redos attacks. supported in the browser, node and deno.
* [doyensec/regexploit](https://github.com/doyensec/regexploit) - find regular expressions which are vulnerable to redos (regular expression denial of service)
* [devina.io/redos-checker](https://devina.io/redos-checker) - examine regular expressions for potential denial of service vulnerabilities


## methodology

### evil regex

evil regex contains:

* grouping with repetition
* inside the repeated group:
    * repetition
    * alternation with overlapping

**examples**

* `(a+)+`
* `([a-za-z]+)*`
* `(a|aa)+`
* `(a|a?)+`
* `(.*a){x}` for x \> 10

these regular expressions can be exploited with `aaaaaaaaaaaaaaaaaaaaaaaa!` (20 'a's followed by a '!').

```ps1
aaaaaaaaaaaaaaaaaaaa! 
```

for this input, the regex engine will try all possible ways to group the `a` characters before realizing that the match ultimately fails because of the `!`. this results in an explosion of backtracking attempts.


### backtrack limit

backtracking in regular expressions occurs when the regex engine tries to match a pattern and encounters a mismatch. the engine then backtracks to the previous matching position and tries an alternative path to find a match. this process can be repeated many times, especially with complex patterns and large input strings.  

**php pcre configuration options**

| name                 | default | note |
|----------------------|---------|---------|
| pcre.backtrack_limit | 1000000 | 100000 for `php < 5.3.7`|
| pcre.recursion_limit | 100000  | / |
| pcre.jit             | 1       | / |


sometimes it is possible to force the regex to exceed more than 100 000 recursions which will cause a redos and make `preg_match` returning false:

```php
$pattern = '/(a+)+$/';
$subject = str_repeat('a', 1000) . 'b';

if (preg_match($pattern, $subject)) {
    echo "match found";
} else {
    echo "no match";
}
```


## references

- [intigriti challenge 1223 - hackbook of a hacker - december 21, 2023](https://simones-organization-4.gitbook.io/hackbook-of-a-hacker/ctf-writeups/intigriti-challenges/1223)
- [mybb admin panel rce cve-2023-41362 - sorceryie - september 11, 2023](https://blog.sorcery.ie/posts/mybb_acp_rce/)
- [owasp validation regex repository - owasp - march 14, 2018](https://wiki.owasp.org/index.php/owasp_validation_regex_repository)
- [pcre > installing/configuring - php manual - may 3, 2008](https://www.php.net/manual/en/pcre.configuration.php#ini.pcre.recursion-limit)
- [regular expression denial of service - redos - adar weidman - december 4, 2019](https://owasp.org/www-community/attacks/regular_expression_denial_of_service_-_redos)