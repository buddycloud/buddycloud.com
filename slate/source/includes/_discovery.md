#Discovery

Whether using Buddycloud through the *REST API* or *XMPP-FTW*, you need to discover where the server runs for your Buddycloud enabled domain.

##REST API Discovery

```plaintext
#In order to resolve the API endpoint for buddycloud.org, do:

dig txt +short _buddycloud-api._tcp.buddycloud.org

#You shall get a TXT record such as the following as response:

"v=1.0" "host=demo.buddycloud.org" "protocol=https" "path=/api" "port=443"



```

**Problem:** Your application is designed for users on multiple Buddycloud sites eacg with their own REST-API. It is necessary to discover the API URL for each user's domain.
* `juliet@capulet.lit` connects to the Capulet Buddycloud API using `https://buddycloud.capulet.lit/api`.
* `romeo@montague.lit` connects to the Montague Buddycloud API using `https://montague.lit/buddycloud/api`.

**Solution:** Buddycloud solves this by using a DNS lookup to discover the REST-API endpoint. 

To find the API for a user's domain:

- Clients query for the `TXT` record of `_buddycloud-api._tcp.<user's domain>.`.  
- The results return an [IANA service record](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=buddycloud). 

Parameter | Description        | Example
----------|--------------------|----------
`v`       | API version number | `v=1.0`
`host`    | server to use      | `host=demo.buddycloud.org` 
`protocol`| which connection type to use | `protocol=https`
`path`    | API prefix         | `path=/api-endpoint`
`port`    | port to use        | `port=443`

The following API URL reflects the above response:  `https://demo.buddycloud.org:443/api-endpoint`.

<aside>Run the API discvery procedure only if you are building an app for users on multiple Buddycloud sites logging in with their full `username@domainname`.</aside>

##XMPP-FTW Discovery

```plaintext
#XMPP-FTW event 'xmpp.buddycloud.discover'

socket.send(
    'xmpp.buddycloud.discover',
    {},
    function(error, data) { console.log(error, data) }
)



```

The same way we need to discover the *REST API*, we need to discover where the Buddycloud server lives in order to use it through *XMPP-FTW*. This procedure is rather simpler compared to the REST API discovery since it is implemented by XMPP-FTW internally.
