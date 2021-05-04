import enum
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MAX_QUEUE_SIZE = 5
RETRY_PREDICT_CNT = 3

INVALID_PARAMS_ERROR = "Invalid params."
PREDICTION_FAILED = "Prediction failed."

TICKERS = {
    'GAZP': ['MOEX', 'MOEXOG'],  # 'USDRUB_TOM'
    'CBOM': ['PIKK', 'GAZP', 'PIKK']
}


class Type(enum.Enum):
    values = 'Значения'
    trend = 'Тренд'


class Methods(enum.Enum):
    straight = 'Прямой'
    recursive = 'Рекурсивный'


class Metrics(enum.Enum):
    mse = 'MSE'


class Model(enum.Enum):
    linear_reg = 'Линейная регрессия'


class Offset(enum.Enum):
    business_year = 'BA'
    business_month = 'BM'
    business_day = 'B'
    week = 'W'
    default = 'B'

    def __str__(self):
        return self.value


class Status:
    ready = 0
    process = 1
    wait = 2
    fail = 3
    invalid = 4


class PredictionData:
    status = None
    data = None

    def __init__(self, status=None, data=None):
        self.status = status
        self.data = data

