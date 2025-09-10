# zip slip

> the vulnerability is exploited using a specially crafted archive that holds directory traversal filenames (e.g. ../../shell.php). the zip slip vulnerability can affect numerous archive formats, including tar, jar, war, cpio, apk, rar and 7z. the attacker can then overwrite executable files and either invoke them remotely or wait for the system or user to call them, thus achieving remote command execution on the victim’s machine.

## summary

* [tools](#tools)
* [methodology](#methodology)
    * [additional notes](#additional-notes)
* [references](#references)


## tools

* [ptoomey3/evilarc](https://github.com/ptoomey3/evilarc) - create tar/zip archives that can exploit directory traversal vulnerabilities
* [usdag/slipit](https://github.com/usdag/slipit) - utility for creating zipslip archives


## methodology

the zip slip vulnerability is a critical security flaw that affects the handling of archive files, such as zip, tar, or other compressed file formats. this vulnerability allows an attacker to write arbitrary files outside of the intended extraction directory, potentially overwriting critical system files, executing malicious code, or gaining unauthorized access to sensitive information.

**example**: suppose an attacker creates a zip file with the following structure:

```
malicious.zip
  ├── ../../../../etc/passwd
  ├── ../../../../usr/local/bin/malicious_script.sh
```

when a vulnerable application extracts `malicious.zip`, the files are written to `/etc/passwd` and /`usr/local/bin/malicious_script.sh` instead of being contained within the extraction directory. this can have severe consequences, such as corrupting system files or executing malicious scripts.


* using [ptoomey3/evilarc](https://github.com/ptoomey3/evilarc):
    ```python
    python evilarc.py shell.php -o unix -f shell.zip -p var/www/html/ -d 15
    ```

* creating a zip archive containing a symbolic link:

    ```ps1
    ln -s ../../../index.php symindex.txt
    zip --symlinks test.zip symindex.txt
    ```

for a list of affected libraries and projects, visit [snyk/zip-slip-vulnerability](https://github.com/snyk/zip-slip-vulnerability)


## references

* [zip slip - snyk - june 5, 2018](https://github.com/snyk/zip-slip-vulnerability)
* [zip slip vulnerability - snyk - april 15, 2018](https://snyk.io/research/zip-slip-vulnerability)
