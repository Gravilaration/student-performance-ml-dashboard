import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

#Loading Dataset
df=pd.read_csv("data/StudentsPerformance.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistics:")
print(df.describe())

#Connect To SQL Database
conn=sqlite3.connect("database/students.db")#Creates a Database by itself

# Storing dataset in SQL
#df.to_sql("students", conn, if_exists="replace", index=False)

#print("\nDataset successfully stored in SQL database!")

# Load data from SQL
df = pd.read_sql("SELECT * FROM students", conn)

print("First 5 rows:")
print(df.head())

# -------- Average Scores --------
print("\nAverage Scores:")
print(df[['math score', 'reading score', 'writing score']].mean())

# -------- Visualization 1: Score Distribution --------
plt.hist(df['math score'], bins=20)
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.show()

# -------- Visualization 2: Gender vs Math Score --------
df.groupby("gender")["math score"].mean().plot(kind="bar")
plt.title("Average Math Score by Gender")
plt.ylabel("Score")
plt.show()

# -------- Visualization 3: Test Preparation Impact --------
df.groupby("test preparation course")["math score"].mean().plot(kind="bar")
plt.title("Impact of Test Preparation on Math Score")
plt.ylabel("Score")
plt.show()

conn.close()