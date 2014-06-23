#Posts

To create new content, your users post to a [channel-node](#channel-nodes).

New post is are automaticaly:

* pushed to the channel's online followers
* spooled up for the channel's offline followers
* pushed to the server's firehose
* archived and retrievable using the [fetch posts](#fetch-posts) method.
* indexed by the [channel crawler](https://github.com/buddycloud/channel-directory)

Different channel types have different post formats.

### Post Parameters

Field       | Description | Set by | Example
------------|-------------|--------|---------
`author`    | BuddycloudID| server | `juliet@capulet.lit`
`content`   | [usually] Activity stream content | user   | `O Romeo, Romeo! wherefore art thou Romeo?` 
`id`        | a unique-per-Buddycloud-site ID | server | `17163726-ea90-453e-ad25-455336a83fd4`
`media`     | a list of media objects the post might refer to | user | `[{"id": "romeo-photo-id", "channel": "alice@capulet.lit"}]`
`replyTo`   | parent post `id` | user |`9b7724d0-7ef5-4331-8974-81754abb7ba0`
`published` | when the post was created | server | `2012-11-02T03:41:55.484Z`
`updated`   | the last time there was a reply in this thread or when the post was created | server | `2012-11-02T03:41:55.484Z`


##Create Post

```shell
curl https://demo.buddycloud.org/api/romeo@buddycloud.org/content/posts \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Content-Type: application/json" \
     -d '{ "content": "O Romeo, Romeo, wherefore art thou Romeo?" }'
```

```shell
201 Created
Location: https://demo.buddycloud.org/romeo@buddycloud.org/content/posts/$POST_ID
```

```javascript
???
```

Creating a post adds a new item to a channel's node. 

???The server will timestamp the message/the client's timestamp will be respected?'

<aside class="warning">You can define your own format for your own application nodes (for example `x-application-chessApp-move-history`). The [default channel nodes](#default-channel-nodes) have a pre-defined format and will reject posts that are not formated according to what the server expects. For example, the `posts` node expects to receive Activity stream events.</aside>

### HTTP Request

`POST https://demo.buddycloud.org/api/:channel-name:/content/posts`

##Delete Post

```shell
@guilhermesgb: Maybe explain beforehand how to retrieve a POST_ID using the GET method?

curl https://demo.buddycloud.org/api/romeo@buddycloud.org/content/posts/$POST_ID \
     -X DELETE \
     -u juliet@buddycloud.org:romeo-forever 
```

```javascript```
???
???
```

Removes a single post from a node.

The Buddycloud server will also issue a retraction message to the channel's subscribers.

<aside>Deleting a post that references a mediaID will not remove the media object from the media server. That should be done seperately using a [delete media](#delete-media) query.</aside>

### HTTP Request

`DELETE https://demo.buddycloud.org/api/:channel-name:/content/:node-name:/:post-id:`

##Fetch Posts

```shell
curl https://demo.buddycloud.org/api/juliet@buddycloud.org/content/posts \
     -X GET \
     -H "Accept: application/json"
     ???Guilherme - can you give an example using pagination please???
```

```shell
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
```

```javascript```
???
???
```

Retrieves one or more posts using [pagination](#pagination) ranges.

The Buddycloud server will store all posts including post revocations (deleted posts).

##Fetch Child Posts


```shell
POST_ID=qux
curl https://demo.buddycloud.org/api/romeo@buddycloud.org/content/posts/$POST_ID/replyto \
     -X GET \
     -H "Accept: application/json"
```

```shell
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

````

Buddycloud uses the [Atom threading extensions](http://www.ietf.org/rfc/rfc4685.txt) to enable you to easily query for child posts.

### HTTP Request
`GET https://demo.buddycloud.org/api/:channel-name:/content/posts/:post-id/replyto`

## Fetch Parent Posts

Often it's useful to quickly show the 20 most recent posts. However some of these posts may references a parent post outside of the client's cache. To retrieve a missing parent post, you can query for the post ID that matches the clients `replyTo`.

```shell
???
```

```javascript

````

### HTTP Request
`GET https://demo.buddycloud.org/api/:channel-name:/content/posts`
`GET https://demo.buddycloud.org/api/:channel-name:/content/posts/:post-id`

###Sync Posts

```shell
???
```

```javascript

````

Sometimes it's useful to quickly retrieve a number of posts to draw a client screen. A client might want to just show the latest 10 posts per channel (older posts can be paged in as the users scrolls down). 

The `sync` query is a "show me [???up to???] 10 posts per channel newer than [date of most recent post in client cache]. This avoids the problem of a very busy channel "drowning" other posts during a client synchronisation.

Paramenter | Required | Value      | Description
-----------|----------|------------|------------
since      | true     | ISO 8601 timestamp ??? seriously??? | of the most recent posts in the client's cache 
max        | false    | integer    | the maximum number of posts to be returned per channel
summary    | false    | true,false | returns only summary information per channel (not posts)

##Upvote Post

```javascript```
???
???
```

```json
???
???
```

Your users can give feedback to eachother by upvoting/liking posts. Upvotes take a value of 1 to 5. It's recommended that for a binary "like" you simply apply a value of 5.

##Access Firehose

```shell
lloyd???
```

```javascript```
???
???
```

The firehose node `???what is the node???` contains a feed of all public channel posts from the local Buddycloud server. 

The firehose node can also be queried for historical posts using [pagination](#pagination)

The firehose will only show posts from public channels.
