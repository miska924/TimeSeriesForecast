import enum
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MAX_QUEUE_SIZE = 5

TICKERS = {
    'GAZP': ['MOEX', 'MOEXOG'], # 'USDRUB_TOM'
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
    wait = 1
    fail = 2
