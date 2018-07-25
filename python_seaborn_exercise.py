#%%
import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')
titanic.head()

#%%
sns.jointplot(y='age', x='fare',data=titanic,)

#%%
sns.distplot(titanic['fare'], kde=False, color='pink')

#%%
sns.boxplot(x='class', y='age', data=titanic)

#%%
sns.violinplot(x='class', y='age', data=titanic,kind="scatter")

#%%
sns.stripplot(x='class', y='age', data=titanic)

#%%
sns.swarmplot(x='class', y='age', data=titanic)

#%%
sns.countplot(titanic['sex'])

#%%
titanic_corr = titanic.corr()
sns.heatmap(titanic_corr)

#%%
fg = sns.FacetGrid(data=titanic, col='sex')
fg.map(plt.hist,'age')