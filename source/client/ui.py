import time

import requests
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import plotly
import plotly.graph_objs as go

from source.back import back

import source._helpers as hlp
from source._helpers import send_request

import source.client.config as ui_cfg
import source.config as cfg
from source.client.design import UiMainWindow

class GUI(QtWidgets.QMainWindow):
    def __init__(self, test):
        super(GUI, self).__init__()
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.setWindowTitle("TimeSeries Forecast")

        if not test:
            self.ui.comboBox_model.addItem("")
            self.ui.comboBox_metric.addItem("")
            self.ui.comboBox_method.addItem("")
            self.ui.comboBox_type.addItem("")
            self.ui.comboBox_offset.addItem("")

        self.ui.comboBox_model.addItems(hlp.get_values(cfg.Model))
        self.ui.comboBox_metric.addItems(hlp.get_values(cfg.Metrics))
        self.ui.comboBox_method.addItems(hlp.get_values(cfg.Methods))
        self.ui.comboBox_type.addItems(hlp.get_values(cfg.Type))
        self.ui.comboBox_offset.addItems(ui_cfg.TRANSLATE.keys())
        
        if test:
            cur = QtCore.QDate.currentDate()
            print(type(cur))
            self.ui.dateEdit_forecast.setDate(cur)
            cur = cur.addDays(-5)
            self.ui.dateEdit_end.setDate(cur)
            cur = cur.addYears(-2)
            self.ui.dateEdit_start.setDate(cur)

        class List(QtWidgets.QListWidget):
            delete = QtCore.pyqtSignal()

            def __new__(cls, a):
                a.__class__ = cls
                return a

            def keyPressEvent(self, event):
                if event.key() == QtCore.Qt.Key_Delete:
                    self.delete.emit()

        self.ui.listWidget = List(self.ui.listWidget)
        self.ui.listWidget.delete.connect(self.del_exogenous)
        self.ui.listWidget.setSelectionMode(QtWidgets.QListWidget.MultiSelection)

        self.ui.pushButton_forecast.clicked.connect(self.predict_series)
        self.ui.pushButton_add_ex.clicked.connect(self.add_exogenous)
        self.ui.lineEdit_exogenous.returnPressed.connect(self.add_exogenous)
        self.ui.pushButton_del_ex.clicked.connect(self.del_exogenous)

    def add_exogenous(self):
        if self.ui.lineEdit_exogenous.text():
            self.ui.listWidget.insertItem(0, self.ui.lineEdit_exogenous.text())
        self.ui.lineEdit_exogenous.clear()

    def del_exogenous(self):
        selected = self.ui.listWidget.selectedItems()
        for item in selected:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def paint_widget(self, widget, color, role=QtGui.QPalette.Button):
        pal = widget.palette()
        pal.setColor(role, QtGui.QColor(*color))
        widget.setPalette(pal)
    
    def check_empty(self, cb):
        if not cb.currentText():
            self.paint_widget(cb, ui_cfg.error_color)        
            return True
        else:
            self.paint_widget(cb, ui_cfg.correct_cb_color)
            return False

    def predict_series(self):
        flag_correct = True
        for widget in self.ui.horizontalFrame.children():
            if isinstance(widget, QtWidgets.QComboBox):
                if self.check_empty(widget):
                    flag_correct = False
        if self.ui.dateEdit_end.date() <= self.ui.dateEdit_start.date():
            flag_correct = False
            self.paint_widget(self.ui.dateEdit_end, ui_cfg.error_color, QtGui.QPalette.Base)
        else:
            self.paint_widget(self.ui.dateEdit_end, ui_cfg.correct_de_color, QtGui.QPalette.Base)

        if self.ui.dateEdit_forecast.date() <= self.ui.dateEdit_end.date() or \
                            self.ui.dateEdit_forecast.date() <= self.ui.dateEdit_start.date():
            flag_correct = False
            self.paint_widget(self.ui.dateEdit_forecast, ui_cfg.error_color, QtGui.QPalette.Base)
        else:
            self.paint_widget(self.ui.dateEdit_forecast, ui_cfg.correct_de_color, QtGui.QPalette.Base)
        if not flag_correct:
            print("WARNING: Incorrect input!")
            return

        
        params = hlp.PredictParams(
            self.ui.comboBox_series.currentText(),
            self.ui.comboBox_model.currentText(),
            [self.ui.listWidget.item(i).text() for i in range(self.ui.listWidget.count())],
            self.ui.comboBox_metric.currentText(),
            self.ui.comboBox_method.currentText(),
            self.ui.comboBox_type.currentText(),
            self.ui.dateEdit_start.date().toString("yyyy-MM-dd"),
            self.ui.dateEdit_end.date().toString("yyyy-MM-dd"),
            self.ui.dateEdit_forecast.date().toString("yyyy-MM-dd"),
            ui_cfg.TRANSLATE[self.ui.comboBox_offset.currentText()]
        )

        # Getting forecast and time series from backend
        req_res = self._predict_request(params)
        while not req_res.get('success', False):
            req_res = self._predict_request(params)
            time.sleep(1)

        print(req_res)
        data = self._get_request(req_res['id'])

        if data.get('status', None) is not cfg.Status.ready:
            print(data)
            return

        data = data['data']
        x, y, x_pred, y_pred = data["X"], data["Y"], data["PredictedX"], data["PredictedY"]

        print(x, y)

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Known values'))
        fig.add_trace(go.Scatter(x=x_pred, y=y_pred, mode='lines', name='Forecast'))
        fig.update_layout(
            title={
                'text': self.ui.comboBox_series.currentText(),
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(size=40)
            },
            xaxis_title={
                "text": "Timeline",
                "font": dict(size=20)
            },
            yaxis_title={
                "text": "Value",
                "font": dict(size=20)
            }
        )
        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        self.ui.webView.setHtml(html)

    @staticmethod
    def _predict_request(params):
        return send_request(method='POST', url='http://158.101.168.149:8080/predict', data=params.__dict__)

    @staticmethod
    def _get_request(uid):
        params = {
            'id': uid
        }
        res = send_request(method='GET', url='http://158.101.168.149:8080/get', params=params)
        while res.get('status', cfg.Status.fail) in [cfg.Status.wait, cfg.Status.process]:
            res = send_request(method='GET', url='http://158.101.168.149:8080/get', params=params)
            time.sleep(20)
        return res


if __name__ == '__main__':
    test = False
    if len(sys.argv) > 1:
        test = (sys.argv[1] == '--test')
    app = QtWidgets.QApplication([])
    application = GUI(test)
    application.show()

    sys.exit(app.exec())
