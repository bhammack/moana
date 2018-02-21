var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// Mongo auto generates the _id field for each element in the collection.
var VehicleSchema = new mongoose.Schema({
    name: String,
    dateLastContacted: Date,
    telemetry: [{ type: Schema.Types.ObjectId, ref: 'Telemetry' }]
});

module.exports = mongoose.model('Vehicle', VehicleSchema);