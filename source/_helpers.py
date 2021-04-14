import sys
from dataclasses import dataclass

from source import config as cfg


# Класс характеризующий параметры, передающиеся из UI в предиктор
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
    offset: cfg.Period


def error_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
