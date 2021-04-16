import numpy as np
import pandas as pd
import sklearn.metrics as metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


class Models:
    # trains linear regression model and runs it on test data
    # returns string with values of the main metrics of the result
    @staticmethod
    def test_linear_regression(data: pd.DataFrame, test_size=0.33, random_state=42):
        data = data.to_numpy()
        x = data[:, 1:]
        y = data[:, 0]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)
        model = Models.train_linear_regression(x_train, y_train)
        y_pred = model.predict(x_test)

        return Models._regression_results(y_test, y_pred)

    # trains liner regression model on given data and returns it
    @staticmethod
    def train_linear_regression(x: np.ndarray, y: np.ndarray) -> LinearRegression:
        model = LinearRegression()
        model.fit(x, y)

        return model

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
