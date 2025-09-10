# contributing

payloadsallthethings' team :heart: pull requests.

feel free to improve with your payloads and techniques !

you can also contribute with a :beers: irl, or using the [sponsor](https://github.com/sponsors/swisskyrepo) button.

## pull requests guidelines

in order to provide the safest payloads for the community, the following rules must be followed for **every** pull request.

- payloads must be sanitized
    - use `id`, and `whoami`, for rce proof of concepts
    - use `[redacted]` when the user has to replace a domain for a callback. e.g: xsshunter, burpcollaborator etc.
    - use `10.10.10.10` and `10.10.10.11` when the payload require ip addresses
    - use `administrator` for privileged users and `user` for normal account
    - use `p@ssw0rd`, `password123`, `password` as default passwords for your examples
    - prefer commonly used name for machines such as `dc01`, `exchange01`, `workstation01`, etc
- references must have an `author`, a `title`, a `link` and a `date`
    - use [wayback machine](wayback.archive.org) if the reference is not available anymore.
    - the date must be following the format `month number, year`, e.g: `december 25, 2024`
    - references to github repositories must follow this format: `[author/tool](https://github.com/url) - description`

every pull request will be checked with `markdownlint` to ensure consistent writing and markdown best practices. you can validate your files locally using the following docker command:

```ps1
docker run -v $pwd:/workdir davidanson/markdownlint-cli2:v0.15.0 "**/*.md" --config .github/.markdownlint.json --fix
```

## techniques folder

every section should contains the following files, you can use the `_template_vuln` folder to create a new technique folder:

- **readme.md**: vulnerability description and how to exploit it, including several payloads, more below
- **intruder**: a set of files to give to burp intruder
- **images**: pictures for the readme.md
- **files**: some files referenced in the readme.md

## readme.md format

use the example folder [_template_vuln/](https://github.com/swisskyrepo/payloadsallthethings/blob/master/_template_vuln/) to create a new vulnerability document. the main page is [readme.md](https://github.com/swisskyrepo/payloadsallthethings/blob/master/_template_vuln/readme.md). it is organized with sections for a title and description of the vulnerability, along with a summary table of contents linking to the main sections of the document.

- **tools**: lists relevant tools with links to their repositories and brief descriptions.
- **methodology**: provides a quick overview of the approach used, with code snippets to demonstrate exploitation steps.
- **labs**: references online platforms where similar vulnerabilities can be practiced, each with a link to the corresponding lab.
- **references**: lists external resources, such as blog posts or articles, providing additional context or case studies related to the vulnerability.
