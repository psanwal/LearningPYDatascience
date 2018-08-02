# Logistic regression is a way to do classification of data about to which class it belongs.
# 1. If a lona will get default.
# 2. Diseases Diagonosis
# Above classifications are binary in nature.
# Logistic regression plot vary between 0 and 1 with probability on Y axis.
# Sigmoid (aka logitc) functions takes any value and output value between 0 and 1.
# 0.5 or 50% probability acts here as cutoff point. If probability is less than .5 then point belongs to class 0 and vice versa.
# Once we train our classification model, we can evaluate them using confusion matrix.

#%%
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

#%%
df = pd.read_csv(r'C:\Users\pankaj.sanwal\Desktop\PythonStuff\Python-Data-Science-and-Machine-Learning-Bootcamp\Python-Data-Science-and-Machine-Learning-Bootcamp\Machine Learning Sections\Logistic-Regression\titanic_train.csv')
df.head()

#%%
df['Pclass'].unique()
df['Pclass'].nunique()
df['Pclass'].value_counts()

#%%
# df.isnull() will return a boolean dataframe with True only at place where value is nan.
# Plotting heatmap based on boolean dataframe can show which data is missing.
sns.heatmap(data=df.isnull(), yticklabels=False, cbar=False)

#%%
# Generating dummy columns for Categorical values.
is_male = pd.get_dummies(df['Sex'], drop_first=True)
embarked = pd.get_dummies(df['Embarked'], drop_first=True)
df = pd.concat([df , is_male, embarked], axis=1)
# Dropping columns which would not add any value to our model.
df.drop(['Sex','Embarked','Name','Ticket','Cabin','PassengerId'], axis=1, inplace=True)

#%%
df.head()
mean_age = pd.DataFrame(df.groupby(['Pclass'])['Age'].mean())
df['Age'].apply(lambda x : x if x.isnull() else 1)


