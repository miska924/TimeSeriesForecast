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

        tickers = set()
        for (key, value) in cfg.TICKERS.items():
            tickers.add(key)
            for ticker in value:
                tickers.add(ticker)

        with requests.Session() as session:
            for ticker in tqdm(tickers):
                data = apimoex.get_board_history(session, ticker, date_start, date_end)
                if not data:
                    return

                for item in data:
                    item['TRADEDATE'] = pd.to_datetime(item['TRADEDATE'])

                df = pd.DataFrame(data)[['TRADEDATE', 'CLOSE']].rename(columns={'CLOSE': ticker})
                result = result.join(df.set_index('TRADEDATE'), how='outer')

        result = result.resample(offset).apply('last')
        result = result.dropna(axis=0, how='all')
        result.to_csv('table.csv')

        try:
            os.stat('../../prepared')
        except:
            os.mkdir('../../prepared')

        for TICK in result:
            prepared = DataProcess.get_prepared_data_frame(result[TICK], result.index)
            prepared.to_csv(f'../../prepared/{TICK}.csv')

    @staticmethod
    def get_prepared_data_frame(series, index, regressors=(), diffs_count=2, x_lags=3, y_lags=4, average_y_days=5):
        # plt.title(series.name)
        # plt.plot(series)
        # plt.show()

        index = [i for i in range(len(index))]
        new_index = [i for i in range(len(index) + max(x_lags, y_lags))]
        series.index = index
        res = pd.DataFrame(index=new_index).join(series).rename(columns={series.name: 0})


        # average Y days:
        l, r = 1, 2
        average = res[0].copy()
        for k in range(1, average_y_days):
            average += res[0].shift(k)
        res = res.join(
            pd.DataFrame(index=new_index).join(
                average.copy() / average_y_days
            ).rename(columns={res[0].name: l}),
            how='outer'
        )

        # diffs:
        l, r = r, r + diffs_count
        if diffs_count > 0:
            res = res.join(
                pd.DataFrame(index=index).join(
                    res[0].copy() - res[0].copy().shift(1)
                ).rename(columns={0: l}),
                how='outer'
            )
        for i in range(l + 1, r):
            res = res.join(
                pd.DataFrame(index=index).join(
                    res[i - 1].copy()
                ).rename(columns={i - 1: i}),
                how='outer'
            )
            res[i] = res[i] - res[i].shift(1)

        # X lags:
        l, r = 1, r
        last = r
        for i in range(l, r):
            for j in range(x_lags):
                res = res.join(
                    pd.DataFrame(index=new_index).join(
                        res[i].copy().shift(j + 1)
                    ).rename(columns={i: last}),
                    how='outer'
                )
                last += 1
        r = last

        # Y lags:
        l, r = r, r + y_lags
        for i in range(y_lags):
            res = res.join(
                pd.DataFrame(index=new_index).join(
                    res[0].copy().shift(i + 1)
                ).rename(columns={0: l + i}),
                how='outer'
            )
        return res
