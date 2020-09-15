import pandas as pd
import pandas_datareader.data as web

dji = web.DataReader('^DJI', data_source='yahoo', start='8/8/1995', end='8/7/2004')
print(dji.info())
print(dji[0:10])

dji.to_csv('DJIndex.csv')


