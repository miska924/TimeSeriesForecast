from dataclasses import dataclass
from typing import Dict, List
from PyQt5 import QtWidgets, QtGui
import numpy as np

import source.config as cfg

@dataclass
class ModelParams:
    backend: cfg.Model
    widgets: List[str]
    params: List[str]
    metrics: Dict[str, any]


class TRANSLATE:
    Model = {
        "Линейная регрессия" : ModelParams(
            backend=cfg.Model.linear_reg, 
            widgets=["exogenous_wrapper"],
            params=["exogenous_variables"],
            metrics={}
        ),
        "Наивная модель" : ModelParams(
            backend=cfg.Model.naive, 
            widgets=[],
            params=[],
            metrics={}
        ),
        "Стационарный лин. рег.": ModelParams(
            backend=cfg.Model.stationary_linear_regression,
            widgets=["exogenous_wrapper"],
            params=["exogenous_variables"],
            metrics={}
        ),
        "Волшебный Ансамбль": ModelParams(
            backend=cfg.Model.magic_ensemble,
            widgets=["exogenous_wrapper"],
            params=["exogenous_variables"],
            metrics={}
        ),
        "ETS": ModelParams(
            backend=cfg.Model.ets,
            widgets=["ets_wrapper"],
            params=["trend", "dumped"],
            metrics={}
        ),
        "Случайный лес": ModelParams(
            backend = cfg.Model.random_forest_regressor,
            widgets=[
                "exogenous_wrapper",
                "estimators_wrapper", 
                "metric_wrapper", 
                "min_samples_leaf_wrapper", 
                "max_samples_wrapper"
            ],
            params=[
                "exogenous_variables", 
                "n_estimators", 
                "criterion", 
                "min_samples_leaf", 
                "max_samples"
            ],
            metrics={
                "MSE": cfg.RFCriterion.mse,
                "MAE": cfg.RFCriterion.mae
            }
        )
    }

    Offset = {
        "День": cfg.Offset.business_day,
        "Неделя": cfg.Offset.week,
        "Месяц": cfg.Offset.business_month,
        "Год": cfg.Offset.business_year
    }

    ETSTrend = {
        "Аддитивный": cfg.ETSTrend.additive,
        "Мультипликативный": cfg.ETSTrend.multiplicative,
        "Без тренда": cfg.ETSTrend.no_trend
    }

tmp_app = QtWidgets.QApplication([])
tmp = QtWidgets.QWidget()
correct_color = tmp.palette().color(QtGui.QPalette.Window)
del tmp
del tmp_app

correct_vect = np.array(correct_color.getRgb()[:3])
red_vect = np.array([255, 0, 0])
red_vect = np.round(red_vect + (correct_vect - red_vect) * 0.3)
error_color = QtGui.QColor(*red_vect).name()

correct_color = correct_color.name()
