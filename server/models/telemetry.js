var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// Mongo auto generates the _id field for each element in the collection.
var TelemetrySchema = new mongoose.Schema({
    vehicle: { type: Schema.Types.ObjectId, ref: 'Vehicle' },
    dateReceived: { type: Date, default: Date.now },
    temperature: Number,
    altitude: Number,
    battery: Number
    //latitude: Number,
    //longitude: Number,
});

module.exports = mongoose.model('Telemetry', TelemetrySchema);