from my_preprocessing import read_data, check_types, check_nulls, check_duplicated
from my_preprocessing import check_outliers, visual, split_data, scale_columns, encode_columns
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys
import os


#output.txt
sys.stdout = open('output.txt', 'w')

#plots
if not os.path.exists('plots'):
    os.makedirs('plots')


#read data 
df = read_data('titanic.csv')
print("\nData Description:")
print(df.describe())
print("\nData Info:")
print(df.info())


#remove the unimportant cols
df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)


#check_datatypes
print("The original data")
print(check_types(df))

#convert some cols 
cols = ['Survived', 'Pclass', 'Sex', 'SibSp', 'Parch','Embarked']
df[cols] = df[cols].astype('category')

print("The data after converting")
print(check_types(df))


#check nulls
print("\nNull values")
print(check_nulls(df))

#handling nulls
df.dropna(subset=["Embarked"], inplace=True)
df.drop("Cabin", axis=1, inplace=True)
median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)


#check duplicated
check_duplicated(df)

#visualization
visual(df)
for i, fig in enumerate(plt.get_fignums(), start=1):
    plt.figure(fig)
    plt.savefig(f'plots/plot_{i}.png')
    plt.close()

sys.stdout = open('output.txt', 'a')


#data splitting
X, y = split_data(df, 'Survived')


#data scaling
df_scaled = scale_columns(df, ['Age', 'Fare'])

#data encoding
df_encoded_onehot = encode_columns(df, ['Sex', 'Embarked'], encoding_type='OneHotEncoding')
df_encoded_label = encode_columns(df, ['Sex', 'Embarked'], encoding_type='label')

#close output file
sys.stdout.close()
