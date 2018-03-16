const mqtt = require('mqtt');
const Telemetry = require('./models/telemetry');

module.exports = {
    configure: function(client) {
        client.on('connect', () => {
            console.log('mqtt connected');
            client.subscribe('telemetry');
        });
        client.on('error', (error) => {
            console.log(error);
        });
        client.on('message', (topic, message) => {
            var msgString = message.toString();
            console.log(`${topic}: ${msgString}`);
            switch(topic) {
                case 'telemetry/altitude': 
                    
                    break;
            }
            var obj = JSON.parse(msgString.toString());
            var telemetry = new Telemetry();
            telemetry.altitude = obj.altitude;
            telemetry.power = obj.power;
            telemetry.temperature = obj.temperature;
            telemetry.save((err) => {
                if (err) {
                    console.log('error on saving telemetry packet');
                } else {
                    console.log('telemetry packet captured');
                }
            });
        });
    }
}