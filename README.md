# YuvaIntern Data Science Virtual Internship — Comprehensive Assessment Repository

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.9.1-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-3.0.6-darkblue.svg)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Internship-Completed-brightgreen.svg)](https://yuvaintern.com/my-internships)

This repository contains the complete portfolio of technical deliverables, source code, analytical models, interactive Jupyter notebooks, and formal Word assessment reports (`.docx`) for the **YuvaIntern Data Science Virtual Internship**.

---

## Repository Architecture & Task Structure

The project is structured into six discrete milestones covering data science foundations, hands-on environment implementation, real-world data exploration, tool mastery, executive analytics, and an end-to-end machine learning capstone.

```text
├── Submissions/                                             # Ready-to-Upload Word Reports (.docx)
│   ├── Task_1_Data_Science_Fundamentals_Assessment.docx
│   ├── Task_2_Hands_On_Data_Lab_Implementation.docx
│   ├── Task_3_Real_World_Dataset_Analysis_Project.docx
│   ├── Task_4_Data_Science_Tool_Mastery_Project.docx
│   ├── Task_5_Analytics_Report_and_Insights_Documentation.docx
│   └── Task_6_Final_Data_Science_Capstone_Project.docx
│
├── Task_01_Fundamentals_Assessment/                         # Task 1: Core Theory & Python Basics
│   ├── fundamentals_assessment.py                           # Custom statistical estimators from scratch
│   ├── Task_01_Fundamentals_Assessment.ipynb                # Interactive notebook walkthrough
│   └── Task_1_Data_Science_Fundamentals_Assessment.docx     # Comprehensive technical assessment report
│
├── Task_02_Hands_On_Data_Lab/                              # Task 2: Environment & Practical Exercises
│   ├── data_lab_exercises.py                                # Vectorization benchmarks & academic EDA
│   ├── Task_02_Hands_On_Data_Lab.ipynb                      # Lab execution notebook
│   ├── figures/                                             # High-resolution benchmark & distribution plots
│   └── Task_2_Hands_On_Data_Lab_Implementation.docx         # Formal lab implementation report
│
├── Task_03_Real_World_Dataset_Analysis/                     # Task 3: Real-World Dataset Exploration
│   ├── data/                                                # Raw & cleaned Telco Customer Churn datasets
│   │   ├── raw_telco_churn.csv                              # 7,043 rows with raw whitespace anomalies
│   │   └── cleaned_telco_churn.csv                          # Imputed and coerced clean dataset
│   ├── eda_analysis.py                                      # Full EDA and bivariate statistical script
│   ├── Task_03_Dataset_Analysis.ipynb                       # Exploratory analysis notebook
│   ├── figures/                                             # Publication-grade charts (DPI=300)
│   └── Task_3_Real_World_Dataset_Analysis_Project.docx      # Rigorous EDA and retention findings report
│
├── Task_04_Tool_Mastery/                                   # Task 4: High-Performance Data Tools
│   ├── tool_mastery_exercises.py                            # NumPy matrix math, Pandas piping, ML pipelines
│   ├── Task_04_Tool_Mastery.ipynb                           # Tool mastery notebook
│   ├── figures/                                             # Performance curves and pairplots
│   └── Task_4_Data_Science_Tool_Mastery_Project.docx        # In-depth architectural mastery report
│
├── Task_05_Analytics_Report_Insights/                      # Task 5: Business Analytics & Reporting
│   ├── business_analytics.py                                # Executive KPI scorecard and waterfall math
│   ├── Task_05_Analytics_Insights.ipynb                     # Business insights notebook
│   ├── figures/                                             # MRR trends, CLV cohorts, and retention funnel
│   └── Task_5_Analytics_Report_and_Insights_Documentation.docx # Executive business review report
│
├── Task_06_Final_Capstone_Project/                          # Task 6: End-to-End ML Capstone Project
│   ├── data/
│   │   └── capstone_dataset.csv                             # Preprocessed dataset for model training
│   ├── capstone_ml_pipeline.py                              # Logistic Regression, Random Forest & LightGBM
│   ├── Task_06_Final_Capstone.ipynb                         # Capstone walkthrough notebook
│   ├── figures/                                             # ROC curves, confusion matrices, ROI curves
│   └── Task_6_Final_Data_Science_Capstone_Project.docx      # Production-grade Capstone project report
│
├── SUBMISSION_GUIDE.md                                      # Master Guide: Copy-paste descriptions (>200 words)
├── requirements.txt                                         # Python package dependencies
└── generate_all_tasks_data_and_charts.py                    # Master automation script
```

---

## Overview of Assessment Milestones

### Task 1: Data Science Fundamentals Assessment
- **Key Concepts**: CRISP-DM lifecycle, memory mutability, functional programming, descriptive and inferential statistics, probability distributions, Central Limit Theorem, Type I & Type II decision errors, and data taxonomy (Nominal, Ordinal, Interval, Ratio).
- **Practical Exercises**: Built descriptive statistical routines from scratch in pure Python, validating non-parametric resistance to outliers compared to parametric measures.

### Task 2: Hands-On Data Lab Implementation
- **Key Concepts**: Configured a modern Python 3.13 analytical workspace with Jupyter, NumPy, Pandas, Matplotlib, Seaborn, and Scikit-Learn.
- **Benchmarks**: Empirical benchmarking squaring 500,000 array elements demonstrated a **~45x speedup** using NumPy SIMD vectorization over standard Python loops. Analyzed a cohort of 350 students to establish a **Pearson r = +0.768** correlation between study hours and academic performance.

### Task 3: Real-World Dataset Analysis Project
- **Dataset**: Standardized IBM Telco Customer Churn dataset (7,043 subscribers, 18 features).
- **Methodology**: Detected and coerced dirty whitespace anomalies in `TotalCharges`, applied domain-specific imputation, and conducted univariate and bivariate analysis.
- **Core Findings**: Month-to-month contracts exhibit an acute churn risk (>40%), while 2-year contracts show strong retention (<3%). Subscribers with high monthly charges ($75–$105) on fiber optic plans experience higher friction, highlighting key areas for pricing and service optimization.

### Task 4: Data Science Tool Mastery Project
- **Key Concepts**: Advanced NumPy contiguous striding and BLAS GEMM matrix operations; Pandas MultiIndex aggregation, method chaining with `.pipe()`, and memory optimization; Seaborn statistical pairplots; and Scikit-Learn `ColumnTransformer` pipelines that prevent data leakage during cross-validation.

### Task 5: Analytics Report & Insights Documentation
- **Key Concepts**: Executive Business Review (EBR) evaluating subscription economics across a balanced KPI scorecard: MRR ($565k), ARR ($6.78M), Churn Rate, CLV ($2,283 median), CAC ($450), and Net Revenue Retention (92.4%).
- **Strategic Impact**: Identified $485,000 in annualized revenue loss driven by churn and proposed a three-phase retention roadmap yielding an estimated **5.3x Net ROI**.

### Task 6: Final Data Science Capstone Project
- **Project Title**: *Predictive Customer Churn & Retention Optimization Engine: Production Machine Learning Architecture, Evaluation, and Deployment Strategy*.
- **Machine Learning Architecture**: Evaluated balanced Logistic Regression, Random Forest, and Gradient Boosting pipelines using 5-Fold Stratified Cross-Validation on holdout records (N = 1,409).
- **Performance Highlights**:
  - **ROC-AUC**: 0.8733 (Logistic Regression) / 0.8621 (Gradient Boosting)
  - **F1-Score**: 0.7741 / 0.7615
  - **Recall**: 84.46% (identifies >84% of all churning customers)
- **Financial Simulation**: Targeting the top 20% highest-risk subscribers captures **72% of all churners**, producing **$184,000 in net saved value** on the test cohort with a **4.2x campaign ROI**.
- **Production Architecture**: RESTful FastAPI inference specification, containerized Docker deployment, and Population Stability Index (PSI) drift monitoring.

---

## Installation & Environment Setup

Clone this repository and set up a virtual environment:

```bash
# 1. Clone repository
git clone https://github.com/panchaksharayya12/Yuvaintern.git
cd Yuvaintern

# 2. Create and activate a virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 3. Install required packages
pip install -r requirements.txt
```

---

## Running the Pipeline & Reproducing Results

To regenerate all datasets, recalculate machine learning benchmarks, render charts, and recompile Word reports:

```bash
# Generate datasets and high-resolution figures
python generate_all_tasks_data_and_charts.py

# Recompile all 6 formal Word documents
python build_all_word_reports.py
```

---

## Author & Acknowledgments

- **Intern**: Data Science Intern
- **Program**: [YuvaIntern Virtual Internship Program](https://yuvaintern.com/my-internships)
- **Track**: Data Science & Machine Learning
- **Submission Date**: October 2026
