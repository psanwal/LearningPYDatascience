#%%
import pandas as pd
import numpy as np
df = pd.read_csv(r'C:\Users\pankaj.sanwal\Desktop\PythonStuff\Python-Data-Science-and-Machine-Learning-Bootcamp\Python-Data-Science-and-Machine-Learning-Bootcamp\Machine Learning Sections\Decision-Trees-and-Random-Forests\loan_data.csv')
df.head(200)
#%%
import seaborn as sns
from matplotlib import pyplot as plt
plt.figure(figsize=(15,10))
#%%
sns.countplot(df['purpose'], hue=df['not.fully.paid'])
#%%
sns.countplot(df['not.fully.paid'])
#%%
sns.distplot(df[df['credit.policy']==1]['fico'],bins=30,kde=False,label='credit.policy=1')
sns.distplot(df[df['credit.policy']==0]['fico'],bins=30,kde=False,label='credit.policy=0')
plt.legend()
#%%
sns.distplot(df[df['not.fully.paid']==1]['fico'],bins=30,kde=False,label='not.fully.paid=1')
sns.distplot(df[df['not.fully.paid']==0]['fico'],bins=30,kde=False,label='not.fully.paid=0')
plt.legend()
#%%
sns.jointplot(df['fico'],df['int.rate'])
#%%
sns.lmplot(data=df,x='fico',y='int.rate',hue='credit.policy',col='not.fully.paid')
#%%
final_data = pd.get_dummies(data=df,columns=['purpose'],drop_first=True)
final_data.info()
#%%
from sklearn.model_selection import train_test_split
x=final_data.drop('not.fully.paid',axis=1)
y=final_data['not.fully.paid']
x_train,x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=101)
#%%
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)
dt_preditc = dt.predict(x_test)
#%%
print(classification_report(y_test,dt_preditc))
#%%
print(confusion_matrix(y_test,dt_preditc))
#%%
rf = RandomForestClassifier(n_estimators=200)
rf.fit(x_train,y_train)
rf_predict = rf.predict(x_test)
#%%
print(classification_report(y_test,rf_predict))
#%%
print(confusion_matrix(y_test,rf_predict))





