from dataclasses import dataclass
from typing import List
import source.config as cfg
from PyQt5 import QtWidgets, QtGui, QtWebEngineWidgets
import numpy as np
import enum

@dataclass
class ModelParams:
    backend: cfg.Model
    widgets: List[str]

    def __init__(self, backend: cfg.Model, widgets: List[str]):
        self.backend = backend
        self.widgets = widgets

class TRANSLATE(enum.Enum):
    Model = {
        "Линейная регрессия" : ModelParams(
            backend=cfg.Model.linear_reg, 
            widgets=["exogenous_wrapper"]
        ),
        "Наивная модель" : ModelParams(
            backend=cfg.Model.naive, 
            widgets=[]
        ),
        "Стационарный лин. рег.": ModelParams(
            backend=cfg.Model.stationary_linear_regression,
            widgets=["exogenous_wrapper"]
        ),
        "Волшебный Ансамбль": ModelParams(
            backend=cfg.Model.ansamble,
            widgets=["exogenous_wrapper"]
        )
    }
    Metrics = {
        "MSE": cfg.Metrics.mse
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
