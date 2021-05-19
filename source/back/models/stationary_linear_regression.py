import datetime
from typing import List

import pandas as pd
from dateutil import parser
from sklearn.linear_model import LinearRegression as LR

from source._helpers import PredictParams
from source.back.data_process import DataProcess
from source.back.models._model import BaseModel


class Model(BaseModel):
    model: LR
    df: pd.DataFrame
    df_prepared: pd.DataFrame
    filtered_columns: List[str]
    right: int

    def __init__(self, df=None):
        self.df = df

    def load(self, params: PredictParams):
        self.df = DataProcess.load_data_from_moex(params.ticker, params.start_date, params.end_date,
                                                  params.offset.value, params.exogenous_variables)

    def train(self, shift: int):
        df_copy = self.df.copy()

        for i, col in enumerate(df_copy.columns):
            df_copy = DataProcess.replace_with_diff(df_copy.copy(), col, shift)
            if i != 0:
                df_copy[col] = df_copy[col].shift(shift)

        df_copy = DataProcess.get_prepared_data_frame(df_copy)
        df_copy = df_copy.dropna(axis=0, how='any')
        self.df_prepared = df_copy.copy()

        self.filtered_columns = DataProcess.get_filtered_data_frame_columns(df_copy, mrmr=False)

        df_copy = df_copy[self.filtered_columns].to_numpy()
        x = df_copy[:, 1:]
        y = df_copy[:, 0]
        self.model = LR()
        self.model.fit(x, y)

    def predict(self):
        return self.df[self.df.columns[0]][-1] + self.model.predict(self.df_prepared.tail(1)[self.filtered_columns[1:]])[0]
