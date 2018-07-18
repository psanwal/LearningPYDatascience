##--------------Series-----------------
## Its same as numpy arrays and infact built on top of numpy array object.
## We can access series elements using elements unlike numpy arrays.

import numpy as np
import pandas as pd

lables = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20,'c':30}

print(pd.Series(data = my_data))
##Pass a list
print(pd.Series(data = my_data, index=lables)) 

##Pass numpy array
pd.Series(arr)
##pass a python dictionary 
pd.Series(d) 

## Pandas Series can hold any datatypes, even system defined functions like len, print etc.
## Series index will mostly be either string or interger.
ser1 = pd.Series([1,2,3,4],['USA', 'USSR', 'Germany', 'France'])
ser2 = pd.Series([1,2,5,4],['USA', 'USSR', 'Germany', 'Japan'])

## Very basic operations like addition of 2 series are generrally based on indexes of series.
## Like in ser1 and ser2 abaove, ser1 + ser2 will add interger values for which index is same.
## USA will become 2 , USSR will beocome 4 but since France and Jaapan donot match, they both will appear in resulting series but value will be nan.
ser1 + ser2

##---------------DataFrames--------------------
from numpy.random import randn
np.random.seed(101)

## Random numbers work by starting with a number (the seed), multiplying it by a large number, then taking modulo of that product.
## The resulting number is then used as the seed to generate the next "random" number.
## When you set the seed (every time), it does the same thing every time, giving you the same numbers.

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

## Accessing the columns in dataframe
print(df['W']) ## This will retrun a series (column W) as dataframe is just collection of series which uses same indexes.
print(df[['X','Y']]) ## This will retun a dataframe (column W and X).

## Accesing the rows and subset of rows and columns in dataframes.
print(df.loc['A']) ## This will return a single row with index A, it will be of type series, same as when we selected a column from dataframe.
print(df.iloc[0]) ## This will again retrun the first row but as you can see by usig iloc we can use index too to select rows in a dataframe.
print(df.loc['B','Y']) ## this will retrun value at Row B and Column Y.
print(df.loc[['A','B'],['W','X']]) ## This will return values in rows A and B and Columns W and X.

##Adding a new column to dataframe.
df['new'] = df['W'] + df['Y']
print(df)

## Removing a Column
df.drop('new', axis=1)
print(df)

## Removing a row
df.drop('E',axis=0)
print(df)

## To make changes like drop permanenet we have to provide inplace = TRUE
df.drop('A', axis=0,inplace=True)
print(df)

# Boolean dataframe works eactly same as boolean numpy array.
# below will return a boolean array with TRUE and FALSE based upo which field meets the condition.
print(df > 0)

# Now as we did in numpy arrays, if we pass this to df itself, a dataframe will be retruined,
# with values corresponding to True values and nan corresponding to FALSE value.
print(df[df>0])

# most probably we dont want to se these nan values. therefore we generally dont pass whole dataframe, 
# but only a column (pandas series). This will remove the row which has FALSE value in the series and 
# will retun rest rows. Basically it removed the nan values. Will remove row C from the output as in column, 
# Value in row C is actually less then 0.
print(df[df['W']>0]) # This will retun a dataframe.
print(df[df['W']<0]) # This will retun a single row but it will still be a dataframe.

# Conditional selection in dataframe always returns a dataframe, which means you can cascade operations on the retrun results of selection
# operation. below will return column X from the result of the dataframe selection operation.
print(df[df['W']>0]['X']) # This will retun a Series.
print(df[df['W']>0][['X','Y']]) # This will retun a DataFrame.

# Conditional formating can be done with 2 or more conditions as well. Keep in mind that using AND instead of & will lead to an error.
# It is because AND operator can only compare 2 discrete boolean values. When a series of boolean values are passed, operator gets confused.
# Therefore when you want to use AND for series of boolean values, use & instaed. Similarly in place of OR use | 'Pipe' symbol.
print(df[(df['W']>0) & (df['Y']>0)])

#---------------Index---------------------
#Reset the index back to default index which is a range 0,1,2,3...etc. this way older inxed will become a column of a dataframe with column name as 'index'.
print(df.reset_index())

# If you want a column to be new index of your dataframe, use set_index().but remember this will overwrite the existing index unlike
# reset_index() which add the older index as a new column in dataframe.
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
newindex = 'pan pra bha vin bhu'.split()
print(newindex)
df['New index'] = newindex
df1 = df.set_index('New index')
print(df1)

