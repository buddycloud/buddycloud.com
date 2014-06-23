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

Your app can receive realtime upates for all Buddycloud events. These events include:
* new posts from followed channels
* new posts from all public channels via the firehose
* new follow requests
* subscription updates (For example "you were approved as a moderator on dev-ops@example.com)

When your users are not online, these events are spooled up in rhe user's inbox. 

To begin receiving messages since the user was last online, and enable streaming of subsequent events, you should tell the server that the client is now online.

@@@Lloyd - how are invites spooled up? 
@@@Lloyd - how are follow requests spooled up?

<aside>Buddycloud uses the ???Justin: GRIT specification??? from and [Fanout's](https://fanout.io) realtime content delivery network for scaling realtime event pushes. The [Fanout.io Documentation](https://fanout.io/docs/) has details on getting this setup.</aside>