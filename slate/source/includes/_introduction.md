#Introduction 

We have tried to optimise the Buddycloud API to make it as easy as possible to build your app. In general, 
* The REST API is optimised for mobile app development.
* The Javascript calls are better for realtime web application programming.

We recommend you start testing against the buddycloud API running at `demo.buddycloud.org/api`. You can then run your own Buddyclouyd stack, using the [hosting](https://hosting.buddycloud.com) service or [self-install](/install) your own Buddycloud stack.

##Time Format
All timestamps are [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format ("2012-08-21T22:31:20+0000"). In [strftime](http://pubs.opengroup.org/onlinepubs/007908799/xsh/strftime.html) format: `*%Y-%m-%dT%H:%M:%SZ*`

##Encoding
The Buddycloud API speaks UTF-8 encoding. (`Content-Type` of `application/json; charset=utf-8`)

##Authentication
Buddycloud uses HTTP [basic authentication](http://en.wikipedia.org/wiki/Basic_access_authentication). The `BuddycloudID` should also include the user's domain (`user@example.com`). 

##External Authentication
You can authenticate your Buddycloud users against your own site.

The external authentication features will backhaul login requests to your own API and if successful, log your user in. (If this is useful, please contact us on the reach-a-developer@buddycloud.com email address and we can enable it for you.)