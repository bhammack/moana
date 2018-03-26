const express = require('express');
const router = express.Router();
const HttpStatus = require('http-status-codes');

// Mongoose models
var Telemetry = require('../models/telemetry');
var Points = require('../models/points');
// https://gist.github.com/subfuzion/669dfae1d1a27de83e69

// Get the root of the API. Use this as a help to show what endpoints are available.
router.get('/', (req, res) => {
  res.json({message: 'rest api root access'});
});

router.route('/telemetry')
  .get((req, res) => {
    Telemetry.find({}, (err, telemetry) => {
      if (err) {
        res.status(HttpStatus.INTERNAL_SERVER_ERROR).send(err);
      } else {
        res.status(HttpStatus.OK).json(telemetry);
      }
    });
  });

// Standard crud opertions on the points schema.
router.route('/points')
  .get((req, res) => {
    Points.find({}, (err, points) => {
      if (err) {
        res.status(HttpStatus.INTERNAL_SERVER_ERROR).send(err);
      } else {
        res.status(HttpStatus.OK).json(points);
      }
    });
  })
  .post((req, res) => {
    var point = new Points();
    point.markerId = req.body.markerId;
    point.description = req.body.description;
    point.latitude = req.body.latitude;
    point.longitude = req.body.longitude;
    point.save((err) => {
      if (err) {
        res.status(HttpStatus.NOT_FOUND).send(err);
      } else {
        res.status(HttpStatus.OK).json(point);
      }
    });
  })
  .delete((req, res) => {
    // Delete is done by the marker's lat and lng, which is the only unique identifier in our system (not pretty, I know).
    Points.findOneAndRemove({ 'latitude': req.query.latitude, 'longitude': req.query.longitude }, (err, point) => {
      if (err) {
        res.status(HttpStatus.NOT_FOUND).send(err);
      } else {
        res.status(HttpStatus.OK).json(point);
      }
    });
  });

module.exports = router;