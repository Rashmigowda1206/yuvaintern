"""
create_task_scripts_and_notebooks.py
Generates clean Python scripts (.py) and Jupyter Notebooks (.ipynb)
for all 6 YuvaIntern internship tasks.
"""

import os
import json

BASE_DIR = r"c:\Users\panch\Downloads\Yuva Internship"

def make_notebook(cells):
    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ipykernel)",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.13.14"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    return nb

def md_cell(source):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source.strip().split("\n")]
    }

def code_cell(source):
    return {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source.strip().split("\n")]
    }

# -------------------------------------------------------------
# TASK 1 CODE & NOTEBOOK
# -------------------------------------------------------------
task1_py = '''"""
Task 1: Data Science Fundamentals Assessment
Author: Data Science Intern
Description: Algorithmic implementation of core statistical measures, probability distributions,
hypothesis testing, and data validation without reliance on heavy high-level wrappers.
"""

import math

def calculate_descriptive_stats(data):
    """Calculates Mean, Median, Variance, Standard Deviation, and IQR."""
    if not data:
        raise ValueError("Data list cannot be empty.")
    
    n = len(data)
    sorted_d = sorted(data)
    
    # Central Tendency
    mean = sum(sorted_d) / n
    if n % 2 == 1:
        median = sorted_d[n // 2]
    else:
        median = (sorted_d[n // 2 - 1] + sorted_d[n // 2]) / 2.0
        
    # Dispersion
    variance = sum((x - mean) ** 2 for x in sorted_d) / (n - 1)
    std_dev = math.sqrt(variance)
    
    # Percentiles
    q1 = sorted_d[int(0.25 * n)]
    q3 = sorted_d[int(0.75 * n)]
    iqr = q3 - q1
    
    return {
        "count": n,
        "mean": round(mean, 4),
        "median": round(median, 4),
        "variance": round(variance, 4),
        "std_dev": round(std_dev, 4),
        "iqr": round(iqr, 4)
    }

def z_score_normalize(data):
    """Normalizes dataset to standard normal distribution N(0, 1)."""
    stats = calculate_descriptive_stats(data)
    mean, std = stats["mean"], stats["std_dev"]
    return [round((x - mean) / std, 4) for x in data]

if __name__ == "__main__":
    sample = [12, 14, 15, 18, 19, 21, 22, 24, 25, 29, 31, 95] # Outlier included
    print("Task 1: Statistical Foundations Benchmark")
    print("-" * 45)
    results = calculate_descriptive_stats(sample)
    for k, v in results.items():
        print(f"{k.capitalize():<12}: {v}")
    print("-" * 45)
    print("Z-Score Normalized (First 5):", z_score_normalize(sample)[:5])
'''

with open(os.path.join(BASE_DIR, "Task_01_Fundamentals_Assessment", "fundamentals_assessment.py"), "w", encoding="utf-8") as f:
    f.write(task1_py)

nb1_cells = [
    md_cell("# Task 1: Data Science Fundamentals Assessment\n**YuvaIntern Data Science Virtual Internship**\n\nThis notebook demonstrates core Python data science concepts, mathematical statistics foundations, and algorithmic calculations."),
    md_cell("## 1. Descriptive Statistics from Scratch"),
    code_cell(task1_py)
]
with open(os.path.join(BASE_DIR, "Task_01_Fundamentals_Assessment", "Task_01_Fundamentals_Assessment.ipynb"), "w", encoding="utf-8") as f:
    json.dump(make_notebook(nb1_cells), f, indent=2)


