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
    except:
        print(traceback.format_exc())
        return PredictionData(status=cfg.Status.fail, data=cfg.CROSS_VALIDATION_FAILED)

    return PredictionData(
        data={
            "mse": sum(mse) / len(mse),
            "mape": sum(mape) / len(mape)
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
        model=cfg.Model.ets,
        ticker='PIKK',
        start_date='2014-07-03',
        end_date='2021-03-03',
        forecast_date='2020-06-09',
        offset=cfg.Offset.business_month,
        cv_period=10,
        cv_shift=1,
        cv_predict_days=1,
        params={
            "trend": cfg.ETSTrend.additive,
            "dumped": False
        },
        upload=False,
        uploaded_data=[['', 'PIKK', 'GMKN', 'LSRG', 'CBOM', 'GAZP'], ['2016-06-30', '250.0', '8540.0', '823.0', '3.98', '139.51'], ['2016-07-29', '250.0', '9444.0', '907.5', '3.98', '137.3'], ['2016-08-31', '271.8', '9571.0', '878.0', '4.13', '134.95'], ['2016-09-30', '292.0', '9812.0', '891.0', '4.25', '134.9'], ['2016-10-31', '285.0', '9344.0', '879.5', '4.275', '138.84'], ['2016-11-30', '279.0', '10371.0', '916.5', '4.275', '148.8'], ['2016-12-30', '290.0', '10122.0', '952.0', '4.3', '154.55'], ['2017-01-31', '285.9', '9629.0', '1001.0', '4.262', '149.8'], ['2017-02-28', '290.0', '9311.0', '952.5', '4.231', '134.0'], ['2017-03-31', '296.6', '8929.0', '927.0', '4.39', '127.9'], ['2017-04-28', '288.2', '8747.0', '870.0', '4.414', '136.75'], ['2017-05-31', '302.0', '7902.0', '906.5', '4.24', '120.28'], ['2017-06-30', '296.9', '8068.0', '820.0', '4.5', '118.49'], ['2017-07-31', '292.8', '8930.0', '725.0', '4.436', '116.1'], ['2017-08-31', '289.9', '9790.0', '779.5', '4.58', '117.97'], ['2017-09-29', '316.3', '9920.0', '807.0', '4.599', '122.2'], ['2017-10-31', '311.6', '10592.0', '815.0', '4.547', '125.9'], ['2017-11-30', '299.6', '9876.0',
'796.0', '4.35', '132.15'], ['2017-12-29', '326.5', '10850.0', '826.5', '4.742', '130.5'], ['2018-01-31', '306.0', '11608.0', '842.0', '4.66', '143.36'], ['2018-02-28', '323.1', '11159.0', '859.0', '4.734', '143.16'], ['2018-03-30', '315.2', '10760.0', '874.0', '4.849', '142.33'], ['2018-04-30', '306.3', '10814.0', '836.0', '4.62', '145.93'], ['2018-05-31', '329.8', '11111.0', '836.5', '4.842', '145.0'], ['2018-06-29', '334.0', '11399.0', '849.5', '4.927', '141.01'], ['2018-07-31', '342.5', '10882.0', '774.0', '4.944', '143.79'], ['2018-08-31', '364.0', '11220.0', '721.0', '5.0', '149.95'], ['2018-09-28', '347.6', '11388.0', '676.0', '5.049', '162.61'], ['2018-10-31', '352.3', '11000.0', '629.5', '5.028', '155.47'], ['2018-11-30', '351.1', '12738.0', '639.0', '5.195', '161.29'], ['2018-12-31', '376.3', '13039.0', '597.8', '5.17', '153.5'], ['2019-01-31', '352.0', '13596.0', '656.0', '5.375', '162.82'], ['2019-02-28', '359.0', '14114.0', '637.4', '5.515', '158.99'], ['2019-03-29', '353.8', '13720.0', '660.0', '5.967', '149.61'], ['2019-04-30', '365.5', '14342.0', '666.0', '5.93', '163.95'], ['2019-05-31', '368.4', '13718.0', '693.2', '5.96', '215.1'], ['2019-06-28', '374.9', '14308.0', '782.2', '5.965', '232.83'], ['2019-07-31', '395.0', '14646.0', '778.8', '5.962', '236.9'], ['2019-08-30', '387.3', '16088.0', '763.4', '5.958', '232.15'], ['2019-09-30', '400.5', '16686.0', '722.0', '5.778', '225.9'], ['2019-10-31', '348.0', '17888.0', '709.8', '5.772', '260.0'], ['2019-11-29', '385.7', '17046.0', '760.0', '5.939', '257.54'], ['2019-12-31', '400.4', '19102.0', '764.0', '5.879', '256.4'], ['2020-01-31', '435.6', '20800.0', '905.0', '5.778', '226.7'], ['2020-02-28', '390.9', '20250.0', '827.0', '5.65', '202.65'], ['2020-03-31', '410.0', '19518.0', '587.0', '5.495', '181.41'], ['2020-04-30', '391.5', '20478.0', '604.0', '5.45', '190.0'], ['2020-05-29', '383.9', '22110.0', '584.8', '5.415', '199.95'], ['2020-06-30', '377.0', '22026.0', '590.6', '5.424', '198.72']]
    )
    res = run_cross_validation(tmp_params)
    print(res.data)
    # tmp_params = PredictParams(
    #     model=cfg.Model.naive,
    #     ticker=list(cfg.TICKERS.keys())[0],
    #     exogenous_variables=[],
    #     start_date=start_date,
    #     end_date=end_date,
    #     forecast_date='2021-05-09',
    #     offset=offset,
    #     cv_period=127,
    #     cv_shift=15,
    #     cv_predict_days=2
    # )
    # res = run_cross_validation(tmp_params)
    # print(res.data)

