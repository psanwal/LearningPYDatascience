#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_breast_cancer
#%%
Cancer = load_breast_cancer()
print(Cancer['DESCR'])
#%%
df = pd.DataFrame(Cancer['data'],columns=Cancer['feature_names'])
df.shape
#%%
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)
#%%
# PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)
#%%
x_pca.shape
#%%
plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=Cancer['target'])
#%%
pca.components_
#%%
sns.heatmap(pca.components_)