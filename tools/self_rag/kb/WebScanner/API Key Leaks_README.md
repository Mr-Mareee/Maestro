# api key and token leaks

> api keys and tokens are forms of authentication commonly used to manage permissions and access to both public and private services. leaking these sensitive pieces of data can lead to unauthorized access, compromised security, and potential data breaches.

## summary

- [tools](#tools)
- [methodology](#methodology)
    - [common causes of leaks](#common-causes-of-leaks)
    - [validate the api key](#validate-the-api-key)
- [reducing the attack surface](#reducing-the-attack-surface)
- [references](#references)

## tools

- [aquasecurity/trivy](https://github.com/aquasecurity/trivy) - general purpose vulnerability and misconfiguration scanner which also searches for api keys/secrets
- [blacklanternsecurity/badsecrets](https://github.com/blacklanternsecurity/badsecrets) - a library for detecting known or weak secrets on across many platforms
- [d0ge/sign-saboteur](https://github.com/d0ge/sign-saboteur) - signsaboteur is a burp suite extension for editing, signing, verifying various signed web tokens
- [mazen160/secrets-patterns-db](https://github.com/mazen160/secrets-patterns-db) - secrets patterns db: the largest open-source database for detecting secrets, api keys, passwords, tokens, and more.
- [momenbasel/keyfinder](https://github.com/momenbasel/keyfinder) - is a tool that let you find keys while surfing the web
- [streaak/keyhacks](https://github.com/streaak/keyhacks) - is a repository which shows quick ways in which api keys leaked by a bug bounty program can be checked to see if they're valid
- [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) - find credentials all over the place
- [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates) - use these templates to test an api token against many api service endpoints

    ```powershell
    nuclei -t token-spray/ -var token=token_list.txt
    ```

## methodology

- **api keys**: unique identifiers used to authenticate requests associated with your project or application.
- **tokens**: security tokens (like oauth tokens) that grant access to protected resources.

### common causes of leaks

- **hardcoding in source code**: developers may unintentionally leave api keys or tokens directly in the source code.

    ```py
    # example of hardcoded api key
    api_key = "1234567890abcdef"
    ```

- **public repositories**: accidentally committing sensitive keys and tokens to publicly accessible version control systems like github.

    ```ps1
    ## scan a github organization
    docker run --rm -it -v "$pwd:/pwd" trufflesecurity/trufflehog:latest github --org=trufflesecurity
    
    ## scan a github repository, its issues and pull requests
    docker run --rm -it -v "$pwd:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys --issue-comments --pr-comments
    ```

- **hardcoding in docker images**: api keys and credentials might be hardcoded in docker images hosted on dockerhub or private registries.

    ```ps1
    # scan a docker image for verified secrets
    docker run --rm -it -v "$pwd:/pwd" trufflesecurity/trufflehog:latest docker --image trufflesecurity/secrets
    ```

- **logs and debug information**: keys and tokens might be inadvertently logged or printed during debugging processes.

- **configuration files**: including keys and tokens in publicly accessible configuration files (e.g., .env files, config.json, settings.py, or .aws/credentials.).

### validate the api key

if assistance is needed in identifying the service that generated the token, [mazen160/secrets-patterns-db](https://github.com/mazen160/secrets-patterns-db) can be consulted. it is the largest open-source database for detecting secrets, api keys, passwords, tokens, and more. this database contains regex patterns for various secrets.

```yaml
patterns:
  - pattern:
      name: aws api gateway
      regex: '[0-9a-z]+.execute-api.[0-9a-z._-]+.amazonaws.com'
      confidence: low
  - pattern:
      name: aws api key
      regex: akia[0-9a-z]{16}
      confidence: high
```

use [streaak/keyhacks](https://github.com/streaak/keyhacks) or read the documentation of the service to find a quick way to verify the validity of an api key.

- **example**: telegram bot api token

    ```ps1
    curl https://api.telegram.org/bot<token>/getme
    ```

## reducing the attack surface

check the existence of a private key or aws credentials before commiting your changes in a github repository.

add these lines to your `.pre-commit-config.yaml` file.

```yml
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: detect-aws-credentials
    -   id: detect-private-key
```

## references

- [finding hidden api keys & how to use them - sumit jain - august 24, 2019](https://web.archive.org/web/20191012175520/https://medium.com/@sumitcfe/finding-hidden-api-keys-how-to-use-them-11b1e5d0f01d)
- [introducing signsaboteur: forge signed web tokens with ease - zakhar fedotkin - may 22, 2024](https://portswigger.net/research/introducing-signsaboteur-forge-signed-web-tokens-with-ease)
- [private api key leakage due to lack of access control - yox - august 8, 2018](https://hackerone.com/reports/376060)
- [saying goodbye to my favorite 5 minute p1 - allyson o'malley - january 6, 2020](https://www.allysonomalley.com/2020/01/06/saying-goodbye-to-my-favorite-5-minute-p1/)
