import datetime
import sys

from source import config as cfg
from source._helpers import PredictParams, get_values, save_file
from source.server.data_process import DataProcess
from source.server.models import Models


def run(params: PredictParams):
    result = DataProcess.get_processed(params.ticker, params.start_date, params.end_date, params.offset)
    print(Models.test_linear_regression(result))
    save_file(result, f"{params.ticker}.csv")


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

    tmp_params = PredictParams(
        list(cfg.TICKERS.keys())[0],
        None,
        None,
        None,
        None,
        None,
        start_date,
        end_date,
        offset
    )
    run(tmp_params)
