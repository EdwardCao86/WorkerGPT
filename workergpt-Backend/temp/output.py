
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 从csv文件中读取数据
data = pd.read_csv('./admin/csv/german_credit.csv')

# 处理可能的数据缺失问题
data = data.fillna(0)

# 计算相关性矩阵
corr_matrix = data.corr()

# 绘制热力图
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('./temp/correlation_heatmap.png')

