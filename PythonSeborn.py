#%%
import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()
# dist plot : Distribution of univariate variable (singel column of dataframe)
# This plot gives us a hsitogram and a line called KDE (Kernal density estimation).
sns.distplot(tips['total_bill'])

#%%
#we can remove it by passing KDE in distplot
sns.distplot(tips['total_bill'], kde=False)

#%%
# bins define the buckets on x-axis
sns.distplot(tips['total_bill'], kde=False, bins=30)

#%%
# joint plots : this is basicaaly combition of 2 dist plots (bi-variate).
# This gives us 3 figures in total. 2 univariate histograms , one for each variable and a combined plot which drwars one varibale in x-axis and other on y-axis.
# kind parameter defines the type of plot we use to display the combined plot.
# kind must be either 'scatter', 'reg', 'resid', 'kde', or 'hex'
sns.jointplot(tips['total_bill'],tips['tip'], kind='hex')
sns.jointplot(tips['total_bill'],tips['tip'], kind='reg')
sns.jointplot(tips['total_bill'],tips['tip'], kind='kde')

#%%
# Pair Plot : This is gonna show pair wise relationship across full dataframe
# Hue parameter will define the categorical column in the plot.
# Palette are some color palette already defined in matplotlib. We will discuss them later.
sns.pairplot(tips,hue='sex', palette='coolwarm')

#%%
# Rug plots is very simple and is univariate like dist plots.
# However, they just draw a dash on x-axis for each data point.
# Relation between dist and rug plot can be explained as (Height of histogram in dist plot is actally the number of dashed in rug plot for specified bin)
sns.rugplot(tips['total_bill'])
sns.kdeplot(tips['total_bill'])
# KDE stands for Kernel Density Estimation. It is derieved from rug plot.
# If we draw a normal distribution with each rug plot data point at the center and sum all of them up, we will come to KDE.

#%%
##-------------Plotting Categorical Data-----------------------------------##
import seaborn as sns
import numpy as np
tips = sns.load_dataset('tips')
tips.head()
# Bar plot takes and x arguement of categorical type and y arguement of numerical type.
# estimatoe is a aggregate function on which the numerical column will be aggregated and shown with respect of categorical data.
# So in short this is same as average (default estimator, you can specify any others or even can define your own) total bill group by gender.
sns.barplot(data=tips, x='sex', y='total_bill', estimator=np.std)

# Count plot just counts the occurence of each value of categorical data passed.
# It takes only x argement as y axis will show the count.
sns.countplot(data=tips, x='sex')

#%%
# Box Plot : x is categorical and y should be numerical,data will hold dataframe.

sns.boxplot(data=tips,x='day',y='total_bill')

# Violin Plot
