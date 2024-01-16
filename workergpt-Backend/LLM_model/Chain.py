import zhipuai

from .openaiLLM import ChatGLM
from .Retrieval import VectorDB
# from .zhipuLLM import ChatGLM
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

def text_stream(template : str, query : dict, db : VectorDB, topk: int = 10):
	prompt = ChatPromptTemplate.from_template(template)
	model =  ChatGLM()
	output_parser = StrOutputParser()
	values = db.query(query['query'])["documents"][0]
	print(db.count())
	print(values)
	print(len(values))
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
