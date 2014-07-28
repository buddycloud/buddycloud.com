#Subscriptions

The subscription list includes all the channels a user follows and their role in the channel. 

Retrieving a user's channel subscription list will return:

* the channels (and channel-nodes) that they follow (`owner`, `moderator`, `publisher`, `member` )
* the private channels (and channel-nodes) they have asked (subscription state of `pending`) to follow.

### Subscription Privacy

Users can only request their own subscriptions.

##Fetch Subscriptions

```shell
#GET https://demo.buddycloud.org/api/subscribed

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

```javascript

```

Returns the user's channel subscriptions as a JSON object. The object's keys are of the form `{channel}` `/` `{node}`, the values denote the subscription type (`owner`, `moderator`, `publisher`, `member` or `pending`).

##Follow Channel

```shell
#POST https://demo.buddycloud.org/api/subscribed

curl https://demo.buddycloud.org/api/subscribed \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Content-Type: application/json" \
     -d '{ "romeo@buddycloud.org/posts": "publisher" }'
```

```javascript

```
Following behavior is dependent on the channel type:

* Following an _open_ channel is automatically allowed.
* Following a _private_ channel generates a `pending` subscription request

Following a _private_ channel:

* the user is added to the channel's `pending` subscription list
* the channel's `owner` or a `moderator` receives a subscription request (immediately if they are online or queued up for when they come online)
* either the channels `owner` or any of the channels `moderator`s approves [or rejects] and the result is then sent back to the user trying to follow the channel ???how???
* the user's subscription state is changed to `subscribed`, `publisher` (or `none` if rejected) depending on the channel's `default_affiliation`. 

<aside>The channel `owner` and `moderator` roles can adjust the `default_affiliation` is set in [#Update Metadata].</aside>


##Unfollow Channel

```shell
POST https://demo.buddycloud.org/api/subscribed

curl https://demo.buddycloud.org/api/subscribed \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Content-Type: application/json" \
     -d '{ \
             "romeo@buddycloud.org/posts": "none" \
         }'
```

```javascript

```

Unfollowing a private channel removes the ability to read, upvote or delete posts. 

Unfollowing a private channel will require re-requesting a subscription and re-approval of a moderator. 
