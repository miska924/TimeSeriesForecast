#!/usr/bin/python3
import os

from tqdm import tqdm
import pandas as pd
import requests
import apimoex
import sys
import datetime
import matplotlib.pyplot as plt

# BA - business year
# BM - business month
# B  - business day (default)
# W  - week

offsets = ('BA', 'BM', 'B', 'W', '-')


def error_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


if len(sys.argv) != 4:
    raise Exception(f'WRONG FORMAT\nExample:\n\t{sys.argv[0]} 2016-06-01 2020-06-01 BM')

if sys.argv[-1] not in offsets:
    raise Exception("WRONG FORMAT\navailable offsets:", ' '.join(offsets))

date_start, date_end, offset = sys.argv[1:]

if date_start == '-':
    date_start = '2016-06-01'

if date_end == '-':
    date_end = datetime.date.today()

if offset == '-':
    offset = 'B'

error_print(date_start, date_end, offset)

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


def get_prepared_data_frame(series, index):
    res = pd.DataFrame(index=index).join(series).rename(columns={series.name: '0'})
    plt.title(series.name)
    plt.plot(series)
    plt.show()
    for i in range(1, 10):
        res = res.join(
            pd.DataFrame(index=index).join(
                res[str(i - 1)].copy()
            ).rename(columns={str(i - 1): str(i)}),
            how='outer'
        )
        res[str(i)] = res[str(i)] - res[str(i)].shift(1)
    return res


try:
    os.stat('prepared')
except:
    os.mkdir('prepared')

for TICK in result:
    prepared = get_prepared_data_frame(result[TICK], result.index)
    prepared.to_csv(f'prepared/{TICK}.csv')
