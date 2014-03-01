'use strict';

var socket = null
var messageCount = 1
var manualPageRetrievalQueue = 0

var addStatusMessage = function(message) {
    $('<li>' + message + '</li>').prependTo('ul.status')
}

/* jshint -W117 */
$(window.document).ready(function() {

    console.log('Page loaded...')

    socket = new Primus('https://xmpp-ftw.jit.su')

    socket.on('error', function(error) { console.log(error) })

    socket.on('open', function() {
        addStatusMessage('Websocket connection established')
    })

    socket.on('timeout', function(reason) {
        console.log('Connection failed: ' + reason)
    })

    socket.on('end', function() {
        addStatusMessage('SOCKET CONNECTION CLOSED')
        socket = null
    })

    socket.on('xmpp.error.client', function(error) {
        addStatusMessage('XMPP Error: ' + error)
    })

    socket.on('xmpp.connection', function(details) {
        addStatusMessage('Logged in as: ' +
            details.jid.user + '@' +
            details.jid.domain + '/' +
            details.jid.resource
        )
        socket.send('xmpp.buddycloud.discover', { server: 'channels.buddycloud.org' }, function(error, server) {
            if (error) return console.error('Discovery error', error)
            addStatusMessage('Discovered channel server @ ' + server)
            socket.send('xmpp.buddycloud.register', {}, function() {
                addStatusMessage('Registered with the server')
                socket.send('xmpp.buddycloud.presence', {})
                addStatusMessage('Informed server we are online and ready to receive push messages')
            })
        })
    })

    socket.send(
        'xmpp.login.anonymous',
        { jid: 'anon.buddycloud.org' }
    )

})