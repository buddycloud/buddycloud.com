#Followers

Followers of the nodes in a channel have one of the following affiliations:

Affiliation | User sees      | Description
-----------|----------------|-------------
`owner`    |`owner`         |add/remove moderators 
`moderator`|`moderator`     |approve subscription requests & delete posts
`publisher`|`follower+post` |create new posts
`member`   |`follower`      |only view posts
`pending`  |`pending`       |nothing
`outcast`  | `null`         |only visibile to the `owner` and `moderator` affiliation.

The `outcast` affiliation is useful for dealing with abusive users. 

<aside>Once a user is an `outcast`, they can no longer post or generate subscripion requests to that channel. Only the channel's `owner` and the channel's `moderator`s can view users the list of `outcast` users.</aside>

##Fetch Followers

```shell
#GET https://demo.buddycloud.org/api/{channelId}/subscribers/{nodeId}

curl https://demo.buddycloud.org/api/romeo@buddycloud.org/subscribers/posts \
     -X GET \
     -u romeo@buddycloud.org:juliet-forever \
     -H "Content-Type: application/json"

#Response would be as follows:

200 OK
Content-Type: application/json

{
    "romeo@buddycloud.org": "owner",
    "benvolio@buddycloud.org": "publisher"
}
```

```javascript
















```

This request returns a list of channel followers and their affiliation in the channel.

Public channels | Private Channels
----------------|------------------
Return the list without authentication | requesting user must also be an `owner` `moderator` `publisher` or `member` of the channel

##Retrieve Pending Followers

```shell
#GET https://demo.buddycloud.org/api/{channelId}/subscribers/{nodeId}/approve

curl https://demo.buddycloud.org/api/romeo@buddycloud.org/subscribers/posts/approve \
     -X GET \
     -u romeo@buddycloud.org:juliet-forever \
     -H "Content-Type: application/json"

#Response would be as follows:

200 OK
Content-Type application/json

[
    {
        "subscription": "subscribed",
        "jid": "benvolio@buddycloud.org"
    },
    {
        "subscription": "pending",
        "jid": "juliet@buddycloud.org"
    },
    {
        "subscription": "pending",
        "jid": "tybalt@buddycloud.org"
    }
]
```

```javascript


























```

Retrieves the list of subscriptions of a node. Returns a list of objects containing the subscriber JID and the values of its subscription state (`subscribed` or `pending`).

##Authorise Pending Followers

```shell
#POST https://demo.buddycloud.org/api/{channelId}/subscribers/{nodeId}/approve

curl https://demo.buddycloud.org/api/romeo@buddycloud.org/subscribers/posts/approve \
     -X POST \
     -u romeo@buddycloud.org:juliet-forever \
     -H "Content-Type: application/json" \
     -d '[ \
             { \
                 "subscription": "subscribed", \
                 "jid": "juliet@buddycloud.org" \
             }, \
             { \
                 "subscription": "none", \
                 "jid": "tybalt@buddycloud.org" \
             } \
         ]'
```

```javascript

















```

This allows a channel's `owner` or `moderator` to approve or deny incoming subscription requests.

Subscription State | Description
-------------|--------------
`pending`    | No action taken by `owner` or `moderator`.
`subscribed` | Permission to follow channel granted. 
`none`       | Permission to follow channel denied.


##Alter Follower Affiliations

```shell
#POST https://demo.buddycloud.org/api/{channelId}/subscribers/{nodeId}

curl https://demo.buddycloud.org/api/romeo@buddycloud.org/subscribers/posts \
     -X POST \
     -u romeo@buddycloud.org:juliet-forever \
     -H "Content-Type: application/json" \
     -d '{ \
             "juliet@buddycloud.org": "member" \
         }'

```

```javascript










```

This enables users to promote (or demote) user subscriptions to `publisher`, `member` or even `moderator`. By setting a subscription to `outcast`, the user is banned.
