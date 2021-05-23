import enum
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MAX_QUEUE_SIZE = 5
CLEAN_PREDICT_CNT = 3
MAX_PREDICTIONS_SIZE = 30
CLEAN_TIMEOUT = 60 * 60 * 1000 * 1000

INVALID_PARAMS_ERROR = "Invalid params."
PREDICTION_FAILED = "Prediction failed."
CROSS_VALIDATION_FAILED = "Cross validation failed."

TICKERS = {
    'GAZP': ['IMOEX', 'MOEXOG'],  # 'USDRUB_TOM'
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
    linear_reg = 'linear_regression'
    naive = 'naive'
    stationary_linear_regression = 'stationary_linear_regression'
    ansamble = 'ansamble'


class Offset(enum.Enum):
    business_year = 'BA'
    business_month = 'BM'
    business_day = 'B'
    week = 'W'
    default = 'B'


class Status:
    ready = 0
    process = 1
    wait = 2
    fail = 3
    invalid = 4


class PredictionData:
    status = None
    data = None
    timestamp = None

    def __init__(self, status=None, data=None):
        self.status = status
        self.data = data
        self.timestamp = time.time_ns()

    def format(self):
        return self.__dict__
