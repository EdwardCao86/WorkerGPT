import base64
from flask import Flask, render_template, request ,Response
import os
from flask import jsonify
import json
import time

from .LLM_model.DocumentLoader import DocumentLoader
from .LLM_model.DocumentSpliter import DocumentSpliter
from .LLM_model.Retrieval import VectorDB

from .global_arg.config import config_setting

app = Flask(__name__)
config_setting(app)

from .LLM_model.Chain import text_stream, analyze_stream, analyze_chat_stream
import subprocess
import json
import glob
import os
vectorDB = VectorDB('db/admin')
app.logger.info('VectorDB has been loaded')
documentLoader = DocumentLoader()
app.logger.info('DocumentLoader has been loaded')
documentSpliter = DocumentSpliter()
app.logger.info('DocumentSpliter has been splited')

@app.route('/api/upload', methods=['POST'])
def upload_file():
	if 'file' not in request.files:
		return 'No file uploaded', 400

	file = request.files['file']

	if file.filename == '':
		return 'No selected file', 400

	file_extension = file.filename.split('.')[-1]

	dir_name = 'admin/' + file_extension

	if not os.path.exists(dir_name):
		os.makedirs(dir_name)

	# 保存上传的文件到服务器
	file.save('admin/' + file_extension + '/' + file.filename)
	
	app.logger.info('admin/' + file_extension + '/' + file.filename)
	
	documents = documentSpliter.split_document(documentLoader.load_file('admin', filename=file.filename))
	print(documents)
	res = vectorDB.add(documents)
	app.logger.info(res)
	return 'File uploaded successfully'


@app.route('/api/download', methods=['GET'])
def get_file():
	filename = request.args.get('filename')  # 从查询参数中获取文件名
	if not filename:
		file_json = {'filename': '', 'content': '', 'success': False, 'message': 'No filename provided'}
		return jsonify(file_json), 400

	# 构建完整文件路径
	filepath = os.path.join('admin', filename.split('.')[-1] ,filename)

	app.logger.info(filepath)

	if not os.path.isfile(filepath):
		file_json = {'filename': filename, 'content': '', 'success': False, 'message': 'File not found'}
		return jsonify(file_json), 400

	# 读取文件内容并转换为JSON格式
	with open(filepath, 'r',encoding='utf-8') as file:
		content = file.read()
		file_json = {'filename': filename, 'content': content, 'success': True, 'message': 'File loaded successfully'}

	# 返回JSON格式的文件内容
	return jsonify(file_json)


@app.route('/api/delete', methods=['POST'])
def delete_file():
	file = request.get_json()
	filename = file['filename']
	if not filename:
		file_json = {'filename': '', 'success': False, 'message': 'No filename provided'}
		return jsonify(file_json), 400

	filetype = filename.split('.')[-1]
	filepath = os.path.join('admin', filetype, filename)
	app.logger.info(filepath)
	if not os.path.isfile(filepath):
		file_json = {'filename': filename, 'success': False, 'message': 'File not found'}
		return jsonify(file_json), 400

	os.remove(filepath)
	file_json = {'filename': filename, 'success': True, 'message': 'File deleted successfully'}
	res = vectorDB.delete('admin' , filename)
	app.logger.info(res)
	return jsonify(file_json)

@app.route('/api/chat', methods=['POST'])
def chat():
	data = request.get_json()
	query = data['query']
	topk = 10

	print(os.getcwd())
	
	with open('./prompt/Document.txt', 'r', encoding='utf-8') as document_file, open('./prompt/Query.txt', 'r', encoding='utf-8') as query_file:
		document_template = document_file.read()
		query_template = query_file.read()
	
	def generate_response():
		with app.app_context():
			stream = text_stream(template=document_template + query_template, query={"query": query}, db=vectorDB, topk=topk)
			for events in stream:
				app.logger.info(events)
				yield json.dumps(events).encode()

	return Response(generate_response(), mimetype='application/json')

@app.route('/api/analyze', methods=['POST'])
def analyze():
	clean()
	data = request.get_json()
	path = data['path']
	res = analyze_stream(query={"path": path})
	
	result = []
	for p in res:
		# Execute Python file
		image_files = run_and_get_file_name(p)
		
		for image_path in image_files:
			# Read the image and convert it to base64
			with open(image_path, 'rb') as f:
				image_data = f.read()
				image_base64 = base64.b64encode(image_data).decode('utf-8')
			
			# Create JSON object for each image
			image_json = {
				'path': image_path,
				'image': image_base64
			}
			
			result.append(image_json)
	
	return jsonify(result)

@app.route('/api/analyze_chat', methods=['POST'])
def analyze_chat():
	clean()
	data = request.get_json()
	path = data['path']
	res = analyze_chat_stream(query={"path": path, "提示" : data['query']})
	
	result = []
	for p in res:
		# Execute Python file
		image_files = run_and_get_file_name(p)
		
		# Assuming the generated image has a specific name and location
		
		for image_path in image_files:
			# Read the image and convert it to base64
			with open(image_path, 'rb') as f:
				image_data = f.read()
				image_base64 = base64.b64encode(image_data).decode('utf-8')
			
			# Create JSON object for each image
			image_json = {
				'path': image_path,
				'image': image_base64
			}
			
			result.append(image_json)
	
	return jsonify(result)

def run_and_get_file_name(pyname: str):
	# 图片文件所在的目录
	directory = "./temp/"

	# 在Python文件运行前获取文件列表
	before = set(glob.glob(directory + '*.png'))

	# 运行Python文件
	subprocess.run(["python", pyname])

	# 等待一段时间，确保Python文件已经完成运行
	time.sleep(10)

	# 在Python文件运行后获取文件列表
	after = set(glob.glob(directory + '*.png'))

	# 找出新创建的文件
	new_files = after - before

	return new_files

def clean():
	directory = "./temp/"
	files = os.listdir(directory)
	for file in files:
		if file.endswith(".png"):
			os.remove(os.path.join(directory, file))

if __name__ == '__main__':
	clean()
	app.run()

if __name__ == '__main__':
	app.run()
