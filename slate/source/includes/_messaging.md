#Direct Messaging

Direct messages give you a quick way to send messages betwen users on your Buddycloud site and to users on remote Buddycloud sites. Direct messaging uses XMPP's native messaging.
 
##Post Message

```javascript```
socket.send(
  'xmpp.chat.receipt',
      {
        "to": "other@evilprofessor.co.uk/laptop",
        "id": "message-number-5"
      }
  )
```

> Message delivery receipts are received via the `xmpp.chat.receipt` event

```javascript```
socket.on('xmpp.chat.receipt', function(data) {
  console.log(data);
            /*
             * {
             *   from: { domain: 'evilprofessor.co.uk', user: 'lloyd', resource: 'laptop' },
             *   id: 'message-number-5'
             * }
             */
        }
```

```json
        socket.on('xmpp.chat.receipt', function(data) {
            console.log(data);
            /*
             * {
             *   from: { domain: 'evilprofessor.co.uk', user: 'lloyd', resource: 'laptop' },
             *   id: 'message-number-5'
             * }
             */
        }
```

This sends a message to another user. Messages will be stored for the user if they are not online. 

##Retrieve Messages

```javascript```
socket.on('xmpp.chat.message', function(data) {
  console.log(data)
  })
```

```json
{
  from: {
    domain: 'buddycloud.com',
    user: 'friend'
    },
    content: 'What time should we go out tonight?',
    format: 'plain',
 /* delay: {
      from: 'evilprofessor.co.uk',
      when: '2013-06-03T19:56Z',
      reason: 'Offline storage'
      }, */
 /* state: 'active' */
 /* archived: [
    { by: { domain: 'buddycloud.com' }, id: 'archive:1' }
    ] */
}
```

To begin receiving messages your application should enable [realtime event](#realtime-events) sending. Messages will then arrive as they are sent without needing to poll.

