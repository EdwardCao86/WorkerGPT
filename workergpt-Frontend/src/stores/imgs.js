import { defineStore } from 'pinia'
import {ref} from "vue";


export const useImgsStore = defineStore('imgs', () => {
    const imgs = ref([])
    function changeImgs(newImg) {
        imgs.value.push(newImg)
    }
    function clean() {
        imgs.value = []
    }
    return {imgs,changeImgs,clean}
})

