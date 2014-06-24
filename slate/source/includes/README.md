#Conventions to keep us consistient

##Showing variables:

Denote variables with `{variable name}`

- not `:variable name`
- not `:variable name:`

eg: `GET https://demo.buddycloud.org/api/{channelID}/media/{Mediaid}`

##Channel types:

channel access: `public` and `private`

- (not open, or closed)

##Naming variables:

Variable | Description
---------|------------
`channelID`| (the JID-like part) we call it the `channelID` (not `channel-name`)
`mediaID` | the id of a media object
`buddycloudID`| user's log in / their jid (we nevr mention `jid`)

##Examples

Use examples from romeo and juliet. (not alice and bob)

## Table headings 

* Capitalise table headings
* arguments should be nicely code formatted eg: `username`
* `true` and `false`  not true and false

eg:

Argument   | Required | Notes
---------- | -------- |------------
`username`   | `true`     | Must contain a domain element that matches the virtual host.
`password`   | `true`     | The API is agnostic to password strength requirements.
`email`      | `false`    | An Email address to receive push notifications and password resets.
