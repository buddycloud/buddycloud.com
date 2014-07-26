#Introduction 

The listed API calls give you access to the entire Buddycloud stack. The API calls are designed to make it easy to add rich in-app messaging and social features to your web or mobile app.

The API calls are tailored to the differing constraints of web and mobile application development. In general:

* the *REST API* is optimised for mobile app development.
* *[XMPP-FTW](https://xmpp-ftw.jit.su/manual/extensions/buddycloud/)* is better for realtime web application programming.

Both methods can be used against:

* **buddycloud.org** (recommended), whose REST API endpoint runs at `https://demo.buddycloud.org/api`
* the [hosting](https://hosting.buddycloud.com) service
* or a [self-install](/install) of the Buddycloud stack

<aside>Throughout most of this documentation, the *REST API* or *XMPP-FTW* calls will be displayed on the right column when the corresponding tabs are selected.

But sometimes a given section in the document is specially focused on one of these alternatives - that will be explicitly indicated as a such case.</aside>

###Getting Help
We really want this API to be useful to you. If you run into problems please [contact](/contact) us. [Documentation fixes](https://github.com/buddycloud/buddycloud.com/tree/master/slate/source/includes) and ideas for improvements are always welcome.

These pages are generated using [Slate](https://github.com/tripit/slate).

##REST API Conventions

###Encoding
The REST API uses UTF-8 character encoding.

Request headers should include a `Content-Type` of `application/json; charset=utf-8`.

###Authentication
The REST API uses HTTP [basic authentication](http://en.wikipedia.org/wiki/Basic_access_authentication). The `username` should also include the user's domain (`user@example.com`).

###External Authentication
Buddycloud's backend enables you to authenticate your users against your own site by forwarding login requests to your own API. [Email](mailto:reach-a-developer@buddycloud.com) us to to have this feature enabled for your domain.

###Time Format
All timestamps are [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format e.g. ("2012-08-21T22:31:20+0000").

##XMPP-FTW Conventions

###Data Format
[XMPP-FTW](https://xmpp-ftw.jit.su) provides a JSON layer on top of XMPP via a Data Transport mechanism such as [Primus](http://primus.io). Visit <https://xmpp-ftw.jit.su> for more details.
