Title: Slate API
url: slate-api
save_as: slate-api.html
order: 2
table_of_contents: false
show_in_top_menu: false
slate: true

---
title: Buddycloud API Reference

language_tabs:
  - shell
  - javascript
  - sequence-diagram

toc_footers:
  - <a href='#'>Sign Up for a Buddycloud developer hosting</a>

includes:
  - errors

search: true
---

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

#Pagination

All Buddycloud API resources have support for handling large results. Results are paginated. 
    
## Query Parameters

Parameter | Reqired          | Description
--------- | ---------------- | -----------
max       | False            | The maximum number of returned entries
before    | False            | Get posts before this timestamp
first     | False            | ??? is this a date and what format???
last      | False            | ??? is this a date and what format???
after     | False            | Return only entries older than the entry with the specified ID.
index     | False            | The element's (for example, a post) position in the result set

#API discovery

When `user@example.com` starts a Buddycloud-enabled app, the app must discover the API for `example.com`. Clients query for the `TXT` record of `_buddycloud-api._tcp.buddycloud.org`.

Post-it note: Your home Buddycloud server will then pass messages to followers on remote buddycloud server. Consider buddycloud.org a testing server for trying out requests.

```shell
# to resolve the API endpoint for buddycloud.org we use:
dig txt +short _buddycloud-api._tcp.buddycloud.org 
```

```shell
"v=1.0" "host=demo.buddycloud.org" "protocol=https" "path=/api" "port=443"
```

> This test tells us that client calls should be made against `https://buddycloud.example.com:443/api`

```javascript
socket.send(
  'xmpp.buddycloud.discover',
  {},
  function(error, address) { console.log(error, address) }
)
```

> If a server is discovered the `data` will contain the channel server host. If no server is found, `error` will be populated.

```json
???
```

#Users

Create user accounts that can then use the service

Arguments  | Required | Description
---------- | -------- |------------
username   | True     | Must contain a domain element that matches the virtual host.
password   | True     |
email      | False    | Address to receive push notifications and password resets

##Create User

> POST https://demo.buddycloud.org/api/account

```shell 
curl https://demo.buddycloud.org/api/account \
	-X POST \
	-H "Content-Type: application/json" \
	-d '{ "username": "alice@buddycloud.org", \
           "password": "tell-no-one", \
           "email": "alice@buddycloud.org" \
        }'
```

```javascript
socket.send(
  'xmpp.login',
  {
    "jid": "romeo@buddycloud.org",
    "password": "juliet-forever",
    "register": true
  }
)
```

```json
???
```

##Delete User

Removes a user from the system 

<aside class="warning">Deleting a user will delete their account. It will not delete their channels. To completely remove the user, an application should first delete their channels, then the user account.</aside>

> POST https://demo.buddycloud.org/api/????

```shell 
curl https://demo.buddycloud.org/api/????
????
```

```javascript```
???
```

```json
???
```

##Change Password

???what does it do???

> POST https://demo.buddycloud.org/api/????

```shell 
curl https://demo.buddycloud.org/api/????
???
```

```javascript```
???
```

```json
???
```

##Reset Password

Resets the user's password and sends a reset token via email.

> POST https://demo.buddycloud.org/api/????

> Example request

```shell 
curl https://demo.buddycloud.org/api/????
 -
```

```javascript```
???
```

```json
???
```

#Realtime Events

Start receciving realtime events from local and remote Buddycloud servers.

```shell
#Justin needs to tell us how to do this
```

```javascript
socket.send('xmpp.buddycloud.presence', {})
```

#Channels
Following a channel grants one access to that channels current [and future] nodes. The following default nodes are created. Additional nodes can be created by the channel owner.

Each user has a channel automatically created for them on sign-up that that matches their ID. For example `user@example.com` will have a channel created called `user@example.com`


##Create Channel
##Update Metadata
##Delete Channel
##Default Nodes

node            | Description | Example
--------------- | ----------- | ----------
status          | A one line ???string format??? status message | Build completed - happy days
posts           | ATOM formatted activy stream | 
geoloc-previous | Where they were              |    
geoloc-current  | Where they are               |
geoloc-future   | Where they will go next      |

##Create Node
Create a new Application node (for example `/user/user@example.com/game-highscores), do ???

