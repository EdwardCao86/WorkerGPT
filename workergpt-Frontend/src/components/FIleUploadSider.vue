<template>
  <el-upload
      class="upload"
      drag
      action="https://run.mocky.io/v3/311e58ad-2924-4180-8901-75bd67f690e9"
      multiple
      :on-remove="handleRemove"
      :on-error="handleError"
      :on-success="handleSuccess"

  >
    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
    <div class="el-upload__text">
      将要上传的文件📁拖到这里 <em>或点击上传</em>
    </div>
    <template #tip>
      <div class="el-upload__tip">
        支持xlsx，docx，csv等文件
      </div>
    </template>
  </el-upload>
</template>

<script setup lang="ts">
import type { UploadProps, UploadUserFile } from 'element-plus'
import { UploadFilled } from '@element-plus/icons-vue'
import {ElMessage} from "element-plus";
// 处理文件移除
const handleRemove: UploadProps['onRemove'] = (file, uploadFiles) => {
  console.log(file, uploadFiles)
  fetch('url')
      .then()
      .catch()

}
const handleError: UploadProps['onError'] = (error, file, uploadFiles) => {
  ElMessage.error('Oops, 文件:'+file.name+'上传失败😿')
}
const handleSuccess: UploadProps['onSuccess'] = (response, uploadFile) => {
  ElMessage({
    message: '成功上传文件' + uploadFile.name + '😊',
    type: 'success',
  })
}
</script>
