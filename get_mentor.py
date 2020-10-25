#!/bin/python3
import pandas as pd
import numpy as np
import requests
import datetime
import pathlib
import apimoex
import sys
import datetime


offset = 'B' # Business day
date_start = '2015-06-01'
date_end = datetime.date.today()
date_range = pd.date_range(date_start, date_end, freq='B')
result = pd.DataFrame(index = date_range)

with open("TICKs", "r") as TICKs:
    TICKs = [line.rstrip() for line in TICKs]
process = 0


with requests.Session() as session:
    for TICK in TICKs:
        data = apimoex.get_board_history(session, TICK, date_start, date_end)
        if not data or not TICK:
            continue
            
        df = pd.DataFrame(data)[['TRADEDATE','CLOSE']].rename(columns={'CLOSE':TICK})
        result = result.join(df.set_index('TRADEDATE'), how='outer')
        
result = result.dropna(axis=0, how='all')
result.to_csv('table.csv')