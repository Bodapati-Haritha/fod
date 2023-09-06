# Define the dataset with diseases and diagnosed patients
disease_data = {
    'DISEASE_NAME': ['Common Cold', 'Diabetes', 'Bronchitis', 'Influenza', 'Kidney Stones'],
    'DIAGNOSED_PATIENTS': [320, 120, 100, 150, 60]
}

# Create a DataFrame from the dataset
import pandas as pd
df = pd.DataFrame(disease_data)

# Sort the DataFrame by the number of diagnosed patients in descending order
df = df.sort_values(by='DIAGNOSED_PATIENTS', ascending=False)

# Get the most common disease (the first row after sorting)
most_common_disease = df.iloc[0]['DISEASE_NAME']
most_common_patients = df.iloc[0]['DIAGNOSED_PATIENTS']

# Print the frequency distribution
print("Frequency distribution of diseases:")
print(df)

# Print the most common disease
print(f"The most common disease is '{most_common_disease}' with {most_common_patients} diagnosed patients.")
