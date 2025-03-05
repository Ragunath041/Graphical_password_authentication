import { createRouter, createWebHistory } from 'vue-router'
import TheWelcome from '../components/TheWelcome.vue'
import MainPage from '../components/MainPage.vue'

const routes = [
  {
    path: '/',
    name: 'Welcome',
    component: TheWelcome
  },
  {
    path: '/main',
    name: 'Main',
    component: MainPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router