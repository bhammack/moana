var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// Mongo auto generates the _id field for each element in the collection.
var TelemetrySchema = new mongoose.Schema({
    dateReceived: { type: Date, default: Date.now },
    temperature: Number,        // degrees f
    altitude: Number,           // feet
    power: Number,              // [0-100] percentage as integer
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