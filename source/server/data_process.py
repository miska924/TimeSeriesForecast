import os

import pandas as pd
import requests
import apimoex
import matplotlib.pyplot as plt
from tqdm import tqdm

from source._helpers import stderr_print
from source import config as cfg


class DataProcess:

    def __init__(self):
        pass

    # takes dataframe with tickers and returns dataframe:
    # [target ticker, exo_ticker_1, exo_ticker_2 , ...]
    @staticmethod
    def _get_dataframe_to_prepare(df, ticker):
        res = pd.DataFrame(index=df.index).join(df[ticker])
        if ticker in cfg.TICKERS:
            for exo in cfg.TICKERS[ticker]:
                if not res.__contains__(exo):
                    res = res.join(df[exo].copy(), how="outer")

        return res

    @staticmethod
    def _get_filtered_data_frame(df):
        # TODO: filter
        return df

    # [THE POINT OF ENTRANCE]:
    @staticmethod
    def get_processed(target_ticker, date_start, date_end, offset):
        # for debug:
        stderr_print(f"""
        Start loading data
        Date start: {date_start}
        Date end: {date_end}
        Offset: {offset}
        """)

        # process:
        loaded_df = DataProcess._load_data_from_moex(target_ticker, date_start, date_end, offset)
        prepared_df = DataProcess._get_prepared_data_frame(loaded_df)
        filtered_df = DataProcess._get_filtered_data_frame(prepared_df)

        return filtered_df

    # load needed tickers from moex and returns dataframe
    @staticmethod
    def _load_data_from_moex(target_ticker, date_start, date_end, offset):
        # generating base dataframe:
        date_range = pd.date_range(date_start, date_end, freq='B')
        result = pd.DataFrame(index=date_range)

        # get list of needed tickers:
        tickers = set()
        tickers.add(target_ticker)
        if cfg.TICKERS.__contains__(target_ticker):
            for ticker in cfg.TICKERS[target_ticker]:
                tickers.add(ticker)

        # load tickers' series from moex:
        with requests.Session() as session:
            for ticker in tqdm(tickers):
                data = apimoex.get_board_history(session, ticker, date_start, date_end)
                if not data:
                    return

                for item in data:
                    item['TRADEDATE'] = pd.to_datetime(item['TRADEDATE'])

                df = pd.DataFrame(data)[['TRADEDATE', 'CLOSE']].rename(columns={'CLOSE': ticker})
                result = result.join(df.set_index('TRADEDATE'), how='outer')

        # cut useless indexes:
        result = result.resample(offset).apply('last')
        result = result.dropna(axis=0, how='all')

        return result

    # join dataframe and named series (sum of two series with coefficients):
    @staticmethod
    def _join(df, a, a_coef=1, b=None, b_coef=-1, name=None):
        # rename series for simplification:
        if name is None:
            name = df.shape[1]
        if a is not None:
            a.name = "TMP"
        if b is not None:
            b.name = "TMP"

        # return joined dataframe:
        return df.join(
            pd.DataFrame(index=df.index).join(
                (a_coef * a if a is not None else 0) + (b_coef * b if b is not None else 0)
            ).rename(columns={a.name: name}),
            how='outer'
        )

    @staticmethod
    def _get_prepared_data_frame(df, diffs_count=2, x_lags=3, y_lags=4, average_y_days=5):
        # rename index & columns:
        index = df.index
        df.set_axis(index, axis=0, inplace=True)
        df.set_axis(['Y'] + [('EXO_' + str(y)) for y in range(df.shape[1] - 1)], axis=1, inplace=True)

        # average Y days:
        average = df[df.columns[0]].copy()
        for k in range(1, average_y_days):
            average += df[df.columns[0]].shift(k)
        df = DataProcess._join(df, average, 1 / average_y_days, name=f'Y_AVRG_{average_y_days}')

        # diffs:
        if diffs_count > 0:
            df = DataProcess._join(df, df[df.columns[0]].copy(), 1, df[df.columns[0]].copy().shift(1), -1,
                                   name=f'Y_DIFF_1')
        current_diff = 2
        for i in range(df.shape[1], df.shape[1] + diffs_count - 1):
            df = DataProcess._join(df, df[df.columns[i - 1]].copy(), 1, df[df.columns[i - 1]].copy().shift(1), -1,
                                   name=f'Y_DIFF_{current_diff}')
            current_diff += 1

        # X lags:
        for i in range(1, df.shape[1]):
            for j in range(x_lags):
                df = DataProcess._join(df, df[df.columns[i]].copy().shift(j + 1), name=f'{df.columns[i]}_LAG_{j + 1}')

        # Y lags:
        for i in range(y_lags):
            df = DataProcess._join(df, df[df.columns[0]].copy().shift(i + 1), name=f'Y_LAG_{i + 1}')

        # cut begin which contains None values:
        df = df.copy()[max(1, average_y_days - 1 + y_lags, x_lags + diffs_count) - 1:]

        return df
