# mfa bypasses

> multi-factor authentication (mfa) is a security measure that requires users to provide two or more verification factors to gain access to a system, application, or network. it combines something the user knows (like a password), something they have (like a phone or security token), and/or something they are (biometric verification). this layered approach enhances security by making unauthorized access more difficult, even if a password is compromised.
> mfa bypasses are techniques attackers use to circumvent mfa protections. these methods can include exploiting weaknesses in mfa implementations, intercepting authentication tokens, leveraging social engineering to manipulate users or support staff, or exploiting session-based vulnerabilities.

## summary

* [response manipulation](#response-manipulation)
* [status code manipulation](#status-code-manipulation)
* [2fa code leakage in response](#2fa-code-leakage-in-response)
* [js file analysis](#js-file-analysis)
* [2fa code reusability](#2fa-code-reusability)
* [lack of brute-force protection](#lack-of-brute-force-protection)
* [missing 2fa code integrity validation](#missing-2fa-code-integrity-validation)
* [csrf on 2fa disabling](#csrf-on-2fa-disabling)
* [password reset disable 2fa](#password-reset-disable-2fa)
* [backup code abuse](#backup-code-abuse)
* [clickjacking on 2fa disabling page](#clickjacking-on-2fa-disabling-page)
* [enabling 2fa doesn't expire previously active sessions](#enabling-2fa-doesnt-expire-previously-active-sessions)
* [bypass 2fa by force browsing](#bypass-2fa-by-force-browsing)
* [bypass 2fa with null or 000000](#bypass-2fa-with-null-or-000000)
* [bypass 2fa with array](#bypass-2fa-with-array)

## 2fa bypasses

### response manipulation

in response if `"success":false`
change it to `"success":true`

### status code manipulation

if status code is **4xx**
try to change it to **200 ok** and see if it bypass restrictions

### 2fa code leakage in response

check the response of the 2fa code triggering request to see if the code is leaked.

### js file analysis

rare but some js files may contain info about the 2fa code, worth giving a shot

### 2fa code reusability

same code can be reused

### lack of brute-force protection

possible to brute-force any length 2fa code

### missing 2fa code integrity validation

code for any user acc can be used to bypass the 2fa

### csrf on 2fa disabling

no csrf protection on disabling 2fa, also there is no auth confirmation

### password reset disable 2fa

2fa gets disabled on password change/email change

### backup code abuse

bypassing 2fa by abusing the backup code feature
use the above mentioned techniques to bypass backup code to remove/reset 2fa restrictions

### clickjacking on 2fa disabling page

iframing the 2fa disabling page and social engineering victim to disable the 2fa

### enabling 2fa doesn't expire previously active sessions

if the session is already hijacked and there is a session timeout vuln

### bypass 2fa by force browsing

if the application redirects to `/my-account` url upon login while 2fa is disabled, try replacing `/2fa/verify` with `/my-account` while 2fa is enabled to bypass verification.

### bypass 2fa with null or 000000

enter the code **000000** or **null** to bypass 2fa protection.

### bypass 2fa with array

```json
{
    "otp":[
        "1234",
        "1111",
        "1337", // good otp
        "2222",
        "3333",
        "4444",
        "5555"
    ]
}
```
