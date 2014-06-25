#Realtime Events

```shell
curl https://demo.buddycloud.org/api/notifications/posts
```

> This will always return 0 items and the latest timestamp:

{
  "last": "1403624041808",
  "items": []
}

> Then, make another request with the "since" query parameter set to the last known timestamp:

```shell
curl https://demo.buddycloud.org/api/notifications/posts?since=1403624094454
```

>This will hang until a response is returned, such as:

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

> Then continue to loop and call this endpoint, using the 'last' value of the previous request in each subsequent call.

```javascript
socket.send('xmpp.buddycloud.presence',
            {}
            )
```
> returns the following on success

```json
???  (does this ACK or just start sending events?)
```

Your app can receive realtime upates for all Buddycloud events. 

Supported realtime events include:

* new posts from followed channels
* new posts from all public channels via the firehose
* new follow requests
* subscription updates (e.g. "a moderator approved your follow request for `citizens-of-verona@verona.lit`")

To begin receiving messages since the user was last online, and enable streaming of subsequent events, you should tell the server that the client is now online.

To retrieve a history of events (for example since last online) use the [message archive management](#retrieve-message-history) API. 

<aside>Buddycloud uses the [GRIP protocol](https://github.com/fanout/pushpin/blob/master/doc/grip-protocol.txt) for realtime event scaling. This works with the Fanout.io content delivery network. To set this up, get a Fanout account and configure the Buddycloud HTTP API component as described in the blog post "[Scaling Buddycloud with Fanout"](http://blog.buddycloud.com/post/59883382741/scaling-buddycloud-with-fanout-io)".</aside>