#Realtime Events

```shell
#You will need to perform at least two HTTP requests
# in order to get updates.
#A mandatory one to get the latest timestamp:

#GET https://demo.buddycloud.org/api/notifications/posts

#Then, provide the latest known time stamp to
# the same endpoint via the url parameter 'since':

#GET https://demo.buddycloud.org/api/notifications/posts?since={timestamp}

#For example:

curl https://demo.buddycloud.org/api/notifications/posts \
     -X GET

#A response example would be as follows:
{
  "last": "1403624041808",
  "items": []
}

curl https://demo.buddycloud.org/api/notifications/posts?since=1403624094454 \
     -X GET

#Response will be as follows:
{
  "last": "1403624094454",
  "items": [
    {
      "id": "f27139a9-f398-4e81-be94-3d14c3b7a39e",
      "source": "test@topics.buddycloud.org/posts",
      "author": "justin@buddycloud.org",
      "published": "2014-06-24T15:34:54.449Z",
      "updated": "2014-06-24T15:34:54.449Z",
      "content": "foo",
      "media":null,
      "replyTo":"d818f9b6-18ef-4b83-8a4e-e2d2ae7d18d5"
    }
  ]
}





















```

```javascript
#First of all, you must send presence in order
# to receive notifications:

#XMPP-FTW event 'xmpp.buddycloud.presence'

socket.send(
    'xmpp.buddycloud.presence',
    {}
)

#Then to get updates of specific events, there
# are other events as well.

#To listen for upcoming items:
#XMPP-FTW event 'xmpp.buddycloud.push.item'

socket.send(
    'xmpp.buddycloud.push.item',
    {}
)

#To be informed if an item was successfully deleted:
#XMPP-FTW event 'xmpp.buddycloud.push.retract'

socket.send(
    'xmpp.buddycloud.push.retract',
    {}
)

#To be informed if a node you follow had its configuration updated:
#XMPP-FTW event 'xmpp.buddycloud.push.configuration'

socket.send(
    'xmpp.buddycloud.push.configuration',
    {}
)

#To be informed of if a subscription change
# occured in a node you're subscribed to:
#XMPP-FTW event 'xmpp.buddycloud.push.subscription'

socket.send(
    'xmpp.buddycloud.push.subscription',
    {}
)

#For affiliation changes:
#XMPP-FTW event 'xmpp.buddycloud.push.affiliation'

socket.send(
    'xmpp.buddycloud.push.affiliation',
    {}
)

#If you're a node onwer or moderator, listen for
# subscription authorisation requests through:
#XMPP-FTW event 'xmpp.buddycloud.push.authorisation'

socket.send(
    'xmpp.buddycloud.push.authorisation',
    {}
)
```

Your app can receive realtime upates for all Buddycloud events, including:

* new posts from followed channels
* new posts from all public channels via the firehose
* new follow requests
* subscription updates (e.g. "a moderator approved your follow request for `citizens-of-verona@verona.lit`")

Tell the server that a client is now online to send spooled messages and begin streaming subsequent events.

To retrieve a history of events (for example, since last online), use the [message archive management](#retrieve-message-history) API. 

<aside>Buddycloud uses the [GRIP protocol](https://github.com/fanout/pushpin/blob/master/doc/grip-protocol.txt) for realtime event scaling. This works with the Fanout.io content delivery network. To set this up, get a Fanout account and configure the Buddycloud HTTP API component as described in the blog post on [scaling Buddycloud with Fanout](http://blog.buddycloud.com/post/59883382741/scaling-buddycloud-with-fanout-io).</aside>
