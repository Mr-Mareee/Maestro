# google web toolkit

> google web toolkit (gwt), also known as gwt web toolkit, is an open-source set of tools that allows web developers to create and maintain javascript front-end applications using java. it was originally developed by google and had its initial release on may 16, 2006.


## summary

* [tools](#tools)
* [methodology](#methodology)
* [references](#references)


## tools

* [fsecurelabs/gwtmap](https://github.com/fsecurelabs/gwtmap) - gwtmap is a tool to help map the attack surface of google web toolkit (gwt) based applications. 
* [gdssecurity/gwt-penetration-testing-toolset](https://github.com/gdssecurity/gwt-penetration-testing-toolset) - a set of tools made to assist in penetration testing gwt applications. 


## methodology

* enumerate the methods of a remote application via it's bootstrap file and create a local backup of the code (selects permutation at random):
    ```ps1
    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js --backup
    ```
* enumerate the methods of a remote application via a specific code permutation
    ```ps1
    ./gwtmap.py -u http://10.10.10.10/olympian/c39ab19b83398a76a21e0cd04ec9b14c.cache.js
    ```
* enumerate the methods whilst routing traffic through an http proxy:
    ```ps1
    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js --backup -p http://127.0.0.1:8080
    ```
* enumerate the methods of a local copy (a file) of any given permutation:
    ```ps1
    ./gwtmap.py -f test_data/olympian/c39ab19b83398a76a21e0cd04ec9b14c.cache.js
    ```
* filter output to a specific service or method: 
    ```ps1
    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js --filter authenticationservice.login
    ```
* generate rpc payloads for all methods of the filtered service, with coloured output
    ```ps1
    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js --filter authenticationservice --rpc --color
    ```
* automatically test (probe) the generate rpc request for the filtered service method
    ```ps1
    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js --filter authenticationservice.login --rpc --probe
    ./gwtmap.py -u http://10.10.10.10/olympian/olympian.nocache.js --filter testservice.testdetails --rpc --probe
    ```


## references

- [from serialized to shell :: exploiting google web toolkit with el injection - stevent seeley - may 22, 2017](https://srcincite.io/blog/2017/05/22/from-serialized-to-shell-auditing-google-web-toolkit-with-el-injection.html)
- [hacking a google web toolkit application - thehackerish - april 22, 2021](https://thehackerish.com/hacking-a-google-web-toolkit-application/)