# server side template injection - asp.net

> server-side template injection (ssti)  is a class of vulnerabilities where an attacker can inject malicious input into a server-side template, causing the template engine to execute arbitrary code on the server. in the context of asp.net, ssti can occur if user input is directly embedded into a template (such as razor, aspx, or other templating engines) without proper sanitization. 


## summary

- [asp.net razor](#aspnet-razor)
    - [asp.net razor - basic injection](#aspnet-razor---basic-injection)
    - [asp.net razor - command execution](#aspnet-razor---command-execution)
- [references](#references)


## asp.net razor

[official website](https://docs.microsoft.com/en-us/aspnet/web-pages/overview/getting-started/introducing-razor-syntax-c)

> razor is a markup syntax that lets you embed server-based code (visual basic and c#) into web pages.


### asp.net razor - basic injection

```powershell
@(1+2)
```

### asp.net razor - command execution

```csharp
@{
  // c# code
}
```


## references

- [server-side template injection (ssti) in asp.net razor - clément notin - april 15, 2020](https://clement.notin.org/blog/2020/04/15/server-side-template-injection-(ssti)-in-asp.net-razor/)