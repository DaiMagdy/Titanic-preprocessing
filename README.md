# Titanic Preprocessing

## 📌 Overview
Python-based preprocessing system for the Titanic dataset with two main approaches:
1. **Jupyter Notebook** – end-to-end ML workflow.
2. **Modular Scripts** – reusable preprocessing & detailed exploration.

## 📂 Dataset
- File: `titanic.csv`
- Records: 891 passengers

## 🏗 Core Components
| File                | Purpose                            | Output            |
|---------------------|------------------------------------|-------------------|
| `titanic.csv`       | Raw dataset                        | 891 records       |
| `my_preprocessing.py` | Preprocessing functions           | Reusable ops      |
| `main.py`           | Orchestrates preprocessing         | `output.txt` + plots |
| `Titanic.ipynb`     | Complete ML workflow               | `submission.csv`  |

## 🚀 How to Run
**Notebook:**
```bash
jupyter notebook Titanic.ipynb
```
**Scripts:**
```bash
python main.py
```



## 📂 Dataset and Data Sources
- **File:** `titanic.csv` (891 passenger records, 12 attributes)
- **Used in:** Both Jupyter notebook & modular script pipelines

### 🗂 Schema Overview
| Column       | Type    | Missing % | Notes                               |
|--------------|---------|-----------|-------------------------------------|
| PassengerId  | Int     | 0.0%      | Unique ID                           |
| Survived     | Int     | 0.0%      | Target variable (0/1)               |
| Pclass       | Int     | 0.0%      | Passenger class (ordinal)           |
| Name         | String  | 0.0%      | High-cardinality text               |
| Sex          | String  | 0.0%      | Binary categorical                  |
| Age          | Float   | 19.9%     | Missing values, critical for modeling |
| SibSp        | Int     | 0.0%      | Siblings/spouses aboard              |
| Parch        | Int     | 0.0%      | Parents/children aboard              |
| Ticket       | String  | 0.0%      | Mixed alphanumeric                  |
| Fare         | Float   | 0.0%      | Skewed distribution                  |
| Cabin        | String  | 77.1%     | Sparse                              |
| Embarked     | String  | 0.2%      | Categorical with minimal missing    |

### 🔄 Data Loading
- **Scripts:** via `read_data('titanic.csv')` from `my_preprocessing.py`
- **Notebook:** direct `pd.read_csv('titanic.csv')`

### 🔧 Feature Processing
| Feature Type        | Columns                 | Processing Functions         |
|---------------------|-------------------------|------------------------------|
| Numerical           | Age, Fare               | `scale_columns()`, `check_outliers()` |
| Ordinal Categorical | Pclass                   | `encode_columns()`           |
| Binary Categorical  | Sex, Survived            | `encode_columns()`           |
| Nominal Categorical | Embarked                 | `encode_columns()`           |
| High Cardinality    | Name, Ticket, Cabin      | Feature extraction/exclusion |
| Identifier          | PassengerId              | Index usage                  |




## ⚙️ Processing Approaches
The repository provides **two main preprocessing approaches**, each for different use cases:

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
| Aspect             | Notebook            | Modular Scripts      |
|--------------------|---------------------|----------------------|
| Primary Goal       | End-to-end ML       | Data quality & reuse |
| Reusability        | Low                 | High                 |
| Visuals            | Inline only         | Saved to files       |
| Data Quality Focus | Basic               | Extensive            |
| Main Output        | `submission.csv`    | Logs + plots         |

### 🛠 Key Modular Functions
- **Data Quality:** `read_data()`, `check_types()`, `check_nulls()`, `check_duplicated()`
- **Processing:** `check_outliers()`, `visual()`, `split_data()`, `scale_columns()`, `encode_columns()`


## 📓 Jupyter Notebook Pipeline
Implemented in `Titanic.ipynb`, this pipeline provides a **complete end-to-end ML workflow** from raw data to prediction file generation.

### 🔄 Workflow Stages
1. **Data Loading & Setup:** Load `titanic.csv` and perform initial exploration.
2. **Integrated Cleaning & Preprocessing:** Handle missing values, feature engineering, and transformations directly in notebook cells.
3. **Model Training & Evaluation:** Train a Logistic Regression model, evaluate results immediately.
4. **Prediction Generation:** Create `submission.csv` formatted for Kaggle submission.

### 📤 Output
| File            | Description |
|-----------------|-------------|
| `submission.csv` | PassengerId + Survived predictions for test set |

### ✅ Advantages
- **Interactive:** Step-by-step execution with inline visuals.
- **Educational:** Shows the full process clearly.
- **Self-contained:** All logic in one file.
- **Reproducible:** Controlled environment for consistent results.

