<template>
  <div id="vue-app">
    <header>
      <app-navbar></app-navbar>
    </header>
    <main>
      <transition name="fade">
        <router-view></router-view>
      </transition>
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
    },
    beforeDestroy: function() {
      console.log('bye bye!');
      this.$mqtt.end();
    }
}
</script>
<style>
  main {
    height: calc(100vh - 56px);
  }

.fade-enter-active, .fade-leave-active {
  transition-property: opacity;
  transition-duration: .25s;
}

.fade-enter-active {
  transition-delay: .25s;
}

.fade-enter, .fade-leave-active {
  opacity: 0
}
</style>