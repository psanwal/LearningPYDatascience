#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.grid_search import GridSearchCV
import seaborn as sns
#%%
df = sns.load_dataset('iris')
df.head()
#%%
sns.pairplot(df,hue='species')
#%%
x = df.drop('species',axis=1)
y = df['species']
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.3)
#%%
svc = SVC()
svc.fit(xtrain,ytrain)
svc_predict = svc.predict(xtest)
#%%
print(confusion_matrix(ytest,svc_predict))
#%%
print(classification_report(ytest,svc_predict))
#%%
grid_param_dict = {'C':[0.1,1,10,100,1000],'gamma':[1,0.1,0.01,0.001,0.001]}
grid = GridSearchCV(SVC(),grid_param_dict,verbose=3)
grid.fit(xtrain,ytrain)
#%%
grid_predict = grid.predict(xtest)
#%%
print(confusion_matrix(ytest,grid_predict))
#%%
print(classification_report(ytest,grid_predict))
