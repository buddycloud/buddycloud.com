#Push Notifications

You can schedule certain message types to be pushed to your users. For example, notifications on @mentions, or posts in a channel they participate in.

Push notifications currently work with Android's GCM and email.

Push notifications are powered by the [Buddycloud Pusher](https://github.com/buddycloud/buddycloud-pusher). The Pusher is designed to be easy to extend to cover new event types in channels and new push systems.


### Query Parameters

Argument                | Value      | Default | Notes
----------------------- | ---------- |-------- | ----
type                    | email,???Abmar - what else??? | The push notification type.
target                  | juliet@buddycloud.com | The email or ???abmar: what else???
postAfterMe             | true,false | ??? | New posts in the same thread
postMentionedMe         | true,false | ??? | When a post in a channel the users follows mentions their ID.
postOnMyChannel         | true,false | ??? | Posts into a channel where the user is an owner
postOnSubscribedChannel | true,false | ??? | Only notifications for subscribed channels ???abmar: why would you get notificiations for other channels???
followMyChannel         | true,false | ??? | Notifies the user when someone follows their channel ???abmar: Only if it's a closed channe or both??? 
followRequest           | true,false | ??? | ???Whats the difference???
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
