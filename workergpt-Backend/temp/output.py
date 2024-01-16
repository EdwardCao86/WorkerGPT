
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('./admin/csv/german_credit.csv')

# Encode non-numeric attributes
data['account_check_status'] = pd.factorize(data['account_check_status'])[0]
data['credit_history'] = pd.factorize(data['credit_history'])[0]
data['purpose'] = pd.factorize(data['purpose'])[0]
data['savings'] = pd.factorize(data['savings'])[0]
data['present_emp_since'] = pd.factorize(data['present_emp_since'])[0]
data['personal_status_sex'] = pd.factorize(data['personal_status_sex'])[0]
data['other_debtors'] = pd.factorize(data['other_debtors'])[0]
data['property'] = pd.factorize(data['property'])[0]
data['other_installment_plans'] = pd.factorize(data['other_installment_plans'])[0]
data['housing'] = pd.factorize(data['housing'])[0]
data['job'] = pd.factorize(data['job'])[0]
data['telephone'] = pd.factorize(data['telephone'])[0]
data['foreign_worker'] = pd.factorize(data['foreign_worker'])[0]

# Calculate correlation matrix
corr_matrix = data.corr().round(2)

# Plot heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')

# Save the plot
plt.savefig('./temp/correlation_heatmap.png')

