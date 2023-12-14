from flask import Flask, render_template, request
import os
from flask import jsonify
from LLM_model.Chain import text_stream

from config import config_setting

app = Flask(__name__)


@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    file_extension = file.filename.split('.')[-1]
    # 保存上传的文件到服务器
    file.save('admin/' + file_extension + '/' + file.filename)

    return 'File uploaded successfully'


@app.route('/api/download', methods=['GET'])
def get_file():
    filename = request.args.get('filename')  # 从查询参数中获取文件名
    if not filename:
        file_json = {'filename': '', 'content': '', 'success': False, 'message': 'No filename provided'}
        return jsonify(file_json)

    # 构建完整文件路径
    filepath = os.path.join('/admin', filename)

    if not os.path.isfile(filepath):
        file_json = {'filename': filename, 'content': '', 'success': False, 'message': 'File not found'}
        return jsonify(file_json)

    # 读取文件内容并转换为JSON格式
    with open(filepath, 'r') as file:
        content = file.read()
        file_json = {'filename': filename, 'content': content, 'success': True, 'message': 'File loaded successfully'}

    # 返回JSON格式的文件内容
    return jsonify(file_json)


@app.route('/api/delete', methods=['GET'])
def delete_file():
    filename = request.args.get('filename')
    if not filename:
        file_json = {'filename': '', 'success': False, 'message': 'No filename provided'}
        return jsonify(file_json)

    filetype = filename.split('.')[-1]
    filepath = os.path.join('admin', filetype, filename)
    if not os.path.isfile(filepath):
        file_json = {'filename': filename, 'success': False, 'message': 'File not found'}
        return jsonify(file_json)

	
    os.remove(filepath)
    file_json = {'filename': filename, 'success': True, 'message': 'File deleted successfully'}
    return jsonify(file_json)


if __name__ == '__main__':
    config_setting(app)
    
    text_stream("请讲一个{topic}的故事。", {"topic": "冰淇淋"})
    app.run()
