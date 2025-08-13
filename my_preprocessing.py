import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import category_encoders as ce
from category_encoders import OneHotEncoder
from IPython.display import display
import os



def read_data(path):
    df = pd.read_csv(path)
    display(df.head())
    return df



def check_types(df):
    dtypes = df.dtypes
    n_uniq = df.nunique()
    return pd.DataFrame({'Dtypes': dtypes, 'Num_unique' : n_uniq}).T



def check_nulls(df):
    null = df.isnull().sum()
    ratio = (null/df.shape[0])*100 
    return pd.DataFrame({'Null_Sum': null, 'Ratio': ratio}).T



def check_duplicated(df):
    print("Before removing duplicated rows:")
    print(f"Duplicated rows count: {df.duplicated().sum()}")
    print(f"Total rows: {len(df)}")

    df.drop_duplicates(inplace=True)

    print("\nAfter removing duplicated rows:")
    print(f"Duplicated rows count: {df.duplicated().sum()}")
    print(f"Total rows: {len(df)}")
    
    return df

 
 

def check_outliers(df):
    num_cols = df.select_dtypes('number').columns
    print("Numeric columns:", num_cols.tolist())

    if len(num_cols) == 0:
        print("Warning: No numeric columns found in dataframe!")
        return

    n = len(num_cols)


    if not os.path.exists('plots'):
        os.makedirs('plots')


    print("Plotting before handling outliers...")
    plt.figure(figsize=(8, max(n*2, 6)))
    for i, col in enumerate(num_cols):
        print(f"Plotting before boxplot for column: {col}")
        plt.subplot(n, 1, i+1)
        sns.boxplot(df[col], orient='h')
        plt.title(f'Before Handling Outliers: {col}')
    plt.tight_layout()
    plt.savefig('plots/outliers_before.png')
    plt.close()

    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_fence = Q1 - 1.5 * IQR
        upper_fence = Q3 + 1.5 * IQR

        df.loc[df[col] < lower_fence, col] = lower_fence
        df.loc[df[col] > upper_fence, col] = upper_fence

    print("Plotting after handling outliers...")
    plt.figure(figsize=(8, max(n*2, 6)))
    for i, col in enumerate(num_cols):
        print(f"Plotting after boxplot for column: {col}")
        plt.subplot(n, 1, i+1)
        sns.boxplot(df[col], orient='h')
        plt.title(f'After Handling Outliers: {col}')
    plt.tight_layout()
    plt.savefig('plots/outliers_after.png')
    plt.close()


def visual(df):
    num_cols = df.select_dtypes('number').columns
    cat_cols = df.select_dtypes('category').columns

    #Numerical features visualization
    # Histogram
    plt.figure(figsize=(15, 3))
    for i, col in enumerate(num_cols):
        plt.subplot(1, len(num_cols), i+1)
        plt.hist(df[col], edgecolor='black')
        plt.title(f'{col} Histogram')
    plt.tight_layout()
    plt.savefig('plots/numerical_histograms.png')
    plt.close()

    # KDE plot
    plt.figure(figsize=(15, 3))
    for i, col in enumerate(num_cols):
        plt.subplot(1, len(num_cols), i+1)
        sns.kdeplot(df[col], fill=True)
        plt.title(f'{col} KDE')
    plt.tight_layout()
    plt.savefig('plots/numerical_kde.png')
    plt.close()


    #Categorical features visualization
    #count plot
    rows = (len(cat_cols) // 3) + 1
    plt.figure(figsize = (14, 4 * rows))
    for i, col in enumerate(cat_cols):
        plt.subplot(rows, 3, i+1)
        sns.countplot(x=col, data=df)
        plt.title(f'{col} Distribution Count plot')
    plt.tight_layout()
    plt.tight_layout()
    plt.savefig('plots/categorical_countplots.png')
    plt.close()


    # Pie plot
    plt.figure(figsize=(9, 4))
    rows = (len(cat_cols) // 3) + 1
    cols = 3
    for i, col in enumerate(cat_cols):
        plt.subplot(rows, cols, i+1)
        unique = df[col].value_counts()
        count = unique.values
        categories = unique.index
        plt.pie(count, labels=categories, startangle=140, autopct='%1.1f%%')
        plt.title(f'{col} Pie plot')

    plt.subplots_adjust(hspace=0.8, wspace=0.3)
    plt.savefig('plots/categorical_pieplots.png')
    plt.close()

def split_data(df, target_col):
    X = df.drop(columns=[target_col])
    y = df[target_col]

    print("X values:")
    print(X.head())
    print("\n Y values:")
    print(y.head())

    return X, y



def scale_columns(df, columns):
    print("Before scaling:")
    print(df[columns].head())

    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[columns] = scaler.fit_transform(df[columns])

    print("\nAfter scaling:")
    print(df_scaled[columns].head())
    
    return df_scaled




def encode_columns(df, columns, encoding_type='OneHotEncoding'):
    print("Before encoding:")
    print(df[columns].head())

    df_encoded = df.copy()
    
    if encoding_type == 'OneHotEncoding':
        encoder = ce.OneHotEncoder(cols=columns, use_cat_names=True)
        df_encoded = encoder.fit_transform(df_encoded)
        
    elif encoding_type == 'label':
        encoder = ce.OrdinalEncoder(cols=columns)
        df_encoded = encoder.fit_transform(df_encoded)
        
    else:
        raise ValueError(f"Unsupported encoding type: {encoding_type}")
    
    
    print("\nAfter encoding:")
    print(df_encoded.head())

    return df_encoded
