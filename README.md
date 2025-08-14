# Titanic Preprocessing

## 📌 Overview

Python-based preprocessing system for the Titanic dataset with **two main approaches**:

1. **Jupyter Notebook** – end-to-end ML workflow.
2. **Modular Scripts** – reusable preprocessing & detailed exploration.

This repository provides both **interactive analysis** (Notebook) and **production-ready preprocessing** (Modular Scripts).

---

## 📂 Dataset

- **File:** `titanic.csv`
- **Records:** 891 passengers
- **Columns:** 12 attributes

### 🗂 Schema Overview

| Column      | Type   | Missing % | Notes                                 |
| ----------- | ------ | --------- | ------------------------------------- |
| PassengerId | Int    | 0.0%      | Unique ID                             |
| Survived    | Int    | 0.0%      | Target variable (0/1)                 |
| Pclass      | Int    | 0.0%      | Passenger class (ordinal)             |
| Name        | String | 0.0%      | High-cardinality text                 |
| Sex         | String | 0.0%      | Binary categorical                    |
| Age         | Float  | 19.9%     | Missing values, critical for modeling |
| SibSp       | Int    | 0.0%      | Siblings/spouses aboard               |
| Parch       | Int    | 0.0%      | Parents/children aboard               |
| Ticket      | String | 0.0%      | Mixed alphanumeric                    |
| Fare        | Float  | 0.0%      | Skewed distribution                   |
| Cabin       | String | 77.1%     | Sparse                                |
| Embarked    | String | 0.2%      | Categorical with minimal missing      |

---

## 🚀 How to Run

**Notebook:**

```bash
jupyter notebook Titanic.ipynb
```

**Scripts:**

```bash
python main.py
```

---

## ⚙️ Processing Approaches

### 📓 1. Notebook Approach

- **Goal:** End-to-end ML pipeline
- **Architecture:** Self-contained notebook
- **Main Output:** `submission.csv` predictions
- **Strengths:** Interactive analysis, inline visualizations
- **Best For:** EDA, ML model development, research, presentations

### 🗂 2. Modular Script Approach

- **Goal:** Comprehensive data exploration & reusable preprocessing
- **Architecture:** Modular function-based
- **Main Output:** `output.txt` logs + saved plots in `plots/`
- **Strengths:** High reusability, detailed data quality checks, automated workflows
- **Best For:** Production pipelines, scheduled processing, multiple dataset versions

### 🔍 Comparison

| Aspect             | Notebook         | Modular Scripts      |
| ------------------ | ---------------- | -------------------- |
| Primary Goal       | End-to-end ML    | Data quality & reuse |
| Reusability        | Low              | High                 |
| Visuals            | Inline only      | Saved to files       |
| Data Quality Focus | Basic            | Extensive            |
| Main Output        | `submission.csv` | Logs + plots         |

### 🛠 Key Modular Functions

- **Data Quality:** `read_data()`, `check_types()`, `check_nulls()`, `check_duplicated()`
- **Processing:** `check_outliers()`, `visual()`, `split_data()`, `scale_columns()`, `encode_columns()`

---

## 📓 Jupyter Notebook Pipeline

Implemented in `Titanic.ipynb`, this pipeline provides a **complete end-to-end ML workflow** from raw data to prediction file generation.

### 🔄 Workflow Stages

1. **Data Loading & Setup**: Load `titanic.csv` and perform initial exploration
2. **Integrated Cleaning & Preprocessing**: Handle missing values, feature engineering, and transformations directly in notebook cells
3. **Model Training & Evaluation**: Train a Logistic Regression model, evaluate results
4. **Prediction Generation**: Create `submission.csv` formatted for Kaggle

### 📤 Output

| File             | Description                                     |
| ---------------- | ----------------------------------------------- |
| `submission.csv` | PassengerId + Survived predictions for test set |

### ✅ Advantages

- Interactive & educational
- Self-contained & reproducible

### ⚠ Limitations

- Lower reusability compared to modular scripts
- Less comprehensive in data quality assessment

---

## 🗂 Modular Script Pipeline

### Key Components

- **main.py** → Orchestrates workflow (logging, plot saving, function calls)
- **my\_preprocessing.py** → Library of preprocessing functions (data quality, visualization, feature engineering)

### Advantages

