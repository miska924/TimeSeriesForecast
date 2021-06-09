from sklearn.ensemble import RandomForestRegressor

from source._helpers import PredictParams, safe_get_key, make_df
from source.back.data_process import DataProcess
from source.back.models._model import BaseModel


class Model(BaseModel):
    # Params:
    # {
    #     "exogenous_variables": list,
    #     "n_estimators": int,
    #     "criterion": cfg.RFCriterion,
    #     "min_samples_leaf": float,
    #     "max_samples" : float,
    # }

    def __init__(self, params: dict):
        self.model = None
        self.df = None
        self.filtered_columns = None

        self.exogenous_variables = safe_get_key(params, 'exogenous_variables',
                                                'No key exogenous_variables in random forest regressor')
        self.n_estimators = safe_get_key(params, 'n_estimators',
                                         'No key n_estimators in random forest regressor params')
        self.criterion = safe_get_key(params, 'criterion', 'No key criterion in random forest regressor params')
        self.min_samples_leaf = safe_get_key(params, 'min_samples_leaf',
                                             'No key min_samples_leaf in random forest regressor params') / 100
        self.max_samples = safe_get_key(params, 'max_samples',
                                        'No key max_samples in random forest regressor params') / 100
        self.max_samples = self.max_samples if self.max_samples != 1 else None

    def load(self, params: PredictParams):
        if params.upload:
            loaded_df = make_df(params.uploaded_data, params.start_date, params.end_date)
        else:
            loaded_df = DataProcess.load_data_from_moex(params.ticker, params.start_date, params.end_date,
                                                        params.offset.value, self.exogenous_variables)
        self.df = DataProcess.get_prepared_data_frame(loaded_df, predict_day=0)

    def train(self, shift: int):
        df_copy = self.df.copy()
        for col in df_copy.columns:
            if col != 'Y':
                df_copy[col] = df_copy[col].shift(shift)
        df_copy = df_copy.dropna(axis=0, how='any')
        self.filtered_columns = DataProcess.get_filtered_data_frame_columns(df_copy, mrmr=False)

        df_copy = df_copy[self.filtered_columns].to_numpy()
        x = df_copy[:, 1:]
        y = df_copy[:, 0]
        self.model = RandomForestRegressor(n_estimators=self.n_estimators, criterion=self.criterion.value,
                                           min_samples_leaf=self.min_samples_leaf, bootstrap=True,
                                           max_samples=self.max_samples, n_jobs=1)
        self.model.fit(x, y)

    def predict(self):
        try:
            return self.model.predict(self.df.tail(1)[self.filtered_columns[1:]])[0]
        except Exception as e:
            print(self.df.tail(1)[self.filtered_columns[1:]])
            raise e
