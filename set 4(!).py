import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataset (replace with your own data)
data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 75000, 80000, 90000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Calculate the covariance matrix
covariance_matrix = df.cov()

# Create a correlation plot (heatmap)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Plot")
plt.show()

# Print the correlation matrix and covariance matrix
print("Correlation Matrix:")
print(correlation_matrix)

print("\nCovariance Matrix:")
print(covariance_matrix)
