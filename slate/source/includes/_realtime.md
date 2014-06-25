#Realtime Events

```shell
# Justin needs to tell us how to do this
```

```javascript
socket.send('xmpp.buddycloud.presence',
            {}
            )
```
> returns the following on success

```json
???  (does this ACK or just start sending events?)
```

Your app can receive realtime upates for all Buddycloud events. Events include:

* new posts from followed channels
* new posts from all public channels via the firehose
* new follow requests
* subscription updates (e.g. "a moderator approved your follow request for `citizens-of-verona@verona.lit`")

To begin receiving messages since the user was last online, and enable streaming of subsequent events, you should tell the server that the client is now online.

To retrieve a history of events (for example since last online) use the [message archive management](#retrieve-message-history) API. 

<aside>Buddycloud uses the [GRIP protocol](https://github.com/fanout/pushpin/blob/master/doc/grip-protocol.txt) for realtime event scaling. This works with the Fanout.io content delivery network. To set this up, get a Fanout account and configure the Buddycloud HTTP API component as described in the blog post "[Scaling Buddycloud with Fanout"](http://blog.buddycloud.com/post/59883382741/scaling-buddycloud-with-fanout-io)".</aside>