# dns rebinding

> dns rebinding changes the ip address of an attacker controlled machine name to the ip address of a target application, bypassing the [same-origin policy](https://developer.mozilla.org/en-us/docs/web/security/same-origin_policy) and thus allowing the browser to make arbitrary requests to the target application and read their responses.

## summary

* [tools](#tools)
* [methodology](#methodology)
* [protection bypasses](#protection-bypasses)
    * [0.0.0.0](#0000)
    * [cname](#cname)
    * [localhost](#localhost)
* [references](#references)


## tools

- [nccgroup/singularity](https://github.com/nccgroup/singularity) - a dns rebinding attack framework. 
- [rebind.it](http://rebind.it/) - singularity of origin web client.
- [taviso/rbndr](https://github.com/taviso/rbndr) - simple dns rebinding service
- [taviso/rebinder](https://lock.cmpxchg8b.com/rebinder.html) - rbndr tool helper


## methodology

**setup phase**:

* register a malicious domain (e.g., `malicious.com`).
* configure a custom dns server capable of resolving `malicious.com` to different ip addresses.

**initial victim interaction**:

* create a webpage on `malicious.com` containing malicious javascript or another exploit mechanism.
* entice the victim to visit the malicious webpage (e.g., via phishing, social engineering, or advertisements).

**initial dns resolution**:

* when the victim's browser accesses `malicious.com`, it queries the attacker's dns server for the ip address.
* the dns server resolves `malicious.com` to an initial, legitimate-looking ip address (e.g., 203.0.113.1).

**rebinding to internal ip**:

* after the browser's initial request, the attacker's dns server updates the resolution for `malicious.com` to a private or internal ip address (e.g., 192.168.1.1, corresponding to the victim’s router or other internal devices).

this is often achieved by setting a very short ttl (time-to-live) for the initial dns response, forcing the browser to re-resolve the domain.

**same-origin exploitation:**

the browser treats subsequent responses as coming from the same origin (`malicious.com`).

malicious javascript running in the victim's browser can now make requests to internal ip addresses or local services (e.g., 192.168.1.1 or 127.0.0.1), bypassing same-origin policy restrictions.


**example:**

1. register a domain.
2. [setup singularity of origin](https://github.com/nccgroup/singularity/wiki/setup-and-installation).
3. edit the [autoattack html page](https://github.com/nccgroup/singularity/blob/master/html/autoattack.html) for your needs.
4. browse to "http://rebinder.your.domain:8080/autoattack.html".
5. wait for the attack to finish (it can take few seconds/minutes).


## protection bypasses

> most dns protections are implemented in the form of blocking dns responses containing unwanted ip addresses at the perimeter, when dns responses enter the internal network. the most common form of protection is to block private ip addresses as defined in rfc 1918 (i.e. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). some tools allow to additionally block localhost (127.0.0.0/8), local (internal) networks, or 0.0.0.0/0 network ranges.

in the case where dns protection are enabled (generally disabled by default), ncc group has documented multiple [dns protection bypasses](https://github.com/nccgroup/singularity/wiki/protection-bypasses) that can be used.

### 0.0.0.0

we can use the ip address 0.0.0.0 to access the localhost (127.0.0.1) to bypass filters blocking dns responses containing 127.0.0.1 or 127.0.0.0/8.

### cname

we can use dns cname records to bypass a dns protection solution that blocks all internal ip addresses.
since our response will only return a cname of an internal server,
the rule filtering internal ip addresses will not be applied.
then, the local, internal dns server will resolve the cname.

```bash
$ dig cname.example.com +noall +answer
; <<>> dig 9.11.3-1ubuntu1.15-ubuntu <<>> example.com +noall +answer
;; global options: +cmd
cname.example.com.            381     in      cname   target.local.
```

### localhost

we can use "localhost" as a dns cname record to bypass filters blocking dns responses containing 127.0.0.1.

```bash
$ dig www.example.com +noall +answer
; <<>> dig 9.11.3-1ubuntu1.15-ubuntu <<>> example.com +noall +answer
;; global options: +cmd
localhost.example.com.            381     in      cname   localhost.
```


## references

- [how do dns rebinding attacks work? - nccgroup - apr 9, 2019](https://github.com/nccgroup/singularity/wiki/how-do-dns-rebinding-attacks-work%3f)
