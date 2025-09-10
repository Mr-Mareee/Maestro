# mass assignment

> a mass assignment attack is a security vulnerability that occurs when a web application automatically assigns user-supplied input values to properties or variables of a program object. this can become an issue if a user is able to modify attributes they should not have access to, like a user's permissions or an admin flag.

## summary

* [methodology](#methodology)
* [labs](#labs)
* [references](#references)


## methodology

mass assignment vulnerabilities are most common in web applications that use object-relational mapping (orm) techniques or functions to map user input to object properties, where properties can be updated all at once instead of individually. many popular web development frameworks such as ruby on rails, django, and laravel (php) offer this functionality.

for instance, consider a web application that uses an orm and has a user object with the attributes `username`, `email`, `password`, and `isadmin`. in a normal scenario, a user might be able to update their own username, email, and password through a form, which the server then assigns to the user object.

however, an attacker may attempt to add an `isadmin` parameter to the incoming data like so:

```json
{
    "username": "attacker",
    "email": "attacker@email.com",
    "password": "unsafe_password",
    "isadmin": true
}
```

if the web application is not checking which parameters are allowed to be updated in this way, it might set the `isadmin` attribute based on the user-supplied input, giving the attacker admin privileges


## labs

* [pentesteracademy - mass assignment i](https://attackdefense.pentesteracademy.com/challengedetailsnoauth?cid=1964)
* [pentesteracademy - mass assignment ii](https://attackdefense.pentesteracademy.com/challengedetailsnoauth?cid=1922)
* [root me - api - mass assignment](https://www.root-me.org/en/challenges/web-server/api-mass-assignment)


## references

- [hunting for mass assignment - shivam bathla - august 12, 2021](https://blog.pentesteracademy.com/hunting-for-mass-assignment-56ed73095eda)
- [mass assignment cheat sheet - owasp - march 15, 2021](https://cheatsheetseries.owasp.org/cheatsheets/mass_assignment_cheat_sheet.html)
- [what is mass assignment? attacks and security tips - yoan montoya - june 15, 2023](https://www.vaadata.com/blog/what-is-mass-assignment-attacks-and-security-tips/)