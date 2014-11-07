#Nodes

Nodes are publish-subscribe streams of posts with the same content type. For example, the channel `juliet@capulet.lit` is an aggregation of nodes for each type of information that `juliet` wants to share. Examples of such nodes could be:

- `juliet@capulet.lit/social` node (the serialization of `juliet@capulet.lit`'s social activities)
- `juliet@capulet.lit/status` node (a text string describing `juliet@capulet.lit`'s mood)
- `juliet@capulet.lit/music-i-liked` node (a hypothetical [activity stream](http://activitystrea.ms/specs/json/1.0/) of music `juliet@capulet.lit` likes)

Each of these nodes have:

- a set of followers;
- a set of publishers;
- metadata (e.g. `title`, `description` and `location` fields).

### Personal Nodes v. Topic Nodes

Buddycloud divides nodes into two categories: `topic` and `personal`.

For example, the channel `juliet@capulet.lit` comprises personal nodes for each type of information that `juliet` wants to share, such as her social activities, reflections on her mood, and the media she comments on. 


Trait       | _Personal_ Node              | _Topic_ Node
------------|---------------------------------|-----------------------
channelID   | e.g. `juliet@capulet.lit/{nodeID}`       | e.g. `montague-family@topics.montague.org/posts`
Purpose     | represents a real person        | represents a topic
Namespace   | created in `<channelID>@example.com` |created in `<channelID>@topics.example.com`
ChannelID   | named after a user's `username`| not tied to a user's `username`
Owned By    | owned by the matching `username`| can be owned by any user
Messaging   | can receive private chat messages| not applicable
Location Sharing| geolocation optionally shared with followers| anyone can search for nearby channels

### Node Privacy Settings

Nodes may be private or public. Node Privacy is controlled by the node's `access_model `:

               |Public Node | Private Node
---------------|---------------|-----------------
access_model   |open           |authorize
visibility     |anyone can view | requires a subscription request to view

The node [metadata](#update-metadata) for _public_ and _private_ node is always publicly accessible.

### Who creates the set of nodes for a channel?

Your application is responsible for creating the set of nodes it is going to use for a given channel. For example, the social application running at <https://demo.buddycloud.org> automatically creates the following nodes everytime a new channel is created:

Name             | Personal Channel |Topic Channel | Description 
-----------------|:---------------: |:------------:|----------------
status           | ✓                | ✓            | a one-line status message 
posts            | ✓                | ✓            | ATOM formatted activity stream 
geoloc-previous  | ✓                | ✗            | where they were              
geoloc-current   | ✓                | ✗            | where they are              
geoloc-future    | ✓                | ✗            | where they will go next   
public-key       | ✓                | ✗            | public key for secure messaging

##Create Node

```shell
#POST https://demo.buddycloud.org/api/{channelID}/{nodeID}

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/posts \
    -X POST \
    -u juliet@buddycloud.org:romeo-forever



















```

```javascript
#XMPP-FTW event 'xmpp.pubsub.create'

socket.send(
    'xmpp.pubsub.create',
    {
        "to": "pubsub.buddycloud.org",
        "node": "/user/juliet@buddycloud.org/posts",
        "options": [
            {
                "var": "buddycloud#channel_type",
                "value": "personal"
            },
            {
                "var": "pubsub#title",
                "value": "Juliet's posts node"
            },
            {
                "var": "pubsub#access_model",
                "value": "open"
            }
        ]
    },
    function(error, data) { console.log(error, data) }
)
```

This allows creation of nodes.

##Delete Node

```shell
#DELETE https://demo.buddycloud.org/api/{channelID}/{nodeID}

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/posts \
    -X DELETE \
    -u juliet@buddycloud.org:romeo-forever




```

```javascript
#XMPP-FTW event 'xmpp.pubsub.delete'

socket.send(
    'xmpp.pubsub.delete',
    {
        "to": "pubsub.buddycloud.org",
        "node": "/user/juliet@buddycloud.org/posts"
    },
    function(error, data) { console.log(error, data) }
)
```

This will remove a node.

##Fetch Metadata

```shell
#GET https://demo.buddycloud.org/api/{channelID}/metadata/{nodeID}

curl https://demo.buddycloud.org/api/juliet@buddycloud.org/metadata/posts \
     -X GET \
     -u juliet@buddycloud.org:romeo-forever
```

```javascript
#XMPP-FTW event 'xmpp.pubsub.config.set'

socket.send(
    'xmpp.pubsub.config.get',
    {
        "to": "pubsub.buddycloud.org",
        "node": "/user/juliet@buddycloud.org/posts",
    },
    function(error, data) { console.log(error, data) }
)
```


Metadata allows you to describe the node, set defaults and even add a location to the node so that it will show up in nearby queries.

Node metadata is always visible for both public and private nodes.

### Parameters

Argument            | Editable | Values | Description
------------------- | -------- | -------| -----------
channelID           | false    | ≤1023 bytes | e.g. `user@example.com` or `topic@topics.example.com`
title               | true     | up to 50 characters | the node's title
description         | true     | up to 200 characters | a short string describing the node 
creation_date       | false    | [RFC3399](https://tools.ietf.org/html/rfc3339) timestamp | when the node was created
access_model        | true    | `open`, `authorize` | whether the node is `public` or `private` **changed description to match style guide**
channel_type        | false   | `personal`, `topic` | whether this is a `personal` node or a `topic` node
default_affiliation | true | `publisher`, `follower` | the permissions a new subscriber is granted

A complete set of node metadata is available from the [Buddycloud protocol specification](http://buddycloud.github.io/buddycloud-xep/#default-roles). 


##Update Metadata

```shell
#POST https://demo.buddycloud.org/api/{channelID}/metadata/{nodeID}

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
#XMPP-FTW event 'xmpp.pubsub.config.set'

socket.send(
    'xmpp.pubsub.config.set',
    {
        "to": "pubsub.buddycloud.org",
        "node": "/user/juliet@buddycloud.org/posts",
        "form": [
            {
                "var": "pubsub#title",
                "value": "New Juliet's Posts Node Title"
            },
            {
                "var": "pubsub#description",
                "value": "Everything about Juliet"
            },
            {
                "var": "buddycloud#default_affiliation",
                "value": "publisher"
            }
        ]
    },
    function(error, data) { console.log(error, data) }
)
```


