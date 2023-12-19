from global_arg.globals import global_vars

import configparser
import os

from LLM_model.DocumentLoader import DocumentLoader
from LLM_model.DocumentSpliter import DocumentSpliter
from LLM_model.Retrieval import VectorDB

vectorDB = VectorDB('db/admin')
documentLoader = DocumentLoader()
documentSpliter = DocumentSpliter()

config = configparser.ConfigParser()
config.read('config.ini')
# print(config.sections())
api_key = config.get("OPEN_AI", "api_key")
global_vars.set("api_key", api_key)
print("USING API KEY: ", api_key)
print(os.environ.get("CUSTOM_ENV_NAME"))

from LLM_model.Chain import text_stream

stream = text_stream(template=
			'''你将依靠下列内容回答问题：
			{document1}
			{document2}
			{document3}
			{document4}
			{document5}
			{document6}
			{document7}
			{document8}
			{document9}
			{document10}
			
			问题是：
			{query}''', query={"query": "你能根据文献讲一个故事吗？"}, db=vectorDB, topk=10)

for i in stream:
	print(i)