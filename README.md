# Student Performance Analysis and Prediction Dashboard

<img width="1364" height="1404" alt="image" src="https://github.com/user-attachments/assets/0be912b6-372a-4a8c-97e8-0a766e327d22" />

# 🎓 Student Performance Analysis & Prediction Dashboard

An end-to-end **Data Science project** that analyzes student exam performance and predicts student outcomes using **Python, SQL, Machine Learning, and an interactive dashboard**.

This project demonstrates the complete **data science workflow** including data analysis, database integration, machine learning model training, and deployment through a web dashboard.

---

# 📊 Project Overview

Understanding the factors that influence student performance is important in education analytics.

This project analyzes student exam performance using a dataset from Kaggle and builds a **machine learning model to predict student performance** based on key attributes such as gender, lunch type, and test preparation.

The project also includes an **interactive Streamlit dashboard** where users can input student characteristics and receive real-time predictions.

---

# 🚀 Features

* Data analysis using **Pandas**
* Data stored and accessed using **SQLite database**
* Data visualization using **Matplotlib**
* Machine Learning model built with **Scikit-Learn**
* Interactive dashboard using **Streamlit**
* End-to-end ML workflow implementation

---

# 🧠 Machine Learning Model

**Algorithm Used:** Logistic Regression

The model predicts whether a student will have:

* ✅ **Good Performance**
* ⚠️ **Poor Performance**

### Features Used

* Gender
* Lunch Type
* Test Preparation Course

### Target Variable

Student performance calculated using the **average exam score**.

---

# 📂 Dataset

Dataset used: **Students Performance in Exams**

Source: Kaggle

It contains information about student demographics and exam scores.

Columns include:

* Gender
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Math Score
* Reading Score
* Writing Score

---

# 📈 Data Analysis

Exploratory Data Analysis was performed to identify patterns and insights such as:

* Score distribution across students
* Impact of test preparation on performance
* Gender-based performance comparison

Visualizations were created using **Matplotlib**.

---

# 🌐 Dashboard

An interactive dashboard built with **Streamlit** allows users to:

1. Select student characteristics
2. Submit the information
3. Receive a prediction from the trained ML model

Run the dashboard with:

```
streamlit run dashboard.py
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/Gravilaration/student-performance-ml-dashboard.git
```

Navigate to the project folder:

```
cd student-performance-ml-dashboard
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the dashboard:

```
streamlit run dashboard.py
```

---

# 📁 Project Structure

```
student-performance-ml-dashboard
│
├── data
│   └── StudentsPerformance.csv
│
├── database
│   └── students.db
│
├── models
│   └── student_model.pkl
│
├── analysis.py
├── train_model.py
├── dashboard.py
│
├── requirements.txt
└── README.md
```

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* SQLite
* Streamlit

---

# 🎯 Learning Outcomes

This project demonstrates practical skills in:

* Data Analysis
* Data Visualization
* SQL Database Integration
* Machine Learning Model Training
* Feature Engineering
* Model Deployment using Streamlit

---

# 👨‍💻 Author

**Abhinav Pratap Singh**

Computer Science Student interested in **Data Science, Machine Learning, and AI development**.

---

# ⭐ Future Improvements

Possible enhancements to the project:

* Use more advanced ML models (Random Forest, XGBoost)
* Add more features for prediction
* Improve dashboard UI
* Deploy the dashboard online
