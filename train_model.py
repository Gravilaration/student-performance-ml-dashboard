import pandas as pd
import sqlite3
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle
import matplotlib.pyplot as plt

# Connect to SQL database
conn = sqlite3.connect("database/students.db")

# Load data
df = pd.read_sql("SELECT * FROM students", conn)
conn.close()

# Create average score
df["average_score"] = (df["math score"] + df["reading score"] + df["writing score"]) / 3

# Create target variable
df["performance"] = df["average_score"].apply(lambda x: 1 if x >= 60 else 0)

# Encode categorical variables
le = LabelEncoder()

df["gender"] = le.fit_transform(df["gender"])
df["lunch"] = le.fit_transform(df["lunch"])
df["test preparation course"] = le.fit_transform(df["test preparation course"])

# Features
X = df[["math score", "reading score", "writing score"]]

# Target
y = df["performance"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy*100:.2f}%")

# Save model
with open("models/student_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")

importance = model.coef_[0]
features = X.columns

plt.bar(features, importance)
plt.title("Feature Importance for Student Performance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.show()