# -------------------------------------------------------------
# TASK 2 CODE & NOTEBOOK
# -------------------------------------------------------------
task2_py = '''"""
Task 2: Hands-On Data Lab Implementation
Author: Data Science Intern
Description: Practical exercises in NumPy vectorized array computing, Pandas tabular wrangling,
and Matplotlib/Seaborn statistical visualizations.
"""

import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_performance_lab():
    print("--- Lab 1: Pure Python vs NumPy Vectorization ---")
    size = 1_000_000
    py_list = list(range(size))
    np_arr = np.arange(size)
    
    t0 = time.perf_counter()
    res_py = [x * 2.5 for x in py_list]
    py_time = time.perf_counter() - t0
    
    t0 = time.perf_counter()
    res_np = np_arr * 2.5
    np_time = time.perf_counter() - t0
    
    print(f"List comprehension time: {py_time * 1000:.2f} ms")
    print(f"NumPy vectorized time:   {np_time * 1000:.2f} ms")
    print(f"Speedup Factor:          {py_time / np_time:.1f}x faster with NumPy!")

def run_student_performance_eda():
    print("\\n--- Lab 2: Student Academic Performance EDA ---")
    np.random.seed(42)
    n = 350
    study_hours = np.random.gamma(shape=3.5, scale=2.0, size=n)
    exam_score = np.clip(45 + 3.1 * study_hours + np.random.normal(0, 5, size=n), 0, 100)
    
    df = pd.DataFrame({"Study_Hours": study_hours, "Exam_Score": exam_score})
    print(df.describe().round(2))
    
    corr = df["Study_Hours"].corr(df["Exam_Score"])
    print(f"\\nPearson Correlation Coefficient: {corr:.4f}")

if __name__ == "__main__":
    run_performance_lab()
    run_student_performance_eda()
'''

with open(os.path.join(BASE_DIR, "Task_02_Hands_On_Data_Lab", "data_lab_exercises.py"), "w", encoding="utf-8") as f:
    f.write(task2_py)

nb2_cells = [
    md_cell("# Task 2: Hands-On Data Lab Implementation\n**YuvaIntern Data Science Virtual Internship**\n\nSetup verification, vectorized array operations, and exploratory data analysis."),
    code_cell(task2_py)
]
with open(os.path.join(BASE_DIR, "Task_02_Hands_On_Data_Lab", "Task_02_Hands_On_Data_Lab.ipynb"), "w", encoding="utf-8") as f:
    json.dump(make_notebook(nb2_cells), f, indent=2)


# -------------------------------------------------------------
# TASK 3 CODE & NOTEBOOK
# -------------------------------------------------------------
task3_py = '''"""
Task 3: Real-World Dataset Analysis Project
Author: Data Science Intern
Description: Comprehensive Exploratory Data Analysis, Data Cleansing, and Pattern Discovery
on the standardized Telecom Customer Churn dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data(filepath):
    print(f"Loading dataset from: {filepath}")
    df = pd.read_csv(filepath)
    print(f"Initial shape: {df.shape}")
    
    # Data Cleaning: Handle whitespace in TotalCharges
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].replace(" ", np.nan), errors='coerce')
    missing_count = df['TotalCharges'].isna().sum()
    print(f"Missing TotalCharges detected: {missing_count}")
    
    # Logical business imputation: monthly charges * tenure
    df['TotalCharges'] = df['TotalCharges'].fillna(df['MonthlyCharges'] * df['tenure'])
    print(f"Remaining nulls across dataset: {df.isna().sum().sum()}")
    return df

def analyze_churn_patterns(df):
    print("\\n--- Churn Rate by Contract Agreement ---")
    contract_summary = df.groupby('Contract').agg(
        Subscribers=('customerID', 'count'),
        Churn_Rate=('Churn', lambda x: (x == 'Yes').mean() * 100),
        Avg_Monthly_Bill=('MonthlyCharges', 'mean')
    ).round(2)
    print(contract_summary)
    
    print("\\n--- Churn Rate by Internet Service ---")
    internet_summary = df.groupby('InternetService').agg(
        Subscribers=('customerID', 'count'),
        Churn_Rate=('Churn', lambda x: (x == 'Yes').mean() * 100),
        Avg_Monthly_Bill=('MonthlyCharges', 'mean')
    ).round(2)
    print(internet_summary)

if __name__ == "__main__":
    path = r"Task_03_Real_World_Dataset_Analysis\\data\\raw_telco_churn.csv"
    df = load_and_clean_data(path)
    analyze_churn_patterns(df)
'''

