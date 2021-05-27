import datetime
from typing import List

import pandas as pd
import statsmodels.api as sm
from dateutil import parser
from sklearn.linear_model import LinearRegression as LR

from source._helpers import PredictParams
from source.back.data_process import DataProcess
from source.back.models._model import BaseModel


class Model(BaseModel):
    def __init__(self):
        self.model = None
        self.df = None
        self.filtered_columns = None
        self.shift = None

    def load(self, params: PredictParams):
        self.df = DataProcess.load_data_from_moex(params.ticker, params.start_date, params.end_date,
                                                  params.offset.value, params.exogenous_variables)
        self.df = self.df[self.df.columns[0]].reset_index(drop=True)

    def train(self, shift: int):
        self.model = sm.tsa.ExponentialSmoothing(self.df, trend='add',
                                                 initialization_method='estimated').fit()
        self.shift = shift

    def predict(self):
        tmp = self.model.forecast(self.shift)
        return tmp.iloc[-1]

    def train_and_predict(self, period: int):
        self.train(period)
        return self.model.forecast(period)
