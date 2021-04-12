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
    eprint(f"WRONG FORMAT\navailiable offsets:", ' '.join(offsets))
    exit(0)

date_start, date_end, offset = sys.argv[1:]

if date_start == '-':
    date_start = '2016-06-01'

if date_end == '-':
    date_end = datetime.date.today()

if offset == '-':
    offset = 'B'

print(date_start, date_end, offset)  # show got instructions

date_range = pd.date_range(date_start, date_end, freq='B')
result = pd.DataFrame(index=date_range)  # .format(formatter=lambda x: x.strftime('%Y-%m-%d')))

with open("TICKs", "r") as TICKs:
    TICKs = [line.rstrip() for line in TICKs]

with requests.Session() as session:
    for TICK in tqdm(TICKs):
        data = apimoex.get_board_history(session, TICK, date_start, date_end)
        if not data or not TICK:
            continue
        for item in data:
            item['TRADEDATE'] = pd.to_datetime(item['TRADEDATE'])

        df = pd.DataFrame(data)[['TRADEDATE', 'CLOSE']].rename(columns={'CLOSE': TICK})
        result = result.join(df.set_index('TRADEDATE'), how='outer')

result = result.resample(offset).apply('last')
result = result.dropna(axis=0, how='all')
result.to_csv('table.csv')


def getPreparedDataFrame(df, index):
    res = pd.DataFrame(index=index).join(df).rename(columns={df.name: '0'})
    print(res)
    for i in range(1, 10):
        col = df.copy()
        res = res.join(
            pd.DataFrame(index=index)
            .join(
                res[str(i - 1)].copy()
            ).rename(columns={str(i - 1): str(i)}),
            how='outer'
        )
        res[str(i)] = res[str(i)] - res[str(i)].shift(1)

    return res


prepared = getPreparedDataFrame(result['GAZP'], result.index)
print(prepared)