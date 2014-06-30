#Channels

Users subscribe to channels, which work in conjunction with nodes. Channels aggregate nodes that share related content. Channels represent broader topics while nodes represent related subtopics. The broad topic (or channel) of dog ownership has the following related subtopics (or nodes): feeding schedule, exercise requirements, training methods, and so on. Buddycloud divides channels into two categories: topic (as above) and personal (see example below).

The personal channel `juliet@capulet.lit` contains nodes for each type of information that `juliet` wants to share, such as her social activities, reflections on her mood, and the media she comments on. When `romeo@montague.lit` follows the channel `juliet@capulet.lit`, the app creates a subscription to all of the nodes under `juliet@capulet.lit`. 

![Channels and Nodes](/theme/static/img/diagrams/channel%20hierachy.png "Channels and Nodes")
**typo in the above pathway: "hierarchy"**


### Personal Channels v. Topic Channels


Trait       | _Personal_ Channel              | _Topic_ Channel
------------|---------------------------------|-----------------------
BuddycloudID| e.g. `juliet@capulet.lit`       | e.g. `montague-family@topics.montague.org`
Purpose     | represents a real person        | represents a topic
Namespace   | created in `<channelID>@example.com` |created in `<channelID>@topics.example.com`
Channel ID  | named after a user's `BuddycloudID`| not tied to a user's `BuddycloudID`
Owned By| owned by the matching `BuddycloudID`| can be owned by any user
Messaging   | can receive private chat messages| not applicable
Location Sharing| geolocation optionally shared with followers| anyone can search for nearby channels

### Channel Privacy Settings

Channels may be private or public. Channel Privacy is controlled by the channel's `access_model `:

               |Public Channel | Private Channel
---------------|---------------|-----------------
access_model   |open           |authorize
visibility     |anyone can view | requires a subscription request to view

The channel [metadata](#update-metadata) for _public_ and _private_ channels is always publicly accessible.

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

<aside>At sign-up, a personal channel is automatically created for each user. For example, `user@example.com` will automatically create a channel called `user@example.com`. Remember, new topic channels are created in their own namespace (`user@topics.example.com`).</aside>

### HTTP Request
`POST https://demo.buddycloud.org/api/{channelID}`


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
title               | true     | up to 50 characters | the channel's title
description         | true     | up to 200 characters | a short string describing the channel 
creation_date       | false    | [RFC3399](https://tools.ietf.org/html/rfc3339) timestamp | when the channel was created
access_model        | true    | `open`, `authorize` | whether the channel is `public` or `private` **changed description to match style guide**
channel_type        | false   | `personal`, `topic` | whether this is a `personal` channel or a `topic` channel
default_affiliation | true | `publisher`, `follower` | the permissions a new subscriber is granted

A complete set of channel metadata is available from the [Buddycloud protocol specification](http://buddycloud.github.io/buddycloud-xep/#default-roles). 

### HTTP Request
`POST https://demo.buddycloud.org/api/{channelID}/metadata/{nodeID}`
