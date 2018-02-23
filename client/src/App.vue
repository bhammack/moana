<template>
  <div id="vue-app">
    <app-navbar></app-navbar>
    <router-view/>
  </div>
</template>

<script>
import AppNavbar from './components/app-navbar.vue'

export default {
  name: 'App',
  components: {
    AppNavbar
  }
}
</script>