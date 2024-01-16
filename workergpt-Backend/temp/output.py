import pandas as pd
import matplotlib.pyplot as plt

# 1. Read CSV file
data = pd.read_csv('./admin/csv/german_credit.csv')

# 2. Visualize default field using pie chart or bar chart
default_counts = data['default'].value_counts()
default_counts.plot(kind='bar')
plt.title('Distribution of Default')
plt.xlabel('Default')
plt.ylabel('Count')
plt.savefig('./temp/default.png')
plt.close()

# 3. Visualize account_check_status field using bar chart
account_check_counts = data['account_check_status'].value_counts()
account_check_counts.plot(kind='bar')
plt.title('Distribution of Account Check Status')
plt.xlabel('Status')
plt.ylabel('Count')
plt.savefig('./temp/account_check_status.png')
plt.close()

# 4. Visualize duration_in_month field using histogram
data['duration_in_month'].hist(bins=20)
plt.title('Distribution of Loan Duration')
plt.xlabel('Duration in Months')
plt.ylabel('Count')
plt.savefig('./temp/duration_in_month.png')
plt.close()

# 5. Visualize credit_history field using bar chart
credit_history_counts = data['credit_history'].value_counts()
credit_history_counts.plot(kind='bar')
plt.title('Distribution of Credit History')
plt.xlabel('History')
plt.ylabel('Count')
plt.savefig('./temp/credit_history.png')
plt.close()

# 6. Visualize purpose field using bar chart
purpose_counts = data['purpose'].value_counts()
purpose_counts.plot(kind='bar')
plt.title('Distribution of Purpose')
plt.xlabel('Purpose')
plt.ylabel('Count')
plt.savefig('./temp/purpose.png')
plt.close()

# 7. Visualize credit_amount field using histogram
data['credit_amount'].hist(bins=20)
plt.title('Distribution of Credit Amount')
plt.xlabel('Amount')
plt.ylabel('Count')
plt.savefig('./temp/credit_amount.png')
plt.close()

# 8. Visualize savings field using bar chart
savings_counts = data['savings'].value_counts()
savings_counts.plot(kind='bar')
plt.title('Distribution of Savings')
plt.xlabel('Savings')
plt.ylabel('Count')
plt.savefig('./temp/savings.png')
plt.close()

# 9. Visualize present_emp_since field using bar chart
present_emp_counts = data['present_emp_since'].value_counts()
present_emp_counts.plot(kind='bar')
plt.title('Distribution of Present Employment')
plt.xlabel('Employment Duration')
plt.ylabel('Count')
plt.savefig('./temp/present_emp_since.png')
plt.close()

# 10. Visualize installment_as_income_perc field using histogram
data['installment_as_income_perc'].hist(bins=20)
plt.title('Distribution of Installment as Income Percentage')
plt.xlabel('Percentage')
plt.ylabel('Count')
plt.savefig('./temp/installment_as_income_perc.png')
plt.close()

# 11. Visualize personal_status_sex field using bar chart
personal_status_counts = data['personal_status_sex'].value_counts()
personal_status_counts.plot(kind='bar')
plt.title('Distribution of Personal Status and Sex')
plt.xlabel('Status and Sex')
plt.ylabel('Count')
plt.savefig('./temp/personal_status_sex.png')
plt.close()

# 12. Visualize other_debtors field using bar chart
other_debtors_counts = data['other_debtors'].value_counts()
other_debtors_counts.plot(kind='bar')
plt.title('Distribution of Other Debtors')
plt.xlabel('Debtors')
plt.ylabel('Count')
plt.savefig('./temp/other_debtors.png')
plt.close()

# 13. Visualize present_res_since field using histogram
data['present_res_since'].hist(bins=20)
plt.title('Distribution of Present Residence Since')
plt.xlabel('Residence Since')
plt.ylabel('Count')
plt.savefig('./temp/present_res_since.png')
plt.close()

# 14. Visualize property field using bar chart
property_counts = data['property'].value_counts()
property_counts.plot(kind='bar')
plt.title('Distribution of Property Type')
plt.xlabel('Property Type')
plt.ylabel('Count')
plt.savefig('./temp/property.png')
plt.close()

# 15. Visualize age field using histogram
data['age'].hist(bins=20)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('./temp/age.png')
plt.close()

# 16. Visualize other_installment_plans field using bar chart
other_installment_counts = data['other_installment_plans'].value_counts()
other_installment_counts.plot(kind='bar')
plt.title('Distribution of Other Installment Plans')
plt.xlabel('Installment Plans')
plt.ylabel('Count')
plt.savefig('./temp/other_installment_plans.png')
plt.close()

# 17. Visualize housing field using bar chart
housing_counts = data['housing'].value_counts()
housing_counts.plot(kind='bar')
plt.title('Distribution of Housing')
plt.xlabel('Housing')
plt.ylabel('Count')
plt.savefig('./temp/housing.png')
plt.close()

# 18. Visualize credits_this_bank field using histogram
data['credits_this_bank'].hist(bins=20)
plt.title('Distribution of Credits This Bank')
plt.xlabel('Credits')
plt.ylabel('Count')
plt.savefig('./temp/credits_this_bank.png')
plt.close()

# 19. Visualize job field using bar chart
job_counts = data['job'].value_counts()
job_counts.plot(kind='bar')
plt.title('Distribution of Job')
plt.xlabel('Job')
plt.ylabel('Count')
plt.savefig('./temp/job.png')
plt.close()

# 20. Visualize people_under_maintenance field using histogram
data['people_under_maintenance'].hist(bins=20)
plt.title('Distribution of People Under Maintenance')
plt.xlabel('People')
plt.ylabel('Count')
plt.savefig('./temp/people_under_maintenance.png')
plt.close()

# 21. Visualize telephone field using bar chart
telephone_counts = data['telephone'].value_counts()
telephone_counts.plot(kind='bar')
plt.title('Distribution of Telephone')
plt.xlabel('Telephone')
plt.ylabel('Count')
plt.savefig('./temp/telephone.png')
plt.close()

# 22. Visualize foreign_worker field using bar chart
foreign_worker_counts = data['foreign_worker'].value_counts()
foreign_worker_counts.plot(kind='bar')
plt.title('Distribution of Foreign Worker')
plt.xlabel('Foreign Worker')
plt.ylabel('Count')
plt.savefig('./temp/foreign_worker.png')
plt.close()
