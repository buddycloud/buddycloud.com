#Realtime

To get content updates in realtime directly through the REST API, your application can rely on long-polling an endpoint specifically designed with this goal in mind. The first section below depicts it in detail.

But to make your application truly aware of all kinds of Buddycloud events, you'll need more.

If you're building a mobile app, you can set it up so that it will listen for incoming push notifications when important events happen. The last sections below describe every step needed to make your app fully Buddycloud-powered.

Otherwise, the recommended thing is to have your app use [XMPP-FTW](https://xmpp-ftw.jit.su/manual/extensions/buddycloud/). Please also refer to this guide with more on [how to get started](http://buddycloud.com/get-started-javascript).

##New Post Updates

> ###First, get the last known timestamp

> `GET` /api/notifications/posts

> ###Example

> Asking for the last known timestamp, using `curl`:

```shell
curl https://buddycloud.com/api/notifications/posts \
    -X GET
```

> Response would be as follows:

```shell
{
    "last": "$LAST_TIMESTAMP",
    "items": []
}
```

> ###Finally, start long polling

> `GET` /api/notifications/posts?since=`lastTT`

> ###Example

> Using the last known timestamp to start long polling:

```shell
curl https://buddycloud.com/api/notifications/posts?since=$LAST_TIMESTAMP \
    -X GET
```

> Once a new update arrives, response would be as follows:

```shell
{
    "last": "$LAST_TIMESTAMP_UPDATED",
    "items": [
        {
            "id": "$POST_ID",
            "source": "juliet@buddycloud.com/posts"
            "author": "romeo@buddycloud.com"
            "published": "2014-06-24T15:34:54.449Z",
            "updated": "2014-06-24T15:34:54.449Z",
            "content": "This the newest post in town",
            "media": null,
            "replyTo": "$PARENT_POST_ID"
        }
        ...
        [Potentially more posts from this node or other nodes here]
    ]
```

> Don't forget that the last known timestamp now is `$LAST_TIMESTAMP_UPDATED`!

###Get New Post Updates By Long Polling

Use this endpoint to start long polling for new posts updates.
Multiple updates shall arrive at a time, for all nodes the user is subscribed to (the user your app is currently working with).

Your application will need to provide the last known timestamp `lastTT` everytime it makes a new long polling request.
On the right there are good examples of the intended flow of this process of getting new posts updates.

A new posts update should arrive in the form of a JSON response comprised of all the new posts' contents alongside information about the nodes that the new post belong to, respectively (the `source` key of each post has this value).
