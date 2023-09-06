import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the dataset
df = pd.read_csv('customer_data.csv')

# Step 2: Encode categorical features
label_encoder = LabelEncoder()
df['Contract'] = label_encoder.fit_transform(df['Contract'])
df['PaymentMethod'] = label_encoder.fit_transform(df['PaymentMethod'])

# Step 3: Split the dataset into features (X) and the target variable (y)
X = df.drop(['CustomerID', 'Churn'], axis=1)  # Features
y = df['Churn']  # Target variable

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Create and train the Decision Tree Classifier model
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Step 6: Make predictions and evaluate the model
y_pred = clf.predict(X_test)

# Step 7: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{confusion}")
print(f"Classification Report:\n{classification_rep}")
