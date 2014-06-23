#Introduction 

In general, 

* The REST API is optimised for mobile app development.
* The Javascript calls are better for realtime web application programming.

We recommend you start testing against the buddycloud API running at `demo.buddycloud.org/api`. You can then run your own Buddyclouyd stack, using the [hosting](https://hosting.buddycloud.com) service or [self-install](/install) your own Buddycloud stack.

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

All documentation is generated using [Slate](https://github.com/tripit/slate).