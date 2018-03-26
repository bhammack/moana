var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// Mongo auto generates the _id field for each element in the collection.

// Schema for points of interest. Either marked by the end user, or auto marked by the quadcopter.
var PointSchema = new mongoose.Schema({
    name:           String,
    description:    { type: String, default: '' },
    markerId:       Number,
    latitude:       Number,
    longitude:      Number,
    altitude:       { type: Number, default: 0 }
});

module.exports = mongoose.model('Point', PointSchema);