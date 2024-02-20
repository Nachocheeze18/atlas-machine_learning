#!/usr/bin/env python3
"""Rename the column Timestamp to Datetime
Convert the timestamp values to datatime values
Display only the Datetime and Close columns"""
import pandas as pd
from_file = __import__('2-from_file').from_file


df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
1
df.rename(columns={'Timestamp': 'Datetime'}, inplace=True)
df['Datetime'] = pd.to_datetime(df['Datetime'])
df = df[['Datetime', 'Close']]
print(df.tail())
