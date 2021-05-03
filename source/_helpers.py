import enum
import os
import sys
from dataclasses import dataclass
from source import config as cfg


# Класс характеризующий параметры, передающиеся из client в предиктор
@dataclass
class PredictParams:
    ticker: str
    model: str
    exogenous_variables: list
    metrics: str
    prediction_method: str
    prediction_type: str
    start_date: str
    end_date: str
    forecast_date: str
    offset: cfg.Offset

    def __init__(self, ticker: str, model: str, exogenous_variables: list, metrics: str, prediction_method: str,
                 prediction_type: str, start_date: str, end_date: str, forecast_date: str, offset):
        self.ticker = ticker
        self.model = model
        self.exogenous_variables = exogenous_variables
        self.metrics = metrics
        self.prediction_method = prediction_method
        self.prediction_type = prediction_type
        self.start_date = start_date
        self.end_date = end_date
        self.forecast_date = forecast_date
        if type(offset) is str:
            self.offset = cfg.Offset(offset)
        else:
            self.offset = offset



def stderr_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_values(e) -> list:
    return [item.value for item in e]


def dates_from_array(array):
    return [str(x)[:10] for x in array]


def save_file(df, filename):
    tmp_dir = os.path.join(cfg.BASE_DIR, "tmp")
    try:
        os.stat(tmp_dir)
    except:
        os.mkdir(tmp_dir)

    path = os.path.join(tmp_dir, filename)
    df.to_csv(path)
