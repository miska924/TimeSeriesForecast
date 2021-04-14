import enum
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

TICKERS = {
    'CBOM': [],
    'GAZP': [],
    'GMKN': [],
    'PIKK': [],
    'LSRG': [],
    'DSKY': [],
    'ALRS': [],
    'CHMF': [],
    'FLOT': [],
}


class Period(enum.Enum):
    business_year = 'BA'
    business_month = 'BM'
    business_day = 'B'
    week = 'W'
    default = 'B'

    @staticmethod
    def get_values() -> list:
        return [item.value for item in Period]
