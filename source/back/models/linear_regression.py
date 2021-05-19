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
    filtered_columns: List[str]

    def __init__(self, df=None):
        self.df = df

    def load(self, params: PredictParams):
        self.df = DataProcess.get_processed(params)

    def train(self, shift: int):
        df_copy = self.df.copy()
        for col in df_copy.columns:
            if col != 'Y':
                df_copy[col] = df_copy[col].shift(shift)
        df_copy = df_copy.dropna(axis=0, how='any')
        self.filtered_columns = self.df.columns
        DataProcess.get_filtered_data_frame_columns(df_copy, mrmr=False)

        df_copy = df_copy[self.filtered_columns].to_numpy()
        x = df_copy[:, 1:]
        y = df_copy[:, 0]
        self.model = LR()
        self.model.fit(x, y)

    def predict(self):
        return self.model.predict(self.df.tail(1)[self.filtered_columns[1:]])[0]
