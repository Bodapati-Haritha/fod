import numpy as np
import matplotlib.pyplot as plt

# Create the dataset
data = {
    'Smoking': [20, 15, 5, 25, 30, 10, 18, 22, 8, 12],
    'LungCancer': [5, 4, 1, 6, 8, 2, 3, 7, 1, 2]
}

# Convert the dataset to NumPy arrays
smoking = np.array(data['Smoking'])
lung_cancer = np.array(data['LungCancer'])

# Calculate the correlation coefficient
correlation_coefficient = np.corrcoef(smoking, lung_cancer)[0, 1]

# Create a scatter plot
plt.scatter(smoking, lung_cancer, c='blue', label='Data Points')

# Add labels and title
plt.xlabel('Smoking Habits')
plt.ylabel('Lung Cancer Incidence')
plt.title('Smoking Habits vs. Lung Cancer Incidence')

# Add a trendline (linear regression line)
z = np.polyfit(smoking, lung_cancer, 1)
p = np.poly1d(z)
plt.plot(smoking, p(smoking), "r--", label='Trendline')

# Add legend
plt.legend()

# Display the correlation coefficient
print(f"Correlation Coefficient: {correlation_coefficient:.2f}")

# Show the scatter plot
plt.show()
