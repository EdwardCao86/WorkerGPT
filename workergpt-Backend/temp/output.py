
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 从./admin/csv/german_credit.csv读取CSV文件
data = pd.read_csv("./admin/csv/german_credit.csv")

# 编码非数值属性字段为数值属性
data["default"] = data["default"].map({"Yes": 1, "No": 0})
data["account_check_status"] = data["account_check_status"].map({"< 0 DM": 0, "0 <= ... < 200 DM": 1, ">= 200 DM / salary assignments for at least 1 year": 2, "no checking account": 3})
data["credit_history"] = data["credit_history"].map({"existing credits paid back duly till now": 0, "critical account/ other credits existing (not at this bank)": 1, "delay in paying off in the past": 2, "all credits at this bank paid back duly": 3, "no credits taken/ all credits paid back duly": 4})
data["purpose"] = data["purpose"].map({"radio/television": 0, "education": 1, "furniture/equipment": 2, "car (new)": 3, "car (used)": 4, "business": 5, "domestic appliances": 6, "repairs": 7, "others": 8, "retraining": 9})
data["savings"] = data["savings"].map({"< 100 DM": 0, "100 <= ... < 500 DM": 1, "500 <= ... < 1000 DM": 2, ">= 1000 DM": 3, "unknown/ no savings account": 4})
data["present_emp_since"] = data["present_emp_since"].map({"unemployed": 0, "< 1 year": 1, "1 <= ... < 4 years": 2, "4 <= ... < 7 years": 3, ">= 7 years": 4})
data["personal_status_sex"] = data["personal_status_sex"].map({"male : divorced/separated": 0, "female : non-single or male : single": 1, "male : married/widowed": 2, "female : single": 3})
data["other_debtors"] = data["other_debtors"].map({"none": 0, "co-applicant": 1, "guarantor": 2})
data["property"] = data["property"].map({"real estate": 0, "savings agreement/life insurance": 1, "car or other": 2, "unknown / no property": 3})
data["other_installment_plans"] = data["other_installment_plans"].map({"bank": 0, "stores": 1, "none": 2})
data["housing"] = data["housing"].map({"rent": 0, "own": 1, "for free": 2})
data["job"] = data["job"].map({"unemployed/ unskilled - non-resident": 0, "unskilled - resident": 1, "skilled employee / official": 2, "management/ self-employed/ highly qualified employee/ officer": 3})
data["telephone"] = data["telephone"].map({"Yes": 1, "No": 0})
data["foreign_worker"] = data["foreign_worker"].map({"Yes": 1, "No": 0})

# 绘制相关性热力图
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr().round(2), annot=True, cmap="coolwarm")
plt.savefig("./temp/correlation_heatmap.png")

