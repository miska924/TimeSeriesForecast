#!/usr/bin/python3
import datetime
import sys

from source import config as cfg
from source._helpers import PredictParams
from source.server.data_process import DataProcess


def run(params: PredictParams):
    DataProcess.load_data(params.start_date, params.end_date, params.offset)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception(f'WRONG FORMAT\nExample:\n\t{sys.argv[0]} 2016-06-01 2020-06-01 BM')

    print(sys.argv)
    if sys.argv[-1] not in cfg.Period.get_values():
        raise Exception("WRONG FORMAT\navailable offsets:", ' '.join(cfg.Period.get_values()))

    start_date, end_date, offset = sys.argv[1:]

    if start_date == '-':
        start_date = '2016-06-01'

    if end_date == '-':
        end_date = datetime.date.today()

    if offset == '-':
        offset = cfg.Period.default

    tmp_params = PredictParams(
        None,
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




