#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_911 = pd.read_csv(r'C:\Users\pankaj.sanwal\Desktop\PythonStuff\Python-Data-Science-and-Machine-Learning-Bootcamp\Python-Data-Science-and-Machine-Learning-Bootcamp\Data-Capstone-Projects\911.csv')
data_911.info()
data_911.head()

#%%
# Top 5 Zip Codes for 911 calls
print(data_911['zip'].value_counts().head())

#%%
# Top 5 town ships for 911 calls
print(data_911['twp'].value_counts().head())

#%%
# Unique Title counts
print(data_911['title'].unique())

#%%
# Unique Title counts
print(data_911['title'].nunique())

#%%
# Adding new column and putting reason/departments info from title column into new column.
data_911['reason'] = data_911['title'].apply(lambda x:x.split(':')[0])

#%%
# Most Common reason
print(data_911['reason'].value_counts().head())

#%%
# Plotting a count plot based on reasons
sns.countplot(data=data_911, x='reason')
plt.show()

#%%
# datatype of timestamp values
print(type(data_911['timeStamp'][0]))

#%%
# Convert the data type from str to datetime
data_911['timeStamp'] = data_911['timeStamp'].apply(pd.to_datetime)
print(type(data_911['timeStamp'][0]))

#%%
# Adding Hour, Month, day Of Week column
data_911['hour'] = data_911['timeStamp'].apply(lambda x:x.hour)
data_911['month'] = data_911['timeStamp'].apply(lambda x:x.month)
data_911['dayofweek'] = data_911['timeStamp'].apply(lambda x:x.dayofweek)

#%%
# Dictionary to map day of week to string name of day
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
data_911['dayofweek_str'] = data_911['dayofweek'].apply(lambda x:dmap[x])

#%%
# Count plot for Day of Week column with Hue as reason column
sns.countplot(x='dayofweek_str',data=data_911, hue='reason')
plt.show()

#%%
# Count plot for month column with Hue as reason column
sns.countplot(x='month',data=data_911, hue='reason')
plt.show()

#%%
# Some months are missing from the above plot. Now we will plot a simple line plot which might fill the missing months in x axis.
data_911_monthgrp = data_911.groupby('month')
data_911_monthgrp_reset = data_911_monthgrp.count().reset_index()
sns.lineplot(x='month', y='timeStamp', data=data_911_monthgrp_reset)

#%%
data_911_monthgrp_reset.head()
sns.lmplot(x='month',y='twp',data=data_911_monthgrp_reset)

#%%
# New Column Date
data_911['date'] = data_911['timeStamp'].apply(lambda x:x.date())
sns.countplot(x=data_911['date'],data=data_911)

#%%
date_grp_date = data_911.groupby('date')
date_grp_date.head()
date_count_date = date_grp_date.count()
date_count_date = date_count_date.reset_index()
#date_count_date.head()
sns.lineplot(data=date_count_date, x=date_count_date['date'], y=date_count_date['timeStamp'])

#%%
fg = sns.FacetGrid(data=data_911,col='reason')
fg.map(plt.hist,'dayofweek')

#%%
data_911.pivot(index='dayofweek_str',columns='hour')

