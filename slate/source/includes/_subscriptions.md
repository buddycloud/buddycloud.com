#Subscriptions

Your users' channel subscriptions are stored on Buddycloud server. The subscription list contains
* the channels (and nodes) that they follow
* the channels (and nodes) that have pending subscriptions

Each item also contain the user's role (`owner`, `moderator`, `publisher`, `member` or `pending`) in that channel.

<aside class="warning">All subscription requests require authentication.</aside>

##Fetch Subscriptions

```shell
curl https://demo.buddycloud.org/api/subscribed \
     -X GET \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Accept: application/json"
```

```shell
200 OK
Content-Type: application/json

{
    "juliet@buddycloud.org": "owner",
    "romeo@buddycloud.org": "pending",
    "capulet@topics.buddycloud.org": "publisher"
}
```

```javascript```
???
```

Returns the user's channel subscriptions as a JSON object. The object's keys are of the form `{channel}`/`{node}`, the values denote the subscription type (`owner`, `moderator`, `publisher`, `member` or `pending`).

### HTTP Request
`GET https://demo.buddycloud.org/api/subscribed`

<aside class="warning">Requires Basic Authentication.</aside>


##Follow Channel

```shell
curl https://demo.buddycloud.org/api/subscribed \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Content-Type: application/json" \
     -d '{ "romeo@buddycloud.org/posts": "publisher" }'
```

```javascript```
???
???
```
Following behavior is dependent on the channel type.

Following an _open_ channel is automatically allowed. 

Following a _private_ channel is generates a subscription request
* the ueser's subscrition state is set to `pending`
* the private channels `owner` or a `moderator` receives a subscription request (immediately if they are online or queued up for when they come online)
* the `owner` or `moderator` approval [or rejection] is then sent back to the user trying to follow the channel
* the user's subscription state is changed to `subscribed` ??? [or `none`] ???

### HTTP Request
`POST https://demo.buddycloud.org/api/subscribed`


##Unfollow Channel

```shell
curl https://demo.buddycloud.org/api/subscribed \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Content-Type: application/json" \
     -d '{ \
             "romeo@buddycloud.org/posts": "none" \
         }'
```

```javascript```
???
???
```

Unfollowing a private channel removes the ability to read, upvote or delete posts. 

Unfollowing a private channel will require re-requesting a subscription and re-approval of a moderator. 

Unfollowing a channel will not remove that user's posts from the channel.

### HTTP Request
`POST https://demo.buddycloud.org/api/subscribed`