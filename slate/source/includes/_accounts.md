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
`email`    | ✗        | for password resets and (optional) push notifications

##Create User

```shell
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

### HTTP Request
`POST https://demo.buddycloud.org/api/account`

##Delete User

```shell
curl https://demo.buddycloud.org/api/account \
     -X DELETE \
     -u juliet@buddycloud.org:romeo-forever
```

```javascript```
???
```

Removes a user account. 

<aside class="warning">Deleting a user will delete their account, _not_ their channels. Your application should first delete their channel(s) then remove the user account.</aside>

### HTTP Request
`DELETE https://demo.buddycloud.org/api/account`

## Change Password

```shell 
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
???
```

Changes the user's `password`.

### HTTP Request
`POST https://demo.buddycloud.org/api/account/pw/change`

##Reset Password

```shell 
curl https://demo.buddycloud.org/api/account/pw/reset \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{ "username": "juliet@buddycloud.org" }'
```

```javascript```
???
```

This resets the user's password by sending a new password to the email address provided by the user during registration.

### HTTP Request
`POST https://demo.buddycloud.org/api/account/pw/reset`
