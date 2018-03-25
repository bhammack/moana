const express = require('express');
const router = express.Router();
const HttpStatus = require('http-status-codes');

//var Points = require('../models/points');
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

  })
  .delete((req, res) => {

  });

module.exports = router;