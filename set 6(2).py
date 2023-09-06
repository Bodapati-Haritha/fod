import pandas as pd
import numpy as np

# Sample data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# Create a DataFrame
df = pd.DataFrame(exam_data)

# Select rows where the score is between 15 and 20 (inclusive)
selected_rows = df[(df['score'] >= 15) & (df['score'] <= 20)]

# Display the selected rows
print(selected_rows)
