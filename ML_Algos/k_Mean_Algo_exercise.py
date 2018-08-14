#%%
import pandas as pd
import numpy as np
import seaborn as sns
#%%
df = pd.read_csv(r'C:\Users\pankaj.sanwal\Desktop\PythonStuff\Python-Data-Science-and-Machine-Learning-Bootcamp\Python-Data-Science-and-Machine-Learning-Bootcamp\Machine Learning Sections\K-Means-Clustering\College_Data')
df.set_index('Unnamed: 0',inplace=True)
df.head()
#%%
sns.scatterplot(df['Grad.Rate'],df['Room.Board'],hue=df['Private'])
#%%
sns.scatterplot(df['F.Undergrad'],df['Outstate'],hue=df['Private'])
#%%
fg1 = sns.FacetGrid(df,hue='Private')
fg1.map(plt.hist,'Outstate')
#%%
fg2 = sns.FacetGrid(df,hue='Private')
fg2.map(plt.hist,'Grad.Rate')
#%%
#df[df['Grad.Rate']>100]
df['Grad.Rate']['Cazenovia College'] = 100
#%%
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix
km = KMeans(n_clusters=2)
km.fit(df.drop('Private',axis=1))
#%%
km.cluster_centers_
#%%
km.labels_
#%%
print(classification_report(df['Private'].apply(lambda x:1 if x=='Yes' else 0),pd.DataFrame(km.labels_)))
#%%
print(confusion_matrix(df['Private'].apply(lambda x:1 if x=='Yes' else 0),pd.DataFrame(km.labels_)))


