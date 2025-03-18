<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import Main from './components/MainPage.vue'
import { ref, onMounted, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const route = useRoute()
const showHeader = computed(() => route.path !== '/main')
</script>

<template>
  <!-- <header v-if="showHeader">
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
    <HelloWorld msg="Graphical User Authentication" />
  </header> -->
  <router-view></router-view>
</template>

<style scoped>
header {
  line-height: 1.5;
  display: flex;
  justify-content: center;
  padding: 1rem;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
