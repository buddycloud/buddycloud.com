#Introduction 

The listed API calls give you access to the entire Buddycloud stack. The API calls are designed to make it easy to add rich in-app messaging and social features to your web or mobile app.

The API calls are tailored to the differing constraints of web and mobile application development. In general, 

* the *REST API* is optimised for mobile app development,
* the *Javascript* calls are better for realtime web application programming.

The API can be used against:

* the demo API endpoint running at `https://demo.buddycloud.org/api` (recommended)
* the [hosting](https://hosting.buddycloud.com) service
* or a [self-install](/install) of the Buddycloud stack

###Getting help
We really want this API to be useful to you. If you run into problems please [contact](/contact) us. [Documenetation fixes](https://github.com/buddycloud/buddycloud.com/tree/master/slate/source/includes) and ideas for improvements are always welcomed.

These pages are generated using [Slate](https://github.com/tripit/slate).

## Conventions

###Encoding
The Buddycloud API uses UTF-8 character encoding.

Request headers should include a `Content-Type` of `application/json; charset=utf-8`.

###Authentication
The Buddycloud API uses HTTP [basic authentication](http://en.wikipedia.org/wiki/Basic_access_authentication). The `BuddycloudID` should also include the user's domain (`user@example.com`).

###Time Format
All timestamps are [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format ("2012-08-21T22:31:20+0000").

###External Authentication
Buddycloud's backend enables you to authenticate your users against your own site.

The external authentication features will backhaul login requests to your own API. [Email](mailto:reach-a-developer@buddycloud.com) us to to have this feature enabled for you domain.

