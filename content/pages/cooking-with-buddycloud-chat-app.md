Title: Add chat to your app
url: cooking-with-buddycloud-chat-app
save_as: cooking-with-buddycloud-chat-app.html
order: 1
show_in_top_menu: false
table_of_contents: true


Aim
---

Add chat to any webp in 10 minutes

Ingredients
-----------

- npm
- web browser
- text editor

Difficulty
----------
Easy

Please ask if you get stuck
-  reach-a-developer@buddycloud.com
-  [@buddycloud](https://twitter.com/buddycloud)

Architecture
------------

- the chat client will use [Primus](primus.io) for messaging over a websocket (with fallback to long polling)
- the XMPP-ftw service takes JSON from the browser and turns it into XMPP messages
- XMPP messages are "handed off" to the XMPP server for realtime delivery

```
  +---------+  HTML/IMG/JS/CSS  +----------+
  | User /  | <---------------+ | xmpp-ftw |
  | Browser |      websocket    | server   |
  +---------+ <---------------> +----------+
                                    ^
                                    | socket
                                    |
                                    v
                                +--------+   component   +------------+
                                |  XMPP  |   connection  | buddycloud |
                                | server |<------------->| component  |
                                +--------+               +------------+
                                    ^
                                    |
                                    v
                               +----------+
                               | External |
                               |   XMPP   |
                               |  server  |
                               +----------+
```

Method
------

<span style="color:green-blue">Estimated time: 2 mins</span>

Let's get setup with a skeleton project.
~~~~ bash
git clone https://github.com/buddycloud/skeleton-project.git
~~~~

Then we get all the npm modules installed and start npm
~~~~ bash
npm -i      # installes npm dependencies
npm start   # starts npm listening on http://127.0.0.1:3000
~~~~

Chatting works as follows
- we create a "channel" and post messages into the channel
- Other users connect and retrieve message history from when they were last online
- Other users are then automatically notified of new messages
- Users can post back to the channel

First up, let's register a user
~~~~ javascript
socket.send(
  'xmpp.register.get',
    { "to": "buddycloud.org"
    },
      function(error, data) { console.log(error, data) }
    )
~~~~

! We don't have in-band registration working. We need to fix this or offer an API call. 

Once we have a registered users, we need to go-online (which tells the server to start sending us events)
~~~~ javascript
socket...
~~~~

Now we will create our channel for sharing chat messages
~~~~ javascript
socket.send(

~~~~

Tell the client that, when it connects, it should pull down the last messages since the local-storage last-time-connected.
~~~~ javascript
socket.send(
~~~~

now send a message to the chat room
~~~~ javascript
socket.send(
~~~~

Since the chat room is open, it can be viewed on demo.buddycloud.org/<full address>

Bonus round:

Set the channel to private
~~~~ javascript
socket.send(
~~~~
