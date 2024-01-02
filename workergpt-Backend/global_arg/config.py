# 读取congif文件 设置全局变量
from . import globals as globals
from .globals import global_vars
import configparser
import logging
import zhipuai
import openai
from flask import Flask

from logging.handlers import RotatingFileHandler  


def config_setting(app : Flask):
	config = configparser.ConfigParser()
	config.read('./config.ini')
	# print(config.sections())
	api_key = config.get("OPEN_AI", "api_key")
	global_vars.set("api_key", api_key)
	app.logger.info("USING API KEY: " + api_key)
	
	openai.api_key = api_key

	logging_level = logging.getLevelNamesMapping()[config.get("LOGGING", "level")]
	global_vars.set("logging_level", logging_level)
	app.logger.info("USING LOGGING LEVEL: " + logging.getLevelName(logging_level))

	logging_file = config.get("LOGGING", "file")
	global_vars.set("logging_file", logging_file)
	app.logger.info("USING LOGGING FILE: " + logging_file)

'''
	# 创建一个日志格式器
	formatter = '%(asctime)s - %(levelname)s - %(message)s'


	# 配置日志记录器  
	logger = logging.getLogger()  
	logger.setLevel(logging_level)  # 设置日志级别  
  
	# 创建日志文件处理器，将日志写入文件  
	file_handler = RotatingFileHandler(logging_file, maxBytes=1024*1024, backupCount=5)  
	file_handler.setLevel(logging_level)  
	
  
	# 创建并设置日志格式  
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
	file_handler.setFormatter(formatter)  
  
	# 将文件处理器添加到日志记录器  
	logger.addHandler(file_handler)

	#测试logger
	app.logger.info("TESTING LOGGER")
'''



