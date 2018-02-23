// Modules ================================================================================================================================
const express       = require('express');
const path          = require('path');
const http          = require('http');
const bodyParser    = require('body-parser');                 // pull information from html POST (express4)
const mongoose      = require('mongoose');                    // for interactions with mongodb
const morgan        = require('morgan');                      // log requests to the console

// Custom includes ========================================================================================================================
const api           = require('./routes/api');                // Get our API router object.
const database      = require('./config/database');           // load database.js exports object

// ES6 promise returned from connect. .then(resolve, reject);
mongoose.connect(database.url, {}).then(
  () => { 
    console.log('mongoose connected');
  }, 
  (err) => {
	console.log('unable to connect to mongo.db instance');
    //console.log(err);
  }
);

// Express configuration ==================================================================================================================
const app = express();
const port = process.env.PORT || '3000';                      // Get port from environment and store in Express.
app.set('port', port);
app.use(bodyParser.json());                                   // parse application/json
app.use(bodyParser.urlencoded({ extended: true }));           // parse application/x-www-form-urlencoded

// Node modules javascript files ==========================================================================================================
//app.use('/scripts', express.static(path.join(__dirname, '../node_modules/vue/dist/'))); // old way for reference
//app.use('/js', express.static('./node_modules/jquery/dist/'));
//app.use('/js', express.static('./node_modules/popper.js/dist/umd/'));
//app.use('/js', express.static('./node_modules/vue/dist/'));
//app.use('/js', express.static('./node_modules/mqtt/dist/'));
//app.use('/js', express.static('./node_modules/axios/dist/'));

// Static routes and content ==============================================================================================================
// This includes js, css, and content folders.
app.use('/', express.static(path.join(__dirname, '../client/dist')));        // set the static files location (/public/js will be /js for clients)
//app.use('/', express.static('./client/dist/'));
//app.use('/', express.static('./node_modules/bootstrap/dist/'));

// API configuration ======================================================================================================================
app.use('/api', api);                                         // Set our api routes

// Express Routes =========================================================================================================================
app.get('*', (req, res) => {                                  // Catch all other routes and return the index file
  res.sendFile(path.join(__dirname, '../client/dist/index.html'));
});

// Server start ===========================================================================================================================
const server = http.createServer(app);                                      // Create HTTP server.
server.listen(port, () => {
  console.log(`Server running on localhost:${port}`);
});
