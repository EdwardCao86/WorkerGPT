<script setup>

import { useInputStore } from '@/stores/inputContent'
import {storeToRefs} from "pinia";
import {UserFilled} from "@element-plus/icons-vue";
import DialogContainer from "@/components/DialogContainer.vue";

const store = useInputStore()

const { inputText }= storeToRefs(store)


</script>

<template>
    <div class="chatContent">
      <el-scrollbar>
        <ul>
          <li v-for="(m) in inputText" class="scrollbar-demo-item">
            <dialog-container :text=m></dialog-container>
          </li>
        </ul>
      </el-scrollbar>
    </div>
</template>

<style scoped>

.chatContent{
  height: 700px;
}

@media screen and (max-width: 500px) {
  .chatContent {
    height: 500px;
  }
}

/* 当显示器宽度大于1200px时，修改高度 */
@media screen and (min-height: 1200px) {
  .chatContent {
    height: 1100px;
  }
}
p {
  word-wrap: break-word;
}
.scrollbar-demo-item {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin: 10px;
  text-align: left;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
ul{
  display: flex;
  flex-direction: column;
}
</style>