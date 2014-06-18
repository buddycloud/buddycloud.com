#Channels

Channels help you group together similar content in nodes in a way that is easily understandable to your users. This content is grouped into nodes. A node is simply a stream of events.

An example: The channel `juliet@capulet.lit` contains nodes for each type of information that `juliet` wants to share. When `romeo@montague.lit` follows the channel `juliet@capulet.lit` a subscription is created for `juliet@capulet.lit` nodes:
- `posts` node (the serialization `juliet@capulet.lit`'s of social activities)
- `status` node (a text string describing `juliet@capulet.lit`'s mood)
- `music-i-liked` (a hypothetical (activity stream)[http://activitystrea.ms/specs/json/1.0/] of music `juliet@capulet.lit` liked)

Together these nodes are described as the `juliet@capulet.lit` channel and share a common set of followers, publishers and metadata.

Your application can use default channel nodes or define new channel nodes with new content types. To make things easier for you, each channel is preconfigured with a group of default nodes:
- `posts`
- `status`
- `geoloc-past`
- `geoloc`
- `geoloc-future`
- `public-key`

<img src="/static/img/diagrams/channels comprise application nodes.png">

### Channel Types

There are two types of channels in Buddycloud:

_Personal_ Channels                            | _Topic_ Channels 
-----------------------------------------------|--------------------------------------------------------------
(for example: `juliet@capulet.lit`)            | (for eample: `montague-family@topics.montague.org`)
created in `<channelID>@example.com` namespace | created in `<channelID>@topics.example.com` namespace
represent a real person                        | represent a topic
named after a user's `BuddycloudID`            | not tied to a user's `BuddycloudID`
channel name matches the user's BuddycloudID   | owned by any user
can also receive private chat messages         | not applicable
geolocation optionally shared with followers   | anyone can search for nearby channels

##Create Topic Channel

```shell
curl https://demo.buddycloud.org/api/capulet@topics.buddycloud.org \
     -X POST
     -u juliet@buddycloud.org:romeo-forever
```

```javascript```
???
???
```

Users can create any number of topic channels. An error is returned if there is an existing channel with the same `ChannelID`.

<aside>At sign-up, each user has a personal channel automatically created for them. For example `user@example.com` will have a channel created called `user@example.com` auto-created. Remember, new topic channels are created in their own namespace (`user@topics.example.com`).</aside>

### HTTP Request
`POST https://demo.buddycloud.org/api/:topic-channel-name`

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

```javascript```
???
???
```

Metadata allows you to describe the channel, set defaults and even add a location to the channel so that it will show up in nearby queries.

Channel metadata is always visible for both public and private channels.

### Parameters

Argument            | Editable | Values | Description
------------------- | -------- | -------| -----------
title               | true     | ??? characters | The channel's title.
description         | true     | ??? characters | A short string describing the channel 
creation_date       | false    | RFC3399 format timestamp | When the channel was created
access_model        | false    | open, authorize | Whether the channel is `open` for anyone to view or if followers should first be `authorize`d to view it.
channel_type        | false    | personal, topic, | Whether this is a users `personal` channel or a `topic` channel
default_affiliation | true | publisher, follower | The role new followers inherit

A complete set of channel metadata is avaliable from the [Buddycloud protocol specification](http://buddycloud.github.io/buddycloud-xep/#default-roles). 

### HTTP Request
`POST https://demo.buddycloud.org/api/:channel-name/metadata/:node`

##Delete Channel

```shell
???@guilhermesgb: There's no way to delete a channel other than using the Delete Account endpoint (makes sense, as one should not exist without the other), so I don't know what should be here. Another problem is: we simply don't have an HTTP API endpoint for deleting specific nodes.

???st: I guess we are missing this... :()

```

```javascript```
???
???
```

Removes a channel from the Buddycloud Server.

<aside class="notice">???Lloyd - could you write about what this does to the subscription list of the channels followers???</aside>


### HTTP Request
`POST https://demo.buddycloud.org/api/????`

##Default Channel Nodes

The following default nodes are created. Additional nodes can be created by the channel owner.

Node Name        | Personal Channel |Topic Channel | Description 
-----------------|:---------------: |:------------:|----------------
status           | ✓                | ✓            | A one line status message 
posts            | ✓                | ✓            | ATOM formatted activy stream 
geoloc-previous  | ✓                | ✗            | Where they were              
geoloc-current   | ✓                | ✗            | Where they are              
geoloc-future    | ✓                | ✗            | Where they will go next   
public-key       | ✓                | ✗            | Public key for secure messaging

Default nodes are defined in the [Buddycloud protocol specification](http://buddycloud.github.io/buddycloud-xep/#well-known-nodes).

##Create Node

```shell
@guilhermesgb: There's no HTTP API endpoint for creating specific nodes.
```

```javascript```
???
???
```

It's recommended to create new nodes for new applications. `X-application-<your-application-name>` will avoid bumping into other developers application data.

For example perhaps your chess app created a `x-application-ChessApp` node.  You could then share this node with competing players and keep state between two games.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`
