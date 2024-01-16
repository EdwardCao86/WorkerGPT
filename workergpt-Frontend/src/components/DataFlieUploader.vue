<template>
  <el-upload
      class="upload"
      drag
      action="/api/upload"
      multiple
      :on-error="handleError"
      :on-success="handleSuccess"
      :on-remove="handleRemove"
      :before-remove="handelBeforeRemove"
      :file-list="filesList"
      :limit = "1"
      :on-exceed="handleExceed"
  >
    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
    <div class="el-upload__text">
      将要上传的文件📁拖到这里 <em>或点击上传</em>
    </div>
    <template #tip>
      <div class="el-upload__tip">
        支持csv文件,一次只能上传一个文件分析
      </div>
    </template>
  </el-upload>
</template>

<script setup lang="ts">
import type { UploadProps} from 'element-plus'
import { UploadFilled } from '@element-plus/icons-vue'
import {ElMessage, ElMessageBox} from "element-plus";
import {ref} from "vue";
const filesList = ref([])

const handleExceed: UploadProps['onExceed'] = (files, uploadFiles) => {
  ElMessage.warning(
      "一次只可以上传一个文件，请移除上一个文件后重试😿"
  )
}

const handelBeforeRemove: UploadProps['beforeRemove'] = (uploadFile) => {
  return ElMessageBox.confirm(
      '确定要移除:'+uploadFile.name+'?',
      '提示',
      {
        confirmButtonText: '确认',
        cancelButtonText: '取消',
        type: 'info',
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
    headers: { "Content-Type": 'application/json' }, // 请求头，指定数据格式为JSON
    body: JSON.stringify({ filename : fileName }) // 请求体，将字符串转换为JSON格式
  };
// 发送请求
  fetch('/api/delete', requestOptions)
      .then(response => response.json())
      .then(data => {
        console.log(data)
        // 在这里处理后端返回的数据
        if (data.success === false) {
          ElMessage.error('Oops, 文件：'+data.filename+'移除失败😿'+data.message)

        }else {
          uploadFiles.splice(uploadFiles.indexOf(uploadFile))
          ElMessage({
            message: '成功移除文件：' + data.filename + '😊',
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
  ElMessage.error('Oops, 文件：'+file.name+'上传失败😿')
}
import { useFileStore } from '@/stores/fileName'

const file = useFileStore()

const handleSuccess: UploadProps['onSuccess'] = (response, uploadFile) => {
  ElMessage({
    message: '成功上传文件：' + uploadFile.name + '😊',
    type: 'success',
  })
  file.changeFile(uploadFile.name)
}
</script>
