#Accounts

Create and destroy user accounts and permit the user to manage and reset their password.

<aside class="notice">A user account enables a user to connect to their messaging service. They will still need to create their personal channel</aside>

### Query Parameters

Argument   | Required | Notes
---------- | -------- |------------
username   | True     | Must contain a domain element that matches the virtual host.
password   | True     | The API is agnostic to password strength requirements.
email      | False    | An Email address to receive push notifications and password resets.

##Create User

```shell 
curl https://demo.buddycloud.org/api/account \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{ \
            "username": "alice@buddycloud.org", \
            "password": "tell-no-one", \
            "email": "alice@buddycloud.org" \
        }'
```

```javascript
socket.send(
    'xmpp.login',
    {
        "jid": "alice@buddycloud.org",
        "password": "tell-no-one",
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
    -H "Authorization: Basic `echo "alice@buddycloud.org:tell-no-one" | base64 -`"
```

```javascript```
???
```

This removes a user account.

<aside class="warning">Deleting a user will delete their account. It will not delete their channels. To completely remove the user, an application should first delete their channels, then the user account.</aside>

### HTTP Request
`DELETE https://demo.buddycloud.org/api/account`

<aside class="warning">Requires Basic Authentication.</aside>

## Change Password

```shell 
curl https://demo.buddycloud.org/api/account/pw/change \
    -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: Basic `echo "alice@buddycloud.org:tell-no-one" | base64 -`" \
    -d '{ \
            "username": "alice@buddycloud.org", \
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
    -d '{ \
            "username": "alice@buddycloud.org" \
        }'
```

```javascript```
???
```

Resets the user's password and sends a reset token via email. (I think. @abmar: how does this work? Generate email with a new password or sends a token?)

### HTTP Request
`POST https://demo.buddycloud.org/api/account/pw/reset`
