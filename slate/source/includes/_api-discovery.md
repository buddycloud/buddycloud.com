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

API discovery takes care of finding the API endpoint to use for each domain running Buddycloud services. 
 
Usually mobile apps will hardcode the API URL (e.g. `https://api.twitter.com/1.1/`) . However if your application is designed for users on multiple Buddycloud it's necessary to discover the API URL for each user's domain. 

For example:

* `juliet@capulet.lit` connects to the Capulet Buddycloud API using `https://buddycloud.capulet.lit/api`.
* `romeo@montague.lit` connects to the Montague Buddycloud API using `https://montague.lit/buddycloud/api`.

To find the API for a users domain:

- clients query for the `TXT` record of `_buddycloud-api._tcp.buddycloud.org.`.  
- The results return an [IANA service record](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=buddycloud). 

Parameter | Description        | Example
----------|--------------------|----------
`v`       | API version number | `v=1.0`
`host`    | server to use      | `host=demo.buddycloud.org` 
`protocol`| which connection type to use | `protocol=https`
`path`    | API prefix         | `path=/api-endpoint`
`port`    | port to use        | `port=443`

The above example would result in the using `https://buddycloud.example.com:443/api-endpoint` as the API.

<aside>You only need run the API discvery if you are building a single app that users on multiple Buddycloud sites will use. That is users logging in with their full BuddycloudIDs.</aside>
