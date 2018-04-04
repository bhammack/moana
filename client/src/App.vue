<template>
  <div id="vue-app">
    <header>
      <navbar></navbar>
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
import Navbar from './components/Navbar.vue'
export default {
    name: 'App',
    components: {
      'navbar': Navbar
    },
    created: function() {
      window.onbeforeunload = this.onBeforeUnload;
    },
    methods: {
      onBeforeUnload: function() {
        this.$mqtt.end(false, function() {
          console.log('connection closed... smell ya later');
        });
      }
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