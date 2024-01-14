import { defineStore } from 'pinia'
import {ref} from "vue";


export const useInputStore = defineStore('input', () => {
    const inputText = ref([])
    function changeContent(content,role) {
        inputText.value.push(
            {
                'content':'User: \n'+content,
                'role':role
            }
        )
    }
    function gptReply() {
        inputText.value.push(
            {
                'content':'',
                'role':'gpt'
            }
        )
    }
    function pushContent(word) {
        const pos = inputText.value.length - 1
        if (word === null) return
        inputText.value[pos].content += word
    }
    return {inputText,changeContent,gptReply,pushContent}
})

