var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// Mongo auto generates the _id field for each element in the collection.

// Schema for points of interest. Either marked by the end user, or auto marked by the quadcopter.
var PointSchema = new mongoose.Schema({
    description:    { type: String, default: '' },
    latitude:       Number,
    longitude:      Number
});

module.exports = mongoose.model('Point', PointSchema);