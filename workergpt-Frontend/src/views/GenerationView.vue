<script setup>

import FIleUploadSider from "@/components/FIleUploadSider.vue";
import InputBox from "@/components/InputBox.vue";
</script>

<template>
  <el-container class="ec">
    <el-aside class="side-bar" width="30%">
      <FIleUploadSider></FIleUploadSider>
    </el-aside>
    <el-container>
      <el-main class="dialog-container">Main</el-main>
      <el-footer class="input-container"><InputBox></InputBox></el-footer>
    </el-container>
  </el-container>
</template>


<style scoped>
.ec{
  height: 100%;
  width: 80%;
  margin: auto;
}
.side-bar{
  height: 100%;
  background-color: whitesmoke;

}
.dialog-container{
  height: 100%;
  background-color: lightgreen;
}

.input-container{
 background-color: yellow;
}

</style>
