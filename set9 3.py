import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
    'Temperature': [20, 22, 18, 23],
    'Rainfall': [0.2, 0.5, 0.1, 0.3]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Calculate the correlation coefficient
correlation_coefficient = df['Temperature'].corr(df['Rainfall'])

# Create a scatter plot
plt.scatter(df['Temperature'], df['Rainfall'])
plt.xlabel('Temperature')
plt.ylabel('Rainfall')
plt.title(f'Correlation Coefficient: {correlation_coefficient:.2f}')
plt.show()

# Print the correlation coefficient
print(f'Correlation Coefficient: {correlation_coefficient:.2f}')
