import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Load the loan data from a CSV file (replace 'loan_data.csv' with your data file)
data = pd.read_csv('loan_data.csv')

# Define the features (X) and target variable (y)
X = data[['Income', 'CreditScore']]
y = data['Approved']

# Split the data into training and testing sets (e.g., 80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a kNN classifier (you can choose the number of neighbors, e.g., k=5)
k = 5
knn_classifier = KNeighborsClassifier(n_neighbors=k)

# Train the classifier on the training data
knn_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = knn_classifier.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)

# Create a scatter plot to visualize the decision boundary of the classifier
plt.figure(figsize=(8, 6))

# Scatter plot for class 0 (Not Approved)
plt.scatter(X_test[y_test == 0]['Income'], X_test[y_test == 0]['CreditScore'], label='Not Approved', c='red', marker='x')

# Scatter plot for class 1 (Approved)
plt.scatter(X_test[y_test == 1]['Income'], X_test[y_test == 1]['CreditScore'], label='Approved', c='blue', marker='o')

# Adding labels and legend
plt.xlabel('Income')
plt.ylabel('Credit Score')
plt.title('Loan Approval Classifier')
plt.legend()
plt.grid(True)
plt.show()
