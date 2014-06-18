#Channels

A channel is a group of nodes.

Each node contains a feed of items with similarly structured content.

For example:
-the `posts` node contains a feed of activity-stream items.
-The `status` node contains a single entry:  your current mood.

Channels (and their nodes) share a common set of followers, publishers and metadata.

Each channel is preconfigured with a group of default nodes:
* `posts`
* `status`
* `geoloc-past`
* `geoloc`
* `geoloc-future`
* `public-key`

Applications can easily create new nodes and content types. For example, a game might create a node `game-highscore` so that followers receive realtime updates of new scores.

Following a channel grants one access to that channels current [and future] nodes. 

<aside>Each user has a channel automatically created for them on sign-up that that matches their ID. For example `user@example.com` will have a channel created called `user@example.com`</aside>

##Create Channel

```shell
@guilhermesgb: The personal channels of a user are created alongside with their accounts through the Create Account endpoint. Through the HTTP API, one can only create topic channels:

curl --user juliet@buddycloud.org:romeo-forever \
    https://demo.buddycloud.org/api/capulet@topics.buddycloud.org \
    -X POST
```

```javascript```
???
???
```

Each Buddycloud user has a personal channel automatically created for them (`user@example.com`). New topic channels are created in their own namespace (`user@topics.example.com`).

### HTTP Request
`POST https://demo.buddycloud.org/api/:topic-channel-name`

<aside class="warning">Requires Basic Authentication.</aside>

##Update Metadata

```shell
curl --user juliet@buddycloud.org:romeo-forever \
    https://demo.buddycloud.org/api/juliet@buddycloud.org/metadata/posts \
    -X POST \
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

Metadata allows you to describe the channel, set defaults and even apply a location to the channel.

Metadata is visible for both public and private channels.

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

<aside class="warning">Requires Basic Authentication.</aside>

##Delete Channel

```shell
@guilhermesgb: There's no way to delete a channel other than using the Delete Account endpoint (makes sense, as one should not exist without the other), so I don`t know what should be here. Another problem is: we simply don't have an HTTP API endpoint for deleting specific nodes.
```

```javascript```
???
???
```

Removes a channel from the system. 

<aside class="notice">???Lloyd - could you write about what this does to the subscription list of the channels followers???</aside>


### HTTP Request
`POST https://demo.buddycloud.org/api/????`

##Default Nodes

The following default nodes are created. Additional nodes can be created by the channel owner.

Channel node    | Description 
--------------- | -----------
status          | A one line status message 
posts           | ATOM formatted activy stream 
geoloc-previous | Where they were              
geoloc-current  | Where they are              
geoloc-future   | Where they will go next   
public-key      | Users can optionally publish their public key

Default nodes are defined in the [Buddycloud protocol specification](http://buddycloud.github.io/buddycloud-xep/#well-known-nodes).

##Create Node

```shell
@guilhermesgb: There's no HTTP API endpoint for creating specific nodes.
```

```javascript```
???
???
```

It's recommended to create new nodes for new application types. You can then use this node for sharing information between devices or as a simple data store for your application.

For example perhaps your chess app created a `x-chess-activity-stream` node.  You could then share this node with competing players and keep state between two games.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`