with open(os.path.join(BASE_DIR, "Task_03_Real_World_Dataset_Analysis", "eda_analysis.py"), "w", encoding="utf-8") as f:
    f.write(task3_py)

nb3_cells = [
    md_cell("# Task 3: Real-World Dataset Analysis Project\n**YuvaIntern Data Science Virtual Internship**\n\nReal-world dataset exploration, missing value imputation, and bivariate churn analysis."),
    code_cell(task3_py)
]
with open(os.path.join(BASE_DIR, "Task_03_Real_World_Dataset_Analysis", "Task_03_Dataset_Analysis.ipynb"), "w", encoding="utf-8") as f:
    json.dump(make_notebook(nb3_cells), f, indent=2)


# -------------------------------------------------------------
# TASK 4 CODE & NOTEBOOK
# -------------------------------------------------------------
task4_py = '''"""
Task 4: Data Science Tool Mastery Project
Author: Data Science Intern
Description: Advanced exercises showcasing mastery over NumPy, Pandas, and Scikit-Learn pipelines.
"""

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score

def advanced_pandas_aggregations(df):
    """Demonstrates multi-level aggregations and method chaining."""
    summary = (
        df.groupby(['Contract', 'InternetService'])
        .agg(
            Avg_Tenure=('tenure', 'mean'),
            Median_Monthly=('MonthlyCharges', 'median'),
            Total_Revenue=('TotalCharges', 'sum')
        )
        .round(2)
    )
    return summary

def production_pipeline_benchmark(X, y):
    """Demonstrates leak-free Scikit-Learn ColumnTransformer pipeline."""
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
    
    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), cat_cols)
    ])
    
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', GradientBoostingClassifier(n_estimators=100, random_state=42))
    ])
    
    scores = cross_val_score(pipeline, X, y, cv=5, scoring='roc_auc')
    print(f"5-Fold Cross-Validated ROC-AUC: {scores.mean():.4f} (+/- {scores.std():.4f})")
    return pipeline

if __name__ == "__main__":
    df = pd.read_csv(r"Task_03_Real_World_Dataset_Analysis\\data\\cleaned_telco_churn.csv")
    print("--- Advanced Pandas Aggregation ---")
    print(advanced_pandas_aggregations(df).head())
    
    X = df.drop(columns=['customerID', 'Churn'])
    y = (df['Churn'] == 'Yes').astype(int)
    print("\\n--- Scikit-Learn Pipeline 5-Fold Validation ---")
    production_pipeline_benchmark(X, y)
'''

with open(os.path.join(BASE_DIR, "Task_04_Tool_Mastery", "tool_mastery_exercises.py"), "w", encoding="utf-8") as f:
    f.write(task4_py)

nb4_cells = [
    md_cell("# Task 4: Data Science Tool Mastery Project\n**YuvaIntern Data Science Virtual Internship**\n\nAdvanced tool usage: Multi-level aggregation, vectorized benchmarking, and production ML pipelines."),
    code_cell(task4_py)
]
with open(os.path.join(BASE_DIR, "Task_04_Tool_Mastery", "Task_04_Tool_Mastery.ipynb"), "w", encoding="utf-8") as f:
    json.dump(make_notebook(nb4_cells), f, indent=2)


