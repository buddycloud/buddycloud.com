#Channels

Channels help you group together similar content in a way that is easily understandable to your users. 

This content is grouped into nodes that together represent a channel. 

Each node node is contains a list of posts.

![Channels and Nodes](/theme/static/img/diagrams/channel%20hierachy.png "Channels and Nodes")



### Channel Types

There are two types of channels in Buddycloud:

_Personal_ Channels                            | _Topic_ Channels 
-----------------------------------------------|--------------------------------------------------------------
e.g. `juliet@capulet.lit`                      | e.g. `montague-family@topics.montague.org`
created in `<channelID>@example.com` namespace | created in `<channelID>@topics.example.com` namespace
represent a real person                        | represent a topic
named after a user's `BuddycloudID`            | not tied to a user's `BuddycloudID`
owned by the maching BuddycloudID              | can be owned by any user
can also receive private chat messages         | not applicable
geolocation optionally shared with followers   | anyone can search for nearby channels

### Channel Privacy Settings

Channels may be private or public.

Channel Privacy is controlled by the channel's `access_model `:

               |Public channel | Private channel
---------------|---------------|-----------------
access_model   |open           |authorize
visibility     |Anyone can view | Requires a subscription request to view

The channel [metadata](#update-metadata) for _public_ and _private_ channels is alway's publically accessible.

##Create Channel

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

<aside class="notice">???Add a bit about how events are sent out to subscribers on the local and remote servers???</aside>


### HTTP Request
`POST https://demo.buddycloud.org/api/????`

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
title               | true     | ???@lloyd: max length? | The channel's title.
description         | true     | ???@lloyd: max length? | A short string describing the channel 
creation_date       | false    | [RFC3399](https://tools.ietf.org/html/rfc3339) timestamp | When the channel was created
access_model        | true    | `open`, `authorize` | Whether the channel is `open` for anyone to view or if followers should first be `authorize`d to view it.
channel_type        | false   | `personal`, `topic` | Whether this is a users `personal` channel or a `topic` channel
default_affiliation | true | `publisher`, `follower` | The role new followers inherit

A complete set of channel metadata is avaliable from the [Buddycloud protocol specification](http://buddycloud.github.io/buddycloud-xep/#default-roles). 

### HTTP Request
`POST https://demo.buddycloud.org/api/:channel-name/metadata/:node`
