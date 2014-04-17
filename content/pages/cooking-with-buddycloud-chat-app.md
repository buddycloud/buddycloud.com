Title: Add chat to your app
url: cooking-with-buddycloud-chat-app
save_as: cooking-with-buddycloud-chat-app.html
order: 1
show_in_top_menu: false
table_of_contents: false


Aim
---

Add chat to a web app in 10 minutes

Ingredients
-----------

- web browser
- Site running Buddycloud
- [Primus](http://primus.io/) (the glue-without-the-goo that looks after websocket and long polling connection handling)
- text editor

Difficulty
----------

<span style="color:green-blue">Easy</span>

Please ask if you get stuck:

-  Email: <reach-a-developer@buddycloud.com>
-  Twitter: [@buddycloud](https://twitter.com/buddycloud)

See it in action
----------------

Working demo in [codepen.io](http://codepen.io/guilhermesgb/pen/lJfLg/)!

Architecture
------------

- the chat client will use [Primus](primus.io) for messaging over a websocket (with fallback to long polling)
- the [XMPP-FTW](https://xmpp-ftw.jit.su) service takes JSON from the browser and turns it into XMPP messages
- XMPP messages are "handed off" to the XMPP server for realtime delivery

```
  +---------+  HTML/IMG/JS/CSS  +----------+
  | User /  | <---------------+ | xmpp-ftw | (we're using: https://xmpp-ftw.buddycloud.com/)
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
npm i .    # installes npm dependencies
npm start  # starts npm listening on http://127.0.0.1:3000
~~~~

Now let's start cooking!

Chatting works as follows
- we create a "channel" and post messages into the channel
- Other users connect and retrieve message history from when they were last online
- Other users are then automatically notified of new messages
- Users can post back to the channel

First up, let's register a user by issuing a POST request to the HTTP API /account endpoint:
~~~~ javascript
var apiLocation = "https://demo.buddycloud.org/api";
var domain = "@buddycloud.org";
_registerUser = function(username, password) {
    var jid = username + domain;
    $.ajax({
        type: "POST",
        url: apiLocation + "/account",
        contentType: "application/json",
        processData: true,
        data: JSON.stringify({
                username: jid,
                password: password,
                email: "email@email.com"
        }),
        success: function(data) {
            window.alert(jid + " registered successfully!");
            $("#toggleRegistrationForm").click();
        },
        error: function(jqXHR) {
            $.ajax({
                 type: "GET",
                 url: apiLocation + "/" + jid + "/metadata/posts",
                 success: function(data) {
                     window.alert(jid + " already exists!");
                 },
                 error: function(jqXHR) {
                     window.alert("Problem trying to register user!");
                 }
            }); 
        }
    });
};
~~~~
If the call fails, we are issuing another call to the API to check whether the usernam is already taken. 

Once we have a registered users, we need to go-online (which tells the server to start sending us events).

~~~~ javascript
function login(jid, password) {
    socket.send(
        'xmpp.login',
        {
            jid: jid,
            password: password
        }
    );
};

socket.on('xmpp.connection', function(data) {
    console.log('Connected as', data.jid);
    discoverBuddycloudServer();
});
~~~~

As you have seen above, once connected you must discover the Buddycloud server:

~~~~
function discoverBuddycloudServer() {
    socket.send(
        'xmpp.buddycloud.discover',
        {},
        function(error, data) {
            if (error) return console.error(error);
            console.log('Discovered Buddycloud server at', data);
            createNode();
            getNodeItems();
        }
    );
}
~~~~

Now we will create our channel for sharing chat messages: it will be ```chat-room@topics.buddycloud.org```

~~~~ javascript
function createNode(){
    socket.send('xmpp.buddycloud.create',
    {
        node : "/user/chat-room@topics.buddycloud.org/chat",
        options: [
            { "var": "buddycloud#channel_type", value : "topic" },
            { "var": "pubsub#title", value : "Chat Topic Channel" },
            { "var": "pubsub#access_model", value : "open" },
            { "var": "buddycloud#default_affiliation", value : "publisher" }
        ]
    },
    function(error, data) {
        console.log('xmpp.buddycloud.create response arrived');
        if (!error){
            console.log('Created Chat Room node', data);
        }
        else if ("cancel" === error.type &&
            "conflict" === error.condition){
                subscribeToNode();
        }
        else {
            console.error(error);
        }
        getNewMessagesNotification();
        sendPresenceToBuddycloudServer();
    });
}
~~~~

As you may have noticed, if the node already exists,
we'll at least make sure the user is subscribed to it (in a best effort approach):
~~~~
function subscribeToNode(){
    var node = "/user/chat-room@topics.buddycloud.org/chat";
    socket.send(
        'xmpp.buddycloud.subscribe',
        {
            "node": node,
        },
        function(error, data) {
            if (error) return console.error(error);
            console.log("Subscribed to Chat Room node");
        }
    );
}
~~~~

Then specify that you want to listen for incoming messages
~~~~
function getNewMessagesNotification(){
    socket.on('xmpp.buddycloud.push.item', function(data) {
        var node = "/user/chat-room@topics.buddycloud.org/chat";
        if ( node === data.node ){ //Notifications of messages on other nodes may arrive as well
            handleItem(data);
        }
    });
}
~~~~

And you must send presence to the buddycloud server to inform it you're online:
~~~~
function sendPresenceToBuddycloudServer(){
    socket.send('xmpp.buddycloud.presence', {});
}
~~~~

Tell the client that, when it connects, it should pull down the last messages since the local-storage last-time-connected (for now simply picking the last 6 items).
~~~~ javascript
var getNodeItems = function(itemId) {
    var data = {
    node: node,
        rsm: { max:6 } 
    }
    if (itemId) { //specify itemId if you want to retrieve a specific item by id
        data.id = itemId;
    }
    socket.send(
        'xmpp.buddycloud.retrieve',
        data,
        handleItems
    );
}
~~~~

now send a message to the chat room
~~~~ javascript
function sendMessage(message){
    var node = "/user/chat-room@topics.buddycloud.org/chat";
    socket.send(
        'xmpp.buddycloud.publish',
        {
            "node": node,
            "content": {
                "atom": {
                    "content": message
                }
            }
        },
        function(error, data) {
            if (error) console.error(error);
            else {
                console.log("Message sent.");
            }
        }
    );
}
~~~~

And that's it!

Working demo in [codepen.io](http://codepen.io/guilhermesgb/pen/lJfLg/).
We also view the source code of this Simple Chat recipe [here](https://github.com/guilhermesgb/chat-recipe)!

Any Questions?
--------------

Want to contribute to this [page](https://github.com/buddycloud/buddycloud.com/blob/master/content/pages/cooking-with-buddycloud-chat-app.md)?

For any questions or concerns, please contact us at <reach-a-developer@buddycloud.com> or at Twitter: [@buddycloud](https://twitter.com/buddycloud)!

Good cooking!
