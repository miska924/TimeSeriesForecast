import source.config as cfg
from PyQt5 import QtWidgets, QtGui, QtWebEngineWidgets

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

if correct_color.red() > 127:
    error_color = "red"
else:
    error_color = "red"

correct_color = correct_color.name()