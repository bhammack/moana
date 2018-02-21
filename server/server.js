// Modules ================================================================================================================================
const express       = require('express');
const path          = require('path');
const http          = require('http');
const bodyParser    = require('body-parser');                 // pull information from html POST (express4)
const mongoose      = require('mongoose');                    // for interactions with mongodb
const morgan        = require('morgan');                      // log requests to the console

// Mongoose configuration =================================================================================================================
var database        = require('./config/database');           // load database.js exports object

// ES6 promise returned from connect. .then(resolve, reject);
mongoose.connect(database.url, {}).then(  
  () => { 
    console.log('mongoose connected');
  }, // connection ready to use.
  err => {
    console.log(err);
  }
);

// Express configuration ==================================================================================================================
const port = process.env.PORT || '3000';                      // Get port from environment and store in Express.
const app = express();

app.use(bodyParser.json());                                   // parse application/json
app.use(bodyParser.urlencoded({ extended: true }));          // parse application/x-www-form-urlencoded
app.use(express.static(path.join(__dirname, '../client/dist')));        // set the static files location (/public/js will be /js for clients)

// API configuration ======================================================================================================================
const api = require('./routes/api');                   // Get our API router object.
app.use('/api', api);                                         // Set our api routes

// Express Routes =========================================================================================================================
app.get('*', (req, res) => {                                  // Catch all other routes and return the index file
  res.sendFile(path.join(__dirname, '../client/dist/index.html'));
});

// Server start ===========================================================================================================================
app.set('port', port);
const server = http.createServer(app);                                      // Create HTTP server.
server.listen(port, () => {
  console.log(`Server running on localhost:${port}`);
});