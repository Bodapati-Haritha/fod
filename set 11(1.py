import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("customer_data.csv")

# Encode categorical variables like 'Contract' and 'PaymentMethod'
label_encoder = LabelEncoder()
data['Contract'] = label_encoder.fit_transform(data['Contract'])
data['PaymentMethod'] = label_encoder.fit_transform(data['PaymentMethod'])

# Convert TotalCharges to numeric (if it's not already)
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')

# Handle missing values if any
data.dropna(inplace=True)

# Define the features (X) and target variable (y)
X = data.drop(['CustomerID', 'Churn'], axis=1)
y = data['Churn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)

# Train the model on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print the evaluation results
print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(confusion)
print("Classification Report:")
print(report)

# Plot the decision tree
plt.figure(figsize=(12, 6))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=["No Churn", "Churn"])
plt.show()
