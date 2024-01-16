import pandas as pd
import matplotlib.pyplot as plt

# 1. default
df = pd.read_csv("./admin/csv/german_credit.csv")
default_counts = df["default"].value_counts()
default_counts.plot(kind="bar")
plt.savefig("./temp/default_distribution.png")
plt.close()

# 2. account_check_status
account_check_counts = df["account_check_status"].value_counts()
account_check_counts.plot(kind="pie")
plt.savefig("./temp/account_check_status_distribution.png")
plt.close()

# 3. duration_in_month
df["duration_in_month"].plot(kind="hist")
plt.savefig("./temp/duration_in_month_distribution.png")
plt.close()

# 4. credit_history
credit_history_counts = df["credit_history"].value_counts()
credit_history_counts.plot(kind="bar")
plt.savefig("./temp/credit_history_distribution.png")
plt.close()

# 5. purpose
purpose_counts = df["purpose"].value_counts()
purpose_counts.plot(kind="bar")
plt.savefig("./temp/purpose_distribution.png")
plt.close()

# 6. credit_amount
df["credit_amount"].plot(kind="hist")
plt.savefig("./temp/credit_amount_distribution.png")
plt.close()

# 7. savings
savings_counts = df["savings"].value_counts()
savings_counts.plot(kind="bar")
plt.savefig("./temp/savings_distribution.png")
plt.close()

# 8. present_emp_since
present_emp_counts = df["present_emp_since"].value_counts()
present_emp_counts.plot(kind="bar")
plt.savefig("./temp/present_emp_since_distribution.png")
plt.close()

# 9. installment_as_income_perc
df["installment_as_income_perc"].plot(kind="hist")
plt.savefig("./temp/installment_as_income_perc_distribution.png")
plt.close()

# 10. personal_status_sex
personal_status_counts = df["personal_status_sex"].value_counts()
personal_status_counts.plot(kind="bar")
plt.savefig("./temp/personal_status_sex_distribution.png")
plt.close()

# 11. other_debtors
other_debtors_counts = df["other_debtors"].value_counts()
other_debtors_counts.plot(kind="bar")
plt.savefig("./temp/other_debtors_distribution.png")
plt.close()

# 12. present_res_since
df["present_res_since"].plot(kind="hist")
plt.savefig("./temp/present_res_since_distribution.png")
plt.close()

# 13. property
property_counts = df["property"].value_counts()
property_counts.plot(kind="bar")
plt.savefig("./temp/property_distribution.png")
plt.close()

# 14. age
df["age"].plot(kind="hist")
plt.savefig("./temp/age_distribution.png")
plt.close()

# 15. other_installment_plans
other_installment_counts = df["other_installment_plans"].value_counts()
other_installment_counts.plot(kind="bar")
plt.savefig("./temp/other_installment_plans_distribution.png")
plt.close()

# 16. housing
housing_counts = df["housing"].value_counts()
housing_counts.plot(kind="bar")
plt.savefig("./temp/housing_distribution.png")
plt.close()

# 17. credits_this_bank
credits_this_bank_counts = df["credits_this_bank"].value_counts()
credits_this_bank_counts.plot(kind="bar")
plt.savefig("./temp/credits_this_bank_distribution.png")
plt.close()

# 18. job
job_counts = df["job"].value_counts()
job_counts.plot(kind="bar")
plt.savefig("./temp/job_distribution.png")
plt.close()

# 19. people_under_maintenance
df["people_under_maintenance"].plot(kind="hist")
plt.savefig("./temp/people_under_maintenance_distribution.png")
plt.close()

# 20. telephone
telephone_counts = df["telephone"].value_counts()
telephone_counts.plot(kind="bar")
plt.savefig("./temp/telephone_distribution.png")
plt.close()

# 21. foreign_worker
foreign_worker_counts = df["foreign_worker"].value_counts()
foreign_worker_counts.plot(kind="bar")
plt.savefig("./temp/foreign_worker_distribution.png")
plt.close()
