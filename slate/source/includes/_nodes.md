#Channel-Nodes

Channel-Nodes are publish-subscribe streams of posts with the same content type. For example, the channel `juliet@capulet.lit` contains nodes for each type of information that `juliet` wants to share. When `romeo@montague.lit` follows the channel `juliet@capulet.lit` a subscription is created for all the nodes under `juliet@capulet.lit`:

- `juliet@capulet.lit/social` channel-node (the serialization of `juliet@capulet.lit`'s social activities)
- `juliet@capulet.lit/status` channel-node (a text string describing `juliet@capulet.lit`'s mood)
- `juliet@capulet.lit/music-i-liked` channel-node (a hypothetical [activity stream](http://activitystrea.ms/specs/json/1.0/) of music `juliet@capulet.lit` likes)

These channel-nodes:

- make up the `juliet@capulet.lit` channel
- share a common set of followers
- share a common set of publishers
- share common metadata (e.g. `title`, `description` and `location` fields)

###Default Channel-Nodes

Your application can use the default channel-nodes or define new channel-nodes with new content types. Creating a new channel automatically creates the following nodes:

Name             | Personal Channel |Topic Channel | Description 
-----------------|:---------------: |:------------:|----------------
status           | ✓                | ✓            | a one-line status message 
posts            | ✓                | ✓            | ATOM formatted activity stream 
geoloc-previous  | ✓                | ✗            | where they were              
geoloc-current   | ✓                | ✗            | where they are              
geoloc-future    | ✓                | ✗            | where they will go next   
public-key       | ✓                | ✗            | public key for secure messaging

<aside>Default nodes are defined in the [Buddycloud protocol specification](http://buddycloud.github.io/buddycloud-xep/#well-known-nodes).</aside>

##Create Channel-Node

```shell
curl https://demo.buddycloud.org/api/juliet@buddycloud.org/daily-diary \
    -X POST \
    -u juliet@buddycloud.org:romeo-forever
```

```javascript
???
???
```

This allows creation of application nodes.

<aside>It's recommended to create new nodes for new applications. For example `x-application-<your-application-name>`.

For example: A chess app would create an `x-application-ChessApp` channel-node. Competing players could use this channel-node to keep state between two games.</aside>

### HTTP Request
`POST https://demo.buddycloud.org/api/{channelID}/{nodeID}`

##Delete Channel-Node

```shell
curl https://demo.buddycloud.org/api/juliet@buddycloud.org/daily-diary \
    -X DELETE \
    -u juliet@buddycloud.org:romeo-forever

```

```javascript
???
???
```

This will remove an application node but not the channel.

### HTTP Request
`DELETE https://demo.buddycloud.org/api/{channelID}/{nodeID}`
