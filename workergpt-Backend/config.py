# 读取congif文件 设置全局变量
from globals import global_vars
import os
import configparser
import logging
import zhipuai


def config_setting(app):
	config = configparser.ConfigParser()
	config.read('./workergpt-Backend/config.ini')
	# print(config.sections())
	api_key = config.get("ZHI_PU_API", "api_key")
	global_vars.set("api_key", api_key)
	print("USING API KEY: ", api_key)
	zhipuai.api_key = api_key

	logging_level = config.get("LOGGING", "level")
	global_vars.set("logging_level", logging_level)
	print("USING LOGGING LEVEL: ", logging_level)

	logging_file = config.get("LOGGING", "file")
	global_vars.set("logging_file", logging_file)
	print("USING LOGGING FILE: ", logging_file)

	# 创建一个日志格式器
	formatter = '%(asctime)s - %(levelname)s - %(message)s'

	logging.basicConfig(format=formatter, level=logging_level, filename=logging_file)


