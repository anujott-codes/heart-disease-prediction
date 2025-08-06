# 🫀 Heart Disease Prediction using Machine Learning

This project focuses on building a machine learning model to predict the presence of heart disease using clinical parameters. It includes model development, evaluation, and deployment using a full-stack UI.

---

## 🔍 Project Overview

In this supervised machine learning project, I applied and compared multiple classification techniques to predict heart disease. The models used include:

- Logistic Regression ✅ *(final model)*
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier
- Support Vector Machine (SVM)
- Naive Bayes

After evaluating performance on metrics such as **accuracy**, **precision**, **recall**, and **ROC-AUC score**, **Logistic Regression** was selected as the most reliable model.

---

## ⚙️ Tech Stack

- **Python 3**
- **scikit-learn**, **pandas**, **numpy**, **matplotlib**, **seaborn**
- **Flask** for backend model serving
- **Streamlit** (prototype UI)
- **React / Next.js** for the final frontend
- **Node.js** and **npm**

---

## 🚀 Setup Instructions

Follow the steps below to run the project locally:

### 🔧 Backend + Frontend Setup

> Open a terminal in your project directory and follow these steps:

#### Step 1: chmod +x scripts/setup.sh
#### Step 2: ./scripts/setup.sh
#### Step 3: python3 scripts/model_integration.py (for macos) or python scripts/model_integration.py (for windows)
#### Step 4: In a new terminal, start the frontend (Next.js on port 3000)
#### npm run dev