#-----------Multi Index and index Hierarchy------------------
outside = 'PQRS PQRS PQRS PQRS ABCD ABCD ABCD ABCD WXYZ WXYZ WXYZ WXYZ'.split()
middle = 'PQ PQ RS RS AB AB CD CD WX WX YZ YZ'.split()
inner = 'P Q R S A B C D W X Y Z'.split()
multilevel = list(zip(outside, middle, inner))
print(multilevel)
multi_level_index = pd.MultiIndex.from_tuples(multilevel)
print(multi_level_index)
multilevel_df = pd.DataFrame(randn(12,4), multi_level_index,['pan','pra','bha','bhu'])
print(multilevel_df)

print(multilevel_df.index.names)
multilevel_df.index.names = ['Groups','Classes', 'Indivisual']
print(multilevel_df)

print(multilevel_df.loc['PQRS'])
print(multilevel_df.loc['PQRS'].loc['RS'])

print(multilevel_df.loc['PQRS'].loc['RS'].loc['R']['pan'])

#-------------CrossSection--------------------
# This will only work with multilevel index.

print(multilevel_df.xs('R',level = 'Indivisual'))


#-------------Missing Data----------------------
# In Pandas when you read data from different sources Pandas fill empty values with NaN. DropNan and FillNaN are 2 methods which can
# be helpfull in such scenario.

df1 = pd.DataFrame({'A':[1,2,np.nan],'B':[1,np.nan,np.nan],'C':[1,2,3]})
print(df1)
print(df1.dropna()) # This will drop any row which has one or more NaN value. So only row 0 will be left.
print(df1.dropna(axis=1)) # This will do same as above except this time columns will be dropped. Only column C will be left.
print(df1.dropna(thresh=2)) # This will not drop rows which have atleast 2 non NaN values. Any row with less than 2 non-NaN values will be dropped.

print(df1.fillna('pan')) # Fillna will help to fill the NaN values with whatever you want.
print(df1.fillna(df1['A'].mean())) # Here nan Values are replaced by mean of a series obtained by selecting a column from dataframe.
print(df1['A'].fillna(df1['A'].mean())) # We can also use fillna and dropna with series obtained by selection of dataframes.

#----------------Group By------------------------------

outer = ['Amazon','Amazon','Amazon','Amazon','Amazon','Amazon','Amazon','Amazon','Google','Google','Google','Google','Google','Google','Google','Google','Facebook','Facebook','Facebook','Facebook','Facebook','Facebook','Facebook','Facebook','Yahoo','Yahoo','Yahoo','Yahoo','Yahoo','Yahoo','Yahoo','Yahoo']
middle = ['HR','HR','Tech','Tech','Admin','Admin','IT','IT','HR','HR','Tech','Tech','Admin','Admin','IT','IT','HR','HR','Tech','Tech','Admin','Admin','IT','IT','HR','HR','Tech','Tech','Admin','Admin','IT','IT']
inner = ['Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure','Earning','Expenditure']

mlindexlist = list(zip(outer,middle,inner))
mlindex = pd.MultiIndex.from_tuples(mlindexlist)
print(np.random.randint(10,340,32))
df2 = pd.DataFrame(np.random.randint(10,340,(32,4)),mlindex,['Jan','Feb','Mar','Apr'])
print(df2)
print(df2.transpose())
df2.index.names = ['Company','Department','KPI']
print(df2)

print(df2.groupby('KPI').sum())
print(df2.groupby('KPI').sum()['Jan'])
print(df2.groupby('KPI').sum()['Jan'].loc['Earning'])

print(df2.groupby('Department').sum())
print(df2.groupby('Department').sum()['Jan'])
print(df2.groupby('Department').sum()['Jan'].loc['HR'])

print(df2.groupby('Department').describe())
print(df2.groupby('Department').describe().transpose())

#--------------------Merging, Joinning and Concatenating data--------------------

dfa = pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2']}, index = [0,1,2])
print(dfa)
dfb = pd.DataFrame({'C':['C0','C1','C2']}, index = [0,1,2])
print(dfb)
dfc = pd.DataFrame({'D':['D0','D1'],'E':['E0','E1']},index=[0,1])
print(dfc)

print(pd.concat([dfa,dfb],axis=0,sort=True))
print(pd.concat([dfa,dfb],axis=1,sort=True))
print(pd.concat([dfa,dfb,dfc],axis=0,sort=True))
print(pd.concat([dfa,dfb,dfc],axis=1,sort=True))

