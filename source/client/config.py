import source.config as cfg
from PyQt5 import QtWidgets, QtGui, QtWebEngineWidgets

TRANSLATE = {
    "День": cfg.Offset.business_day,
    "Неделя": cfg.Offset.week,
    "Месяц": cfg.Offset.business_month,
    "Год": cfg.Offset.business_year
}

error_color = QtGui.QColor(255, 209, 220)
tmp_app = QtWidgets.QApplication([])
tmp = QtWidgets.QComboBox()
correct_cb_color = tmp.palette().color(QtGui.QPalette.Button)
tmp = QtWidgets.QLineEdit()
correct_le_color = tmp.palette().color(QtGui.QPalette.Base)
tmp = QtWidgets.QDateEdit()
correct_de_color = tmp.palette().color(QtGui.QPalette.Base)
del tmp_app
del tmp
