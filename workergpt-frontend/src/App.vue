<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HeadBar from "@/components/HeadBar.vue";
</script>

<template>
  <header>
    <HeadBar></HeadBar>

  </header>

  <RouterView />
</template>

<style scoped>

</style>
