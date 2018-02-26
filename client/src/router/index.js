import Vue from 'vue'
import Router from 'vue-router'
import IndexView from '@/components/IndexView'
import CockpitView from '@/components/CockpitView'
import RecordsView from '@/components/RecordsView'
import AboutView from '@/components/AboutView'
import ApiView from '@/components/ApiView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ugg',
      component: IndexView
    },
    {
      path: '/api',
      name: 'Api',
      component: ApiView
    },
    {
      path: '/cockpit',
      name: 'Cockpit',
      component: CockpitView
    },
    {
      path: '/records',
      name: 'Records',
      component: RecordsView
    },
    {
      path: '/about',
      name: 'doesntmatter',
      component: AboutView
    }
  ]
})
