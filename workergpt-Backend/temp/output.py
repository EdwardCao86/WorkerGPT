
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('./admin/csv/german_credit.csv')

# 数据预处理
num_vars = ['default', 'duration_in_month', 'credit_amount', 'installment_as_income_perc', 'present_res_since',
            'age', 'credits_this_bank', 'people_under_maintenance']
cat_vars = ['account_check_status', 'credit_history', 'purpose', 'savings', 'present_emp_since',
            'personal_status_sex', 'other_debtors', 'property', 'other_installment_plans', 'housing',
            'job', 'telephone', 'foreign_worker']

# 编码非数值属性
df_encoded = df.copy()
for var in cat_vars:
    df_encoded[var] = df[var].astype('category').cat.codes

# 绘制相关性热力图
corr_matrix = df_encoded.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig('./temp/correlation_heatmap.png')

