const mosca = require('mosca');
const Telemetry = require('../models/telemetry');

// Custom override function to determine if a json object has a property.
// https://github.com/mcollina/mosca/wiki/Authentication-&-Authorization
Object.prototype.hasOwnProperty = function (property) {
    return this[property] !== undefined;
};

var mongoSettings = {
    type: 'mongo',
    url: process.env.DB_HOST + '/mosca',
    pubsubCollection: 'pubsub',
    mongo: {}
};
var moscaSettings = {
    port: 1883,
    backend: mongoSettings,
    // Persistence is necessary for the ability to 'retain' messages.
    persistence: {
        factory: mosca.persistence.Mongo,
        url: process.env.DB_HOST + '/mosca'
    }
};
const broker = new mosca.Server(moscaSettings);

broker.on('ready', () => {
    console.log('mqtt broker online');
});
broker.on('clientConnected', (client) => {
    console.log('client connected');
});
broker.on('clientDisconnecting', (client) => {
    console.log('client disconnecting...');
});
broker.on('clientDisconnected', (client) => {
    console.log('client disconnected');
});
broker.on('subscribed', (topic, client) => {

});
broker.on('unsubscribed', (topic, client) => {

});
broker.on('published', (packet, client) => {
    //console.log(packet);
    if (packet.topic == 'telemetry') {
        try {
            var obj = JSON.parse(packet.payload.toString());
            var telemetry = new Telemetry();
            telemetry.altitude = obj.altitude;
            telemetry.power = obj.power;
            telemetry.temperature = obj.temperature;
            telemetry.latitude = obj.latitude;
            telemetry.longitude = obj.longitude;
            telemetry.eventCode = obj.eventCode;

            telemetry.save((err) => {
                if (err) {
                    console.log('error on saving telemetry packet');
                } else {
                    console.log('telemetry packet captured');
                }
            });
        } catch(err) {
            console.log('Could not save telemetry packet');
            console.log(packet.payload.toString());
        }
    }
});

module.exports = broker;