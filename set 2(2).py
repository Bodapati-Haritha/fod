import numpy as np
import matplotlib.pyplot as plt

# Sample data (replace with your own data)
sales = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]
advertising = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

# Calculate the correlation coefficient between sales and advertising
correlation_coefficient = np.corrcoef(sales, advertising)[0, 1]

# Create a scatter plot
plt.scatter(advertising, sales, color='b', label=f'Correlation = {correlation_coefficient:.2f}')
plt.xlabel('Advertising Spending')
plt.ylabel('Number of Sales')
plt.title('Sales vs. Advertising Spending')
plt.legend(loc='upper left')
plt.grid(True)

# Display the scatter plot
plt.show()