### ⚠ Limitations
- Lower reusability compared to modular scripts.
- Less comprehensive in data quality assessment.




## Modular Script Pipeline

The **Modular Script Pipeline** provides a reusable, production-ready approach for Titanic dataset preprocessing, built with two main components:

- **main.py** → Orchestrates the workflow (logging, plot saving, directory management, function calls).
- **my_preprocessing.py** → Library of preprocessing functions (data quality checks, visualizations, feature engineering).

### Key Features
- **Separation of Concerns** → Clear split between orchestration logic and processing functions.
- **Comprehensive Logging** → All print outputs redirected to `output.txt`.
- **Visualization Management** → Plots saved in a dedicated `plots/` directory.
- **Function Design Patterns**:
  - Input validation for safety.
  - Non-destructive transformations (copy before modify).
  - Flexible parameters (supports OneHotEncoding & Label Encoding).
  - Automatic plot generation & saving.

### Advantages
- **Reusability** → Functions can be imported in other projects.
- **Maintainability** → Easy to update individual steps.
- **Testability** → Each function has a single responsibility.
- **Flexibility** → Multiple encoding strategies.
- **Observability** → Detailed logs and visual outputs.
- **Extensibility** → Add new functions without refactoring.

This pipeline differs from the **Jupyter Notebook Pipeline** by focusing on batch processing, automation, and structured code ready for deployment.



# Core Components 

## Overview
This repository contains the core modules for preprocessing Titanic dataset using a **modular Python script approach** (`main.py` and `my_preprocessing.py`). For the full Jupyter notebook pipeline, see **Jupyter Notebook Pipeline**.

## Dataset & Sources
- **CSV file:** `titanic.csv`
- **Source Files:**
  - `main.py`
  - `my_preprocessing.py`

## Core Components
### Function Overview (`my_preprocessing.py`)
| Function | Purpose | Input | Output |
|----------|---------|-------|--------|
| `read_data` | Load CSV and preview | File path | DataFrame |
| `check_types` | Analyze types & unique values | DataFrame | Summary DataFrame |
| `check_nulls` | Count nulls and ratios | DataFrame | Summary DataFrame |
| `check_duplicated` | Remove duplicates | DataFrame | Modified DataFrame |
| `check_outliers` | Detect & cap outliers | DataFrame | Modified DataFrame |
| `visual` | Generate plots | DataFrame | Plot files |
| `split_data` | Split features & target | DataFrame, target col | X, y tuple |
| `scale_columns` | Scale numeric columns | DataFrame, columns | Scaled DataFrame |
| `encode_columns` | Encode categorical cols | DataFrame, cols, type | Encoded DataFrame |

### Pipeline Flow (`main.py`)
1. **Data Loading:** `read_data('titanic.csv')` + remove non-predictive columns
2. **Type Optimization:** Convert relevant columns to `category`
3. **Data Cleaning:** Handle missing values + remove duplicates
4. **Analysis:** Generate visualizations & detect outliers
5. **Feature Engineering:** Split data, scale numeric columns, encode categorical columns

### Integration & Validation
- **Integration:** Functions communicate via pandas DataFrames.
- **Validation Examples:**
  - Numeric columns checked before outlier processing
  - Encoding type validation raises errors for unsupported types
  - Ensure `plots/` directory exists before saving visuals

## System Architecture
- `main.py` orchestrates the workflow.
- `my_preprocessing.py` contains all preprocessing functions.

## Outputs
- Processed DataFrames
- Plots & visualizations
- Logs of transformations

---

**Sources:**  
`main.py` (lines 1–78), `my_preprocessing.py` (lines 1–206)



# Preprocessing Functions Module | DaiMagdy/Titanic-preprocessing

## Overview
Documentation for `my_preprocessing.py` module, containing reusable functions for Titanic dataset preprocessing:  
- Data quality assessment  
- Outlier detection  
- Feature engineering  
- Visualization generation  

For orchestration, see **Pipeline Orchestration**. For outputs, see **Data Visualizations**.

## Function Categories

### 1. Data Loading & Inspection
#### `read_data(path)`
- **Input:** CSV file path  
- **Output:** pandas DataFrame  
- **Details:**  
  - Uses `pd.read_csv()`  
  - Displays first 5 rows  

#### `check_types(df)`
- **Input:** DataFrame  
- **Output:** Summary DataFrame (Dtypes + Num_unique)  
- **Details:** Combines `df.dtypes` and `df.nunique()`  

### 2. Data Quality Assessment
#### `check_nulls(df)`
- **Output:** Summary of null counts & ratios  

