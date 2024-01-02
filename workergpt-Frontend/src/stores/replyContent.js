import { defineStore } from 'pinia';
import {ref} from "vue";

export const useReplyStore = defineStore('reply', () => {
    const replyText = ref([])
    function changeContent(text) {
        replyText.value.push(text)
    }
    return {replyText,changeContent}
})
