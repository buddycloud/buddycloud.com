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
  - shell : cURL
  - javascript : Javascript
  - plaintext : Sequence Diagram

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

```shell
dig txt +short _buddycloud-api._tcp.buddycloud.org
```

```shell
#The response:

"v=1.0 host=demo.buddycloud.org protocol=https path=/api port=443"

#This means that client calls should be made against
#`https://demo.buddycloud.org:443/api`
```

When `user@example.com` starts a Buddycloud-enabled app, the app must discover the API for `example.com`.

Clients query for the `TXT` record of `_buddycloud-api._tcp.buddycloud.org`.

Post-it note: Your home Buddycloud server will then pass messages to followers on remote buddycloud servers. Consider buddycloud.org a testing server for trying out requests.

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

##Change Password

> POST https://demo.buddycloud.org/api/????

```shell 
curl https://demo.buddycloud.org/api/????
???
```

```javascript```
???
```

???what does it do???

##Reset Password

> POST https://demo.buddycloud.org/api/????

```shell 
curl https://demo.buddycloud.org/api/????
 -
```

```javascript```
???
```

Resets the user's password and sends a reset token via email.

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
