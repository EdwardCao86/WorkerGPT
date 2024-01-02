<script setup lang="ts">

import { reactive } from 'vue'
import { useInputStore } from '@/stores/inputContent'
import { Upload } from "@element-plus/icons-vue";
import { useReplyStore } from '@/stores/replyContent';

// 表单上传
// 输入框数据
const inputMessage = reactive({
	content: '',
})
const input = useInputStore()
const reply = useReplyStore()

function submit() {
	input.changeContent(inputMessage.content)
	const inputText = inputMessage.content
	inputMessage.content = ''
	makeGptRequest(inputText)
}

// gpt请求
function makeGptRequest(inputText: string) {

  console.log(inputText)
  const requestOptions = {
    method: 'POST', // 请求方法，可以是GET、POST等
    headers: { "Content-Type": 'application/json' }, // 请求头，指定数据格式为JSON
	body: JSON.stringify({ query : inputText}) // 请求体，将字符串转换为JSON格式
  };
  // 发送请求到后端获取流式输出
  // 发送请求
  fetch('/api/chat', requestOptions)
    .then(response => {
      // 获取可读流
      const reader = response.body.getReader();
  
      // 读取数据
      return new ReadableStream({
        start(controller) {
          function push() {
            reader.read().then(({ done, value }) => {
              // 当数据读取完毕时，关闭流
              if (done) {
                controller.close();
                return;
              }
  		
              // 将数据放入流中
              controller.enqueue(value);
  		
              // 读取下一块数据
              push();
            });
          };
  	
          push();
        }
      });
    })
    .then(stream => {
      // 将流转换为文本
  	console.log(stream)
      return new Response(stream).text();
  	
    })
    .then(result => {
      // 处理结果
	  console.log(result);
	  reply.changeContent(result)
    });
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
							placeholder="😊请在这里输入需要你要问的问题!😊"
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