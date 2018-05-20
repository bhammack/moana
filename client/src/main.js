// This is the main entry point for constructing the single js bundle delivered to the client.

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';

// Css first, then JS.
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import 'font-awesome/css/font-awesome.min.css';
// I hate this library.
import VueMqtt from 'vue-mqtt';

// Dynamically get the current server's hosting information to connect via websockets.
const mqtt_protocol = 'ws';
const mqtt_hostname = window.location.hostname;
const mqtt_port = window.location.port || '80';
var mqtt_host;

console.log(process.env.NODE_ENV)
if (process.env.NODE_ENV == 'development') {
  mqtt_host = 'ws://broker.mqttdashboard.com:8000/mqtt';
} else {
  mqtt_host = mqtt_protocol + '://' + mqtt_hostname + ':' + mqtt_port;
}

const mqtt_options = {
  reconnectPeriod: 5000
}
console.log('Connecting to mqtt broker: ' + mqtt_host);
Vue.use(VueMqtt, mqtt_host, mqtt_options);
Vue.config.productionTip = false;
var vm = new Vue({
  el: '#app',
  router: router,
  components: { App },
  template: '<App/>'
});
