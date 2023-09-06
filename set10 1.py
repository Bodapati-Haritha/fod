import pandas as pd

# Sample data in dictionary format
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Math': [85, 70, 92, 65, 78],
    'Science': [90, 88, 95, 78, 85],
    'History': [75, 82, 88, 68, 72]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Iterate over rows in the DataFrame
for index, row in df.iterrows():
    student_name = row['Student']
    math_score = row['Math']
    science_score = row['Science']
    history_score = row['History']
    
    print(f"Student: {student_name}")
    print(f"Math Score: {math_score}")
    print(f"Science Score: {science_score}")
    print(f"History Score: {history_score}")
    print("\n")
