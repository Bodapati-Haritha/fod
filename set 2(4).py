import numpy as np
import matplotlib.pyplot as plt

# Sample data (replace with your actual dataset)
smoking_patients = [200, 220, 240, 260, 340]
lung_cancer_patients = [25, 30, 35, 40, 60]
years = [2015, 2016, 2017, 2018, 2022]

# Calculate the correlation coefficient between smoking patients and lung cancer patients
correlation_coefficient = np.corrcoef(smoking_patients, lung_cancer_patients)[0, 1]

# Create a scatter plot
plt.scatter(smoking_patients, lung_cancer_patients, c=years, cmap='viridis', label=f'Correlation = {correlation_coefficient:.2f}')
plt.xlabel('Number of Smoking Patients')
plt.ylabel('Number of Lung Cancer Patients')
plt.title('Smoking Patients vs. Lung Cancer Patients')
plt.legend(loc='upper left')
plt.grid(True)

