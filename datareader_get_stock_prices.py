# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:36:29 2021
get stock prices
@author: lux
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime.now()
stock = "AMZN"

df = web.DataReader(stock, 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)

df['Low'].plot(loglog=True)

print(stock)
print(df.tail(10))













    
    





