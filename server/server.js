// Modules ================================================================================================================================
const express       = require('express');
const path          = require('path');
const http          = require('http');
const bodyParser    = require('body-parser');                 // pull information from html POST (express4)
const mongoose      = require('mongoose');                    // for interactions with mongodb
const morgan        = require('morgan');                      // log requests to the console
const mqtt          = require('mqtt');

// Establish Mongodb connector ============================================================================================================
const api           = require('./routes/api');                // Get our API router object.
const database      = require('./config/database');           // load database.js exports object

// ES6 promise returned from connect. .then(resolve, reject);
mongoose.connect(database.url, {}).then(() => { 
    console.log('mongoose connected');
  }, (err) => {
	console.log('unable to connect to mongo.db instance');
  }
);

// Mqtt Subscribers =======================================================================================================================
const client = mqtt.connect('ws://broker.mqttdashboard.com:8000/mqtt');
const Telemetry = require('./models/telemetry');

//const client = mqtt.connect('mqtt://test.mosquitto.org');
client.on('connect', () => {
  console.log('mqtt connected');
  client.subscribe('telemetry');
});
client.on('error', (error) => {
  console.log(error);
});
client.on('message', (topic, message) => {
  //console.log(message.toString());
  var obj = JSON.parse(message.toString());
  var telemetry = new Telemetry();
  telemetry.altitude = obj.altitude;
  telemetry.power = obj.power;
  telemetry.temperature = obj.temperature;
  telemetry.save((err) => {
    if (err) {
      console.log('error on saving telemetry packet');
    } else {
      console.log('telemetry packet captured');
    }
  });


});





// Express configuration ==================================================================================================================
const app = express();
const port = process.env.PORT || '3000';                      // Get port from environment and store in Express.
app.set('port', port);
app.use(bodyParser.json());                                   // parse application/json
app.use(bodyParser.urlencoded({ extended: true }));           // parse application/x-www-form-urlencoded

// Static routes and content ==============================================================================================================
// This includes js, css, and content folders.
app.use('/', express.static(path.join(__dirname, '../client/dist')));

// API configuration ======================================================================================================================
app.use('/api', api);

// Express Routes =========================================================================================================================
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../client/dist/index.html'));
});

// Server start ===========================================================================================================================
const server = http.createServer(app);                                      // Create HTTP server.
server.listen(port, () => {
  console.log(`Server running on localhost:${port}`);
});

