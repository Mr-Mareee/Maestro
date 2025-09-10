# bazaar

> bazaar  (also known as bzr ) is a free, distributed version control system (dvcs) that helps you track project history over time and collaborate seamlessly with others. developed by canonical, bazaar emphasizes ease of use, a flexible workflow, and rich features to cater to both individual developers and large teams.


## summary

* [tools](#tools)
    * [rip-bzr.pl](#rip-bzrpl)
    * [bzr_dumper](#bzr_dumper)
* [references](#references)


## tools

### rip-bzr.pl

* [kost/dvcs-ripper/rip-bzr.pl](https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-bzr.pl)
    ```powershell
    docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper rip-bzr.pl -v -u
    ```

### bzr_dumper

* [seahunoh/bzr_dumper](https://github.com/seahunoh/bzr_dumper)

```powershell
python3 dumper.py -u "http://127.0.0.1:5000/" -o source
created a standalone tree (format: 2a)
[!] target : http://127.0.0.1:5000/
[+] start.
[+] get repository/pack-names
[+] get readme
[+] get checkout/dirstate
[+] get checkout/views
[+] get branch/branch.conf
[+] get branch/format
[+] get branch/last-revision
[+] get branch/tag
[+] get b'154411f0f33adc3ff8cfb3d34209cbd1'
[*] finish
```

```powershell
bzr revert
 n  application.py
 n  database.py
 n  static/
```

## references

- [stem ctf cyber challenge 2019 – my first blog - m3ssap0 / zuzzur3ll0n1 - march 2, 2019](https://ctftime.org/writeup/13380)