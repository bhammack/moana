const express = require('express');
const router = express.Router();
const HttpStatus = require('http-status-codes');

var Vehicle = require('../models/vehicle');
var Telemetry = require('../models/telemetry');


// https://gist.github.com/subfuzion/669dfae1d1a27de83e69




// Get the root of the API. Use this as a help to show what endpoints are available.
router.get('/', (req, res) => {
  res.json({message: 'rest api root access'});
});



router.route('/vehicles')
  .get((req, res) => {
    // Get a list of all registered vehicles in the MOANA system.
    Vehicle.find({}, (err, vehicles) => {
      if (err) {
        res.status(HttpStatus.INTERNAL_SERVER_ERROR).send(err);
      } else {
        res.status(HttpStatus.OK).json(vehicles);
      }
    });
  })
  .post((req, res) => {
    // Post a new vehicle to the collection.
    var vehicle = new Vehicle();
    vehicle.name = req.body.name;
    vehicle.save((err) => {
      if (err) {
        res.status(HttpStatus.NOT_FOUND).send(err);
      } else {
        res.status(HttpStatus.OK).json(vehicle);
      }
    });
  });



router.route('/vehicles/:vehicle_id')
  .get((req, res) => {
    Vehicle.findById(req.params.vehicle_id, (err, vehicle) => {
      if (err) {
        res.status(HttpStatus.NOT_FOUND).send(err);
      } else {
        res.status(HttpStatus.OK).json(vehicle);
      }
    });
  })
  .put((req, res) => {
    Vehicle.findById(req.params.vehicle_id, (err, vehicle) => {
      if (err) {
        res.status(HttpStatus.NOT_FOUND).send(err);
      } else {
        vehicle.name = req.body.name;
        vehicle.save();
        res.status(HttpStatus.OK).json(vehicle);
      }
    });

  })
  .delete((req, res) => {
    // Remove a vehicle. Also remove all of it's recorded telemetry data.
    Vehicle.findByIdAndRemove(req.param.vehicle_id, (err, vehicle) => {
      if (err) {
        res.status(HttpStatus.NOT_FOUND).send(err);
      } else {
        res.status(HttpStatus.OK).json(vehicle); // return the vehicle removed.

        // Now remove the telemetry.
      }
    });
  })



router.route('/vehicles/:vehicle_id/telemetry')
  .get((req, res) => {
    // Get a list of all recorded telemetry objects for a given vehicle_id.
    Vehicle.findById(req.params.vehicle_id).populate('telemetry').exec((err, vehicle) => {
      if (err) {
        res.status(HttpStatus.NOT_FOUND).send(err);
      } else {
        res.status(HttpStatus.OK).json(vehicle.telemetry);
      }
    });
  })
  .post((req, res) => {
    // Add a new telemetry object to the vehicle's list of recorded telemetry.
    var telemetry = new Telemetry(req.body); // This should auto json map?
    Vehicle.findById(req.params.vehicle_id).populate('telemetry').exec((err, vehicle) => {
      telemetry.vehicle = vehicle;
      telemetry.save();
      vehicle.telemetry.push(telemetry);
      vehicle.dateLastContacted = Date.now();
      vehicle.save();
      res.status(HttpStatus.OK).send('it worked!');
    });
  });



router.route('/vehicles/:vehicle_id/telemetry/:telemetry_name')
  .get((req, res) => {
    // In case the client desires just a list of ONE telemetry object, they can call this route.
    // Ex: /vehicles/xys123/telemetry/temperature returns just a bundled list of 
    /*
      {
        temperature: 45
        date-recorded: 122117:12312pm
      }
    */
  });


module.exports = router;