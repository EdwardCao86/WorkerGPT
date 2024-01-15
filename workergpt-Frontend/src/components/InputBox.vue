<script setup lang="ts">

import { reactive } from 'vue'
import { useInputStore } from '@/stores/inputContent'
import { Upload } from "@element-plus/icons-vue";

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
function getQuotedSubstrings(input: string): string[] {
  const substrings: string[] = [];
  const regex = /"([^"]*)"/g;
  let match: RegExpExecArray | null;

  while ((match = regex.exec(input)) !== null) {
    substrings.push(match[1]);
  }

  return substrings;
}
function replaceSingleQuotesWithDoubleQuotes(jsonString: string): object {
  const modifiedJsonString = jsonString.replace(/'/g, '"').replace(/None/g, 'null');
  const jsonObject = JSON.parse(modifiedJsonString);
  return jsonObject;
}



// gpt请求
function makeGptRequest(inputText: string) {

  console.log(inputText)
  input.gptReply()
  const requestOptions = {
    method: 'POST', // 请求方法，可以是GET、POST等
    headers: { "Content-Type": 'application/json' }, // 请求头，指定数据格式为JSON
	body: JSON.stringify({ query : inputText}) // 请求体，将字符串转换为JSON格式
  };
  // 发送请求到后端获取流式输出
  // 发送请求
  fetch('/api/chat', requestOptions)
    .then(async response => {
      //获取UTF8的解码
      const encode = new TextDecoder("utf-8");
      //获取body的reader
      const reader = response.body.getReader();
      // 循环读取reponse中的内容
      while (true) {
        const { done, value } = await reader.read();
        if (done) {
          break;
        }
        // 使用正则表达式匹配所有双引号中间的内容

        let result;
        result = encode.decode(value)

        const quotedSubstrings = getQuotedSubstrings(result);
        for (const substring of quotedSubstrings) {
          const jsonObject = replaceSingleQuotesWithDoubleQuotes(substring);
          const text = jsonObject.choices[0].delta.content
          input.pushContent(text)

        }




      }

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