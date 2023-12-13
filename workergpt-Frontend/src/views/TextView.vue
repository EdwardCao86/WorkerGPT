<script setup>

</script>

<template>
  <el-container class="ec">
    <el-aside class="side-bar" width="300px">Aside</el-aside>
    <el-container>
      <el-main class="dialog-container">Main</el-main>
      <el-footer class="input-container">fotter</el-footer>
    </el-container>
  </el-container>
</template>


<style scoped>
.ec{
  height: 100%;
  width: 80%;
  margin: auto;
}
.main-container{
  background-color: yellowgreen;
  height: 100%;
  width: 80%;
  margin: auto;
}
.side-bar{
  height: 100%;
  background-color: yellow;
}
.dialog-container{
  height: 100%;
  background-color: lightgreen;
}

.input-container{
  background-color: deepskyblue;
}

</style>
