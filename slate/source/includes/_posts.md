#Posts

New posts to a channel are automatically pushed to all subscribers of that channel. Posts to public channels are also pushed to the server's firehose. 

New public posts are automaticaly
* pushed to online subscribers
* pushed to the server's firehose
* queued for offline subscribers
* archived and avalible for querying
* indexed by the [channel crawler](https://github.com/buddycloud/channel-directory)

##Create Post

```shell
curl https://demo.buddycloud.org/api/???? \
 --??? \
 --???
```

```javascript```

```

```json

```

New posts should conform to the content type of the node. 

For example the `posts` node expects Activity Streams format.

### HTTP Request

`POST https://demo.buddycloud.org/api/:channel-name:/content/posts`

##Delete Post

```shell
curl https://demo.buddycloud.org/api/???? \
 --??? \
 --???
```

```javascript```
???
???
```

```json
???
???
```

Removes a single post from a node. 

The Buddycloud server will also issue a retraction message to the channel's subscribers.

### HTTP Request

`???DELETE? https://demo.buddycloud.org/api/:channel-name:/content/posts`

##Fetch Posts

```shell
curl https://demo.buddycloud.org/api/???? \
 --??? \
 --???
```

```javascript```
???
???
```

```json
???
???
```

Retrieves posts using [pagination](#Pagination) ranges.

### Queriyng for child posts

You can query using the [Atom threading extensions](http://www.ietf.org/rfc/rfc4685.txt] for children of posts. ???@abmar: how do we get children? ???

### Quering for parent posts

Often it's useful to quickly paint a clients screen with a query for the 20 most recent posts. However some of these posts may references a parent post outside of the clients post cache. To retrieve a missing parent post, query for the post ID that matches the clients `replyTo`.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`

### Sync Posts

Sometimes it's necessary to quickly retrieve a number of posts to draw a client screen. For example a client that shows 10 posts per channel. In this case, you can run a query that breaks down to "show me [up to] 10 posts per channel newer than [date of most recent post in client cache]. This avoids the problem of a very busy channel "drowning out" other posts during a client synchronisation.

Paramenter | Required | Value      | Description
-----------|----------|------------|------------
since      | true     | ISO 8601 timestamp | of the most recent posts in the client's cache
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

Vote or upvote posts

##Firehose Access

```shell
@justin ???
```

```javascript```
???
???
```

```json
???
???
```

The firehose node `???what is the node???` contains a feed of all public channel posts. It can be queried for historical posts as well as feed out new posts in realtime.
