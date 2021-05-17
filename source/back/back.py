import datetime
import sys
import time
import traceback

import pandas as pd
import numpy as np
from copy import copy
from multiprocessing import Queue, Manager
from tqdm import tqdm
from dateutil import parser
from sklearn import metrics

from source import config as cfg
from source._helpers import PredictParams, get_values, save_file, dates_from_array
from source.back.data_process import DataProcess
from source.back.models import *
from source.config import PredictionData


def clean(predictions: dict):
    current_time = time.time_ns()
    predictions_dict = dict(
        sorted(filter(lambda item: current_time - item[1].timestamp < cfg.CLEAN_TIMEOUT, predictions.items()),
               key=lambda item: item[1].timestamp, reverse=True)[:cfg.MAX_PREDICTIONS_SIZE])
    for key, value in predictions.items():
        if key not in predictions_dict:
            del predictions[key]


def predictor(requests: Queue, predictions: dict):
    counter = 0
    while True:
        if counter == cfg.CLEAN_PREDICT_CNT:
            print("before cleaning:\n", predictions.keys())
            clean(predictions)
            print("after cleaning:\n", predictions.keys())

            counter = 0
            continue

        counter += 1

        data = requests.get()
        uid, data = data['id'], data['data']
        predictions[uid] = PredictionData(status=cfg.Status.process)

        try:
            params = PredictParams(**data)
            print(params)
        except:
            print(traceback.format_exc())
            predictions[uid] = PredictionData(status=cfg.Status.fail, data=cfg.INVALID_PARAMS_ERROR)
            continue

        predictions[uid] = run(params)


def run(params: PredictParams):
    try:
        date_range = pd.date_range(parser.parse(params.end_date) + datetime.timedelta(days=1),
                                   params.forecast_date, freq=params.offset.value)

        model = linear_regression.Model()
        model.load(params)

        res_y, res_index = [], []
        for i, date in tqdm(enumerate(date_range), desc="Predicting"):
            model.train(i + 1)
            res_y.append(model.predict())
            res_index.append(date)
            # print(str(date)[:10], res_y[-1])

        real_df = DataProcess.load_data_from_moex(
            params.ticker,
            params.start_date,
            params.forecast_date,
            params.offset.value
        )
    except:
        print(traceback.format_exc())
        return PredictionData(status=cfg.Status.fail, data=cfg.PREDICTION_FAILED)

    return PredictionData(
        data={
            "X": list(dates_from_array(real_df.index)),
            "Y": list(real_df[params.ticker]),
            "PredictedX": list(dates_from_array(res_index)),
            "PredictedY": list(res_y)
        },
        status=cfg.Status.ready
    )


def cross_validation(params: PredictParams):
    df = DataProcess.get_processed(params)
    mse = []

    for i in range(0, df.shape[0] - params.cv_period - params.cv_predict_days, params.cv_shift):
        model = None
        if params.model == cfg.Model.linear_reg:
            model = linear_regression.Model(df.iloc[i:i + params.cv_period])
        else:
            model = naive.Model(df.iloc[i:i + params.cv_period])
        res = [[], []]
        for days in range(1, params.cv_predict_days + 1):
            model.train(days)
            res[0].append(model.predict())
        res[1] = list(df.iloc[i + params.cv_period:i + params.cv_period + params.cv_predict_days, 0])

        mse.append(metrics.mean_squared_error(res[0], res[1]))

        if mse[-1] > 18000:
            print(mse[-1], df.index[i], df.index[i + params.cv_period - 1],
                  df.index[i + params.cv_period + params.cv_predict_days - 1])

    return sum(mse) / len(mse)


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
        model=cfg.Model.linear_reg,
        ticker=list(cfg.TICKERS.keys())[0],
        exogenous_variables=['IMOEX', 'MOEXOG'],
        start_date=start_date,
        end_date=end_date,
        forecast_date='2021-01-09',
        offset=offset,
        cv_period=300,
        cv_shift=15,
        cv_predict_days=2
    )
    #run(tmp_params)
    print(cross_validation(tmp_params))
    tmp_params = PredictParams(
        model=cfg.Model.naive,
        ticker=list(cfg.TICKERS.keys())[0],
        exogenous_variables=['IMOEX', 'MOEXOG'],
        start_date=start_date,
        end_date=end_date,
        forecast_date='2021-01-09',
        offset=offset,
        cv_period=300,
        cv_shift=15,
        cv_predict_days=2
    )
    print(cross_validation(tmp_params))
