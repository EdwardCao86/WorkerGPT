<script setup lang="ts">

import { reactive } from 'vue'
import { useInputStore } from '@/stores/inputContent'
import { Upload } from "@element-plus/icons-vue";
import { marked } from 'marked'

// 表单上传
// 输入框数据
const inputMessage = reactive({
  content: '',
})
const input = useInputStore()

function submit() {
  input.changeContent(inputMessage.content,'user')
  const inputText = inputMessage.content
  inputMessage.content = ''
  makeGptRequest(inputText)
}
import { useFileStore } from '@/stores/fileName'
import { useImgsStore } from '@/stores/imgs'
const file = useFileStore()
const img = useImgsStore()
// gpt请求
function makeGptRequest(inputText: string) {

  console.log(inputText)
  input.gptReply()
  const requestOptions = {
    method: 'POST', // 请求方法，可以是GET、POST等
    headers: { "Content-Type": 'application/json' }, // 请求头，指定数据格式为JSON
    body: JSON.stringify({ "path" : file.file, "query" : inputText}) // 请求体，将字符串转换为JSON格式
  };
  // 发送请求到后端获取流式输出
  // 发送请求
  fetch('/api/analyze_chat', requestOptions)
      .then(response => response.json())
      .then(result => {
        img.clean()
        console.log(result)
        result.forEach(function(item) {
          console.log(item.image)
          let str = "data:image/png;base64," + item.image
          console.log(str)
          img.changeImgs(str)
        });
      })
}

</script>

<template>
  <div class="input-container">
    <el-form :inline="true" :model="inputMessage" class="input-form">
      <el-row>
        <el-col :span="20" :offset="1">
          <el-form-item style="width: 100%">
            <el-input
                v-model="inputMessage.content"
                :autosize="{ minRows: 1, maxRows: 1 }"
                type="textarea"
                placeholder="😊告诉我你想绘制什么样的图表!😊"
            />
          </el-form-item>
        </el-col>
        <el-col :span="1" :offset="1">
          <el-form-item>
            <el-button type="primary" @click="submit">
              提交<el-icon class="el-icon--right"><Upload /></el-icon>
            </el-button>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
  </div>
</template>

<style scoped>
.input-form {
  width: 100%;
}
el-form-item {
  width: 100%;
}
.input-container {
  height: 30%;
  width: 100%;
  padding-top: 15px;
}
</style>