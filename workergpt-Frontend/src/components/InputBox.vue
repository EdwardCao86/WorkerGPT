<script setup lang="ts">
import {ref} from "vue"
import { reactive } from 'vue'
import { genFileId } from 'element-plus'

// 表单上传



const formData = reactive({
  inputText:''
})

const onSubmit = () => {
  console.log(formData.inputText)
}
</script>

<template>
  <div class="input-container" style="width: 100%">
    <el-form  :inline="true" :model="formData" class="input-form">
      <el-row>
        <el-col :span="20">
          <el-form-item style="width: 100%">
            <el-input
                v-model="formData.inputText"
                :autosize="{ minRows: 1, maxRows: 3 }"
                type="textarea"
                placeholder="😊请在这里输入需要你要问的问题!😊"
            />
          </el-form-item>
        </el-col>
        <el-col :span="4" style="padding-left: 90px">
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