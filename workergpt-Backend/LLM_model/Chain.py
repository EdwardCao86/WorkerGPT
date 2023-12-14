import zhipuai

from . import zhipuLLM 
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

def text_stream(template : str, query : str):
	prompt = ChatPromptTemplate.from_template(template)
	test_prompt =ChatPromptTemplate.from_template("hello world!")
	model = zhipuLLM.ChatGLM()
	# model = CustomLLM(n=10)
	output_parser = StrOutputParser()
	chain1 = prompt | test_prompt
	chain = prompt | model | output_parser

	for chunk in chain1.stream(query):
		print(chunk, end="", flush=True)
	for chunk in chain.stream(query):
    
		print(chunk, end="", flush=True)
	# res = chain.invoke({"topic": "ice cream"})
	# print(res)