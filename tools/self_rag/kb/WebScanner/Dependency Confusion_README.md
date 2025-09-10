# dependency confusion

> a dependency confusion attack or supply chain substitution attack occurs when a software installer script is tricked into pulling a malicious code file from a public repository instead of the intended file of the same name from an internal repository.

## summary

* [tools](#tools)
* [methodology](#methodology)
    * [npm example](#npm-example)
* [references](#references)


## tools

* [visma-prodsec/confused](https://github.com/visma-prodsec/confused) - tool to check for dependency confusion vulnerabilities in multiple package management systems
* [synacktiv/depfuzzer](https://github.com/synacktiv/depfuzzer) - tool used to find dependency confusion or project where owner's email can be takeover.


## methodology

look for `npm`, `pip`, `gem` packages, the methodology is the same : you register a public package with the same name of private one used by the company and then you wait for it to be used.

* dockerhub: dockerfile image
* javascript (npm): package.json
* mvn (maven): pom.xml
* php (composer): composer.json
* python (pypi): requirements.txt

### npm example

* list all the packages (ie: package.json, composer.json, ...)
* find the package missing from https://www.npmjs.com/
* register and create a **public** package with the same name
    * package example : https://github.com/0xsapra/dependency-confusion-expoit


## references

- [exploiting dependency confusion - aman sapra (0xsapra) - 2 jul 2021](https://0xsapra.github.io/website//exploiting-dependency-confusion)
- [dependency confusion: how i hacked into apple, microsoft and dozens of other companies - alex birsan - 9 feb 2021](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)
- [3 ways to mitigate risk when using private package feeds - microsoft - 29/03/2021](https://web.archive.org/web/20210210121930/https://azure.microsoft.com/en-gb/resources/3-ways-to-mitigate-risk-using-private-package-feeds/)
- [$130,000+ learn new hacking technique in 2021 - dependency confusion - bug bounty reports explained - 22 févr. 2021](https://www.youtube.com/watch?v=zfhjwehpbru)