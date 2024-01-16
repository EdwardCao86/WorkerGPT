import pandas as pd
import matplotlib.pyplot as plt

# 从CSV文件中读取数据
data = pd.read_csv('./admin/csv/german_credit.csv')

# 可视化提示1：展示不同default类别的频次并保存结果
default_counts = data['default'].value_counts()
plt.bar(default_counts.index, default_counts.values)
plt.xlabel('default')
plt.ylabel('Frequency')
plt.title('Frequency of Different default')
plt.savefig('./admin/visualizations/default.png')
plt.show()

# 可视化提示2：展示不同account_check_status类别的频次并保存结果
account_check_status_counts = data['account_check_status'].value_counts()
plt.bar(account_check_status_counts.index, account_check_status_counts.values)
plt.xlabel('account_check_status')
plt.ylabel('Frequency')
plt.title('Frequency of Different account_check_status')
plt.savefig('./admin/visualizations/account_check_status.png')
plt.show()

# 可视化提示3：展示不同duration_in_month的分布并保存结果
plt.hist(data['duration_in_month'], bins=10)
plt.xlabel('duration_in_month')
plt.ylabel('Frequency')
plt.title('Distribution of duration_in_month')
plt.savefig('./admin/visualizations/duration_in_month.png')
plt.show()

# 可视化提示4：展示不同credit_history类别的频次并保存结果
credit_history_counts = data['credit_history'].value_counts()
plt.bar(credit_history_counts.index, credit_history_counts.values)
plt.xlabel('credit_history')
plt.ylabel('Frequency')
plt.title('Frequency of Different credit_history')
plt.savefig('./admin/visualizations/credit_history.png')
plt.show()

# 可视化提示5：展示不同purpose类别的频次并保存结果
purpose_counts = data['purpose'].value_counts()
plt.bar(purpose_counts.index, purpose_counts.values)
plt.xlabel('purpose')
plt.ylabel('Frequency')
plt.title('Frequency of Different purpose')
plt.savefig('./admin/visualizations/purpose.png')
plt.show()

# 可视化提示6：展示credit_amount的分布情况并保存结果
plt.hist(data['credit_amount'], bins=10)
plt.xlabel('credit_amount')
plt.ylabel('Frequency')
plt.title('Distribution of credit_amount')
plt.savefig('./admin/visualizations/credit_amount.png')
plt.show()

# 可视化提示7：展示不同savings类别的频次并保存结果
savings_counts = data['savings'].value_counts()
plt.bar(savings_counts.index, savings_counts.values)
plt.xlabel('savings')
plt.ylabel('Frequency')
plt.title('Frequency of Different savings')
plt.savefig('./admin/visualizations/savings.png')
plt.show()

# 可视化提示8：展示不同present_emp_since类别的频次并保存结果
present_emp_since_counts = data['present_emp_since'].value_counts()
plt.bar(present_emp_since_counts.index, present_emp_since_counts.values)
plt.xlabel('present_emp_since')
plt.ylabel('Frequency')
plt.title('Frequency of Different present_emp_since')
plt.savefig('./admin/visualizations/present_emp_since.png')
plt.show()

# 可视化提示9：展示installment_as_income_perc的分布情况并保存结果
plt.hist(data['installment_as_income_perc'], bins=10)
plt.xlabel('installment_as_income_perc')
plt.ylabel('Frequency')
plt.title('Distribution of installment_as_income_perc')
plt.savefig('./admin/visualizations/installment_as_income_perc.png')
plt.show()

# 可视化提示10：展示不同personal_status_sex类别的频次并保存结果
personal_status_sex_counts = data['personal_status_sex'].value_counts()
plt.bar(personal_status_sex_counts.index, personal_status_sex_counts.values)
plt.xlabel('personal_status_sex')
plt.ylabel('Frequency')
plt.title('Frequency of Different personal_status_sex')
plt.savefig('./admin/visualizations/personal_status_sex.png')
plt.show()

