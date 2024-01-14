class GlobalVariables:
	def    __init__(self):
		self.variables = {}

	def get(self, key):
		return self.variables.get(key)

	def set(self, key, value):
		self.variables[key] = value


# 创建全局变量管理器对象
global_vars = GlobalVariables()
