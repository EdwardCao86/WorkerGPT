这是worker-gpt的后端工程。

## 工程架构
这个工程使用flask与langchain配合完成。
主要的代码部分位于LLM_model中，是直接调用大模型与使用Chromadb的部分。

## 部署
首先安装相关的环境
``` bash
conda env create -f environment.yml
```
然后启动这个环境
```bash
conda activate langchain
```
然后启动这个app
```bash
flask run
```
这样后端就启动啦！

