#Accounts

Create and destroy user accounts and permit the user to manage and reset their password.

<aside class="notice">A user account enables a user to connect to their messaging service. They will still need to create their personal channel</aside>

### Query Parameters

Argument   | Required | Notes
---------- | -------- |------------
`username`   | true     | Must contain a domain element that matches the virtual host.
`password`   | true     | The API is agnostic to password strength requirements.
`email`      | false    | An Email address to receive push notifications and password resets.

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

This will create a new user and set their password. 

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

This removes a user account.

<aside class="warning">Deleting a user will delete their account. It will not delete their channels. To completely remove the user, an application should first delete their channels, then the user account.</aside>

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

```javascript```
???
```

Changes a user password to the new password supplied.

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

Resets the user's password by sending a new password to the email address provided by the user during registration.

### HTTP Request
`POST https://demo.buddycloud.org/api/account/pw/reset`
