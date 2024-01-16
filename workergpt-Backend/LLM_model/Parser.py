from langchain.schema.output_parser import BaseOutputParser
import ast
import csv
from ..app import app

file_path = ''

def get_csv_header(path: str):
	with open(path, 'r') as file:
		reader = csv.reader(file)
		header = next(reader)
	return header

class ListParser(BaseOutputParser[dict]):
	def parse(self, text) -> dict:
		print(text)
		return {'path' : file_path , '提示' : text, '字段': str.join(',', get_csv_header(file_path))}

class CodeParser(BaseOutputParser[list]):
	def parse(self, text: str) -> list:
		print(text)
		filenames = []
		filename = './temp/output.py'
		
		with open(filename, 'w', encoding='utf-8') as file:
			file.write(text + '\n')
		
		# Add the filename to the list
		filenames.append(filename)	
		
		# Return the list of filenames
		return filenames
        
		