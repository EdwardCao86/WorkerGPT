import { defineStore } from 'pinia'
import {ref} from "vue";


export const useInputStore = defineStore('input', () => {
    const inputText = ref([])
    function changeContent(text) {
        inputText.value.push(text)
    }

    return {inputText,changeContent}
})