# Merging works here same as in SQL on the basis of a key column
# We can also use Outer, left and right joins while merging. 
dfa = pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2'],'Key':['K0','K1','K2']}, index = [0,1,2])
dfb = pd.DataFrame({'C':['C0','C1','C2'],'D':['D0','D1','D2'],'Key':['K0','K1','K2']}, index = [0,1,2])
print(pd.merge(dfa,dfb,how='inner',on='Key'))

dfa = pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2'],'Key1':['K0','K1','K0'],'Key2':['K1','K2','K0']})
dfb = pd.DataFrame({'C':['C0','C1','C2'],'D':['D0','D1','D2'],'Key1':['K0','K1','K2'],'Key2':['K1','K0','K0']})
print(pd.merge(dfa,dfb,how='inner',on=['Key1','Key2']))

# Joining is same as merging but it does the join on index column unlike merge where we have to specify the key colmn.
# Column name should not be repeated when we are using join, we can specify the alias of duplicate column.
dfa = pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2']})
dfb = pd.DataFrame({'C':['C0','C1','C2'],'D':['D0','D1','D2']})
print(dfa.join(dfb)) # We also have how parameter available here where we can specify inner, outer, left or right.

#-----------------------Operations----------------------
# Finding Unique value
dfa = pd.DataFrame({'A':[1,2,3,4],'B':[222,333,444,444],'C':['abc','def','jki','xyz']})
print(dfa['B'].unique()) # Return an array of unique value in specified column. You have to specify column name.
print(len(dfa['B'].unique())) # Will give the lenght of unique value array retruned by unique method, or we can say give the count of unique values in a column.
print(dfa['B'].nunique()) # Will give the count of unique value in a column.
print(dfa['B'].value_counts()) # Will retrun which value appeared how many times in the column.

# Conditional Seclection refresher.
print(dfa[dfa['A']>2])
print(dfa[(dfa['A']>2) & (dfa['B']==222)])

# Apply function. It is used to apply a user defined fuction to each elemnt of selected data frame (single or multiple columns).
print(dfa[dfa['A']>2].apply(lambda x:x*2))
print(dfa[dfa['A']>2]['A'].apply(lambda x:x*2))

# Removing columns and Rows
dfa.drop('A', inplace= True,axis=1) # This will drop Column A from DataFrame as axis=1
dfa.drop(index=3, inplace= True,axis=1) # This will drop row with index 3
print(dfa)

# Returning Columnname and Indexes.
print(dfa.columns) # This will retun an array of column names.
print(dfa.index) # This will retun the type of index of DataFrame.

# Sorting values.
dfa = pd.DataFrame({'A':[1,2,3,4],'B':[444,333,222,444],'C':['def','abc','xyz','jki']},index=['pan','pra','bwa','vin'])
print(dfa)
print(dfa.sort_values('B'))

# Finding null values in DataFrame
print(dfa.isnull()) # This will return a boolean array with TRUE wherever the value is NULL in dataframe.

# Pivot tables
print(dfa.pivot_table(values='B',index=['A'], columns='C')) # This will create a pivot table using the values, Index and Columns arguement. If a list if passed with more than 2 values then a multilevel index will be created.

#---------------------------Input and Output data with Pandas-----------
dfa.to_csv('SupportFiles\My_Example_File.csv', index=False) # Dump data to csv file. Index is set to false to prevent the index to be exported too. 
# If index too gets exported then you will see an extra column when you import this file next time. 
# Pandas changes index into a new column while exporting it to file if not set to false.
dfb = pd.read_csv('SupportFiles\My_Example_File.csv') # This will import the data from csv.
print(dfb)
dfa.to_excel('Support\FilesMy_Example_Excel.xlsx',sheet_name='Sheet3') # This will write dfa DataFrame to excel file.
dfb = pd.read_excel('Support\FilesMy_Example_Excel.xlsx',sheet_name='Sheet3') # This will read data from excel file. Keep in mind that Pandas can only read data, no formulas or macros will be imported. Pandas may crash if any such file is imported.
print(dfb)

# There are some other methods like pd.read_html() and pd.read_sql() can also be used. read_html will read all table tags from the HTML link provided.
# read_sql is probabaly not the best way to read data for Pandas from SQL. It is advised to use specialised liberaries while working a specific flavour of database.


