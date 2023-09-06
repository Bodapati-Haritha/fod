import pandas as pd

# Sample data in dictionary format
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 32, 28, 22, 30],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Iterate over rows in the DataFrame
for index, row in df.iterrows():
    name = row['Name']
    age = row['Age']
    gender = row['Gender']
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print("\n")
