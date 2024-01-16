import zhipuai

from .openaiLLM import ChatGLM
from .Retrieval import VectorDB
# from .zhipuLLM import ChatGLM
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from .Parser import ListParser, CodeParser
from . import Parser
import csv
import os

def text_stream(template : str, query : dict, db : VectorDB, topk: int = 10):
	prompt = PromptTemplate.from_template(template)
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

def get_csv_header(path: str):
	with open(path, 'r') as file:
		reader = csv.reader(file)
		header = next(reader)
	return header

def analyze_stream(query : str) :

	print(os.getcwd())
	with open('./prompt/CreatePrompt.txt', 'r', encoding='utf-8') as CreatPrompt, open('./prompt/CreateCode.txt', 'r', encoding='utf-8') as CreatCode:
		creat_prompt = CreatPrompt.read()
		creat_code = CreatCode.read()
	

	print(creat_prompt)
	print(creat_code)
	creat_prompt_prompt = PromptTemplate.from_template(creat_prompt)
	creat_code_promt = PromptTemplate.from_template(creat_code)
	model = ChatGLM()

	prompt_parser = ListParser()
	code_parser = CodeParser()

	chain = creat_prompt_prompt | model | prompt_parser | creat_code_promt | model | code_parser

	Parser.file_path = './admin/csv/' + query['path']

	header = get_csv_header(Parser.file_path)

	query['Document'] = str.join(',', header)

	print(query)
	
	return chain.invoke(query)

def analyze_chat_stream(query : str) :
	print(os.getcwd())
	with open('./prompt/CreateCode.txt', 'r', encoding='utf-8') as CreatCode:
		creat_code = CreatCode.read()
	

	print(creat_code)
	creat_code_promt = PromptTemplate.from_template(creat_code)
	model = ChatGLM()

	code_parser = CodeParser()

	chain = creat_code_promt | model | code_parser

	Parser.file_path = './admin/csv/' + query['path']

	header = get_csv_header(Parser.file_path)

	query['path'] = Parser.file_path
	query['字段'] = str.join(',', header)

	print(query)
	
	return chain.invoke(query)

