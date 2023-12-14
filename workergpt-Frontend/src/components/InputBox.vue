<script setup lang="ts">

import { reactive } from 'vue'
import { useInputStore } from '@/stores/inputContent'

// 表单上传
// 输入框数据
const inputMessage = reactive({
  content: '',
})
const store = useInputStore()

function submit () {
  store.changeContent(inputMessage.content)
  inputMessage.content = ''


}
// gpt请求


</script>

<template>
  <div class="input-container">
    <el-form  :inline="true" :model="inputMessage" class="input-form">
      <el-row>
        <el-col :span="20" :offset="1">
          <el-form-item style="width: 100%">
            <el-input
                v-model="inputMessage.content"
                :autosize="{ minRows: 1, maxRows: 2 }"
                type="textarea"
                placeholder="😊请在这里输入需要你要问的问题!😊"
            />
          </el-form-item>
        </el-col>
        <el-col :span="2" style="padding-left: 20px">
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
.input-form{
  width: 100%;
}
el-form-item{
  width: 100%;
}
.input-container{
  height: 30%;
  width: 100%;
  padding-top: 15px;
}
</style>