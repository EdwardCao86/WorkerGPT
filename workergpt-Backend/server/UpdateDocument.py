from flask import Flask, request


@app.route('/upload', methods=['POST'])
def upload_file():
	if 'file' not in request.files:
		return 'No file uploaded'

	file = request.files['file']
	if file.filename == '':
		return 'No selected file'

	# 保存上传的文件到服务器
	file.save('path/to/save/file.txt')

	return 'File uploaded successfully'


if __name__ == '__main__':
	app.run()
