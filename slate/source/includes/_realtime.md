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

Sending this instructs the server to start pushing realtime events from local and remote Buddycloud servers. 

These evnets include, new posts from followed channels, new follow requests (if the user moderates or owns a private channel), updates from events (for example "you were approved as a moderator on dev-ops@example.com).
