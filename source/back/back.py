import datetime
import sys
import time
import traceback

import pandas as pd
import numpy as np
import copy
from multiprocessing import Queue, Lock
from tqdm import tqdm
from dateutil import parser
from sklearn import metrics

import source.back.models
from source import config as cfg
from source._helpers import PredictParams, get_values, make_df, dates_from_array
from source.back.data_process import DataProcess
from source.back.models import *
from source.config import PredictionData
from source.server.config import ExecType


def clean(results: dict):
    current_time = time.time_ns()
    results_dict = dict(
        sorted(filter(lambda item: current_time - item[1].timestamp < cfg.CLEAN_TIMEOUT, results.items()),
               key=lambda item: item[1].timestamp, reverse=True)[:cfg.MAX_PREDICTIONS_SIZE])
    for key, value in results.items():
        if key not in results_dict:
            del results[key]


def executor(requests: Queue, results: dict, requests_lock: Lock, results_lock: Lock):
    counter = 0
    while True:
        if counter == cfg.CLEAN_PREDICT_CNT:
            print("before cleaning:\n", results.keys())
            with results_lock:
                clean(results)
            print("after cleaning:\n", results.keys())

            counter = 0
            continue

        counter += 1

        data = requests.get()
        uid, data, type = data['id'], data['data'], data['type']
        with results_lock:
            results[uid] = PredictionData(status=cfg.Status.process)

        try:
            params = PredictParams(**data)
            print(params)
        except:
            print(traceback.format_exc())
            with results_lock:
                results[uid] = PredictionData(status=cfg.Status.fail, data=cfg.INVALID_PARAMS_ERROR)
            continue

        if type == ExecType.predict:
            tmp = run_prediction(params)
        else:
            tmp = run_cross_validation(params)

        with results_lock:
            results[uid] = tmp


def run_prediction(params: PredictParams):
    try:
        date_range = pd.date_range(parser.parse(params.end_date) + datetime.timedelta(days=1),
                                   params.forecast_date, freq=params.offset.value)

        model = getattr(source.back.models, params.model.value).Model(params.params)
        model.load(params)

        res_y = model.train_and_predict(len(date_range))
        res_index = list(date_range)

        if params.upload:
            real_df = make_df(params.uploaded_data, params.start_date, params.forecast_date)
        else:
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


# Returns MSE and MAPE
def run_cross_validation(params: PredictParams):
    avg_mse = 0
    avg_mape = 0

    try:
        if params.upload:
            loaded_df = make_df(params.uploaded_data, params.start_date, params.end_date)
        else:
            loaded_df = DataProcess.load_data_from_moex(
                params.ticker,
                params.start_date,
                params.end_date,
                params.offset.value,
                params.params.get('exogenous_variables', [])
            )

        mse = []
        mape = []
        for i in tqdm(range(0, loaded_df.shape[0] - params.cv_period - params.cv_predict_days, params.cv_shift)):
            model = getattr(source.back.models, params.model.value).Model(params.params)
            local_params = copy.deepcopy(params)
            local_params.start_date, local_params.end_date = loaded_df.index[i], loaded_df.index[i + params.cv_period - 1]
            local_params.upload, local_params.uploaded_data = params.upload, params.uploaded_data
            model.load(local_params)

            res = [[], []]
            res[0] = model.train_and_predict(params.cv_predict_days)
            res[1] = list(loaded_df.iloc[i + params.cv_period:i + params.cv_period + params.cv_predict_days, 0])

            mse.append(metrics.mean_squared_error(res[1], res[0]))
            mape.append(metrics.mean_absolute_percentage_error(res[1], res[0]))

            if mse[-1] > 18000:
                print(mse[-1], loaded_df.index[i], loaded_df.index[i + params.cv_period - 1],
                      loaded_df.index[i + params.cv_period + params.cv_predict_days - 1])

            avg_mse = sum(mse) / len(mse)
            avg_mape = sum(mape) / len(mape)
    except:
        print(traceback.format_exc())
        return PredictionData(status=cfg.Status.fail, data=cfg.CROSS_VALIDATION_FAILED)

    return PredictionData(
        data={
            "mse": avg_mse,
            "mape": avg_mape
        },
        status=cfg.Status.ready
    )


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
    else:
        offset = cfg.Offset(offset)

    tmp_params = PredictParams(
        model=cfg.Model.gradient_boosting_regressor,
        ticker='MTSS',
        start_date='2016-06-01',
        end_date='2021-05-09',
        forecast_date='2021-05-09',
        offset=offset,
        cv_period=127,
        cv_shift=15,
        cv_predict_days=2,
        params={
            'exogenous_variables': ['IMOEX', 'USD000000TOD'],
            'loss': cfg.GBLoss.huber,
            'learning_rate': 0.01,
            'n_estimators': 100,
            'criterion': cfg.GBCriterion.friedman_mse,
            'min_samples_leaf': 1,
            'alpha': 0.9
        }
    )
    res = run_cross_validation(tmp_params)
    print(res.data)
    exit(0)


    import decimal

    def drange(x, y, jump):
        while x < y:
            yield float(x)
            x = decimal.Decimal(str(x)) + decimal.Decimal(str(jump))

    best_mse, best_mape = 100000, 100
    best_n_estimators, best_min_samples_leaf, best_max_samples = 0, 0, 0

    for n_estimators in range(50, 300, 50):
        for min_samples_leaf in drange(0.0005, 0.1, 0.0005):
            for max_samples in drange(0.1, 1.1, 0.1):

                tmp_params = PredictParams(
                    model=cfg.Model.random_forest_regressor,
                    ticker='GAZP',
                    start_date='2011-06-01',
                    end_date='2021-05-09',
                    forecast_date='2021-05-09',
                    offset=offset,
                    cv_period=127,
                    cv_shift=15,
                    cv_predict_days=2,
                    params={
                        'exogenous_variables': [],
                        'n_estimators': n_estimators,
                        'criterion': 'mse',
                        'min_samples_leaf': min_samples_leaf,
                        'bootstrap': True,
                        'max_samples': max_samples if max_samples < 1 else None,
                    }
                )

                try:
                    res = run_cross_validation(tmp_params)

                    if res.data['mape'] < best_mape:
                        best_mse = res.data['mse']
                        best_mape = res.data['mape']
                        best_n_estimators = n_estimators
                        best_max_samples = max_samples
                        best_min_samples_leaf = min_samples_leaf
                        print(f"""
=====================================
MSE:                {res.data['mse']}
MAPE:               {res.data['mape']}
n_estimators:       {n_estimators}
min_samples_leaf:   {min_samples_leaf}
max_samples:        {max_samples}
                        """)
                except Exception as e:
                    print(f'Error: {e}.')

    print(f"""
================BEST=================
MSE:                {best_mse}
MAPE:               {best_mape}
n_estimators:       {best_n_estimators}
min_samples_leaf:   {best_min_samples_leaf}
max_samples:        {best_max_samples}
          """)


    tmp_params = PredictParams(
        model=cfg.Model.naive,
        ticker=list(cfg.TICKERS.keys())[0],
        start_date=start_date,
        end_date=end_date,
        forecast_date='2021-05-09',
        offset=offset,
        cv_period=127,
        cv_shift=15,
        cv_predict_days=2,
        params={
            'exogenous_variables': []
        }
    )
    res = run_cross_validation(tmp_params)
    print(res.data)
