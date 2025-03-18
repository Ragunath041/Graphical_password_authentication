import { createRouter, createWebHistory } from 'vue-router'
import TheWelcome from '../components/TheWelcome.vue'
import MainPage from '../components/MainPage.vue'
import OtpVerification from '../components/OtpVerification.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: TheWelcome
    },
    {
      path: '/main',
      name: 'main',
      component: MainPage
    },
    {
      path: '/otp',
      name: 'otp',
      component: OtpVerification
    }
  ]
})

export default router