#### `check_duplicated(df)`
- **Output:** Modified DataFrame with duplicates removed  
- **Details:** Logs before/after duplicate stats  

#### `check_outliers(df)`
- **Method:** IQR-based detection & capping  
- **Details:**  
  - Validates numeric columns  
  - Creates `plots/` if not exists  
  - Capping replaces outliers with boundary values  
  - Generates before/after boxplots  

### 3. Visualization Generation
#### `visual(df)`
- Generates histograms, KDE, count plots, and pie charts  
- Saves plots in `plots/` directory  
- Layout managed automatically for numerical & categorical plots  

### 4. Data Transformation
#### `split_data(df, target_col)`
- Splits features `X` and target `y`  
- Displays head of both  

#### `scale_columns(df, columns)`
- MinMax scales numeric columns  
- Displays before/after values  

#### `encode_columns(df, columns, encoding_type='OneHotEncoding')`
- Supports `OneHotEncoding` and `label`  
- Raises `ValueError` for unsupported types  
- Preserves original DataFrame  

## Function Integration
- All functions accept pandas DataFrame as input  
- Some modify DataFrames in-place (`check_duplicated`, `check_outliers`)  
- Others return new DataFrames (`scale_columns`, `encode_columns`)  
- Visualizations are saved to `plots/`  
- Console logs track processing steps  

**Sources:** `my_preprocessing.py` (lines 1–206)


# Pipeline Orchestration | DaiMagdy/Titanic-preprocessing

## Overview
`main.py` acts as the **central orchestrator** for the modular preprocessing pipeline, coordinating function calls from `my_preprocessing.py`, managing outputs, and generating multiple processed datasets.  

For individual function details, see **Preprocessing Functions Module**. For generated outputs, see **Generated Outputs and Results**.

## Orchestration Architecture
- Linear execution model  
- Imports and coordinates all preprocessing functions  
- Manages output streams and directories  

**Sources:** `main.py` (lines 1–2, 11, 14–15)

## Workflow Execution Sequence
The pipeline ensures **data quality checks precede transformations**, and all outputs are captured:

1. **Data Loading:** `read_data('titanic.csv')` → `df`  
2. **Column Removal:** Drop non-predictive columns → modified `df`  
3. **Type Conversion:** Convert categorical columns → modified `df`  
4. **Null Handling:** Fill missing values → modified `df`  
5. **Data Splitting:** `split_data(df, 'Survived')` → `X, y`  
6. **Scaling:** `scale_columns(df, ['Age', 'Fare'])` → `df_scaled`  
7. **OneHot Encoding:** `encode_columns(df, ['Sex', 'Embarked'])` → `df_encoded_onehot`  
8. **Label Encoding:** `encode_columns(df, ['Sex', 'Embarked'])` → `df_encoded_label`  
9. **Multiple Dataset Generation:** Creates different dataset versions for downstream tasks  

**Sources:** `main.py` (lines 11–78)

## Output Management System
- Redirects `sys.stdout` to `output.txt` for logging  
- Maintains separate outputs for plots and logs  
- Ensures `plots/` directory exists  
- Reopens output stream in append mode for subsequent logs  
- Closes output file after pipeline execution  

**Sources:** `main.py` (lines 10–11, 13–15, 58–61, 63, 71, 74–75, 78)

## Error Handling & Resource Management
- Validates file handles and directory existence  
- Ensures clean execution and proper log capture  
- Manages pipeline resources systematically

**Sources:** `main.py` (lines 10–15, 63, 78)



# Generated Outputs and Results | DaiMagdy/Titanic-preprocessing

## Overview
This module documents all **artifacts generated** by the Titanic preprocessing pipeline, including:  
- Processing logs (`output.txt`)  
- Data transformations  
- Visualizations (`plots/` directory)  
- Multiple dataset formats for machine learning  

For preprocessing function details, see **Core Components**. For orchestration, see **Pipeline Orchestration**.

## Processing Logs & Data Quality Metrics
- Logs capture every step in `output.txt`  
- Provides audit trail and data quality improvements  

### Data Transformation Summary
| Stage | Before | After | Details |
|-------|--------|-------|---------|
| Duplicate Removal | 889 rows | 773 rows | 116 duplicates removed |
| Missing Values | Age:177, Cabin:687, Embarked:2 | Reported | Ratios calculated |
| Data Types | Mixed | Optimized | String → category conversion |
| Feature Scaling | Raw numeric | Min-Max normalized | Applied to Age & Fare |
| Encoding | Strings | Numeric | OneHot & Label encoding applied |

