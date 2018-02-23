// This is the main entry point for constructing the single js bundle delivered to the client.

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

// Import bootstrap js
import 'bootstrap'

// Import bootstrap css
import 'bootstrap/dist/css/bootstrap.min.css'
//import '../static/bootswatch-flatly.min.css'

Vue.config.productionTip = false

Vue.component()

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
