from source._helpers import PredictParams
from source.back.data_process import DataProcess
from source.back.models._model import BaseModel

import source.back.models
from source import config as cfg


class Model(BaseModel):
    # Params:
    # {
    #
    # }

    def __init__(self, models=(cfg.Model.linear_reg, cfg.Model.stationary_linear_regression), coefs=(0.4, 0.6), params=({}, {})):
        if len(models) != len(coefs):
            raise Exception("invalid argumets. lengths of lists do not match!")
        self.models = []
        for model in models:
            self.models.append(getattr(source.back.models, model.value).Model())

        self.coefs = coefs

    def load(self, params: PredictParams):
        for model in self.models:
            model.load(params)

    def train(self, shift: int):
        for model in self.models:
            model.train(shift)

    def predict(self):
        res = 0.0
        for i, model in enumerate(self.models):
            res += model.predict() * self.coefs[i]

        return res / sum(self.coefs)

    def train_and_predict(self, period: int):
        res = [0] * period
        coefs_sum = sum(self.coefs)
        for i, model in enumerate(self.models):
            for j, value in enumerate(model.train_and_predict(period)):
                res[j] += value * self.coefs[i] / coefs_sum

        return res
