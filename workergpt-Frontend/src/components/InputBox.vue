<script setup lang="ts">
import {ref} from "vue"
import { reactive } from 'vue'
import { genFileId } from 'element-plus'

// 表单上传
// 输入框数据
const dialogData = reactive({
  inputText: '',
  output: ''
})

// gpt请求

async function onSubmit(){
  const response = await fetch('http://127.0.0.1:7345/api/gpt/get', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: dialogData.inputText,
      role: 'user',
    }),
  });

  if (!response.body) return;
  const reader = response.body.pipeThrough(new TextDecoderStream()).getReader();
  while (true) {
    var { value, done } = await reader.read();
    if (done) break;
    value = value?.replace('undefined', '')
    console.log("received data -", value)
    dialogData.output += value?.replace('undefined', '')
  }
}

</script>

<template>
  <div class="input-container" style="width: 100%">
    <el-form  :inline="true" :model="dialogData" class="input-form">
      <el-row>
        <el-col :span="20" >
          <el-form-item style="width: 100%">
            <el-input
                v-model="dialogData.inputText"
                :autosize="{ minRows: 1, maxRows: 3 }"
                type="textarea"
                placeholder="😊请在这里输入需要你要问的问题!😊"
            />
          </el-form-item>
        </el-col>
        <el-col :span="1">
          <el-form-item>
            <el-button type="primary" @click="onSubmit">提交</el-button>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
  </div>
</template>

<style scoped>
.input-form{
  width: 100%;
}
el-form-item{
  width: 100%;
}
</style>