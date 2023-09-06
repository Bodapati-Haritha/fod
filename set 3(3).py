import pandas as pd
import matplotlib.pyplot as plt

# Load the shoe sales data from the CSV file (replace 'shoe_sales.csv' with your file path)
data = pd.read_csv('shoe_sales.csv')

# Calculate the frequency distribution of shoe sizes
size_counts = data['Shoe_Size'].value_counts().reset_index()
size_counts.columns = ['Shoe_Size', 'Quantity']

# Sort the data by shoe size
size_counts = size_counts.sort_values(by='Shoe_Size')

# Print the frequency distribution table
print("Frequency Distribution of Shoe Sizes Sold:")
print(size_counts)

# Create a bar chart to visualize the distribution
plt.bar(size_counts['Shoe_Size'], size_counts['Quantity'])
plt.xlabel('Shoe Size')
plt.ylabel('Quantity Sold')
plt.title('Shoe Size Frequency Distribution')
plt.xticks(size_counts['Shoe_Size'])
plt.grid(axis='y')

# Show the bar chart
plt.show()
