<template>
  <div id="vue-app">
    <header>
      <app-navbar></app-navbar>
    </header>
    <main>
      <router-view></router-view>      
    </main>
    <footer>
      
    </footer>
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