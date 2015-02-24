##Fetch Child Posts

```shell
#GET https://buddycloud.com/api/{channelID}/content/{nodeId}/{postID}/replyto

curl https://buddycloud.com/api/romeo@buddycloud.org/content/posts/$POST_ID/replyto \
     -X GET \
     -H "Accept: application/json"

#Response will be as follows:

200 OK
Content-Type: application/json

[
    {
        "id": "foo",
        "replyTo": "qux",
        "author": "romeo@buddycloud.com",
        "updated": "1595-06-01T12:00:00Z",
        "content": "But, soft! What light through yonder window breaks? It is the east, and Juliet is the sun.",
        "media": null
    },
    ...
    {
        "id": "bar",
        "replyTo": "qux",
        "author": "romeo@buddycloud.com",
        "updated": "1591-06-04T12:00:00Z",
        "content": "Thus with a kiss I die.",
        "media": null
    }
]
```

```javascript






























```

Buddycloud uses the [Atom threading extensions](http://www.ietf.org/rfc/rfc4685.txt) to enable you to easily query for child posts.

## Sync Posts

```shell










```

```javascript










```

An app might want to just show the latest 10 posts per channel (and query for older posts can be paged in as the users scrolls down). 

The `sync` query returns [up to]`n` posts per channel newer than `<timestamp of most recent post in client cache>`. 

This avoids the problem of a very busy channel "drowning" other posts during a client synchronisation.

Paramenter | Required | Value      | Description
-----------|----------|------------|------------
`since`      | `true`     | [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) timestamp??? | Useful for catching up from the most recent post in the Buddycloud app's cache. 
`max`        | `false`    | integer    | the maximum number of posts to be returned per channel
`summary`    | `false`    | `true`, `false` | returns only summary information per channel (not posts)

##Upvote Post

```shell
#Unsupported Method









```

```javascript
#Unsupported Method









```

Users can can give feedback on posts by upvoting/liking posts. Upvotes take a value of 1 to 5. It's recommended that for a binary "like" you simply apply a value of 5.

##Access Firehose

```shell
#Unsupported Method









```

```javascript
#Unsupported Method









```

The `/firehose` contains a feed of all channel-nodes that you are subscribed to that are cached locally.

The firehose node can also be queried for historical posts using [pagination](#pagination).

If unauthenticated, the firehose will show posts from public channels.

If you are logged in you can also retrieve posts that you subscribe to from private channels.
