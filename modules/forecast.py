# targets -- целевые переменыне",
# regressors -- зависимые переменные",
class ForecastModule:
    def __init__(self, target_name, targets, regressors):
        Y = targets[target_name]
        X = regressors[target_name]
        self.data = pd.concat([Y,X])

    def data_process(self):
    #    2) m лагов y
    #    3) p лагов каждого X_j
    #    4) Среднее значение Y за k дней
        self.dataset = # Ваш датасет с фичами

    def select_features(self, threshold=0.1):
        # self.dataset -> фильтрация -> маска фичей
        # [True]*len(self.dataset.columns)

    def fit_predict_lr(self, train, test):
        return fit_predict

    def direct_dataset_processing(self, H):
        for h in H:
            yield train, test




