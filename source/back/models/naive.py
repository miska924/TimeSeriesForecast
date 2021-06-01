from source._helpers import PredictParams, make_df
from source.back.data_process import DataProcess
from source.back.models._model import BaseModel


class Model(BaseModel):
    # Params:
    # {
    #
    # }

    def __init__(self, params: dict):
        self.model = None
        self.df = None
        self.filtered_columns = None

    def load(self, params: PredictParams):
        if params.upload:
            loaded_df = make_df(params.uploaded_data, params.start_date, params.end_date)
        else:
            loaded_df = DataProcess.load_data_from_moex(params.ticker, params.start_date, params.end_date,
                                                        params.offset.value)
        self.df = DataProcess.get_prepared_data_frame(loaded_df, predict_day=0)

    def train(self, shift: int):
        pass

    def predict(self):
        return self.df['Y'][-1]
