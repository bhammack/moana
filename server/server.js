// Modules ================================================================================================================================
require('dotenv').config();
const express       = require('express');
const path          = require('path');
const http          = require('http');
const bodyParser    = require('body-parser');                 // pull information from html POST (express4)
const mongoose      = require('mongoose');
const morgan        = require('morgan');                      // log requests to the console
const ra2           = require('./plugins/ra2');
const broker        = require('./mosca/broker');              // Get the mosca mqtt broker
const apiRouter     = require('./routes/api');                // Get our API router object

// Establish Mongodb connector ============================================================================================================
const db_host = process.env.DB_HOST || 'mongodb://localhost:27017';
const port = process.env.PORT || '3000';

console.log('"' + ra2.quote() + '"');
mongoose.connect(db_host, {}).then(() => { 
    console.log('mongoose connected');
  }, (err) => {
	  console.log('unable to connect to mongo.db instance');
  }
);

// Express configuration ==================================================================================================================
const app = express();
app.set('port', port);
//app.use(morgan('combined'));
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
broker.attachHttpServer(server);

// Finally, start the http server =========================================================================================================
server.listen(port, () => {
  console.log(`Server running on localhost:${port}`);
});
