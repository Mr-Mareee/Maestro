# business logic errors

> business logic errors, also known as business logic flaws, are a type of application vulnerability that stems from the application's business logic, which is the part of the program that deals with real-world business rules and processes. these rules could include things like pricing models, transaction limits, or the sequences of operations that need to be followed in a multi-step process.


## summary

* [methodology](#methodology)
    * [review feature testing](#review-feature-testing)
    * [discount code feature testing](#discount-code-feature-testing)
    * [delivery fee manipulation](#delivery-fee-manipulation)
    * [currency arbitrage](#currency-arbitrage)
    * [premium feature exploitation](#premium-feature-exploitation)
    * [refund feature exploitation](#refund-feature-exploitation)
    * [cart/wishlist exploitation](#cartwishlist-exploitation)
    * [thread comment testing](#thread-comment-testing)
* [references](#references)


## methodology

unlike other types of security vulnerabilities like sql injection or cross-site scripting (xss), business logic errors do not rely on problems in the code itself (like unfiltered user input). instead, they take advantage of the normal, intended functionality of the application, but use it in ways that the developer did not anticipate and that have undesired consequences.

common examples of business logic errors.

### review feature testing

* assess if you can post a product review as a verified reviewer without having purchased the item.
* attempt to provide a rating outside of the standard scale, for instance, a 0, 6 or negative number in a 1 to 5 scale system.
* test if the same user can post multiple ratings for a single product. this is useful in detecting potential race conditions.
* determine if the file upload field permits all extensions; developers often overlook protections on these endpoints.
* investigate the possibility of posting reviews impersonating other users.
* attempt cross-site request forgery (csrf) on this feature, as it's frequently unprotected by tokens.


### discount code feature testing

* try to apply the same discount code multiple times to assess if it's reusable.
* if the discount code is unique, evaluate for race conditions by applying the same code for two accounts simultaneously.
* test for mass assignment or http parameter pollution to see if you can apply multiple discount codes when the application is designed to accept only one.
* test for vulnerabilities from missing input sanitization such as xss, sql injection on this feature.
* attempt to apply discount codes to non-discounted items by manipulating the server-side request.


### delivery fee manipulation

* experiment with negative values for delivery charges to see if it reduces the final amount.
* evaluate if free delivery can be activated by modifying parameters.


### currency arbitrage

* attempt to pay in one currency, for example, usd, and request a refund in another, like eur. the difference in conversion rates could result in a profit.
    

### premium feature exploitation

* explore the possibility of accessing premium account-only sections or endpoints without a valid subscription.
* purchase a premium feature, cancel it, and see if you can still use it after a refund.
* look for true/false values in requests/responses that validate premium access. use tools like burp's match & replace to alter these values for unauthorized premium access.
* review cookies or local storage for variables validating premium access.


### refund feature exploitation

* purchase a product, ask for a refund, and see if the product remains accessible.
* look for opportunities for currency arbitrage.
* submit multiple cancellation requests for a subscription to check the possibility of multiple refunds.


### cart/wishlist exploitation

* test the system by adding products in negative quantities, along with other products, to balance the total.
* try to add more of a product than is available.
* check if a product in your wishlist or cart can be moved to another user's cart or removed from it.


### thread comment testing

* check if there's a limit to the number of comments on a thread.
* if a user can only comment once, use race conditions to see if multiple comments can be posted.
* if the system allows comments by verified or privileged users, try to mimic these parameters and see if you can comment as well.
* attempt to post comments impersonating other users.


## references

- [business logic vulnerabilities - portswigger - 2024](https://portswigger.net/web-security/logic-flaws)
- [business logic vulnerability - owasp - 2024](https://owasp.org/www-community/vulnerabilities/business_logic_vulnerability)
- [cwe-840: business logic errors - cwe - march 24, 2011](https://cwe.mitre.org/data/definitions/840.html)
- [examples of business logic vulnerabilities - portswigger - 2024](https://portswigger.net/web-security/logic-flaws/examples)