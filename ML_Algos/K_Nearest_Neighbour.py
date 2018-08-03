# K Nearest neighbour calculates distnace of every point from everyother point.
# Then arange it with accending order to find out nearest points.
# Not good for very large datasets.
# Not good for high dimensional data.
# Does not work good with categorical datatypes.

#%%
import pandas as pd
import seaborn as sns
import numpy as np

#%%
df = pd.read_csv(r'C:\Users\pankaj.sanwal\Desktop\PythonStuff\Python-Data-Science-and-Machine-Learning-Bootcamp\Python-Data-Science-and-Machine-Learning-Bootcamp\Machine Learning Sections\K-Nearest-Neighbors\Classified Data', index_col=0)
df.head()

#%%
from sklearn.preprocessing import StandardScaler
sca = StandardScaler()
sca.fit(df.drop('TARGET CLASS',axis=1))
scaled_features = sca.transform(df.drop('TARGET CLASS',axis=1))
scaled_features = pd.DataFrame(scaled_features,columns=df.columns[:-1])

#%%
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

xtrain, xtest, ytrain, ytest = train_test_split(scaled_features,df['TARGET CLASS'], test_size=0.3, random_state=101)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(xtrain, ytrain)
y_prediction = knn.predict(xtest)
print(classification_report(ytest,y_prediction))

#%%
error_rate=[]
for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(xtrain, ytrain)
    y_prediction = knn.predict(xtest)
    error = [1 if x[0] != x[1] else 0 for x in zip(ytest,y_prediction)]
    error_rate.append(np.mean(error))

#%%
sns.lineplot(y=error_rate,x=range(1,40))


