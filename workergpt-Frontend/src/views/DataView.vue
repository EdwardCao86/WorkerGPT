<script setup>

import FIleUploadSider from "@/components/FIleUploadSider.vue";
import InputBox from "@/components/InputBox.vue";
import ChatBox from "@/components/ChatBox.vue";
</script>

<template>
  <el-container class="ec">
    <el-aside class="side-bar" width="300px">
      <FIleUploadSider></FIleUploadSider>
    </el-aside>
    <el-container>
      <el-main class="dialog-container">
        <ChatBox></ChatBox>
      </el-main>
      <el-footer class="input-container">
        <input-box></input-box>
      </el-footer>
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
//background-color: lightgreen;
  overflow: hidden;
}

.input-container{
//background-color: deepskyblue;
}

</style>
