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
        "Linear regression" : ModelParams(
            backend=cfg.Model.linear_reg, 
            widgets=["exogenous_wrapper"],
            params=["exogenous_variables"],
            metrics={}
        ),
        "Naive model" : ModelParams(
            backend=cfg.Model.naive, 
            widgets=[],
            params=[],
            metrics={}
        ),
        "Lin. reg. on derivative": ModelParams(
            backend=cfg.Model.stationary_linear_regression,
            widgets=["exogenous_wrapper"],
            params=["exogenous_variables"],
            metrics={}
        ),
        "Magic Ensemble": ModelParams(
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
        "Random forest": ModelParams(
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
        ),
        "Gradient boosting": ModelParams(
            backend=cfg.Model.gradient_boosting_regressor,
            widgets=[
                "exogenous_wrapper",
                "loss_wrapper",
                "learning_rate_wrapper",
                "estimators_wrapper",
                "metric_wrapper",
                "min_samples_leaf_wrapper"
            ],
            params=[
                "exogenous_variables",
                "loss",
                "learning_rate",
                "n_estimators",
                "criterion",
                "min_samples_leaf",
                "alpha"
            ],
            metrics={
                "Friedman MSE": cfg.GBCriterion.friedman_mse,
                "MSE": cfg.GBCriterion.mse,
                "MAE": cfg.GBCriterion.mae
            }
        )
    }

    Offset = {
        "Day": cfg.Offset.business_day,
        "Week": cfg.Offset.week,
        "Month": cfg.Offset.business_month,
        "Year": cfg.Offset.business_year
    }

    ETSTrend = {
        "Additive": cfg.ETSTrend.additive,
        "Multiplicative": cfg.ETSTrend.multiplicative,
        "No trend": cfg.ETSTrend.no_trend
    }

    GBLoss = {
        "Least squares": cfg.GBLoss.ls,
        "Least absolute deviation": cfg.GBLoss.lad,
        "Huber": cfg.GBLoss.huber,
        "Quantile": cfg.GBLoss.quantile
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
