var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// Mongo auto generates the _id field for each element in the collection.
var TelemetrySchema = new mongoose.Schema({
    dateCreated: Date,          // datetime the vehicle created the packet.
    dateReceived: { type: Date, default: Date.now }, // datetime the packet was received and saved.
    temperature: Number,        // degrees f
    humidity: Number,           // percentage
    altitude: Number,           // feet
    voltage: Number,            // in millivolts
    heading: Number,            // magnetic heading
    speed: Number,              // ground speed
    latitude: Number,           // relative or absolute
    longitude: Number,          // relative or absolute
    eventCode: Number           // enumerable
});

module.exports = mongoose.model('Telemetry', TelemetrySchema);


/*
Need to store:
Altitude - in feet
Air Temperature - celsius, however the user needs the ability to change the units.
Power system health - remaining battery percentage and the remaining flight time
Latitude (relative or absolute)
Longitude (relative or absolute)
Event codes - up to us for any other data we need to declare.
*/


/*
Control commands sent from website to the quadcopter
0 - kill all power
1 - drop payload
2 - pan left
3 - pan right
4 - tilt up
5 - tilt down
6 - lights on
7 - lights off
*/