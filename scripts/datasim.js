const mqtt = require('mqtt');

var client = mqtt.connect('ws://localhost:3000');

setInterval(function() {
    var t = generateTelemetry();
    client.publish('telemetry', JSON.stringify(t), {
        retain: true
    });
}, 1000);




function generateTelemetry() {
    return {
        latitude: randInt(28550000, 28500000) / 1000000.0,
        longitude: randInt(-81250000, -81200000) / 1000000.0,
        altitude: randInt(0, 10),
        power: randInt(60, 75),
        temperature: randInt(70, 80),
        heading: randInt(0, 360),
        eventCode: randInt(0, 15)
    }
}

function randInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}