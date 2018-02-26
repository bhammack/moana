import Vue from 'vue'
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'
import IndexRoute from '@/components/IndexRoute'
import CockpitRoute from '@/components/CockpitRoute'
import RecordsRoute from '@/components/RecordsRoute'
import AboutRoute from '@/components/AboutRoute'
import ApiRoute from '@/components/ApiRoute'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ugg',
      component: IndexRoute
    },
    {
      path: '/api',
      name: 'Api',
      component: ApiRoute
    },
    {
      path: '/cockpit',
      name: 'Cockpit',
      component: CockpitRoute
    },
    {
      path: '/records',
      name: 'Records',
      component: RecordsRoute
    },
    {
      path: '/about',
      name: 'doesntmatter',
      component: AboutRoute
    }
  ]
})
