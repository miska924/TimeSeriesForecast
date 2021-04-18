import enum
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TICKERS = {
    'CBOM': ['PIKK', 'GAZP', 'PIKK'],
    'GAZP': ['GMKN', 'LSRG']
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