# 可视化提示11：展示不同other_debtors类别的频次并保存结果
other_debtors_counts = data['other_debtors'].value_counts()
plt.bar(other_debtors_counts.index, other_debtors_counts.values)
plt.xlabel('other_debtors')
plt.ylabel('Frequency')
plt.title('Frequency of Different other_debtors')
plt.savefig('./admin/visualizations/other_debtors.png')
plt.show()

# 可视化提示12：展示不同present_res_since类别的频次并保存结果
present_res_since_counts = data['present_res_since'].value_counts()
plt.bar(present_res_since_counts.index, present_res_since_counts.values)
plt.xlabel('present_res_since')
plt.ylabel('Frequency')
plt.title('Frequency of Different present_res_since')
plt.savefig('./admin/visualizations/present_res_since.png')
plt.show()

# 可视化提示13：展示不同property类别的频次并保存结果
property_counts = data['property'].value_counts()
plt.bar(property_counts.index, property_counts.values)
plt.xlabel('property')
plt.ylabel('Frequency')
plt.title('Frequency of Different property')
plt.savefig('./admin/visualizations/property.png')
plt.show()

# 可视化提示14：展示age的分布情况并保存结果
plt.hist(data['age'], bins=10)
plt.xlabel('age')
plt.ylabel('Frequency')
plt.title('Distribution of age')
plt.savefig('./admin/visualizations/age.png')
plt.show()

# 可视化提示15：展示不同other_installment_plans类别的频次并保存结果
other_installment_plans_counts = data['other_installment_plans'].value_counts()
plt.bar(other_installment_plans_counts.index, other_installment_plans_counts.values)
plt.xlabel('other_installment_plans')
plt.ylabel('Frequency')
plt.title('Frequency of Different other_installment_plans')
plt.savefig('./admin/visualizations/other_installment_plans.png')
plt.show()

# 可视化提示16：展示不同housing类别的频次并保存结果
housing_counts = data['housing'].value_counts()
plt.bar(housing_counts.index, housing_counts.values)
plt.xlabel('housing')
plt.ylabel('Frequency')
plt.title('Frequency of Different housing')
plt.savefig('./admin/visualizations/housing.png')
plt.show()

# 可视化提示17：展示不同credits_this_bank类别的频次并保存结果
credits_this_bank_counts = data['credits_this_bank'].value_counts()
plt.bar(credits_this_bank_counts.index, credits_this_bank_counts.values)
plt.xlabel('credits_this_bank')
plt.ylabel('Frequency')
plt.title('Frequency of Different credits_this_bank')
plt.savefig('./admin/visualizations/credits_this_bank.png')
plt.show()

# 可视化提示18：展示不同job类别的频次并保存结果
job_counts = data['job'].value_counts()
plt.bar(job_counts.index, job_counts.values)
plt.xlabel('job')
plt.ylabel('Frequency')
plt.title('Frequency of Different job')
plt.savefig('./admin/visualizations/job.png')
plt.show()

# 可视化提示19：展示不同people_under_maintenance类别的频次并保存结果
people_under_maintenance_counts = data['people_under_maintenance'].value_counts()
plt.bar(people_under_maintenance_counts.index, people_under_maintenance_counts.values)
plt.xlabel('people_under_maintenance')
plt.ylabel('Frequency')
plt.title('Frequency of Different people_under_maintenance')
plt.savefig('./admin/visualizations/people_under_maintenance.png')
plt.show()

# 可视化提示20：展示不同telephone类别的频次并保存结果
telephone_counts = data['telephone'].value_counts()
plt.bar(telephone_counts.index, telephone_counts.values)
plt.xlabel('telephone')
plt.ylabel('Frequency')
plt.title('Frequency of Different telephone')
plt.savefig('./admin/visualizations/telephone.png')
plt.show()

# 可视化提示21：展示不同foreign_worker类别的频次并保存结果
foreign_worker_counts = data['foreign_worker'].value_counts()
plt.bar(foreign_worker_counts.index, foreign_worker_counts.values)
plt.xlabel('foreign_worker')
plt.ylabel('Frequency')
plt.title('Frequency of Different foreign_worker')
plt.savefig('./admin/visualizations/foreign_worker.png')
plt.show()