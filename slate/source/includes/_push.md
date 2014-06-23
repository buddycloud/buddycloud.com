#Push Notifications

You can schedule certain message types to be pushed to your users. For example, notifications on @mentions, or posts in a channel they participate in.

Push notifications currently work with Android's GCM and email.

Push notifications are powered by the [Buddycloud Pusher](https://github.com/buddycloud/buddycloud-pusher). The Pusher is designed to be easy to extend to cover new event types in channels and new push systems.

### Query Parameters

Argument                | Value      | Default | Notes
----------------------- | ---------- |-------- | ----
type                    | `email`, `gcm` |   |The push notification type.
target                  | `email` `GCMRegistrationId` | - | An email address or a Google Cloud messenger Registration ID
postAfterMe             | `true`,`false` | `true` | New posts in a thread the user has previously posted
postMentionedMe         | `true`,`false` | `true` | When a post in any channel mentions the user's id.
postOnMyChannel         | `true`,`false` | `true` | Posts into a channel the user owns
postOnSubscribedChannel | `true`,`false` | `false` | Posts in any channels the user subscribes to
followRequest           | `true`,`false` | `true` | A request to follow a private channel the user owns or moderates waits for approval 
followMyChannel         | `true`,`false` | `true` | Someone started following the user's channel

}


##Fetch Settings
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

To fetch the current settings for a `type` of notification, use a `GET` request. This will show a list of the avalible settings for a user.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`


##Update Settings
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

To update a users settings simply `POST` back to the API endpoint.

### HTTP Request
`POST https://demo.buddycloud.org/api/????`
