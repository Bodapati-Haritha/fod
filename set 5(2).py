import pandas as pd

# Sample data
data = {
    'Student ID': ['Student1', 'Student2', 'Student3'],
    'Math': [85, 90, 75],
    'Science': [92, 88, 95],
    'English': [78, 85, 80]
}

# Create a DataFrame with student IDs as index labels
df = pd.DataFrame(data)
df.set_index('Student ID', inplace=True)

# Display the DataFrame
print(df)
