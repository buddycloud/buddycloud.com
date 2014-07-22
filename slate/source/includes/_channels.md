#Channels

Users subscribe to channels, which work in conjunction with nodes. Channels aggregate nodes that share related content. Channels represent broader topics while nodes represent related subtopics. The broad topic (or channel) of dog ownership has the following related subtopics (or nodes): feeding schedule, exercise requirements, training methods, and so on.


![Channels and Nodes](/theme/img/diagrams/channel%20hierachy.png "Channels and Nodes")

##Create Channel

```shell
curl https://demo.buddycloud.org/api/capulet@topics.buddycloud.org \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever
```

```javascript
socket.send(
    'xmpp.buddycloud.create',
    {
        "node": "/user/balcony-speeches@topics.montague.lit/posts",
    },
    function(error, data) { console.log(error, data) }
)
```

Users can create any number of topic channels. An error is returned if there is an existing channel with the same `ChannelID`.

<aside>At sign-up, a personal channel is automatically created for each user. For example, `juliet@capulet.lit` signing up will trigger the server to automatically create a channel called `juliet@capulet.lit`. Remember, new topic channels are created in their own namespace (`channelID@topics.example.com`).</aside>

### HTTP Request
`POST https://demo.buddycloud.org/api/{channelID}`


##Delete Channel

```shell
curl https://demo.buddycloud.org/api/capulet@topics.buddycloud.org \
     -X DELETE \
     -u juliet@buddycloud.org:romeo-forever
```

```javascript
???	
???
```

Removes a channel from the Buddycloud Server.

<aside class="notice">???Add a bit about how events are sent out to subscribers on the local and remote servers???</aside>


### HTTP Request
`DELETE https://demo.buddycloud.org/api/{channelID}`

##Update Metadata

```shell
curl https://demo.buddycloud.org/api/juliet@buddycloud.org/metadata/posts \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Content-Type: application/json" \
     -d '{ \
            "title": "New Juliet`s Posts Node Title", \
            "description": "Everything about Juliet", \
            "default_affiliation": "publisher" \
         }'
```

```javascript
???
???
```

Metadata allows you to describe the channel, set defaults and even add a location to the channel so that it will show up in nearby queries.

Channel metadata is always visible for both public and private channels.

### Parameters

Argument            | Editable | Values | Description
------------------- | -------- | -------| -----------
channelID           | false    | ≤1023 bytes | e.g. `user@example.com` or `topic@topics.example.com`
title               | true     | up to 50 characters | the channel's title
description         | true     | up to 200 characters | a short string describing the channel 
creation_date       | false    | [RFC3399](https://tools.ietf.org/html/rfc3339) timestamp | when the channel was created
access_model        | true    | `open`, `authorize` | whether the channel is `public` or `private` **changed description to match style guide**
channel_type        | false   | `personal`, `topic` | whether this is a `personal` channel or a `topic` channel
default_affiliation | true | `publisher`, `follower` | the permissions a new subscriber is granted

A complete set of channel metadata is available from the [Buddycloud protocol specification](http://buddycloud.github.io/buddycloud-xep/#default-roles). 

### HTTP Request
`POST https://demo.buddycloud.org/api/{channelID}/metadata/{nodeID}`
