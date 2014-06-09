#Followers

Queries who follows a channel. The data back doesn't isn't sorted in any particular order. 

<aside class="warning">
Users follow channels. You should never see a channel with the metadata `channeltype=topic` following a channel.
</aside>

##Fetch Followers

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
{
  "alice@example.com/posts": "owner",
  "bob@example.com/posts": "publisher",
  "public@topics.example.com/posts": "publisher"
}
```

Retrieves a list of followers and their role in that channel.

???we really need a way to query by role type - eg show me just the moderators of this channel???

### HTTP Request
`GET https://demo.buddycloud.org/api/????`

##Authorise Pending Followers

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
[
  {"subscription": "subscribed", "jid": "bob@example.com"},
  {"subscription": "none", "jid": "john@example.com"}
]
```

Retrieves the list of subscriptions of a node. Returns a list of objects containing the subscriber JID and the values of its subscription state ("subscribed" or "pending").

### HTTP Request
`POST https://demo.buddycloud.org/api/????`

##Alter Follower Roles

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

???What does it do goes here. Write in the Third person: "This command enables this feature and you should be aware of...???

### HTTP Request
`POST https://demo.buddycloud.org/api/????`
