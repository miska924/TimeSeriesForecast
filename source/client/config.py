import source.config as cfg
from PyQt5 import QtWidgets, QtGui, QtWebEngineWidgets
import numpy as np

TRANSLATE = {
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