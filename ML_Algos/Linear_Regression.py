#%%
import pandas as pd
import numpy as np
import seaborn as sns

#%%
df = pd.read_csv(r'C:\Users\pankaj.sanwal\Desktop\PythonStuff\Python-Data-Science-and-Machine-Learning-Bootcamp\Python-Data-Science-and-Machine-Learning-Bootcamp\Machine Learning Sections\Linear-Regression\USA_Housing.csv')
df.info()
df.columns

#%%
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
sns.pairplot(df)

#%%
# Split Data into X array and Y array. X is data we are givn with, Y is the value we want to predict.
x = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.4, random_state=101)

#%%
# Instantiating linear model object
lm = LinearRegression()
lm.fit(x_train, y_train)

#%%
# Checking Coefficients and intercept
lm.coef_
lm.intercept_

#%%
# Putting coefficient in a data frame.
df_coeff = pd.DataFrame(lm.coef_,x.columns,columns=['Coefficients'])
df_coeff

#%%
# Predictions
predictions_y = lm.predict(x_test)
predictions_y

#%%
# If scatter plot appers to be alliged roughly in a straight line the your prediction us more accurate.
sns.scatterplot(y_test,predictions_y)

#%%
# Plotting the histogram of residuals. Residuals is the vertical distnace or delta between the predicted value and actual value.
# If the plot comes out to be normally distributed then it means predictions are very good.
# Residuals = (y_test-predictions_y)
# if the dist plot is not normal then we may have to go back and analyze if linear regression is the correct choice, we might to change the estimator algo.
sns.distplot(y_test-predictions_y)

#%%
# Regression evaluaton matrix
# There are 3 most common ones
# 1. Mean absolute error (MAE).
# 2. Mean of squarred errors (MSE).
# 3. Squarroot of the mean of squared errors (RMSE).
# We would want to minimise all these errors.
from sklearn import metrics
metrics.mean_absolute_error(y_test, predictions_y)

#%%
metrics.mean_squared_error(y_test, predictions_y)

#%%
np.sqrt(metrics.mean_squared_error(y_test, predictions_y))

# -------------Bias Variance Tradeoff---------------------
