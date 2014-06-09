#API discovery

```shell
# to resolve the API endpoint for buddycloud.org
dig txt +short _buddycloud-api._tcp.buddycloud.org 
```

```shell
"v=1.0" "host=demo.buddycloud.org" "protocol=https" "path=/api" "port=443"
```

> This test tells us that client calls should be made against `https://buddycloud.example.com:443/api`

```javascript
socket.send(
  'xmpp.buddycloud.discover',
  {},
  function(error, address) { console.log(error, address) }
)
```

> The data variable will have the Buddycloud server address. For example `buddycloud.example.com`


When `user@example.com` starts a Buddycloud-enabled app, the app must discover the corrent API endpoint for `example.com`. Likewise `user@other-domain.com` will retrieve a different API endpoint. To find out the API for a domain, clients query for the `TXT` record of `_buddycloud-api._tcp.buddycloud.org`.  See the [IANA service record](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=buddycloud)) if you are curious. 

<aside>User's _home_ Buddycloud server passes messages to followers on remote Buddycloud server.</aside>
