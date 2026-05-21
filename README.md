# Social Media Addiction Risk Prediction

## Project Overview
Social Media Addiction Risk Prediction is a Machine Learning based project developed to analyze user behavioral patterns and predict the level of social media addiction risk. The project focuses on identifying addiction tendencies by evaluating factors such as daily social media usage time, sleep duration, mental health score, academic performance, and social interaction behavior.

The system applies multiple Machine Learning algorithms to compare prediction performance and identify the most effective model for addiction risk classification. The project also includes clustering analysis to group users with similar behavioral characteristics.

---

## Project Description
This project demonstrates the practical application of Machine Learning in behavioral analysis and mental health related prediction systems. Various supervised and unsupervised learning techniques were implemented to study the relationship between user habits and addiction risk levels.

Several Machine Learning models including Logistic Regression, Decision Tree, Support Vector Machine (SVM), Random Forest, Naive Bayes, K-Nearest Neighbors (KNN), and KMeans Clustering were trained and evaluated using the dataset. Among all models, Random Forest achieved the highest accuracy of 91.5%, making it the best performing model for this project.

The project workflow includes:
- Data Collection
- Data Preprocessing
- Feature Selection
- Feature Scaling
- Model Training
- Model Evaluation
- Clustering Analysis
- Model Saving using Joblib

KMeans clustering was additionally used to identify groups of users with similar social media usage patterns through elbow method and silhouette score analysis.

---

## Objectives
- Analyze social media usage behavior
- Predict addiction risk using Machine Learning
- Compare the performance of multiple ML algorithms
- Identify the best performing predictive model
- Study behavioral patterns using clustering techniques

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

---

## Machine Learning Models Implemented
- Multiple Linear Regression
- Logistic Regression
- Decision Tree
- Support Vector Machine (SVM)
- Random Forest
- Naive Bayes
- K-Nearest Neighbors (KNN)
- KMeans Clustering

---

## Model Performance

| Model | Accuracy |
|---|---|
| Multiple Linear Regression | 61.1% |
| Logistic Regression | 71% |
| Decision Tree | 79% |
| SVM | 90% |
| Random Forest | 91.5% |
| Naive Bayes | 86.5% |
| KNN | 80.5% |

### Best Performing Model
Random Forest achieved the highest accuracy of 91.5%, making it the most effective model for predicting social media addiction risk.

---

## Features Used
- Daily Usage Hours
- Sleep Hours Per Night
- Mental Health Score
- Academic Performance
- Age
- Gender
- Social Interaction Score

---

## Clustering Analysis
KMeans clustering was applied to group users based on behavioral similarities related to social media usage and addiction tendencies. Elbow method and silhouette score analysis were used to determine the optimal number of clusters.

---

## Future Enhancements
- Integration of Deep Learning models
- Real-time addiction risk monitoring system
- Web application deployment
- Mobile application integration
- Personalized recommendation system for addiction prevention

---

## Conclusion
This project highlights the effectiveness of Machine Learning techniques in predicting social media addiction risk using behavioral and psychological factors. Comparative analysis of multiple algorithms showed that Random Forest provided the best overall performance. The project can be further extended into real-world healthcare, educational, and behavioral monitoring applications.
