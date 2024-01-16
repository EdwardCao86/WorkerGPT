import { createRouter, createWebHistory } from 'vue-router'

import IndexView from "@/views/IndexView.vue";
import DataView from "@/views/DataView.vue";
import TextGeneration from "@/views/GenerationView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: IndexView
    },
    {
      path: '/DataAnalysis',
      name: 'DataAnalysis',
      component: DataView
    },
    {
      path: '/TextGeneration',
      name: 'TextGeneration',
      component: TextGeneration
    }
  ]
})

export default router
