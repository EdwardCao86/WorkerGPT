import zhipuai

import globals
from zhipuLLM import ChatGLM
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
import configparser
from globals import global_vars

config = configparser.ConfigParser()
config.read('../config.ini')
# print(config.sections())
api_key = config.get("ZHI_PU_API", "api_key")
global_vars.set("api_key", api_key)
print("USING API KEY: ", api_key)
zhipuai.api_key = globals.global_vars.get("api_key")

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatGLM()
# model = CustomLLM(n=10)
output_parser = StrOutputParser()
# prompt |
chain = model | output_parser

for chunk in chain.stream("请讲述一个关于“冰淇淋”的笑话"):
    print(chunk, end="", flush=True)
# res = chain.invoke({"topic": "ice cream"})
# print(res)