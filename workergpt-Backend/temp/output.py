
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('./admin/csv/data.csv')

# Encode non-numeric fields as numeric fields
data['education'] = data['education'].astype('category').cat.codes
data['marital-status'] = data['marital-status'].astype('category').cat.codes
data['occupation'] = data['occupation'].astype('category').cat.codes
data['relationship'] = data['relationship'].astype('category').cat.codes
data['race'] = data['race'].astype('category').cat.codes
data['sex'] = data['sex'].astype('category').cat.codes
data['native-country'] = data['native-country'].astype('category').cat.codes
data['income'] = data['income'].astype('category').cat.codes

# Calculate correlation matrix
corr = data.corr()

# Plot the correlation matrix as a heatmap
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")

# Save the plot to a file
plt.savefig('./temp/correlation_heatmap.png')

