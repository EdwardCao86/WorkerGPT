
import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
data = pd.read_csv('./admin/csv/学生成绩.csv', encoding='utf-8', na_values='NaN')

# 绘制年龄分布图
plt.hist(data['年龄'].dropna(), bins=10, edgecolor='k')
plt.xlabel('年龄')
plt.ylabel('人数')
plt.title('年龄分布图')

# 保存图片
plt.savefig('./temp/年龄分布图.png')

