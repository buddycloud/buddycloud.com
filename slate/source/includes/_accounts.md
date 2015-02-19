#Accounts

Your users will need to authenticate against the server with a username that looks like `username`@`domain`. For example `username@example.buddycloud.com`.

### Query Parameters

Argument   | Required | Notes
---------- |:--------:|------------
`username` | ✓        | always of form `user@example.com`; ≤1023 bytes
`password` | ✓        | ≤1023 bytes
`email`    | ✓        | an email for password resets and optional push notifications

##Create User

> `POST` /api/account

```shell
curl https://buddycloud.com/api/account \
     -X POST \
     -H "Content-Type: application/json; charset=utf-8" \
     -d '{ \
            "username": "juliet@buddycloud.org", \
            "password": "romeo-forever", \
            "email": "juliet@buddycloud.org" \
         }'
```

This will create a new account for `username` and set their `password` and `email`. The email is used for password resets and for optional alerts from the [push notification](#push-notifications) system.

##Delete User

> `DELETE` /api/account

```shell
curl https://buddycloud.com/api/account \
     -X DELETE \
     -u juliet@buddycloud.org:romeo-forever
```

Removes a user account. 

<aside class="warning">Your application should first delete their channel(s) then remove the user account. Deleting a user will delete their account, _not_ their channels.</aside>

## Change Password

> `POST` /api/account/pw/change

```shell 
curl https://buddycloud.com/api/account/pw/change \
     -X POST \
     -u juliet@buddycloud.org:romeo-forever \
     -H "Content-Type: application/json; charset=utf-8" \
     -d '{ \
            "username": "juliet@buddycloud.org", \
            "password": "new-password" \
         }'
```

Changes the user's `password`.

##Reset Password

> `POST` /api/account/pw/reset

```shell 
curl https://buddycloud.com/api/account/pw/reset \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{ "username": "juliet@buddycloud.org" }'
```

This resets the user's `password` by sending a new password to the `email` address provided by the user during registration.
