#Posts

New posts to a node are automaticaly:

* pushed to the channel's online followers
* spooled up for the channel's offline followers
* pushed to the [firehose](#access-firehose)
* archived and retrievable using the [fetch posts](#fetch-posts) method.
* indexed by the [channel crawler](https://github.com/buddycloud/channel-directory)

Different channel types have different post formats.

> Below are field value examples for each parameter field:

### Post Parameters

Field       | Description | Responsible | <div style="display:none;">Example</div>
------------|-------------|--------|---------
`author`    | the `username` of this post's author, set by the server  | server | <div class="highlight"><pre style="position:absolute; right:0px;"><code>juliet@capulet.lit</code></pre></div>
`content`   | the post's content - usually this is activity stream content | user   | <div class="highlight"><pre style="position:absolute; right:0px;"><code>O Romeo, Romeo! Wherefore art thou Romeo?</code></pre></div>
`id`        | the unique post ID assigned to this post by the server | server | <div class="highlight"><pre style="position:absolute; right:0px;"><code>17163726-ea90-453e-ad25-455336a83fd4</code></pre>
`media`     | a list of media objects this post might refer to | user | <div class="highlight"><pre style="position:absolute; right:0px;"><code>[ { "id": "romeo-photo-id", "channel": "alice@capulet.lit" } ]</code></pre></div>
`replyTo`   | the parent post `id` if this post is a reply to another post | user | <div class="highlight"><pre style="position:absolute; right:0px;"><code>9b7724d0-7ef5-4331-8974-81754abb7ba0</code></pre></div>
`published` | the date when this post was created | server | <div class="highlight"><pre style="position:absolute; right:0px;"><code>2012-11-02T03:41:55.484Z</code></pre></div>
`updated`   | the last time there was a reply in this thread or when the post was created | server | <div class="highlight"><pre style="position:absolute; right:0px;"><code>2012-11-02T03:41:55.484Z</code></pre></div>


##Create Post

```shell
#POST https://demo.buddycloud.org/api/{channelID}/content/{nodeId}

curl https://demo.buddycloud.org/api/romeo@buddycloud.org/content/posts \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Content-Type: application/json" \
     -d '{ "content": "O Romeo, Romeo, wherefore art thou Romeo?" }'

#Response will be as follows:

201 Created
Location: https://demo.buddycloud.org/romeo@buddycloud.org/content/posts/$POST_ID
```

```javascript












```

<aside>You can define your own format for your own application nodes (e.g. `x-application-chessApp-move-history`). The [default channel nodes](#default-channel-nodes) have a pre-defined format and will reject posts that are not formated according to what the server expects. For example, the `posts` node expects to receive Activity stream events.</aside>

##Delete Post

```shell
#DELETE https://demo.buddycloud.org/api/{channelID}/content/{nodeID}/{postID}

curl https://demo.buddycloud.org/api/romeo@buddycloud.org/content/posts/$POST_ID \
     -X DELETE \
     -u juliet@buddycloud.org:romeo-forever 





```

```javascript










```

Removes a post from a node.

When a post is deleted,

* the post is deleted from the channel-node's history,
* a retraction message is sent to online users.

<aside>Deleting a post that references a mediaID will not remove the media object from the media server. That should be done seperately using a [delete media](#delete-media) query.</aside>

##Fetch Posts

```shell
#GET https://demo.buddycloud.org/api/{channelId}/content/{nodeId}

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/content/posts \
     -X GET \
     -H "Accept: application/json"

#Response would be as follows:

200 OK
Content-Type: application/json

[
    {
        "id": "foo",
        "author": "romeo@buddycloud.org",
        "updated": "1595-06-01T12:00:00Z",
        "content": "But, soft! What light through yonder window breaks? It is the east, and Juliet is the sun.",
        "media": null
    },
    ...
    {
        "id": "bar",
        "author": "romeo@buddycloud.org",
        "updated": "1591-06-04T12:00:00Z",
        "content": "Thus with a kiss I die.",
        "media": null
    }
]

#But if you want to use pagination:
#GET https://demo.buddycloud.org/api/{channelId}/content/{nodeId}?{queryParameter}={value}

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/content/posts?max=3 \
     -X GET \
     -H "Accept: application/json"

#Then, response would be as follows:

200 OK
Content-Type: application/json

{
    "items": [
        {
            "id": "foo",
            "author": "romeo@buddycloud.org",
            "updated": "1595-06-01T12:00:00Z",
            "content": "But, soft! What light through yonder window breaks? It is the east, and Juliet is the sun.",
            "media": null
        },
        ...
        {
            "id": "bar",
            "author": "romeo@buddycloud.org",
            "updated": "1591-06-04T12:00:00Z",
            "content": "Thus with a kiss I die.",
            "media": null
        }
    ],
    "rsm": {
        "count": "3",
        "index": "0"
    }
}
```

```javascript
































































```

Retrieves one or more posts using [pagination](#pagination) ranges.

This is useful for retrieving just the posts from an individual node. Consider using the [sync posts](#sync-posts) call for requesing posts across all channels a user follows.

<aside>Often it's useful to quickly show the 20 most recent posts. However some of these posts may reference a parent post outside of the apps's cache. 

To retrieve a missing parent post, you can query for the post ID referenced by the post's `replyTo`.</aside>


##Fetch Child Posts

```shell
#GET https://demo.buddycloud.org/api/{channelID}/content/{nodeId}/{postID}/replyto

curl https://demo.buddycloud.org/api/romeo@buddycloud.org/content/posts/$POST_ID/replyto \
     -X GET \
     -H "Accept: application/json"

#Response will be as follows:

200 OK
Content-Type: application/json

[
    {
        "id": "foo",
        "replyTo": "qux",
        "author": "romeo@buddycloud.org",
        "updated": "1595-06-01T12:00:00Z",
        "content": "But, soft! What light through yonder window breaks? It is the east, and Juliet is the sun.",
        "media": null
    },
    ...
    {
        "id": "bar",
        "replyTo": "qux",
        "author": "romeo@buddycloud.org",
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
