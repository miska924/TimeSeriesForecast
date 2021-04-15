from PyQt5 import QtWidgets, QtGui, QtCore
from source.client.design import Ui_MainWindow
import sys
import source._helpers as hlp
import source.client.config as ui_cfg
import source.config as cfg


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox_series.addItem("")
        self.ui.comboBox_model.addItem("")
        self.ui.comboBox_metric.addItem("")
        self.ui.comboBox_method.addItem("")
        self.ui.comboBox_type.addItem("")
        self.ui.comboBox_offset.addItem("")

        self.ui.comboBox_series.addItems(cfg.TICKERS.keys())
        self.ui.comboBox_model.addItems(hlp.get_values(cfg.Model))
        self.ui.comboBox_metric.addItems(hlp.get_values(cfg.Metrics))
        self.ui.comboBox_method.addItems(hlp.get_values(cfg.Methods))
        self.ui.comboBox_type.addItems(hlp.get_values(cfg.Type))
        self.ui.comboBox_offset.addItems(ui_cfg.TRANSLATE.keys())

        self.ui.comboBox_series.currentTextChanged.connect(self.change_exogenous)

    @QtCore.pyqtSlot(str)
    def change_exogenous(self, ticker):
        self.ui.listWidget.clear()
        if (ticker):
            self.ui.listWidget.addItems(cfg.TICKERS[ticker])

app = QtWidgets.QApplication([])
application = GUI()
application.show()

sys.exit(app.exec())