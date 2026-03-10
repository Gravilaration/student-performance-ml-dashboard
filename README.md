#**🎓 Student Performance ML Dashboard**

## Dashboard Preview

<img width="1298" height="1249" alt="image" src="https://github.com/user-attachments/assets/567676a0-4529-49bb-b0c9-194c5906b413" />

<img width="1173" height="1373" alt="image" src="https://github.com/user-attachments/assets/02306b85-1831-4d70-a907-d2ce3882bcd9" />



# 🎓 Student Performance ML Dashboard

An end-to-end **Data Science and Machine Learning project** that analyzes student exam data and predicts student performance using **Python, SQL, and Machine Learning**, with an **interactive Streamlit dashboard**.

---

# 📊 Project Overview

This project explores a dataset of student exam results and builds a **machine learning model** to predict whether a student will perform well based on their scores.

The project demonstrates a full **data science pipeline**:

Dataset → Data Analysis → SQL Database → Machine Learning Model → Interactive Dashboard

---

# 🚀 Key Features

* Data analysis using **Pandas**
* Data stored and accessed using **SQLite**
* Data visualization using **Matplotlib**
* Machine Learning model using **Logistic Regression**
* Interactive dashboard built with **Streamlit**
* Real dataset from **Kaggle**

---

# 🧠 Machine Learning Model

**Algorithm:** Logistic Regression

The model predicts whether a student's performance is:

* ✅ Good Performance
* ⚠️ Poor Performance

### Features Used

* Math Score
* Reading Score
* Writing Score

### Target Variable

Student performance calculated from the **average score** of the three exams.

---

# 📂 Dataset

Dataset: **Students Performance in Exams**

Source: Kaggle

The dataset includes:

* Gender
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Math Score
* Reading Score
* Writing Score

---

# 📈 Data Analysis

Exploratory Data Analysis (EDA) was performed to understand patterns in student performance.

Examples of insights explored:

* Distribution of exam scores
* Average performance across subjects
* Relationship between different exam scores

Visualizations were created using **Matplotlib**.

---

# 🌐 Interactive Dashboard

The project includes a **Streamlit dashboard** where users can input exam scores and receive a prediction from the trained ML model.

### Dashboard Capabilities

* View dataset summary
* Explore score distributions
* Enter student scores
* Get real-time ML predictions

Run the dashboard with:

streamlit run dashboard.py

---

# ⚙️ Installation

Clone the repository:

git clone https://github.com/Gravilaration/student-performance-ml-dashboard.git

Navigate to the project folder:

cd student-performance-ml-dashboard

Install dependencies:

pip install -r requirements.txt

Run the dashboard:

streamlit run dashboard.py

---

# 📁 Project Structure

student-performance-ml-dashboard

data/
StudentsPerformance.csv

database/
students.db

models/
student_model.pkl

analysis.py
train_model.py
dashboard.py
requirements.txt
README.md

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

# 🎯 Skills Demonstrated

This project demonstrates practical skills in:

* Data Analysis
* Data Visualization
* SQL Database Integration
* Machine Learning Model Training
* Feature Engineering
* Building Interactive Data Apps

---

# 👨‍💻 Author

**Abhinav Pratap Singh**

Computer Science student interested in **Data Science, Machine Learning, and AI development**.

---

# ⭐ Future Improvements

Possible future upgrades:

* Add more advanced ML models (Random Forest, XGBoost)
* Improve dashboard UI
* Deploy the dashboard online
* Add more dataset features for prediction

