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
import seaborn as sns
import numpy as np
tips = sns.load_dataset('tips')
tips.head()
# Box Plot : x is categorical and y should be numerical,data paremeter will hold dataframe.
# Box plot shows the quartiles of the dataset.
# Hue parameter adds another layer fo data to box plots.
sns.boxplot(data=tips,x='day',y='total_bill', hue='smoker')

#%%
# Violin Plot
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True)

#%%
# Strip Plot
sns.stripplot(x='day', y='total_bill',data=tips, jitter=True, hue='sex', split=True)

#%%
# SwarmPlot : Combination of scatter and Strip plot.
sns.violinplot(data=tips, x='day', y='total_bill')
sns.swarmplot(data=tips, x='day', y='total_bill', color='black')

#%%
#Factor Plot : They are most general form of all types of plot.
# It takes a kind arguement which defines the factor plot itself. in other words you can use any plot we have used before in king arguement.
sns.factorplot(data=tips, x='day', y='total_bill', kind='violin')

#---------------------Matrix Plots (Primarily heat maps)-----------------------
#%%
import seaborn as sns
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

# Heat maps are generally used to show data which is in form of matrices. values in the matrix will be assigned to a fragient scale and you can see the relatove change in datacells thru this graph.
# Matrices here means the data value in a cell should be related to index and column name.
# in Tips dataframe, index are just sequential numbers. To chnage this dataset into a meaningfull matrix we can use dataframe's corr() method.
tc = tips.corr()
sns.heatmap(tc)
fc = flights.corr()
sns.heatmap(fc)

# Annotation=True will annotate the actual numericall values in the cells
sns.heatmap(tc, annot=True)

# cmap takes a string arguement which represents the color map.
sns.heatmap(tc, annot=True, cmap='coolwarm')

#%%
flights.head()
fp = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(fp)

#%%
sns.heatmap(fp, cmap='coolwarm', linewidths=1, linecolor='white')

#%%
## Cluster Map : These plots actually cluster the information in the matrix based on similarity.
# They are basically the heat maps but clustered.
sns.clustermap(fp, cmap='coolwarm', standard_scale=1)

#%%
#---------------------GRIDS Plots---------------------
import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()

# Pair plot as we read earlier just plots every column in the dataset with every other column.
sns.pairplot(iris)

#%%
# Pair grid is similar to pairplot but user will have a lot more controls about the graph being retirned but for that you have to provide extra arguements.
sns.PairGrid(iris) # This will retrun empty plots
# This is how to use PairGrid
import matplotlib.pyplot as plt
f = sns.PairGrid(iris)
f.map_diag(sns.distplot)
f.map_upper(plt.scatter)
f.map_lower(sns.kdeplot)

#%%
# Facetgrid
fg = sns.FacetGrid(data=tips, row='time', col='smoker')
fg.map(plt.scatter, 'total_bill', 'tip')


#%%
#----------------------Regression Plots-------------------------
# lmplot shows a simple liner regression plots.
# if You want to take a third diemnsion then assign a categorial datatype to hue parameter.
# You can also set the markers and increase size of markers.
sns.lmplot(x='total_bill', y='tip', data=tips, hue='smoker', markers=['o','v'], scatter_kws={'s':100})

#%%
# Unlike hue col will force LM plot to draw 2 separate graps for separate class of categorical data.
# Now if you want to add a parameter further use row.
# Now if you still want to add another parameter ,. you can still use hue.
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time', hue='day')

#%%
#---------------------------Set Styles----------------------
sns.set_style() # Add tickets, chnage back ground colour. Check other options in documentation.
sns.despine() # Remoe the x axis and y axis lines.
# You can set the size in 2 ways. call plt.figure(figsize=()) before plotting any sns plot.
# Or you can pass size and aspect parameter in almost every sns plot.
sns.set_context() # It takes a context parameter like poster. if you still want bigger font then you can pass fontsize too.

#%%
#Palettes and colours. You can acually google the palette names for matplotlib.
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='seismic')