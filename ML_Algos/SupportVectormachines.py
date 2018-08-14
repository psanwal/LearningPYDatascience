#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
cancer.keys()

#%%
df_features = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
df_features

#%%
cancer['target']

#%%
from sklearn.model_selection import train_test_split
x = df_features
y = cancer['target']
xtrain, xtest,ytrain, ytest = train_test_split(x,y,test_size=0.3, random_state=101)

#%%
from sklearn.svm import SVC
svc = SVC()
svc.fit(xtrain,ytrain)

#%%
from sklearn.metrics import classification_report, confusion_matrix
predict_y = svc.predict(xtest)

#%%
y.shape
#%%
print(confusion_matrix(ytest,predict_y))
#%%
print(classification_report(ytest,predict_y))
#%%
from sklearn.grid_search import GridSearchCV
param_dict = {'C':[0.1,1,10,100,1000],'gamma':[1,0.1,0.01,0.001,0.0001]}
grid = GridSearchCV(SVC(),param_dict,verbose=3)
grid.fit(xtrain,ytrain)
#%%
grid.best_estimator_
#%%
grid.best_score_
#%%
grid.best_params_
#%%
grid_predict = grid.predict(xtest)
#%%
print(confusion_matrix(ytest,grid_predict))
#%%
print(classification_report(ytest,grid_predict))