- **Reusability:** Functions can be imported in other projects
- **Maintainability:** Easy to update steps individually
- **Testability:** Each function has single responsibility
- **Flexibility:** Multiple encoding strategies
- **Observability:** Detailed logs & visual outputs
- **Extensibility:** Add new functions without refactoring

---

## 🏗 Core Components

### Function Overview (`my_preprocessing.py`)

| Function           | Purpose                       | Input                 | Output             |
| ------------------ | ----------------------------- | --------------------- | ------------------ |
| `read_data`        | Load CSV and preview          | File path             | DataFrame          |
| `check_types`      | Analyze types & unique values | DataFrame             | Summary DataFrame  |
| `check_nulls`      | Count nulls & ratios          | DataFrame             | Summary DataFrame  |
| `check_duplicated` | Remove duplicates             | DataFrame             | Modified DataFrame |
| `check_outliers`   | Detect & cap outliers         | DataFrame             | Modified DataFrame |
| `visual`           | Generate plots                | DataFrame             | Plot files         |
| `split_data`       | Split features & target       | DataFrame, target col | X, y tuple         |
| `scale_columns`    | Scale numeric columns         | DataFrame, columns    | Scaled DataFrame   |
| `encode_columns`   | Encode categorical cols       | DataFrame, cols, type | Encoded DataFrame  |

---

## ⚙️ Pipeline Orchestration (`main.py`)

1. Load data → `df`
2. Remove non-predictive columns
3. Convert categorical columns
4. Handle missing values
5. Split data → `X, y`
6. Scale numeric columns
7. Encode categorical columns (OneHot & Label)
8. Generate multiple dataset versions
9. Redirect logs to `output.txt` and save plots in `plots/`

---

## 📝 Processing Logs & Data Transformations

- **Duplicates removed:** 891 → 773 rows
- **Missing Values & Type Optimizations:**

| Column   | Missing Values | Ratio | Data Type Optimization |
| -------- | -------------- | ----- | ---------------------- |
| Age      | 177            | 19.9% | float64 → numeric      |
| Cabin    | 687            | 77.1% | object → categorical   |
| Embarked | 2              | 0.2%  | object → categorical   |
| Sex      | 0              | 0%    | object → categorical   |
| Pclass   | 0              | 0%    | int64 → categorical    |

- **Feature Scaling:** Min-Max (Age & Fare)
- **Categorical Encoding:** OneHot & Label Encoding

---

## 📊 Data Visualizations

### Numerical

| Type            | File                      | Purpose               |
| --------------- | ------------------------- | --------------------- |
| Histograms      | numerical\_histograms.png | Distribution analysis |
| KDE Plots       | numerical\_kde.png        | Density estimation    |
| Outliers Before | outliers\_before.png      | Pre-processing        |
| Outliers After  | outliers\_after.png       | Post-processing       |

### Categorical

| Type        | File                        | Purpose                     |
| ----------- | --------------------------- | --------------------------- |
| Count Plots | categorical\_countplots.png | Frequency analysis          |
| Pie Charts  | categorical\_pieplots.png   | Proportional representation |

- Libraries: `matplotlib`, `seaborn`, `pandas`
- Automatic column classification (numerical/categorical)
- Layout: multi-subplot, consistent styling

---

## 🏗 System Architecture & Technical Implementation

- Dual-architecture: Modular (`main.py` + `my_preprocessing.py`) & Notebook (`Titanic.ipynb`)
- Stateless functions; modular & reusable
- Memory-safe: DataFrame copies for non-destructive operations

### Dependencies

| Library               | Purpose                   |
| --------------------- | ------------------------- |
| pandas                | Data manipulation         |
| sklearn.preprocessing | MinMax scaling            |
| category\_encoders    | OneHot/Label encoding     |
| matplotlib.pyplot     | Plotting                  |
| seaborn               | Statistical visualization |

### I/O & Artifacts

| Artifact Type     | Function          | File Pattern              |
| ----------------- | ----------------- | ------------------------- |
| Logs              | Multiple          | output.txt                |
| Numerical Plots   | visual()          | plots/numerical\_\*.png   |
| Categorical Plots | visual()          | plots/categorical\_\*.png |
| Outlier Analysis  | check\_outliers() | plots/outliers\_\*.png    |

### Extensibility

- Add new analysis/encoding/visualization functions
- Notebook allows interactive analysis & model development

---

**Sources:**\
`main.py` (1–79), `my_preprocessing.py` (1–206), `Titanic.ipynb` (1–2850), `output.txt`, `plots/`

