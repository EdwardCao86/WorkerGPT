import { createRouter, createWebHistory } from 'vue-router'

import IndexView from "@/views/IndexView.vue";
import DataView from "@/views/DataView.vue";
import TextView from "@/views/TextView.vue";

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
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../views/AboutView.vue')
    },
    {
      path: '/TextAnalysis',
      name: 'TextAnalysis',
      component: TextView
    }
  ]
})

export default router
