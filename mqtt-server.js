const mosca = require('mosca');

// mosca is not scaleable. If you need a scaleable solution, use mosquitto.


// TODO: Figure out how to make this work with your mongo server. Store all messages into the same collection we query from.
var backend_settings = {
    type: 'mongo',
    url: 'mongodb://localhost:27017/mqtt',
    pubsubCollection: 'ascoltatori', // wtf is this
    mongo: {}
}


// https://github.com/mcollina/mosca/wiki/MQTT-over-Websockets
var server = new mosca.Server({
    port: 1883,
    http: {
        port: 8000,
        bundle: true,
        static: './'
    }
    // backend: backend_settings
});

server.on('clientConnected', (client) => {
    console.log('client connected:', client.id);
});

server.on('clientDisconnected', (client) => {
    console.log('client disconnected:', client.id);
});

server.on('ready', () => {
    console.log('mqtt server up');
});

server.on('published', (packet, client) => {
    console.log('client:', client.id, 'published:', packet);
});

/*
server.publish({
    topic: 'this/topic',
    payload: '',
    qos: 2,
    retain: false
}, () => {
    console.log('callback for publish');
});
*/