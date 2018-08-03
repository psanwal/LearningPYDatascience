#%%
import pandas as pd
df = pd.read_csv(r'C:\Users\pankaj.sanwal\Desktop\PythonStuff\Python-Data-Science-and-Machine-Learning-Bootcamp\Python-Data-Science-and-Machine-Learning-Bootcamp\Machine Learning Sections\Logistic-Regression\advertising.csv')
df.head()

#%%
import seaborn as sns
sns.heatmap(df.isnull(),yticklabels=False,cbar=False)

#%%
sns.pairplot(data=df)

#%%
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

#%%
x = df.drop(['Clicked on Ad', 'Timestamp','Ad Topic Line','City','Country'],axis=1)
y = df['Clicked on Ad']
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3,random_state = 101)

#%%
lor = LogisticRegression()
lor.fit(x_train, y_train)
prediction = lor.predict(x_test)

#%%
print(classification_report(y_test,prediction))
