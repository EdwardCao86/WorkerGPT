import zhipuai

from . import openaiLLM 
from . import Retrieval
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from logging import getLogger

def text_stream(template : str, query : dict, db : Retrieval.VectorDB, topk: int = 10):
	prompt = ChatPromptTemplate.from_template(template)
	model = openaiLLM.ChatGLM()
	output_parser = StrOutputParser()
	values = db.query(query['query'])["documents"][0]
	res = {}
	for i in range(topk):
		res['document' + str(i + 1)] = ''
	for i in range(len(values)):
		res['document' + str(i + 1)] = values[i]
	chain = prompt | model | output_parser
	res['query'] = query['query']
	print(res)

	for chunk in chain.stream(res):
		yield chunk
