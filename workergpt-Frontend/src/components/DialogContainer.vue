<script setup>
import {ref, toRefs, watch} from "vue";
import MarkdownIt from 'markdown-it'
import { marked } from 'marked'
const props = defineProps({
  text:{}
})

//使用父组件传递过来的值
const { content } = toRefs(props)
const md = new MarkdownIt()

</script>

<template>
  <div v-if="text.role === 'user'">
    <span>🟦</span>
    <p v-html="md.render(text.content.replace(/\\n/g, '\n'))"></p>
  </div>
  <div v-else>
    <span>🟩</span>
    <p v-html="md.render(text.content.replace(/\\n/g, '\n'))"></p>
  </div>
</template>
<style scoped>

</style>