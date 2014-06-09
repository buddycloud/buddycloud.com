#Subscriptions

The subscription list contains the channels and nodes that a user follows.

##Fetch Subscriptions

```shell
curl https://demo.buddycloud.org/api/????

```

```javascript```
???
???
```

```json
???
???
```

Returns the user's channel subscriptions as a JSON object. The object's keys are of the form `{channel}`/`{node}`, the values denote the subscription type (`owner`, `publisher`, `member` or `pending`).


### HTTP Request
`GET https://demo.buddycloud.org/api/????`



##Follow Channel

```shell
curl https://demo.buddycloud.org/api/???? \
 --??? \
 --???
```

```javascript```
???
???
```

```json
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
`POST https://demo.buddycloud.org/api/????`

##Unfollow Channel

```shell
curl https://demo.buddycloud.org/api/???? \
 --??? \
 --???
```

```javascript```
???
???
```

```json
???
???
```

This unfollows a channel. Unfollowing a closed channel will require re-requesting a subscription and re-approval of a moderator.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`
