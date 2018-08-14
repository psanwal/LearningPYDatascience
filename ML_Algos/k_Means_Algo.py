#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

#%%
## Generating fake data
## Result is actually a tuple.
## First elemt of tuple is a list of 200 list having 2 elements each (for 2 features) 
data = make_blobs(n_samples=200,n_features=2,centers=4,cluster_std=1.8,random_state=101)

#%%
x = data[0][:,0]
#%%
y = data[0][:,1]
#%%
from sklearn.cluster import KMeans
kmean = KMeans(n_clusters=4)
kmean.fit(data[0]) 
#%%
kmean.cluster_centers_
#%%
kmean.labels_
#%%
sns.scatterplot(x,y,hue=data[1],cmap='rainbow')
#%%
sns.scatterplot(x,y,hue=kmean.labels_,cmap='rainbow')
