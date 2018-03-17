// Modules ================================================================================================================================
require('dotenv').config();
const express       = require('express');
const path          = require('path');
const http          = require('http');
const bodyParser    = require('body-parser');                 // pull information from html POST (express4)
const mongoose      = require('mongoose');
const morgan        = require('morgan');                      // log requests to the console
const mqtt          = require('mqtt');                        // might not need this
const mosca         = require('mosca');
const ra2           = require('./plugins/ra2');

// Establish Mongodb connector ============================================================================================================
const apiRouter     = require('./routes/api');                // Get our API router object.
const db_host = process.env.DB_HOST || 'mongodb://localhost:27017';
const port = process.env.PORT || '3000';

console.log('"' + ra2.quote() + '"');
mongoose.connect(db_host, {}).then(() => { 
    console.log('mongoose connected');
  }, (err) => {
	  console.log('unable to connect to mongo.db instance');
  }
);

// Mqtt Subscribers =======================================================================================================================
/*
const client = mqtt.connect('ws://broker.mqttdashboard.com:8000/mqtt');
const Telemetry = require('./models/telemetry');

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
*/
// Express configuration ==================================================================================================================
const app = express();
app.set('port', port);
app.use(morgan('combined'));
app.use(bodyParser.json());                                   // parse application/json
app.use(bodyParser.urlencoded({ extended: true }));           // parse application/x-www-form-urlencoded

// Express routes =========================================================================================================================
app.use('/', express.static(path.join(__dirname, '../client/dist')));
app.use('/api', apiRouter);
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../client/dist/index.html'));
});

// Server start ===========================================================================================================================
const server = http.createServer(app);

// Attach the message broker to the http server for websocket support on the same port ====================================================
var backendstore = {
  type: 'mongo',
  url: process.env.DB_HOST + '/mqtt',
  pubsubCollection: 'ascoltatori',
  mongo: {}
}
var broker = new mosca.Server({
  port: 1883
  //backend: backendstore
});
broker.on('ready', () => {
  console.log('mqtt broker online');
});
broker.on('clientConnected', (client) => {
  console.log('client connected');
});
broker.on('clientDisconnected', (client) => {
  console.log('client disconnected');
});
broker.on('published', (packet, client) => {
  console.log(packet);
});
broker.attachHttpServer(server);

// Finally, start the http server =========================================================================================================
server.listen(port, () => {
  console.log(`Server running on localhost:${port}`);
});
