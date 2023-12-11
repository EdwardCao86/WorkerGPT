<script setup>
//Pinia使用
import { useCounterStore } from '../stores/counter.js'
const store = useCounterStore()

</script>

<template>
<div>
  <h1>count:{{store.count}}</h1>
  <button @click="store.increment()">+1</button>
</div>
</template>

<style scoped>

</style>