import os

import pandas as pd
import requests
import apimoex
import matplotlib.pyplot as plt
from tqdm import tqdm

from source._helpers import error_print
from source import config as cfg


class DataProcess:

    def __init__(self):
        pass

    @staticmethod
    def load_data(date_start, date_end, offset):
        print(f"""
        Start loading data
        Date start: {date_start}
        Date end: {date_end}
        Offset: {offset}
        """)

        date_range = pd.date_range(date_start, date_end, freq='B')
        result = pd.DataFrame(index=date_range)  # .format(formatter=lambda x: x.strftime('%Y-%m-%d')))

        with requests.Session() as session:
            for ticker in tqdm(cfg.TICKERS.keys()):
                data = apimoex.get_board_history(session, ticker, date_start, date_end)
                if not data:
                    continue

                for item in data:
                    item['TRADEDATE'] = pd.to_datetime(item['TRADEDATE'])

                df = pd.DataFrame(data)[['TRADEDATE', 'CLOSE']].rename(columns={'CLOSE': ticker})
                result = result.join(df.set_index('TRADEDATE'), how='outer')

        result = result.resample(offset).apply('last')
        result = result.dropna(axis=0, how='all')
        result.to_csv('table.csv')

        try:
            os.stat('prepared')
        except:
            os.mkdir('prepared')

        for TICK in result:
            prepared = DataProcess.get_prepared_data_frame(result[TICK], result.index)
            prepared.to_csv(f'prepared/{TICK}.csv')

    @staticmethod
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
