var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// Mongo auto generates the _id field for each element in the collection.
var PointSchema = new mongoose.Schema({
    dateReceived: { type: Date, default: Date.now },
    temperature: Number,
    altitude: Number,
    power: Number
    //latitude: Number,
    //longitude: Number,
});

module.exports = mongoose.model('Telemetry', TelemetrySchema);