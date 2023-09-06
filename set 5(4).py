import pandas as pd
import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
data = {
    'Product Category': ['Electronics', 'Clothing', 'Electronics', 'Toys', 'Clothing'],
    'Sales Amount': [1000, 500, 800, 300, 600]
}

df = pd.DataFrame(data)

# Group by product category and sum the sales amount
category_sales = df.groupby('Product Category')['Sales Amount'].sum().reset_index()

# Create line plot
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.plot(category_sales['Product Category'], category_sales['Sales Amount'], marker='o', linestyle='-', color='blue')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')
plt.title('Total Sales Amount by Product Category (Line Plot)')
plt.xticks(rotation=45)
plt.grid(True)

# Create scatter plot
plt.subplot(132)
plt.scatter(df['Product Category'], df['Sales Amount'], color='red', marker='o', alpha=0.6)
plt.xlabel('Product Category')
plt.ylabel('Sales Amount')
plt.title('Sales Amount by Product Category (Scatter Plot)')
plt.xticks(rotation=45)
plt.grid(True)

# Create bar plot
plt.subplot(133)
plt.bar(category_sales['Product Category'], category_sales['Sales Amount'], color='green')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')
plt.title('Total Sales Amount by Product Category (Bar Plot)')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Adjust layout for subplots
plt.tight_layout()

# Show all plots
plt.show()
