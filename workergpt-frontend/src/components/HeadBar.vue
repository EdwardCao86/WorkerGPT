<template>
  <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
  >
    <el-menu-item index="0">
      <h1 id="title">WorkerGPT</h1>
    </el-menu-item>
    <div class="flex-grow" />
    <el-menu-item index="1">文档处理</el-menu-item>
    <el-menu-item index="2">数据分析</el-menu-item>
  </el-menu>

</template>

<script lang="ts" setup>
import { ref } from 'vue'

const activeIndex = ref('0')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}
#title {
  background: linear-gradient(to right, deepskyblue, lawngreen);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
