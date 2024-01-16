<script setup>

import FIleUploadSider from "@/components/FIleUploadSider.vue";
import InputBox from "@/components/InputBox.vue";
import ChatBox from "@/components/ChatBox.vue";
import DataInput from "@/components/DataInput.vue";
import DataFlieUploader from "@/components/DataFlieUploader.vue";
import ImgContainer from "@/components/ImgContainer.vue";
</script>

<template>
  <el-container class="ec">
    <el-aside class="side-bar" width="300px">
      <DataFlieUploader></DataFlieUploader>
    </el-aside>
    <el-container>
      <el-main class="dialog-container">
        <imgContainer></imgContainer>
      </el-main>
      <el-footer class="input-container">
        <DataInput></DataInput>
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
