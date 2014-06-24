#Introduction 

The listed API calls enable you to build mobile and web applications that include a rich messaging and social features using the Buddycloud stack.

The API calls are tailored to the different constraints of web and mobile application development. In general, 

* the *REST API* is optimised for mobile app development,
* the *Javascript* calls are better for realtime web application programming.

The API can be used against:

* the demo API endpoint running at `https://demo.buddycloud.org/api` (recommended)
* the [hosting](https://hosting.buddycloud.com) service
* or a [self-install](/install) of the Buddycloud stack

##Encoding
The Buddycloud API uses UTF-8 encoding.

Request headers should include a `Content-Type` of `application/json; charset=utf-8`.

##Authentication
Buddycloud uses HTTP [basic authentication](http://en.wikipedia.org/wiki/Basic_access_authentication). The `BuddycloudID` should also include the user's domain (`user@example.com`).

##Time Format
All timestamps are [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format ("2012-08-21T22:31:20+0000"). In [strftime](http://pubs.opengroup.org/onlinepubs/007908799/xsh/strftime.html) format: `*%Y-%m-%dT%H:%M:%SZ*`

##External Authentication
You can authenticate your Buddycloud users against your own site.

The external authentication features will backhaul login requests to your own API and if successful, log your user in. (email [reach-a-developer@buddycloud.com](mailto:reach-a-developer@buddycloud.com) to have this feature enabled.)

##Getting help
We really want this API to be useful to you. If you run into problems please [contact](/contact) us. [Documenetation fixes](https://github.com/buddycloud/buddycloud.com/tree/master/slate/source/includes) and ideas for improvements are always welcomed.

Documentation is generated using [Slate](https://github.com/tripit/slate).