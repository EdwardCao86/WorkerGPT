<template>
  <el-upload
      class="upload"
      drag
      action="https://run.mocky.io/v3/311e58ad-2924-4180-8901-75bd67f690e9"
      multiple
      :on-error="handleError"
      :on-success="handleSuccess"
      :on-remove="handleRemove"
      :before-remove="handelBeforeRemove"
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
import type { UploadProps} from 'element-plus'
import { UploadFilled } from '@element-plus/icons-vue'
import {ElMessage, ElMessageBox} from "element-plus";
const handelBeforeRemove: UploadProps['beforeRemove'] = (uploadFile, uploadFiles) => {
  return ElMessageBox.confirm(
      '确定要移除'+uploadFile.name+'?',
      'Warning',
      {
        confirmButtonText: '确认',
        cancelButtonText: '取消',
        type: 'warning',
      }
  )
      .then(() => true
      )
      .catch(() => {
        ElMessage({
          type: 'info',
          message: '移除取消',
        })
        return false
      })
}

// 处理文件移除
const handleRemove: UploadProps['onRemove'] = (uploadFile, uploadFiles) => {
  uploadFiles.push(uploadFile)
  const fileName = uploadFile.name;
  console.log(fileName)
// 请求参数
  const requestOptions = {
    method: 'POST', // 请求方法，可以是GET、POST等
    headers: { 'Content-Type': 'application/json' }, // 请求头，指定数据格式为JSON
    body: JSON.stringify({ filename : fileName }) // 请求体，将字符串转换为JSON格式
  };
// 发送请求
  fetch('https://run.mocky.io/v3/930341e1-c2ca-4562-9a55-c1d26875e515', requestOptions)
      .then(response => response.json())
      .then(data => {
        console.log(data)
        // 在这里处理后端返回的数据
        if (data.success === false) {
          ElMessage.error('Oops, 文件:'+data.filename+'移除失败😿'+data.message)

        }else {
          uploadFiles.splice(uploadFile)
          ElMessage({
            message: '成功移除文件:' + data.filename + '😊',
            type: 'success',
          })
        }
      })
      .catch(error => {
        // 在这里处理请求错误
        console.error('Error:', error);
        return false
      });
}


const handleError: UploadProps['onError'] = (error, file) => {
  ElMessage.error('Oops, 文件:'+file.name+'上传失败😿')
}
const handleSuccess: UploadProps['onSuccess'] = (response, uploadFile) => {
  ElMessage({
    message: '成功上传文件' + uploadFile.name + '😊',
    type: 'success',
  })
}
</script>
