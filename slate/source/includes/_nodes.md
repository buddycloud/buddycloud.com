#Channel-Nodes

Channel-Nodes are publish-subscribe streams of posts with the same content type.

An example: The channel `juliet@capulet.lit` contains nodes for each type of information that `juliet` wants to share. When `romeo@montague.lit` follows the channel `juliet@capulet.lit` a subscription is created for all the nodes under `juliet@capulet.lit`:

- `juliet@capulet.lit/posts` channel-node (the serialization `juliet@capulet.lit`'s of social activities)
- `juliet@capulet.lit/status` channel-node (a text string describing `juliet@capulet.lit`'s mood)
- `juliet@capulet.lit/music-i-liked` channel-node (a hypothetical [activity stream](http://activitystrea.ms/specs/json/1.0/) of music `juliet@capulet.lit` liked)

These channel-nodes:

- are described as the `juliet@capulet.lit` channel,
- share a common set of followers,
- share a common set of publishers,
- share common metadata (e.g. _title_, _description_, _location_ fields)

###Default Channel-Nodes

Your application can use the default channel-nodes or define new channel-nodes with new content types. Each channel is preconfigured with the the default channel-nodes:

Name             | Personal Channel |Topic Channel | Description 
-----------------|:---------------: |:------------:|----------------
status           | ✓                | ✓            | A one line status message 
posts            | ✓                | ✓            | ATOM formatted activy stream 
geoloc-previous  | ✓                | ✗            | Where they were              
geoloc-current   | ✓                | ✗            | Where they are              
geoloc-future    | ✓                | ✗            | Where they will go next   
public-key       | ✓                | ✗            | Public key for secure messaging

<aside>Default nodes are defined in the [Buddycloud protocol specification](http://buddycloud.github.io/buddycloud-xep/#well-known-nodes).</aside>

##Create Channel-Node

```shell
@guilhermesgb: There's no HTTP API endpoint for creating specific nodes.
```

```javascript```
???
???
```

It's recommended to create new nodes for new applications. `X-application-<your-application-name>` will avoid bumping into other developers' application namespaces.

For example: A chess app would create an `x-application-ChessApp` channel-node.  Competing players could use this channel-node to keep state between two games.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`

##Delete Channel-Node

```shell
@guilhermesgb: There's no HTTP API endpoint for creating specific nodes.
```

```javascript```
???
???
```

This will remove an application node. This will not remove the channel.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`
