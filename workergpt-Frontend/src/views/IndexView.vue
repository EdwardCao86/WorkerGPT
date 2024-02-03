<script setup>

</script>

<template>
  <el-card class="box-card">
    <div class="index-container">
      <el-row :gutter="20">
        <el-col :span="8" :offset="8">
          <img src="../assets/icon.png">
        </el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col :span="24">
          <div class="text-container">
            <h1>😎你好，我是WorkerGPT😎</h1>
            <p>🩷我可以帮助你解决数据与文档相关文件的问题</p>
            <p>💙智能问答可以根据你提供的资料进行知识问答，当然没有提供资料的情况下也可以工作</p>
            <p>💚数据分析可以根据你的要求绘制表格数据的分析图表，例如:“帮我绘制年龄的分布图”</p>
          </div>
        </el-col>
      </el-row>
    </div>
  </el-card>
</template>

<style scoped>

.box-card {
  width: 80%;
  margin: auto;
  height: 100%;
  background-color: whitesmoke;
  overflow-y: auto; /* 显示垂直滚动条 */
}


img{
  width: 100%;
  height: 100%;
}

.text-container{
  text-align: center;
}

p {
  font-weight: bold;

}
</style>