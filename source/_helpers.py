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


def stderr_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_values(e) -> list:
    return [item.value for item in e]


def save_file(df, filename):
    tmp_dir = os.path.join(cfg.BASE_DIR, "tmp")
    try:
        os.stat(tmp_dir)
    except:
        os.mkdir(tmp_dir)

    path = os.path.join(tmp_dir, filename)
    df.to_csv(path)
