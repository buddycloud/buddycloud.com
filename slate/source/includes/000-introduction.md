#Introduction 

Buddycloud has APIs optimised for both mobile and for web applications. 

* The REST API is optimised for mobile app development.
* Every API call also has a matching Javascript call for realtime web application programming.

<aside>To make Buddycloud as accessible as possible, all these API calls should work against the test instance running on buddycloud.org. Consider buddycloud.org a good reference implementation. Of course you are welcome to download the mobile or web API source code and run your own API.</aside>

##Time Format
All dates are in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format (example: "2012-08-21T22:31:20+0000"). In [strftime](http://pubs.opengroup.org/onlinepubs/007908799/xsh/strftime.html) format, `*%Y-%m-%dT%H:%M:%SZ*`

##Encoding
Each string passed to and from the buddycloud API must be UTF-8 encoded. (In the case of JSON set `Content-Type` to `application/json; charset=utf-8`)

##Authentication
Buddycloud uses HTTP Basic method. The username should also include the domain. For example `user@example.com` works/`user` not. 

<aside class="warning">Always authenticate a user against their home API server. While it may be possible to authenticate against a third-party API server, this could potentially expose user credentials.</aside>
