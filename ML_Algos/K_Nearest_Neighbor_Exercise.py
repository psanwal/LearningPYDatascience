#%%
import pandas as pd
import seaborn as sns
import numpy as np

#%%
df = pd.read_csv(r'C:\Users\pankaj.sanwal\Desktop\PythonStuff\Python-Data-Science-and-Machine-Learning-Bootcamp\Python-Data-Science-and-Machine-Learning-Bootcamp\Machine Learning Sections\K-Nearest-Neighbors\KNN_Project_Data', index_col=0)
df.head()

#%%
df.reset_index(inplace=True)
df.head()

#%%
sns.pairplot(df)

#%%
from sklearn.preprocessing import StandardScaler
sca = StandardScaler()
sca.fit(df.drop('TARGET CLASS',axis=1))
scaler_features = sca.transform(df.drop('TARGET CLASS',axis=1))
scaler_features = pd.DataFrame(scaler_features, columns=df.drop('TARGET CLASS',axis=1).columns)
scaler_features.head()

#%%
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(scaler_features,df['TARGET CLASS'], test_size=0.3, random_state=101)

#%%
error_rate = []
for i in range(1,40):
    kne = KNeighborsClassifier(n_neighbors=i)
    kne.fit(xtrain,ytrain)
    pre_kne = kne.predict(xtest)
    error_rate.append(np.mean([1 if x[0] != x[1] else 0 for x in zip(ytest,pre_kne)]))

error_rate

#%%
sns.lineplot(x=range(1,40), y= error_rate)
