#Subscriptions

The subscription list contains the channels and nodes that a user follows.

##Fetch Subscriptions

```shell
curl --user juliet@buddycloud.org:romeo-forever \
    https://demo.buddycloud.org/api/subscribed \
    -X GET \
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

Returns the user's channel subscriptions as a JSON object. The object's keys are of the form `{channel}`/`{node}`, the values denote the subscription type (`owner`, `publisher`, `member` or `pending`).


### HTTP Request
`GET https://demo.buddycloud.org/api/subscribed`

<aside class="warning">Requires Basic Authentication.</aside>


##Follow Channel

```shell
curl --user juliet@buddycloud.org:romeo-forever \
    https://demo.buddycloud.org/api/subscribed \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{ \
            "romeo@buddycloud.org/posts": "publisher" \
        }'
```

```javascript```
???
???
```

Users can automatically follow open channels. 

Users can request access to a closed channel.

Following works as follows:
* following an open channel, immediate
* following a closed channel generates a subscription request
* a moderator of the closed channel receives a subscription request (immediately if they are online or queued up for when they come online)
* the approval or rejection is then sent back to the user trying to follow the channel

### HTTP Request
`POST https://demo.buddycloud.org/api/subscribed`

<aside class="warning">Requires Basic Authentication.</aside>

##Unfollow Channel

```shell
curl --user juliet@buddycloud.org:romeo-forever \
    https://demo.buddycloud.org/api/subscribed \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{ \
            "romeo@buddycloud.org/posts": "none" \
        }'
```

```javascript```
???
???
```

This unfollows a channel. Unfollowing a closed channel will require re-requesting a subscription and re-approval of a moderator.

### HTTP Request
`POST https://demo.buddycloud.org/api/subscribed`

<aside class="warning">Requires Basic Authentication.</aside>
