#%%
import pandas as pd
sal = pd.read_csv('SupportFiles/Salaries.csv')
print(sal.head())
sal.info()
print(sal[sal['BasePay'] != 'Not Provided' ]['BasePay'].dropna().astype(float).mean())
print(sal[sal['OvertimePay'] != 'Not Provided' ]['OvertimePay'].dropna().astype(float).max())
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])
print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'])
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName'])
print(sal[sal['BasePay'] != 'Not Provided' ][['BasePay','Year']].dropna().astype(float).groupby('Year').mean())

#%%
len(sal['JobTitle'].unique())
sal['JobTitle'].nunique()
sal['JobTitle'].value_counts().head()
sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)
sal[sal['JobTitle'].str.contains('Chief', case=True)]['JobTitle']

#%%
import pandas as pd
ecom = pd.read_csv('SupportFiles/Ecommerce Purchases')
ecom.head()
ecom.info()
ecom['Purchase Price'].mean()
ecom['Purchase Price'].max()
ecom['Purchase Price'].min()


#%%
ecom.info()
ecom[ecom['Language'] == 'en'].count()
ecom[ecom['Job']=='Lawyer'].count()
ecom['AM or PM'].value_counts()
ecom['Job'].value_counts().head(5)

#%%
ecom.info()
from collections import Counter
ecom[ecom['Lot']=='90 WT']['Purchase Price']
ecom[ecom['Credit Card'] == 4926535242672853]['Email']
ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95.0)].count()
ecom[ecom['CC Exp Date'].str.contains('/25')].count()
ecom['Email'].apply(lambda email:email.split('@')[1]).value_counts().head(5)

