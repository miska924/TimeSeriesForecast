import datetime
import os
import traceback

import pandas as pd
import requests
import apimoex
from tqdm import tqdm
from sklearn import feature_selection

from source._helpers import stderr_print, PredictParams
from source.back.moex_api import MoexAPI
from source import config as cfg


class DataProcess:
    cache = {}

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

    # filters relevant columns using mutual info or mrmr method
    @staticmethod
    def get_filtered_data_frame_columns(df: pd.DataFrame, mrmr=False, features_left_cnt=10):
        if features_left_cnt >= len(df.columns) - 1:
            return df.columns

        if mrmr and len(df.columns) - features_left_cnt < 10:
            import pymrmr
            return [df.columns.values[0]] + pymrmr.mRMR(df, 'MID', features_left_cnt)
        else:
            data = df.to_numpy()
            correlations = feature_selection.mutual_info_regression(data[:, 1:], data[:, 0])
            treshold = sorted(correlations, reverse=True)[features_left_cnt]

            columns = []
            for i, col in enumerate(df.columns[1:]):
                if len(columns) < features_left_cnt and correlations[i] > treshold:
                    columns.append(col)
            for i, col in enumerate(df.columns[1:]):
                if len(columns) < features_left_cnt and correlations[i] == treshold:
                    columns.append(col)

            return [df.columns.values[0]] + columns

    # [THE POINT OF ENTRANCE]:
    @staticmethod
    def get_processed(params: PredictParams) -> pd.DataFrame:
        # for debug:
        stderr_print(f"""
        Start loading data
        Date start: {params.start_date}
        Date end: {params.end_date}
        Offset: {params.offset}
        """)

        # process:
        loaded_df = DataProcess.load_data_from_moex(params.ticker, params.start_date, params.end_date,
                                                    params.offset.value, params.exogenous_variables)
        prepared_df = DataProcess.get_prepared_data_frame(loaded_df, predict_day=0)
        # filtered_df = DataProcess._get_filtered_data_frame(prepared_df)

        return prepared_df

    # load needed tickers from moex and returns dataframe
    @staticmethod
    def load_data_from_moex(target_ticker, date_start, date_end, offset, exo=None):
        if exo is None:
            exo = []
        # generating base dataframe:
        date_range = pd.date_range(date_start, date_end, freq='B')
        result = pd.DataFrame(index=date_range)

        # get list of needed tickers:
        tickers = [target_ticker]
        for ticker in exo:
            if ticker not in tickers:
                tickers.append(ticker)

        # load tickers' series from moex:
        with requests.Session() as session:
            for ticker in tickers:
                if ticker in DataProcess.cache:
                    cached = DataProcess.cache[ticker]
                    if cached.index[0] <= date_range[0] and date_range[-1] <= cached.index[-1]:
                        result = result.join(cached.copy().loc[date_range[0]:date_range[-1]],
                                             how='outer')
                        continue

                info = MoexAPI.get_ticker_info(session, ticker)
                data = apimoex.get_board_history(session, ticker, date_start, date_end, market=info['market'],
                                                 board=info['boardid'], engine=info['engine'])
                if not data:
                    print(f'Empty data for {ticker}')
                    return

                for item in data:
                    item['TRADEDATE'] = pd.to_datetime(item['TRADEDATE'])

                df = pd.DataFrame(data)[['TRADEDATE', 'CLOSE']].rename(columns={'CLOSE': ticker})
                DataProcess.cache[ticker] = df.set_index('TRADEDATE')
                result = result.join(DataProcess.cache[ticker], how='outer')

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
    def replace_with_diff(df, a: str, shift=0):
        if shift == 0:
            stderr_print('replace_with_diff shift 0')
            return

        df[a] = df[a] - df[a].shift(shift)
        return df

    @staticmethod
    def get_prepared_data_frame(df, diffs_count=2, x_lags=3, y_lags=4, average_y_days=5, predict_day=0):
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

        for col in df.columns:
            if col != 'Y':
                df[col] = df[col].shift(predict_day)
        # df = df.dropna(axis=0, how='any')
        return df
