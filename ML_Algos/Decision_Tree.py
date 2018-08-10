#%%
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

#%%
df = pd.read_csv(r'C:\Users\pankaj.sanwal\Desktop\PythonStuff\Python-Data-Science-and-Machine-Learning-Bootcamp\Python-Data-Science-and-Machine-Learning-Bootcamp\Machine Learning Sections\Decision-Trees-and-Random-Forests\kyphosis.csv')
df.head()

#%%
sns.pairplot(data=df, hue='Kyphosis')

#%%
x = df.drop('Kyphosis',axis=1)
y= df['Kyphosis']
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3)

#%%
dcf = DecisionTreeClassifier()
dcf.fit(x_train,y_train)
dcf_predict = dcf.predict(x_test)

#%%
print(classification_report(y_test,dcf_predict))
print(confusion_matrix(y_test,dcf_predict))

#%%
rf = RandomForestClassifier(n_estimators=200)
rf.fit(x_train, y_train)
rf_predict = rf.predict(x_test)
print(classification_report(y_test,rf_predict))
print(confusion_matrix(y_test,rf_predict))

