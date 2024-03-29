import statsmodels.api as sm

from source import config as cfg
from source._helpers import PredictParams, safe_get_key, make_df
from source.back.data_process import DataProcess
from source.back.models._model import BaseModel


class Model(BaseModel):
    # Params:
    # {
    #     "trend": cfg.ETSTrend,
    #     "dumped": bool
    # }

    def __init__(self, params: dict):
        self.model = None
        self.df = None
        self.filtered_columns = None
        self.shift = None

        self.trend: cfg.ETSTrend = safe_get_key(params, 'trend', 'No key trend in ETS params')
        self.dumped = safe_get_key(params, 'dumped', 'No key dumped in ETS params')

    def load(self, params: PredictParams):
        if params.upload:
            loaded_df = make_df(params.uploaded_data, params.start_date, params.end_date)
        else:
            loaded_df = DataProcess.load_data_from_moex(params.ticker, params.start_date, params.end_date,
                                                        params.offset.value)
        self.df = loaded_df[loaded_df.columns[0]].reset_index(drop=True)

    def train(self, shift: int):
        if self.trend != cfg.ETSTrend.no_trend:
            self.model = sm.tsa.ExponentialSmoothing(self.df, trend=self.trend.value, damped_trend=self.dumped,
                                                     initialization_method='estimated').fit()
        else:
            self.model = sm.tsa.ExponentialSmoothing(self.df, initialization_method='estimated').fit()

        self.shift = shift

    def predict(self):
        tmp = self.model.forecast(self.shift)
        return tmp.iloc[-1]

    def train_and_predict(self, period: int):
        self.train(period)
        return self.model.forecast(period)
