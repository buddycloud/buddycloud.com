#Accounts

Your app will need to authenticate users. Some methods are

* the user creates a `username` and `password`
* your app uses the mobile [phone number](http://en.wikipedia.org/wiki/MSISDN) as the `username`
* no user interaction (your application backend provides a blind `username` and `password` to connect with Buddycloud services)

### Query Parameters

Argument   | Required | Notes
---------- |:--------:|------------
`username` | ✓        | always of form `user@example.com`
`password` | ✓        | any UTF-8 characters
`email`    | ✗        | an email for password resets and (optional) push notifications

### Username Domain
A user with an email of `user@example.com` can also have a Buddycloud `username` of `username@example.com` by using the hosting service or running your own Buddycloud stack on the same domain.

##Create User

```shell
#POST https://demo.buddycloud.org/api/account

curl https://demo.buddycloud.org/api/account \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{ \
            "username": "juliet@buddycloud.org", \
            "password": "romeo-forever", \
            "email": "juliet@buddycloud.org" \
         }'
```

```javascript
socket.send(
    'xmpp.login',
    {
        "jid": "juliet@buddycloud.org",
        "password": "romeo-forever",
        "register": true
    }
)
```

This will create a new account for `username` and set their `password`. You can optionally pass in an `email` for password reset and for alerts from the [push notification](#push-notifications) system (e.g. "Someone followed your channel").

##Delete User

```shell
#DELETE https://demo.buddycloud.org/api/account

curl https://demo.buddycloud.org/api/account \
     -X DELETE \
     -u juliet@buddycloud.org:romeo-forever
```

```javascript
socket.send(
    'xmpp.register.unregister',
    {
        "to": "buddycloud.org"
    }
)
```

Removes a user account. 

<aside class="warning">Deleting a user will delete their account, _not_ their channels. Your application should first delete their channel(s) then remove the user account.</aside>

## Change Password

```shell 
#POST https://demo.buddycloud.org/api/account/pw/change

curl https://demo.buddycloud.org/api/account/pw/change \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Content-Type: application/json" \
     -d '{ \
            "username": "juliet@buddycloud.org", \
            "password": "new-password" \
         }'
```

```javascript
socket.send(
    'xmpp.register.password',
    {
        "to": "buddycloud.org",
        "username": "juliet",
        "password": "new-password"
    }
)
```

Changes the user's `password`.

##Reset Password

```shell 
#POST https://demo.buddycloud.org/api/account/pw/reset

curl https://demo.buddycloud.org/api/account/pw/reset \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{ "username": "juliet@buddycloud.org" }'
```

```javascript
Unsupported Method
```

This resets the user's password by sending a new password to the email address provided by the user during registration.
