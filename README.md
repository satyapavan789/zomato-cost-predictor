🍽️ Zomato Restaurant Cost Prediction

🔗 Live Demo:
👉https://zomato-cost-predictor-kdnax3v93ugz56u5sdiaun.streamlit.app/


📌 Project Overview

This project predicts the approximate cost for two people at a restaurant using real-world Zomato restaurant data.
It is an end-to-end Data Science project, covering everything from EDA and feature engineering to model deployment on the cloud.

The goal was to build a production-ready machine learning system, not just a notebook-based model.

🎯 Problem Statement
Restaurant cost estimation helps:
Users filter restaurants based on budget platforms understand pricing patterns, Businesses analyze factors influencing cost.
This problem is framed as a regression task, where the target variable is the approximate cost for two people.

📂 Dataset Description

The dataset contains restaurant-level information such as:
Ratings
Votes
Number of cuisines
Restaurant type
Location
Online order availability
Table booking availability
The data includes:
Missing values
Mixed numerical and categorical features
Real-world noise and skewed distributions

🔍 Exploratory Data Analysis (EDA)
Key insights from EDA:
Restaurant cost distribution is right-skewed

Higher votes and ratings are associated with higher cost

Fine Dining and Lounge restaurants tend to be more expensive

Location and restaurant type significantly influence pricing

EDA guided decisions for:
Feature selection
Handling missing values
Feature engineering strategies

🛠️ Feature Engineering
Important engineered features include:

Number of cuisines offered by a restaurant

Popularity score derived from ratings and votes

Business logic indicators such as high-cost signals

Encoded restaurant type and location

These features helped capture non-linear patterns in restaurant pricing.

⚙️ Preprocessing Pipeline
A robust preprocessing pipeline was built using scikit-learn:

Numerical features: median imputation + scaling

Categorical features: most-frequent imputation + one-hot encoding

Implemented using ColumnTransformer

This ensures:
No data leakage
Consistent preprocessing during training and inference

🤖 Model Building & Evaluation
Models trained and evaluated:
Random Forest Regressor (baseline)
XGBoost Regressor (final model)

Evaluation strategy:
Train–test split with stratification
Cross-validation
RMSE as the evaluation metric
XGBoost was selected due to better generalization on unseen data.

🚀 Deployment
The final trained pipeline (preprocessing + model) was:
Serialized using joblib Deployed as an interactive web application using Streamlit hosted on Streamlit Cloud, Key deployment challenges handled:
Feature schema mismatch and consistent preprocessing at inference, Library version compatibility

🖥️ Web Application Features
User-friendly input interface
Real-time cost prediction
Input validation to prevent invalid predictions
Clean UI suitable for demos and interviews

🧰 Tech Stack
Programming: python
Data Analysis: Pandas, NumPy
Machine Learning: scikit-learn, XGBoost
Visualization: Matplotlib, Seaborn
Deployment: Streamlit, Streamlit Cloud
Version Control: Git, GitHub

📊 Results
Achieved RMSE ≈ ~70 on unseen test data
Successfully deployed a working ML model accessible via web


🙌 Acknowledgements
This project was built as part of a hands-on learning journey in Data Science and Machine Learning, focusing on real-world problems and production-ready solutions.

📬 Contact
If you’d like to discuss this project or provide feedback, feel free to reach out:

LinkedIn: https://www.linkedin.com/in/satya-pavan-00b1bb340?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

Email: satyapavankumar@gmail.com
