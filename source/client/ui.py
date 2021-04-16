from PyQt5 import QtWidgets, QtGui, QtCore
from source.client.design import Ui_MainWindow
import sys
import source._helpers as hlp
import source.client.config as ui_cfg
import source.config as cfg
# TEST
import plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd

class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("TimeSeries Forecast")

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

        self.ui.pushButton.clicked.connect(self.predict_series)

    @QtCore.pyqtSlot(str)
    def change_exogenous(self, ticker : str):
        self.ui.listWidget.clear()
        if (ticker):
            self.ui.listWidget.addItems(cfg.TICKERS[ticker])

    def predict_series(self):
        params = hlp.PredictParams(
            self.ui.comboBox_series.currentText(),
            self.ui.comboBox_model.currentText(),
            [self.ui.listWidget.item(i).text() for i in range(self.ui.listWidget.count())],
            self.ui.comboBox_metric.currentText(),
            self.ui.comboBox_method.currentText(),
            self.ui.comboBox_type.currentText(), 
            self.ui.dateEdit_start.date().toString("yyyy-MM-dd"),
            self.ui.dateEdit_end.date().toString("yyyy-MM-dd"),
            ui_cfg.TRANSLATE[self.ui.comboBox_offset.currentText()]
        )
        
        # Getting forecast and timeseries from backend
        
        # Example
        x = np.arange(0, 30, 0.1)
        def f(x):
            return x * (1 + np.sin(x))
            
        fig = go.Figure()
        # fig.show()

        fig.add_trace(go.Scatter(x=x[:100], y=f(x[:100]), mode='lines', name='Known values'))
        fig.add_trace(go.Scatter(x=x[100:], y=x[100:], mode='lines', name='Forecast'))
        fig.update_layout(
            title={
                'text': self.ui.comboBox_series.currentText(),
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(size=40)
            },
            xaxis_title={
                "text" : "Timeline",
                "font" : dict(size=20)
            },
            yaxis_title={
                "text" : "Value",
                "font" : dict(size=20)
            }
        )
        # fig = Figure(Scatter(x=x, y=y))
        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'
        
        self.ui.webView.setHtml(html)


app = QtWidgets.QApplication([])
application = GUI()
application.show()

sys.exit(app.exec())