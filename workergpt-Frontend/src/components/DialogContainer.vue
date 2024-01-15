<script setup>
import {ref, toRefs, watch} from "vue";
import MarkdownIt from 'markdown-it'
import { marked } from 'marked'
const props = defineProps({
  content:{}
})

//使用父组件传递过来的值
const { content } = toRefs(props)
const mark = ref('')
const md = new MarkdownIt()

// // const md = MarkdownIt()
// watch(() => props.content, (newMarkdown) => {
//   mark.value = md.render(newMarkdown)
//   // console.log(newMarkdown)
//   console.log(marked(mark.value))
// });


</script>

<template>
  <div v-if="content.role === 'user'">
    <p>🟦<br>{{content.content}}</p>
  </div>
  <div v-else>
    <p>🟩<br>{{content.content}}</p>
  </div>
</template>
<style scoped>

</style>