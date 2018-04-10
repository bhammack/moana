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

const mqtt_host = 'ws://broker.mqttdashboard.com:8000/mqtt';
const mqtt_options = {}
Vue.use(VueMqtt, mqtt_host, mqtt_options);
Vue.config.productionTip = false;
var vm = new Vue({
  el: '#app',
  router: router,
  components: { App },
  template: '<App/>'
});
