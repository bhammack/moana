import Vue from 'vue'
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'
import Cockpit from '@/components/Cockpit'
import Records from '@/components/Records'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ugg',
      component: Cockpit
    },
    {
      path: '/api',
      name: 'Api',
      component: null
    },
    {
      path: '/cockpit',
      name: 'Cockpit',
      component: Cockpit
    },
    {
      path: '/records',
      name: 'Records',
      component: Records
    }
  ]
})