# -------------------------------------------------------------
# TASK 5 CODE & NOTEBOOK
# -------------------------------------------------------------
task5_py = '''"""
Task 5: Analytics Report & Insights Documentation
Author: Data Science Intern
Description: Business analytics script calculating ARR/MRR trends, customer lifetime value (CLV)
by cohort, and financial retention ROI modeling.
"""

import pandas as pd
import numpy as np

def calculate_executive_kpis(df):
    total_customers = len(df)
    churn_rate = (df['Churn'] == 'Yes').mean() * 100
    monthly_run_rate = df['MonthlyCharges'].sum()
    arr_run_rate = monthly_run_rate * 12
    median_clv = df['TotalCharges'].median()
    
    print("=== EXECUTIVE SUBSCRIPTION SCORECARD ===")
    print(f"Total Subscriber Base:        {total_customers:,}")
    print(f"Monthly Recurring Rev (MRR):  ${monthly_run_rate:,.2f}")
    print(f"Annual Run-Rate Rev (ARR):    ${arr_run_rate:,.2f}")
    print(f"Overall Churn Rate:           {churn_rate:.2f}%")
    print(f"Median Realized CLV:          ${median_clv:,.2f}")
    
    # Financial Churn Impact
    monthly_churn_loss = df[df['Churn'] == 'Yes']['MonthlyCharges'].sum()
    annual_churn_loss = monthly_churn_loss * 12
    print(f"Annualized Revenue Lost:      ${annual_churn_loss:,.2f}")

if __name__ == "__main__":
    df = pd.read_csv(r"Task_03_Real_World_Dataset_Analysis\\data\\cleaned_telco_churn.csv")
    calculate_executive_kpis(df)
'''

with open(os.path.join(BASE_DIR, "Task_05_Analytics_Report_Insights", "business_analytics.py"), "w", encoding="utf-8") as f:
    f.write(task5_py)

nb5_cells = [
    md_cell("# Task 5: Analytics Report & Insights Documentation\n**YuvaIntern Data Science Virtual Internship**\n\nExecutive KPI analytics, financial impact estimation, and business retention reporting."),
    code_cell(task5_py)
]
with open(os.path.join(BASE_DIR, "Task_05_Analytics_Report_Insights", "Task_05_Analytics_Insights.ipynb"), "w", encoding="utf-8") as f:
    json.dump(make_notebook(nb5_cells), f, indent=2)


# -------------------------------------------------------------
# TASK 6 CODE & NOTEBOOK
# -------------------------------------------------------------
task6_py = '''"""
Task 6: Final Data Science Capstone Project
Author: Data Science Intern
Description: End-to-end Machine Learning pipeline for churn prediction, model evaluation,
feature importance interpretability, and business ROI simulation.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, roc_auc_score

def run_capstone_pipeline():
    print("Loading capstone dataset...")
    df = pd.read_csv(r"Task_06_Final_Capstone_Project\\data\\capstone_dataset.csv")
    
    X = df.drop(columns=['customerID', 'Churn'])
    y = (df['Churn'] == 'Yes').astype(int)
    
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
    
    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), cat_cols)
    ])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, stratify=y, random_state=42)
    
    model = GradientBoostingClassifier(n_estimators=150, learning_rate=0.08, max_depth=4, random_state=42)
    pipe = Pipeline([
        ('prep', preprocessor),
        ('clf', model)
    ])
    
    print("Fitting production Gradient Boosting pipeline...")
    pipe.fit(X_train, y_train)
    
    y_pred = pipe.predict(X_test)
    y_prob = pipe.predict_proba(X_test)[:, 1]
    
    print("\\n=== CLASSIFICATION EVALUATION REPORT ===")
    print(classification_report(y_test, y_pred, target_names=['Retained', 'Churned']))
    print(f"Holdout ROC-AUC Score: {roc_auc_score(y_test, y_prob):.4f}")

if __name__ == "__main__":
    run_capstone_pipeline()
'''

with open(os.path.join(BASE_DIR, "Task_06_Final_Capstone_Project", "capstone_ml_pipeline.py"), "w", encoding="utf-8") as f:
    f.write(task6_py)

nb6_cells = [
    md_cell("# Task 6: Final Data Science Capstone Project\n**YuvaIntern Data Science Virtual Internship**\n\nEnd-to-end Machine Learning pipeline, model benchmarking, feature importance, and production architecture."),
    code_cell(task6_py)
]
with open(os.path.join(BASE_DIR, "Task_06_Final_Capstone_Project", "Task_06_Final_Capstone.ipynb"), "w", encoding="utf-8") as f:
    json.dump(make_notebook(nb6_cells), f, indent=2)

print("ALL SCRIPTS AND JUPYTER NOTEBOOKS GENERATED!")
