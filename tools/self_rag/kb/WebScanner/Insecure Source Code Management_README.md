# insecure source code management

> insecure source code management (scm) can lead to several critical vulnerabilities in web applications and services. developers often rely on scm systems like git and subversion (svn) to manage their source code versions. however, poor security practices, such as leaving .git and .svn folders in production environments exposed to the internet, can pose significant risks. 


## summary

* [methodology](#methodology)
    * [bazaar](./bazaar.md)
    * [git](./git.md)
    * [mercurial](./mercurial.md)
    * [subversion](./subversion.md)
* [labs](#labs)
* [references](#references)


## methodology

exposing the version control system folders on a web server can lead to severe security risks, including: 

- **source code leaks** : attackers can download the entire source code repository, gaining access to the application's logic.
- **sensitive information exposure** : embedded secrets, configuration files, and credentials might be present within the codebase.
- **commit history exposure** : attackers can view past changes, revealing sensitive information that might have been previously exposed and later mitigated.
     

the first step is to gather information about the target application. this can be done using various web reconnaissance tools and techniques. 

* **manual inspection** : check urls manually by navigating to common scm paths.
    * http://target.com/.git/
    * http://target.com/.svn/

* **automated tools** : refer to the page related to the specific technology.

once a potential scm folder is identified, check the http response codes and contents. you might need to bypass `.htaccess` or reverse proxy rules.

the nginx rule below returns a `403 (forbidden)` response instead of `404 (not found)` when hitting the `/.git` endpoint.

```ps1
location /.git {
  deny all;
}
```

for example in git, the exploitation technique doesn't require to list the content of the `.git` folder (http://target.com/.git/), the data extraction can still be conducted when files can be read.


## labs

* [root me - insecure code management](https://www.root-me.org/fr/challenges/web-serveur/insecure-code-management)


## references

- [hidden directories and files as a source of sensitive information about web application - apr 30, 2017](https://github.com/bl4de/research/tree/master/hidden_directories_leaks)