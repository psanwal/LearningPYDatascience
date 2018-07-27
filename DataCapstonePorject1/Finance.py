# *  Bank of America BAC
# * CitiGroup C
# * Goldman Sachs GS
# * JPMorgan Chase JPM
# * Morgan Stanley MS
# * Wells Fargo WFC

#%%
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data
import numpy as np
import datetime
import seaborn as sns

#%%
start = datetime.datetime(2006,1,1)
end = datetime.datetime(2016,12,31)
BAC = data.DataReader('BAC','morningstar',start,end).reset_index().drop(columns='Symbol').set_index('Date')
C = data.DataReader('C','morningstar',start,end).reset_index().drop(columns='Symbol').set_index('Date')
GS = data.DataReader('GS','morningstar',start,end).reset_index().drop(columns='Symbol').set_index('Date')
JPM = data.DataReader('JPM','morningstar',start,end).reset_index().drop(columns='Symbol').set_index('Date')
MS = data.DataReader('MS','morningstar',start,end).reset_index().drop(columns='Symbol').set_index('Date')
WFC = data.DataReader('WFC','morningstar',start,end).reset_index().drop(columns='Symbol').set_index('Date')

#%%
ticker_list = ['BAC','C','GS','JPM','MS','WFC']
stock_details = pd.concat([BAC,C,GS,JPM,MS,WFC],axis=1,keys=ticker_list)
stock_details.columns.names = ['Stock Ticker','Stock Info']

#%%
# Max close for each company
for ticker in ticker_list:
    stock_details[ticker]['Close'].max()

stock_details.xs(key='Close',axis=1,level='Stock Info').max()

#%%
# Creating returns dataframe.
stock_returns = pd.DataFrame()
for ticker in ticker_list:
    stock_returns[ticker] = stock_details[ticker]['Close'].pct_change()

stock_returns.head()

#%%
sns.pairplot(data=stock_returns[1:], kind='scatter')

#%%
# find out date of max and min gain for each bank and analyze the result.
stock_returns.idxmax()
stock_returns.max()
stock_returns.idxmin()
stock_returns.min()
stock_return_max = pd.concat([stock_returns.idxmax(),stock_returns.max()], axis=1)
stock_return_min = pd.concat([stock_returns.idxmin(),stock_returns.min()],axis=1)
stock_return_max.columns = ['Date','Max_Value']
stock_return_min.columns = ['Date','Min_Value']
stock_return_max
stock_return_min

#%%
# Find the standard deviation of whole period and for 2015.
stock_returns.std()
stock_returns.loc['2015-01-01':'2015-12-31'].std()

#%%
# Dist plot of returns for morgan stanley for year 2015
sns.distplot(stock_returns.loc['2015-01-01':'2015-12-31']['MS'])

#%%
# Dist plot of returns for morgan stanley for year 2015
sns.distplot(stock_returns.loc['2008-01-01':'2008-12-31']['C'])

#%%
stock_details.xs(key='Close',axis=1,level='Stock Info')
sns.lineplot(data=stock_details.xs(key='Close',axis=1,level='Stock Info'),hue='stock Ticker')
