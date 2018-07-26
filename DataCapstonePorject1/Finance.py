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

#%%
start = datetime.datetime(2006,1,1)
end = datetime.datetime(2016,12,31)
BAC = data.DataReader('BAC','morningstar',start,end).reset_index().drop(columns='Symbol')
C = data.DataReader('C','morningstar',start,end).reset_index().drop(columns='Symbol')
GS = data.DataReader('GS','morningstar',start,end).reset_index().drop(columns='Symbol')
JPM = data.DataReader('JPM','morningstar',start,end).reset_index().drop(columns='Symbol')
MS = data.DataReader('MS','morningstar',start,end).reset_index().drop(columns='Symbol')
WFC = data.DataReader('WFC','morningstar',start,end).reset_index().drop(columns='Symbol')

#%%
ticker_list = ['BAC','C','GS','JPM','MS','WFC']
stock_details = pd.concat([BAC,C,GS,JPM,MS,WFC],axis=1,keys=ticker_list)
stock_details.head()
#stock_details.columns.names()