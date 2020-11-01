#!/bin/python3
from tqdm import tqdm
import pandas as pd
import numpy as np
import requests
import datetime
import pathlib
import apimoex
import sys
import datetime

# BA - business year
# BM - business month
# B  - business day (default)
# W  - week

offsets = ('BA', 'BM', 'B', 'W', '-')

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

if len(sys.argv) != 4:
    eprint(f"WRONG FORMAT\nExample:\n\t{sys.argv[0]} 2016-06-01 2020-06-01 BM")
    exit(0)

if sys.argv[-1] not in offsets:
    eprint(f"WRONG FORMAT\navailiable offsets:",' '.join(offsets))
    exit(0)

date_start, date_end, offset = sys.argv[1:]

if date_start == '-':
    date_start = '2016-06-01'

if date_end == '-':
    date_end = datetime.date.today()

if offset == '-':
    offset = 'B'

print(date_start, date_end, offset) #show got instructions

date_range = pd.date_range(date_start, date_end, freq='B')
result = pd.DataFrame(index = date_range)

with open("TICKs", "r") as TICKs:
    TICKs = [line.rstrip() for line in TICKs]

with requests.Session() as session:
    for TICK in tqdm(TICKs):
        data = apimoex.get_board_history(session, TICK, date_start, date_end)
        if not data or not TICK:
            continue
            
        df = pd.DataFrame(data)[['TRADEDATE','CLOSE']].rename(columns={'CLOSE':TICK})
        result = result.join(df.set_index('TRADEDATE'), how='outer')

result = result.resample(offset).apply('last')
result = result.dropna(axis=0, how='all')
result.to_csv('table.csv')


