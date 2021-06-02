import enum
import json
import os
import sys
from dataclasses import dataclass
from typing import List

import numpy as np
import pandas as pd

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from source import config as cfg


# Класс характеризующий параметры, передающиеся из client в предиктор
@dataclass
class PredictParams:
    ticker: str = None
    model: cfg.Model = None
    start_date: str = None
    end_date: str = None
    forecast_date: str = None
    offset: cfg.Offset = None
    cv_shift: int = None
    cv_period: int = None
    cv_predict_days: int = None
    params: dict = None
    upload: bool = False
    uploaded_data: List[List[str]] = None


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


def safe_get_key(data, key, message=None):
    if key not in data:
        raise Exception(message if message else f"No key {key} in dict.")

    return data[key]


@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=5))
def send_request(method: str, url: str, params=None, headers=None, cookies=None, data=None, json=None) -> any:
    with requests.Session() as session:
        with session.request(method=method,
                             url=url,
                             params=params,
                             headers=headers,
                             cookies=cookies,
                             timeout=5,
                             data=data,
                             json=json) as response:
            return response.json()


PUBLIC_ENUMS = {
    'Model': cfg.Model,
    'Offset': cfg.Offset,
    'ETSTrend': cfg.ETSTrend
}


class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj) in PUBLIC_ENUMS.values():
            return {"__enum__": str(obj)}
        return json.JSONEncoder.default(self, obj)


def as_enum(d):
    if "__enum__" in d:
        name, member = d["__enum__"].split(".")
        return getattr(PUBLIC_ENUMS[name], member)
    else:
        return d


def make_df(uploaded_data, start_date, end_date):
    columns = uploaded_data[0][1:]
    uploaded_data = np.array(uploaded_data[1:]).T

    res = pd.DataFrame(
        uploaded_data[1:, :].T,
        columns=columns,
        index=pd.to_datetime(uploaded_data[0, :])
    )
    res = res.apply(pd.to_numeric)
    print(res.columns)

    res = res.loc[start_date:end_date]
    res.columns = res.columns.astype(str)

    return res
