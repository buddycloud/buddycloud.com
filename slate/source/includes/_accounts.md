#Accounts

Your users will need to authenticate against the server with a username that looks like `user`@`domain`. For example `user@example.buddycloud.com`.

### Query Parameters

Argument   | Required | Notes
---------- |:--------:|------------
`username` | ✓        | always of form `user@example.com`; ≤1023 bytes
`password` | ✓        | any UTF-8 characters
`email`    | ✓        | an email for password resets and optional push notifications

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
#Unsupported Method









```

This will create a new account for `username` and set their `password`. You can optionally pass in an `email` for password resets and for alerts from the [push notification](#push-notifications) system (e.g. "Someone followed your channel").

##Delete User

```shell
#DELETE https://demo.buddycloud.org/api/account

curl https://demo.buddycloud.org/api/account \
     -X DELETE \
     -u juliet@buddycloud.org:romeo-forever





```

```javascript
#XMPP-FTW event 'xmpp.register.unregister'

socket.send(
    'xmpp.register.unregister',
    {
        "to": "buddycloud.org"
    }
)


```

Removes a user account. 

<aside class="warning">Your application should first delete their channel(s) then remove the user account. Deleting a user will delete their account, _not_ their channels.</aside>

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
#XMPP-FTW event 'xmpp.register.password'

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
#Unsupported Method









```

This resets the user's password by sending a new password to the email address provided by the user during registration.
