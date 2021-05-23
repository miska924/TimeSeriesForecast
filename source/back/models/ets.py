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
        # self.df = DataProcess.get_prepared_data_frame(loaded_df, predict_day=0)
        self.df = self.df[self.df.columns[0]]

    def train(self, shift: int):
        self.model = sm.tsa.ExponentialSmoothing(self.df, trend='add', damped=True).fit()
        self.shift = shift

        # df_copy = self.df.copy()
        # for col in df_copy.columns:
        #     if col != 'Y':
        #         df_copy[col] = df_copy[col].shift(shift)
        # df_copy = df_copy.dropna(axis=0, how='any')
        # self.filtered_columns = DataProcess.get_filtered_data_frame_columns(df_copy, mrmr=False)
        #
        # df_copy = df_copy[self.filtered_columns].to_numpy()
        # x = df_copy[:, 1:]
        # y = df_copy[:, 0]
        # self.model = LR()
        # self.model.fit(x, y)

    def predict(self):
        try:
            tmp = self.model.forecast(self.shift)
            print("\n\n\n", tmp, "\n\n\n")
            return tmp.iloc[-1]
        except Exception as e:
            # print(self.df.tail(1)[self.filtered_columns[1:]])
            raise e
