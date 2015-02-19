#Posts

New posts to a node are automaticaly:

* pushed to the channel's online followers
* spooled up for the channel's offline followers
* pushed to the [firehose](#access-firehose)
* archived and retrievable using the [fetch posts](#fetch-posts) method.
* indexed by the [channel crawler](https://github.com/buddycloud/channel-directory)

Different channel types have different post formats.

> Field value examples:

### Post Parameters

Field       | Description | Responsible | <div style="display:none;">Example</div>
------------|-------------|--------|---------
`author`    | the `username` of this post's author, set by the server  | server | <div class="highlight"><pre style="position:absolute; right:0px;"><code>juliet@capulet.lit</code></pre></div>
`content`   | the post's content - usually this is activity stream event | user   | <div class="highlight"><pre style="position:absolute; right:0px;"><code>O Romeo, Romeo! Wherefore art thou Romeo?</code></pre></div>
`id`        | the unique post ID assigned to this post by the server | server | <div class="highlight"><pre style="position:absolute; right:0px;"><code>17163726-ea90-453e-ad25-455336a83fd4</code></pre>
`media`     | a list of media objects this post might refer to | user | <div class="highlight"><pre style="position:absolute; right:0px;"><code>[ { "id": "romeo-photo-id", "channel": "alice@capulet.lit" } ]</code></pre></div>
`replyTo`   | the parent post `id` if this post is a reply to another post | user | <div class="highlight"><pre style="position:absolute; right:0px;"><code>9b7724d0-7ef5-4331-8974-81754abb7ba0</code></pre></div>
`published` | the date when this post was created | server | <div class="highlight"><pre style="position:absolute; right:0px;"><code>2012-11-02T03:41:55.484Z</code></pre></div>
`updated`   | the last time there was a reply in this thread or when the post was created | server | <div class="highlight"><pre style="position:absolute; right:0px;"><code>2012-11-02T03:41:55.484Z</code></pre></div>


##Create Post

> `POST` /api/`channelID`/content/`nodeID`

> ###Example
> Creating a new post to the `posts` node of `romeo@buddycloud.org`, using `curl`:

```shell
curl https://demo.buddycloud.org/api/romeo@buddycloud.org/content/posts \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Content-Type: application/json" \
     -d '{ "content": "O Romeo, Romeo, wherefore art thou Romeo?" }'
```

> Response will be as follows:

```shell
HTTP/1.1 201 Created

Location: https://demo.buddycloud.org/romeo@buddycloud.org/content/posts/$POST_ID
```

Use this endpoint to create new post to a given node.

<aside>You can define your own format for your own application nodes (e.g. <kbd>x-application-chessApp-move-history</kbd>). The default channel nodes have a pre-defined format and will reject posts that are not formated according to what the server expects. For example, the <kbd>posts</kbd> node expects to receive Activity stream events.</aside>

##Delete Post

> `DELETE` /api/`channelID`/content/`nodeID`/`postID`

> ###Example
> Deleting post of id `$POST_ID` from the `posts` node of `romeo@buddycloud.org`, using `curl`:

```shell
curl https://demo.buddycloud.org/api/romeo@buddycloud.org/content/posts/$POST_ID \
     -X DELETE \
     -u juliet@buddycloud.org:romeo-forever 
```

Removes a post from a node.

When a post is deleted,

* the post is deleted from the channel-node's history,
* a retraction message is sent to online users.

<aside>Deleting a post that references a <kbd>mediaID</kbd> will not remove the media object from the media server. That should be done seperately using a delete media query.</aside>

##Fetch Posts

> `GET` /api/`channelID`/content/`nodeID`

> ###Example
> Fetching the 20 most recent posts from a node, using `curl`:

```shell
curl https://demo.buddycloud.org/api/juliet@buddycloud.org/content/posts \
     -X GET \
     -H "Accept: application/json"
```

> Response would be as follows:

```shell
HTTP/1.1 200 OK
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
```

> ###Same endpoint using pagination

> `GET` /api/`channelID`/content/`nodeID`?`param`=`val`&`param`=`val`...

> ###Example
> Fetching posts from a node using pagination, using `curl`:

```shell
curl https://demo.buddycloud.org/api/juliet@buddycloud.org/content/posts?max=3 \
     -X GET \
     -H "Accept: application/json"
```

> Then, response would be as follows:

```shell
HTTP/1.1 200 OK
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

Retrieves one or more posts using pagination ranges.

This is useful for retrieving just the posts from an individual node.

<aside>Often it's useful to quickly show the 20 most recent posts. However some of these posts may reference a parent post outside of the apps' cache. 

To retrieve a missing parent post, you can query for the post ID referenced by the post's <kbd>replyTo</kbd> field.</aside>

###Pagination

Buddycloud uses [Result Set Management](http://xmpp.org/extensions/xep-0059.html) for pagination. This is useful when:

* building mobile applications and needing to limit the amount of data that the API sends back. 
* your app needs to retrieve new messages since it was last online.

###Query Parameters

You will pass pagination parameters via the URL query part.

Parameter | Description
--------- |  -----------
`max`     | The maximum number of returned entries
`before`  | Get posts before this timestamp
`after`   | Return only entries older than the entry with the specified ID

###Response Attributes

The following attributes are returned in a paged query response:

Parameter | Description
--------- |  -----------
`count`   | The total number of entries that the query would return
`first`   | The ID of the first item in the page
`last`    | The ID of the last item in the page
