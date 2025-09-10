# http hidden parameters

> web applications often have hidden or undocumented parameters that are not exposed in the user interface. fuzzing can help discover these parameters, which might be vulnerable to various attacks.


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [bruteforce parameters](#bruteforce-parameters)
    * [old parameters](#old-parameters)
* [references](#references)


## tools

* [portswigger/param-miner](https://github.com/portswigger/param-miner) - burp extension to identify hidden, unlinked parameters.
* [s0md3v/arjun](https://github.com/s0md3v/arjun) - http parameter discovery suite
* [sh1yo/x8](https://github.com/sh1yo/x8) - hidden parameters discovery suite
* [tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls) - fetch all the urls that the wayback machine knows about for a domain
* [devanshbatham/paramspider](https://github.com/devanshbatham/paramspider) - mining urls from dark corners of web archives for bug hunting/fuzzing/further probing


## methodology

### bruteforce parameters

* use wordlists of common parameters and send them, look for unexpected behavior from the backend. 
    ```ps1
    x8 -u "https://example.com/" -w <wordlist>
    x8 -u "https://example.com/" -x post -w <wordlist>
    ```

wordlist examples: 

- [arjun/large.txt](https://github.com/s0md3v/arjun/blob/master/arjun/db/large.txt)
- [arjun/medium.txt](https://github.com/s0md3v/arjun/blob/master/arjun/db/medium.txt)
- [arjun/small.txt](https://github.com/s0md3v/arjun/blob/master/arjun/db/small.txt)
- [samlists/sam-cc-parameters-lowercase-all.txt](https://github.com/the-xentropy/samlists/blob/main/sam-cc-parameters-lowercase-all.txt)
- [samlists/sam-cc-parameters-mixedcase-all.txt](https://github.com/the-xentropy/samlists/blob/main/sam-cc-parameters-mixedcase-all.txt)


### old parameters

explore all the url from your targets to find old parameters.

* browse the [wayback machine](http://web.archive.org/)
* look through the js files to discover unused parameters


## references

- [hacker tools: arjun – the parameter discovery tool - intigriti - may 17, 2021](https://blog.intigriti.com/2021/05/17/hacker-tools-arjun-the-parameter-discovery-tool/)
- [parameter discovery: a quick guide to start - yeswehack - april 20, 2022](http://web.archive.org/web/20220420123306/https://blog.yeswehack.com/yeswerhackers/parameter-discovery-quick-guide-to-start)