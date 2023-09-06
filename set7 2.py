import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame with the provided data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'ProductA': [15000, 18000, 20000, 22000, 24000],
    'ProductB': [8000, 8500, 9000, 9500, 10000],
    'ProductC': [12000, 13000, 14000, 15000, 16000]
}

df = pd.DataFrame(data)

# Line Plot for Monthly Sales of Product A
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['ProductA'], marker='o', linestyle='-', color='blue', label='Product A')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales of Product A')
plt.legend()
plt.grid(True)

# Q-Q Plot for Product B
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title('Q-Q Plot for Product B')
plt.scatter(df['ProductB'], sorted(df['ProductB']), c='red', edgecolors='k')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')

# Bar Plot for Monthly Sales of Product C
plt.subplot(1, 2, 2)
plt.bar(df['Month'], df['ProductC'], color='green', label='Product C')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales of Product C')
plt.legend()

plt.tight_layout()
plt.show()
