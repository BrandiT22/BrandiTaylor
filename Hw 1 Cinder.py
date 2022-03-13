import pandas as pd

import numpy as np

 

import statsmodels.formula.api as sm # module for stats models

from statsmodels.iolib.summary2 import summary_col # module for presenting stats models outputs nicely

 

from pathlib import Path

import sys

import os

 

home = str(Path.home())

print(home)

 

#%%

if sys.platform == 'linux':

    inputDir = '/datasets/stocks/'

elif sys.platform == 'win32':

    inputDir = '\\datasets\stocks\\'

else :

    inputDir = '/datasets/stocks/'

   

print(sys.platform)

print(inputDir)

 

 

#%%

def price2ret(prices,retType='simple'):

    if retType == 'simple':

        ret = (prices/prices.shift(1))-1

    else:

        ret = np.log(prices/prices.shift(1))

    return ret

 

# %% Parse date stk_NFLX1

 

stk_NFLX =  pd.read_csv("c:\\Users\\lynae\\Fin510\\stk_NFLX1.csv",index_col='Date',parse_dates=True)

df_stk1 = stk_NFLX

# %% Parse Date stk_NFLX2

stk_NFLX=  pd.read_csv("c:\\Users\\lynae\\Fin510\\stk_NFLX2.csv",index_col='Date',parse_dates=True)

df_stk2 = stk_NFLX


# %% Parse date stk_CCL

 

stk_CCL =  pd.read_csv("c:\\Users\\lynae\\Fin510\\stk_CCL.csv",index_col='Date',parse_dates=True)

df_stk1 = stk_CCL

# %% Parse Date stk_CCLwrds2

stk_CCLwrds2=  pd.read_csv("c:\\Users\\lynae\\Fin510\\stk_CCLwrds2.csv",index_col='Date',parse_dates=True)

df_stk2 = stk_CCLwrds2


# %% Parse date stk_MTDR

stk_MTDR =  pd.read_csv("c:\\Users\\lynae\\Fin510\\stk_MTDR.csv",index_col='Date',parse_dates=True)

df_stk1 = stk_MTDR

# %% Parse Date stk_MTDRwrds2

stk_MTDRwrds2=  pd.read_csv("c:\\Users\\lynae\\Fin510\\stk_MTDRwrds2.csv",index_col='Date',parse_dates=True)

df_stk2 = stk_MTDRwrds2

#%%   merge & compare sources

df_stock_factor = pd.merge(df_stk1,df_stk2,left_index=True,right_index=True) # Merging the stock and factor returns dataframes

df_stock_factor['compare'] = df_stock_factor['Adj Close_x'] - df_stock_factor['Adj Close_y'] #calulate adj close diff between sources

print(df_stock_factor['compare'])
