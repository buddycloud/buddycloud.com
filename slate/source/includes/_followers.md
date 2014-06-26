#Followers

Channel followers can have different roles.

Role       | User sees      | Description
-----------|----------------|-------------
`owner`    |`owner`         |add and remove `moderator`s
`moderator`|`moderator`     |approve new `followers` and delete posts
`publisher`|`follower+post` |create posts
`member`   |`follower`      |only view posts
`pending`  |`pending`       |nothing
`outcast`  | `null`         |only visibile to the `owner` and `moderator` roles.

The `outcast` role is useful for dealing with abusive users. 

Once a user is `outcast`, they can no longer post or generate subscripion requests to that channel. Only the channel's `owner` and `moderator`s can view users with the `outcast` role.

<aside class="warning">
Users follow channels. You should never see a _topic_ channel with the metadata `channeltype=topic` following a channel.
</aside>

##Fetch Followers

```shell
curl https://demo.buddycloud.org/api/romeo@buddycloud.org/subscribers/posts \
     -X GET
```

```shell
200 OK
Content-Type: application/json

{
    "romeo@buddycloud.org": "owner",
    "benvolio@buddycloud.org": "publisher"
}
```

```javascript```
???
???
```

Retrieves a list of followers and their role in that channel.

???we really need a way to query by role type - eg show me just the moderators of this channel???

### HTTP Request
`GET https://demo.buddycloud.org/api/:channel-name/subscribers/:node`

##Retrieve Pending Followers

```shell
curl https://demo.buddycloud.org/api/romeo@buddycloud.org/subscribers/posts/approve \
     -X GET \
     -u romeo@buddycloud.org:juliet-forever
```

```shell
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
???
???
```

Retrieves the list of subscriptions of a node. Returns a list of objects containing the subscriber JID and the values of its subscription state (`subscribed` or `pending`).

### HTTP Request
`GET https://demo.buddycloud.org/api/:channel-name/subscribers/:node/approve`

##Authorise Pending Followers

```shell
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

```javascript```
???
???
```

This allows you to approve or deny incoming subscription requests, by assigning states to these subscription requests. Possible states are: `subscribed`, in order to approve the request; or `none`, in order to deny it.

### HTTP Request
`POST https://demo.buddycloud.org/api/:channel-name/subscribers/:node/approve`

##Alter Follower Roles

```shell
curl https://demo.buddycloud.org/api/romeo@buddycloud.org/subscribers/posts \
     -X POST \
     -u romeo@buddycloud.org:juliet-forever \
     -H "Content-Type: application/json" \
     -d '{ \
             "juliet@buddycloud.org": "member" \
         }'
```

```javascript```
???
???
```

This lets you promote (or demote) user subscriptions to `publisher`, `member` or even `moderator`. By setting a subscription to `outcast` you will be actively banning that user.

### HTTP Request
`POST https://demo.buddycloud.org/api/:channel-name/subscribers/:node`
