from dataclasses import dataclass
from typing import List
from PyQt5 import QtWidgets, QtGui
import numpy as np

import source.config as cfg

@dataclass
class ModelParams:
    backend: cfg.Model
    widgets: List[str]
    params: List[str]


class TRANSLATE:
    Model = {
        "Линейная регрессия" : ModelParams(
            backend=cfg.Model.linear_reg, 
            widgets=["exogenous_wrapper"],
            params=["exogenous_variables"]
        ),
        "Наивная модель" : ModelParams(
            backend=cfg.Model.naive, 
            widgets=[],
            params=[]
        ),
        "Стационарный лин. рег.": ModelParams(
            backend=cfg.Model.stationary_linear_regression,
            widgets=["exogenous_wrapper"],
            params=["exogenous_variables"]
        ),
        "Волшебный Ансамбль": ModelParams(
            backend=cfg.Model.ansamble,
            widgets=["exogenous_wrapper"]
        ),
        "ETS": ModelParams(
            backend=cfg.Model.ets,
            widgets=["ets_wrapper"],
            params=["trend", "dumped"]
        )
    }

    Method = {
        "Прямой": cfg.Methods.straight,
        "Рекурсивный": cfg.Methods.recursive
    }

    Type = {
        "Значения": cfg.Type.values,
        "Тренд": cfg.Type.trend
    }

    Offset = {
        "День": cfg.Offset.business_day,
        "Неделя": cfg.Offset.week,
        "Месяц": cfg.Offset.business_month,
        "Год": cfg.Offset.business_year
    }

    ETSTrend = {
        "Аддитивный": cfg.ETSTrend.additive,
        "Мультипликативный": cfg.ETSTrend.multiplicative
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