### Scaling & Encoding Results
- **Min-Max Scaling:**  
  - Age: 22 → 0.271  
  - Fare: 7.25 → 0.014  
- **OneHot Encoding:** Creates binary columns (e.g., Sex_male, Embarked_S)  
- **Label Encoding:** Converts categories to numeric codes (male=1, female=2, S=1, C=2, Q=3)  

## Visualization System
- Generated via `visual()` function in `plots/` directory  
- Provides insights into distributions, categorical frequencies, and outlier effects  

| Type | Files | Purpose |
|------|-------|---------|
| Numerical Distributions | numerical_histograms.png, numerical_kde.png | Age & Fare distributions, skewness |
| Categorical Analysis | categorical_countplots.png, categorical_pieplots.png | Pclass, Sex, Embarked frequencies |
| Outlier Detection | outliers_before.png, outliers_after.png | IQR-based outlier capping |

## Data Quality Improvements
- **Duplicate Removal:** `check_duplicated()`  
- **Missing Value Reporting:**  
  - Age: 177 (19.9%)  
  - Cabin: 687 (77.1%)  
  - Embarked: 2 (0.2%)  

## Multiple Output Formats
- **OneHot Encoded:** binary columns for categorical variables  
- **Label Encoded:** numeric codes for categorical variables  
- Provides flexibility for different ML models  

## Output File Organization
- Structured directories for logs, visualizations, and processed datasets  
- `output.txt` captures:  
  - Initial data overview  
  - Type conversion results  
  - Null value analysis  
  - Duplicate detection  
  - Feature splitting  
  - Scaling documentation  
  - Encoding results  

**Sources:** `output.txt` (lines 1–133), `plots/`


# Processing Logs and Data Transformations | DaiMagdy/Titanic-preprocessing

## Overview
This document summarizes **data quality improvements, transformations, and feature engineering** applied to the Titanic dataset, captured in `output.txt`.  

For visualizations, see **Data Visualizations**. For function details, see **Preprocessing Functions Module**.

## Data Quality Assessment & Cleaning
- **Initial dataset:** 891 records → **773 records** after duplicate removal  
- **Data type optimizations:** convert to categorical/numeric as appropriate  

| Column   | Missing Values | Ratio  | Data Type Optimization |
|----------|----------------|--------|----------------------|
| Age      | 177            | 19.9%  | float64 → numeric    |
| Cabin    | 687            | 77.1%  | object → categorical |
| Embarked | 2              | 0.2%   | object → categorical |
| Sex      | 0              | 0%     | object → categorical |
| Pclass   | 0              | 0%     | int64 → categorical  |

- **Duplicate removal:** reduces dataset by 13.3% while keeping integrity  

## Feature Engineering & Transformations
### Data Splitting
- `split_data()` separates target (`Survived`) from features → `X, y`  

### Numerical Feature Scaling
| Feature | Original Range | Scaled Range | Method        |
|---------|----------------|-------------|---------------|
| Age     | 22 - 38        | 0.271 - 0.472 | Min-Max Scaling |
| Fare    | 7.25 - 71.28   | 0.014 - 0.139 | Min-Max Scaling |

### Categorical Encoding
- **One-Hot Encoding:** creates binary columns for categories (e.g., Sex_male, Embarked_S)  
- **Label Encoding:** converts categories to numeric codes (e.g., male=1, female=2, S=1, C=2, Q=3)  

## Processing Log Structure
- Captures **systematic progression** of preprocessing steps  
- Shows **before/after samples** for each transformation  
- Supports **audit trail and reproducibility**  

### Data Quality Improvements Summary
| Metric                  | Original | Transformed | Improvement                        |
|-------------------------|---------|------------|-----------------------------------|
| Total Records           | 891     | 773        | 116 duplicates removed             |
| Data Types              | Mixed   | Optimized  | Reduced memory usage               |
| Feature Scaling         | Raw     | Normalized | ML algorithm compatibility         |
| Categorical Encoding    | Strings | Numeric    | Algorithm compatibility            |
| Missing Value Documentation | Undocumented | Comprehensive | Quality assessment |

**Sources:** `output.txt` (lines 1–133)


# Data Visualizations | DaiMagdy/Titanic-preprocessing

## Overview
The visualization system in the modular preprocessing pipeline (`my_preprocessing.py`) generates **exploratory data analysis charts** and **quality assessment plots** for numerical and categorical variables.  

For data transformations, see **Processing Logs and Data Transformations**.

## Visualization Types

