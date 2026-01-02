 Zomato Restaurant Cost Prediction

Live Demo:
https://zomato-cost-predictor-kdnax3v93ugz56u5sdiaun.streamlit.app/

Overview:
-Built an end-to-end machine learning regression system to predict the average cost for two people at restaurants using real-world Zomato data.
-The project focuses on data understanding, feature engineering, model evaluation, and deployment readiness.

Problem Statement:
-Restaurant pricing depends on multiple factors such as location, cuisines, ratings, and popularity.
-The objective was to predict restaurant cost accurately while avoiding data leakage and ensuring reliable model evaluation.

Approach:
-Performed exploratory data analysis (EDA) to understand pricing trends, outliers, ratings, votes, and restaurant types.
-Engineered meaningful features such as number of cuisines and popularity indicators.
-Built regression models using Linear Regression, Decision Tree, and Random Forest.
-Used cross-validation and RMSE to compare models and select the best-performing one.
-Implemented ColumnTransformer pipelines to prevent data leakage.
-Addressed schema mismatch issues during deployment by aligning training and inference inputs.

Model Evaluation:
-Compared models Random Forest and XGBoost using RMSE and cross-validation.
-Selected XGBoost based on stable performance and lower error.

Tools & Technologies:
Python | Pandas | NumPy | scikit-learn | Streamlit

Outcome:
This project demonstrates the complete machine learning lifecycle, from raw data analysis to deployment considerations, with a strong focus on robust evaluation and practical problem-solving.

Acknowledgements:
This project was built as part of a hands-on learning journey in Data Science and Machine Learning, focusing on real-world problems and production-ready solutions.
