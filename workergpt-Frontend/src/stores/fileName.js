import { defineStore } from 'pinia'
import {ref} from "vue";


export const useFileStore = defineStore('file', () => {
    const file = ref('')
    function changeFile(newFile) {
        file.value = newFile
    }
    return {file,changeFile}
})

