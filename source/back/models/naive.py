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
        loaded_df = DataProcess.load_data_from_moex(params.ticker, params.start_date, params.end_date,
                                                    params.offset.value, params.exogenous_variables)
        self.df = DataProcess.get_prepared_data_frame(loaded_df, predict_day=0)

    def train(self, shift: int):
        pass

    def predict(self):
        return self.df['Y'][-1]
