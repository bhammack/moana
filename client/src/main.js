// This is the main entry point for constructing the single js bundle delivered to the client.

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';

// Import bootstrap js
import 'bootstrap';
// Import bootstrap css
import 'bootstrap/dist/css/bootstrap.min.css';
//import '../static/bootswatch-flatly.min.css'

//import $ from 'jquery';
import mqtt from 'async-mqtt';
import axios from 'axios';

import 'datatables.net-bs4/css/dataTables.bootstrap4.css';
import 'datatables.net-bs4';
//require('datatables.net-bs4')(window, $);

Vue.config.productionTip = false;
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});

// var client = mqtt.connect('mqtt://test.mosquitto.org')
// // Connect does not return a promise...
// client.on('connect', () => {
//   // sub
//   console.log('connect response')
// })

