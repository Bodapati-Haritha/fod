import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with the provided data
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Patients_Smoke': [130, 150, 160, 180, 200],
    'Patients_LungCancer': [8, 10, 12, 15, 50]
}

df = pd.DataFrame(data)

# Calculate the correlation coefficient
correlation_coefficient = df['Patients_Smoke'].corr(df['Patients_LungCancer'])

# Create a scatter plot
plt.scatter(df['Patients_Smoke'], df['Patients_LungCancer'])
plt.xlabel('Patients Who Smoke')
plt.ylabel('Patients with Lung Cancer')
plt.title(f'Correlation Coefficient: {correlation_coefficient:.2f}')
plt.grid(True)
plt.show()

# Print the correlation coefficient
print(f'Correlation Coefficient: {correlation_coefficient:.2f}')
