#API discovery

To avoid needing to hard-code an When `user@example.com` starts a Buddycloud-enabled app, the app must discover the API for `example.com`. Clients query for the `TXT` record of `_buddycloud-api._tcp.buddycloud.org`.

<aside>User's _home_ Buddycloud server passes messages to followers on remote Buddycloud server.</aside>

```shell
# to resolve the API endpoint for buddycloud.org we use:
dig txt +short _buddycloud-api._tcp.buddycloud.org 
```

```shell
"v=1.0" "host=demo.buddycloud.org" "protocol=https" "path=/api" "port=443"
```

This test tells us that client calls should be made against `https://buddycloud.example.com:443/api`

```javascript
socket.send(
  'xmpp.buddycloud.discover',
  {},
  function(error, address) { console.log(error, address) }
)
```

If a server is discovered the `data` will contain the channel server host. If no server is found, `error` will be populated.

```json
???
```

