import Vue from 'vue'
import Router from 'vue-router'
import HomeView from '@/components/HomeView'
import CockpitView from '@/components/CockpitView'
import RecordsView from '@/components/RecordsView'
import AboutView from '@/components/AboutView'
import ApiView from '@/components/ApiView'
import MapVue from '@/components/MapVue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: HomeView
    },
    {
      path: '/home',
      component: HomeView
    },
    {
      path: '/api',
      component: ApiView
    },
    {
      path: '/cockpit',
      component: CockpitView
    },
    {
      path: '/records',
      component: RecordsView
    },
    {
      path: '/about',
      component: AboutView
    },
    {
      path: '/map',
      component: MapVue
    }
  ]
})
