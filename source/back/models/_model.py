import numpy as np
import pandas as pd
import sklearn.metrics as metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from source._helpers import PredictParams


class BaseModel:

    def load(self, params: PredictParams):
        raise NotImplementedError()

    def train(self, shift: int):
        raise NotImplementedError()

    def predict(self):
        raise NotImplementedError()

    # returns string with values of the main metrics of the result
    @staticmethod
    def _regression_results(y_test, y_pred) -> str:
        # Regression metrics
        explained_variance = metrics.explained_variance_score(y_test, y_pred)
        mean_absolute_error = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        mean_squared_log_error = metrics.mean_squared_log_error(y_test, y_pred)
        median_absolute_error = metrics.median_absolute_error(y_test, y_pred)
        r2 = metrics.r2_score(y_test, y_pred)

        return (f"""
        explained_variance: {round(explained_variance, 4)}
        mean_absolute_error: {round(mean_absolute_error, 4)}
        mean_squared_log_error: {round(mean_squared_log_error, 4)}
        median_absolute_error: {round(median_absolute_error, 4)}
        MSE: {round(mse, 4)}
        r2: {round(r2, 4)}
        """)