### Numerical Data
| Type | File | Purpose | Generated By |
|------|------|---------|--------------|
| Histograms | numerical_histograms.png | Distribution analysis | `visual()` |
| KDE Plots | numerical_kde.png | Density estimation | `visual()` |
| Outlier Analysis (Before) | outliers_before.png | Pre-processing outliers | `check_outliers()` |
| Outlier Analysis (After) | outliers_after.png | Post-processing validation | `check_outliers()` |

### Categorical Data
| Type | File | Purpose | Generated By |
|------|------|---------|--------------|
| Count Plots | categorical_countplots.png | Frequency analysis | `visual()` |
| Pie Charts | categorical_pieplots.png | Proportional representation | `visual()` |

## Technical Implementation
- **Automatic column classification:**  
  - Numerical: `int64`, `float64`  
  - Categorical: `object`, `category`  
  - Target column excluded from feature visualizations  
- **Libraries used:** `matplotlib`, `seaborn`, `pandas`  
- **Integration:** visualizations reflect post-preprocessing state and complement logs in `output.txt`  

## File Organization & Naming
- **Format:** PNG, high-resolution  
- **Naming pattern:** `{datatype}_{plottype}.png`  
  - Numerical prefix: `numerical_`  
  - Categorical prefix: `categorical_`  
  - Plot types: `histograms`, `kde`, `countplots`, `pieplots`  
  - Special: `outliers_before.png`, `outliers_after.png`  
- **Layout:** Multi-subplot arrangements, consistent seaborn styling  

## Output Characteristics
- Covers **all variables**, both numerical & categorical  
- Includes **before/after outlier treatment**  
- Provides **distribution insights** (parametric & non-parametric)  
- Supports **frequency and proportion analysis** for categorical variables  

**Sources:** `my_preprocessing.py` (lines 1–200), `plots/`


# System Architecture & Technical Implementation | DaiMagdy/Titanic-preprocessing

## Overview
This document describes the technical design, library dependencies, data flow, and integration points of the Titanic preprocessing system.  

The system uses a **dual-architecture approach**:
- **Modular pipeline** (`main.py` + `my_preprocessing.py`) → structured logging & file artifacts  
- **Self-contained notebook** (`Titanic.ipynb`) → inline processing & direct ML predictions

## System Design Patterns
- **Modular architecture:** function-based pipeline with orchestrated sequence of preprocessing calls  
- **Self-contained:** notebook-based inline execution  
- Stateless functions: each preprocessing function operates independently, preserving original data

## Library Dependencies
| Library | Purpose | Usage Example |
|---------|--------|---------------|
| pandas | Data manipulation | `read_data()`, `check_types()`, `check_nulls()` |
| sklearn.preprocessing | Feature scaling | `scale_columns()` (MinMaxScaler) |
| category_encoders | Categorical encoding | `encode_columns()` (OneHot/Ordinal) |
| matplotlib.pyplot | Plot generation | `visual()`, `check_outliers()` |
| seaborn | Statistical visualization | `visual()` |

## Data Flow & Memory Management
- Functions return **new DataFrames** (e.g., `scale_columns`, `encode_columns`)  
- Some operations are in-place with explicit return (e.g., `check_duplicated`)  
- Copies used to preserve data integrity: `df.copy()`

## I/O & Artifact Generation
| Artifact Type | Function | File Pattern | Content |
|---------------|----------|--------------|---------|
| Analysis Log | Multiple | `output.txt` | Structured text analysis |
| Numerical Plots | `visual()` | `plots/numerical_*.png` | Histograms, KDE plots |
| Categorical Plots | `visual()` | `plots/categorical_*.png` | Count plots, pie charts |
| Outlier Analysis | `check_outliers()` | `plots/outliers_*.png` | Before/after boxplots |

## Function Interface Patterns
- **Data Analysis:** `DataFrame → DataFrame/Display`  
  - `check_types(df)`, `check_nulls(df)`, `check_duplicated(df)`  
- **Data Transformation:** `DataFrame + params → DataFrame`  
  - `scale_columns(df, columns)`, `encode_columns(df, columns, type)`  
  - `split_data(df, target_col) → X, y`

## Error Handling & Validation
- `check_outliers()` → validates numeric columns  
- `encode_columns()` → raises ValueError for unsupported types  
- `visual()` → dynamic column type detection  

## Extensibility
- Modular design allows **plugin-style extensions**:  
  - Add new analysis functions in `my_preprocessing.py`  
  - Extend `encode_columns()` with new encoding types  
  - Add or modify visualizations in `visual()`  
- Notebook approach allows **interactive analysis & model dev**

**Sources:** `main.py` (1–79), `my_preprocessing.py` (13–205), `Titanic.ipynb` (1–2850)
