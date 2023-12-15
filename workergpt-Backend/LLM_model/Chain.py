import zhipuai

from . import zhipuLLM 
from . import Retrieval
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

def text_stream(template : str, query : dict, db : Retrieval.VectorDB, topk: int = 10):
	prompt = ChatPromptTemplate.from_template(template)
	model = zhipuLLM.ChatGLM()
	output_parser = StrOutputParser()
	keys = list(range(1, len(topk)))
	values = db.query(query)["documents"]
	query.update({key: value for key, value in zip(keys, values)})
	chain = prompt | model | output_parser

	for chunk in chain.stream(query):
		print(chunk, end="", flush=True)
