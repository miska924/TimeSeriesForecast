from source._helpers import PredictParams
from source.back.models._model import BaseModel
from source.back.models.ensemble import Model as EnsembleModel
from source import config as cfg


class Model(BaseModel):
    # Params:
    # {
    #     "exogenous_variables": list
    # }

    def __init__(self, params: dict):
        self.ensemble = EnsembleModel(
            models=(cfg.Model.linear_reg, cfg.Model.stationary_linear_regression),
            coefs=(0.4, 0.6),
            params=(params, params)
        )

    def load(self, params: PredictParams):
        self.ensemble.load(params)

    def train(self, shift: int):
        self.ensemble.train(shift)

    def predict(self):
        return self.ensemble.predict()

    def train_and_predict(self, period: int):
        return self.ensemble.train_and_predict(period)
