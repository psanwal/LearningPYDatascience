#%%
# Importing useful libs
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

#%%
# Reading Data
df = pd.read_csv(r'C:\Users\pankaj.sanwal\Desktop\PythonStuff\Python-Data-Science-and-Machine-Learning-Bootcamp\Python-Data-Science-and-Machine-Learning-Bootcamp\Machine Learning Sections\Linear-Regression\Ecommerce Customers')
df.head()

#%%
df.columns

#%%
df.describe()

#%%
sns.pairplot(df)

#%%
# Split Data into train and test sets
y = df['Yearly Amount Spent']
x = df[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
x_train,x_test, y_train,y_test = train_test_split(x,y,test_size=0.3 , random_state=101)

#%%
# Training the modle based on training data
lm = LinearRegression()
lm.fit(x_train, y_train)

#%%
# Chekcing Coefficient and intercept
df_coeff = pd.DataFrame(lm.coef_,index=x.columns,columns=['Coefficients'])
df_coeff

#%%
lm.intercept_

#%%
# Predicting lable on test data
y_prediction = lm.predict(x_test)
y_residuals = y_prediction - y_test

#%%
# Plotting residuals
sns.distplot(y_residuals)

#%%
# Cheking metrices
MAE_error = metrics.mean_absolute_error(y_test,y_prediction)
MSE_error = metrics.mean_squared_error(y_test,y_prediction)
RMSE_error = np.sqrt(MSE_error)

#%%
# Calculating R2 value. Our model explains about 99% of the variance, which is very good.
RSquare = metrics.explained_variance_score(y_test,y_prediction)
RSquare
