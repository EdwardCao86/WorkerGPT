import logging
import os

from langchain.document_loaders import TextLoader, CSVLoader, PyPDFLoader, \
	DirectoryLoader, JSONLoader, BSHTMLLoader, UnstructuredMarkdownLoader


def get_fileloader(filetype: str, file_name: str = ''):
	if file_name == '':
		if filetype == 'txt':
			return TextLoader
		elif filetype == 'csv':
			return CSVLoader
		# json格式使用jq依赖，无法在win上正常运作，先不做支持。
		# elif filetype == 'json':
		# 	return JSONLoader(file_path=file_name, jq_schema='.messages[].content')
		elif filetype == 'html':
			return BSHTMLLoader
		elif filetype == 'md':
			return UnstructuredMarkdownLoader
		elif filetype == 'pdf':
			return PyPDFLoader

	if filetype == 'txt':
		return TextLoader(file_name, encoding='utf-8').load()
	elif filetype == 'csv':
		return CSVLoader(file_path=file_name, encoding='utf-8').load()
	# json格式使用jq依赖，无法在win上正常运作，先不做支持。
	# elif filetype == 'json':
	# 	return JSONLoader(file_path=file_name, jq_schema='.messages[].content')
	elif filetype == 'html':
		return BSHTMLLoader(file_path=file_name, open_encoding='utf-8').load()
	elif filetype == 'md':
		return UnstructuredMarkdownLoader(file_path=file_name).load()
	elif filetype == 'pdf':
		res = PyPDFLoader(file_path=file_name).load()
		for item in res:
			item.page_content = item.page_content.replace(' ', '')
		return res
	else:
		return None


class DocumentLoader:
	username = None

	def __init__(self):
		pass

	def load_directory(self, username: str):
		self.username = username
		documents = list()
		for item in os.listdir(username):
			item_path = os.path.join(username, item)
			if os.path.isdir(item_path):
				documents.extend(self._load_directory(item))
		return documents
	
	def load_file(self, username: str, filename: str):
		self.username = username
		filetype = filename.split('.')[-1]
		loader_cls = get_fileloader(filetype, './' + username + '/' + filetype + '/' + filename)
		text_loader = loader_cls
		return text_loader

	def _load_directory(self, filetype: str):
		glob_path = self.username + '/' + filetype + '/'
		text_loader_kwargs = {'autodetect_encoding': True}
		directory_loader = DirectoryLoader(glob_path, use_multithreading=True, loader_cls=get_fileloader(filetype),
										   silent_errors=True, loader_kwargs=text_loader_kwargs)
		return directory_loader
