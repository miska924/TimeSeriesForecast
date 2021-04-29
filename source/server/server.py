import datetime
import sys

import pandas as pd
import numpy as np
from copy import copy

from source import config as cfg
from source._helpers import PredictParams, get_values, save_file, dates_from_array
from source.server.data_process import DataProcess
from source.server.models import Models
from dateutil import parser


def run(params: PredictParams):
    date_range = pd.date_range(parser.parse(params.end_date) + datetime.timedelta(days=1),
                               params.forecast_date, freq=params.offset.value)

    df = DataProcess.get_processed(params.ticker, params.start_date, params.end_date, params.offset.value)\
        .join(pd.DataFrame(index=date_range), how="outer")
    res_y, res_index = [], []
    for i, date in enumerate(date_range):
        for col in df.columns:
            if col != 'Y':
                df[col] = df[col].shift(1)
        df_train = df.dropna(axis=0, how='any')
        filtered_columns = DataProcess.get_filtered_data_frame_columns(df_train, mrmr=False)
        model = Models.train_linear_regression(df_train[filtered_columns])
        res_y.append(model.predict(df.loc[[date], filtered_columns[1:]])[0])
        res_index.append(date)
        print(str(date)[:10], res_y[-1])

    save_file(df, f"{params.ticker}.csv")

    real_df = DataProcess.load_data_from_moex(
        params.ticker,
        params.start_date,
        params.forecast_date,
        params.offset.value,
        need_exo=False
    )

    return dates_from_array(real_df.index), real_df[params.ticker], dates_from_array(res_index), res_y


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception(f'WRONG FORMAT\nExample:\n\t{sys.argv[0]} 2016-06-01 2020-06-01 BM')

    print(sys.argv)
    if sys.argv[-1] not in get_values(cfg.Offset):
        raise Exception("WRONG FORMAT\navailable offsets:", ' '.join(get_values(cfg.Offset)))

    start_date, end_date, offset = sys.argv[1:]

    if start_date == '-':
        start_date = '2016-06-01'

    if end_date == '-':
        end_date = datetime.date.today()

    if offset == '-':
        offset = cfg.Offset.default

    tmp_params = PredictParams(
        list(cfg.TICKERS.keys())[0],
        None,
        None,
        None,
        None,
        None,
        start_date,
        end_date,
        '2021-01-09',
        offset
    )
    run(tmp_params)