#Posts
##Create Post
##Delete Post
##Fetch Posts
Mention sync endpoint
##Upvote Post
##Firehose Access

#Subscriptions
##Fetch Subscriptions 
##Follow Channel
##Unfollow Channel

#Followers
##Fetch Followers
##Authorise Pending Followers
##Alter Follower Roles

#Messaging
##Send Message
##Retrieve Messages
Mention MAM

#Media Objects
##Media Metadata
##Fetch Media
###Special MediaIDs
##Post Media
##Delete Media

#Search
##Search by Content
Mention private search

##Search by Author
##Search by Metadata
##Search by Location

#Push Notifications
##Fetch Settings
##Update Settings

#Social Discovery

Useful for onboarding new users, Buddycloud can recommend similar channels to a channel, and iscovery Based on the (search and crawler), Buddycloud 

##Recommend Channels
##Similar Channels
##Popular Channels

#Import friends
##Social Graph comparison


# Introduction

Welcome to the Kittn API! You can use our API to access Kittn API endpoints, which can get information on various cats, kittens, and breeds in our database.

We have language bindings in Shell, Ruby, and Python! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.

This example API documentation page was created with [Slate](http://github.com/tripit/slate). Feel free to edit it and use it as a base for your own API's documentation.

# Authentication

> To authorize, use this code:

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
```

```python
import 'kittn'

api = Kittn.authorize('meowmeowmeow')
```

```shell
# With shell, you can just pass the correct header with each request
curl "api_endpoint_here"
  -H "Authorization: meowmeowmeow"
```

> Make sure to replace `meowmeowmeow` with your API key.

Kittn uses API keys to allow access to the API. You can register a new Kittn API key at our [developer portal](http://example.com/developers).

Kittn expects for the API key to be included in all API requests to the server in a header that looks like the following:

`Authorization: meowmeowmeow`

<aside class="notice">
You must replace `meowmeowmeow` with your personal API key.
</aside>

# Kittens

## Get All Kittens

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.get
```

```python
import 'kittn'

api = Kittn.authorize('meowmeowmeow')
api.kittens.get()
```

```shell
curl "http://example.com/api/kittens"
  -H "Authorization: meowmeowmeow"
```

> The above command returns JSON structured like this:

```json
[
  {
    "id": 1,
    "name": "Fluffums",
    "breed": "calico",
    "fluffiness": 6,
    "cuteness": 7
  },
  {
    "id": 2,
    "name": "Isis",
    "breed": "unknown",
    "fluffiness": 5,
    "cuteness": 10
  }
]
```

This endpoint retrieves all kittens.

### HTTP Request

`GET http://example.com/kittens`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
include_cats | false | If set to true, the result will also include cats.
available | true | If set to false, the result will include kittens that have already been adopted.

<aside class="success">
Remember — a happy kitten is an authenticated kitten!
</aside>

## Get a Specific Kitten

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.get(2)
```

```python
import 'kittn'

api = Kittn.authorize('meowmeowmeow')
api.kittens.get(2)
```

```shell
curl "http://example.com/api/kittens/3"
  -H "Authorization: meowmeowmeow"
```

> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "name": "Isis",
  "breed": "unknown",
  "fluffiness": 5,
  "cuteness": 10
}
```

This endpoint retrieves a specific kitten.

<aside class="warning">If you're not using an administrator API key, note that some kittens will return 403 Forbidden if they are hidden for admins only.</aside>

### HTTP Request

`GET http://example.com/kittens/<ID>`

### URL Parameters

Parameter | Description
--------- | -----------
ID        | The ID of the cat to retrieve

