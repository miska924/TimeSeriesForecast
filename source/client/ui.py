import json
from os import error
import time
import requests
import sys

from PyQt5 import QtWidgets, QtCore, QtGui

import plotly
import plotly.graph_objs as go

from source.back import back
import source._helpers as hlp
from source._helpers import send_request
import source.client.config as ui_cfg
import source.config as cfg
from source.client.design import Ui_MainWindow
import source.client.custom_widgets as cw


class GUI(QtWidgets.QMainWindow):
    def __init__(self, test):
        super(GUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("TimeSeries Forecast")

        self.lineEdits = [self.ui.lineEdit_series]
        self.comboBoxes_general = [
            self.ui.comboBox_model,
            self.ui.comboBox_method,
            self.ui.comboBox_type,
            self.ui.comboBox_offset
        ]
        self.comboBoxes_cv = [self.ui.comboBox_metric]
        self.spinBoxes = [self.ui.spinBox_shift, self.ui.spinBox_period, self.ui.spinBox_preddays]

        if not test:
            for cb in self.comboBoxes_general:
                cb.addItem("")
            for cb in self.comboBoxes_cv:
                cb.addItem("")
                

        self.ui.comboBox_model.addItems(ui_cfg.TRANSLATE.Model.value.keys())
        self.ui.comboBox_metric.addItems(ui_cfg.TRANSLATE.Metrics.value.keys())
        self.ui.comboBox_method.addItems(ui_cfg.TRANSLATE.Method.value.keys())
        self.ui.comboBox_type.addItems(ui_cfg.TRANSLATE.Type.value.keys())
        self.ui.comboBox_offset.addItems(ui_cfg.TRANSLATE.Offset.value.keys())

        cur = QtCore.QDate.currentDate()
        self.ui.dateEdit_forecast.setDate(cur)
        cur = cur.addDays(-30 if test else -7)
        self.ui.dateEdit_end.setDate(cur)
        cur = cur.addYears(-2)
        self.ui.dateEdit_start.setDate(cur)

        self.ui.listWidget.__class__ = cw.List

        self.ui.cv_wrapper.hide()

        self.ui.listWidget.delete.connect(self.del_exogenous)
        self.ui.pushButton_forecast.clicked.connect(self.predict_series)
        self.ui.pushButton_add_ex.clicked.connect(self.add_exogenous)
        self.ui.lineEdit_exogenous.returnPressed.connect(self.add_exogenous)
        self.ui.pushButton_del_ex.clicked.connect(self.del_exogenous)
        self.ui.checkBox_cv.stateChanged.connect(self.update_cv)


    def add_exogenous(self):
        if self.ui.lineEdit_exogenous.text():
            self.ui.listWidget.insertItem(0, self.ui.lineEdit_exogenous.text())
        self.ui.lineEdit_exogenous.clear()

    def del_exogenous(self):
        selected = self.ui.listWidget.selectedItems()
        for item in selected:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def update_cv(self, state):
        if state:
            self.ui.cv_wrapper.show()
            self.ui.pushButton_forecast.setText("Оценить")
        else:
            self.ui.cv_wrapper.hide()
            self.ui.pushButton_forecast.setText("Спрогнозировать")

    def paint_widget(self, widget, color: str):
        widget_name = widget.objectName() + "_wrapper"
        widget = self.ui.centralwidget.findChild(QtWidgets.QWidget, widget_name)
        widget.setStyleSheet(
            "QWidget#" + widget_name + " {\n"
            "border: 2px solid " + color + ";\n"
            "border-radius: 5px;\n"
            "}"
        )

    def check_correct(self, widget, data):
        if not data:
            self.paint_widget(widget, ui_cfg.error_color)
            return False
        else:
            self.paint_widget(widget, ui_cfg.correct_color)
            return True

    def plot(self, data):
        x, y, x_pred, y_pred = data["X"], data["Y"], data["PredictedX"], data["PredictedY"]

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Known values'))
        fig.add_trace(go.Scatter(x=x_pred, y=y_pred, mode='lines', name='Forecast'))
        fig.update_layout(
            title={
                'text': self.ui.lineEdit_series.text(),
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
    def get_html_table_row(contents, header: bool = False):
        res = "<tr>"
        sep_start = "<th>" if header else "<td>"
        sep_end = "</th>" if header else "</td>"
        for elem in contents:
            res += sep_start + elem + sep_end
        res += "</tr>"
        return res
        
    @staticmethod
    def prettify_cv_data(errors):
        errors['mape'] = f"{errors['mape'] * 100 :.{3}f}%"
        errors['mse'] = f"{errors['mse']:.{3}f}"

    def print_cv(self, model: str, error_model, baseline: str, error_baseline):
        self.prettify_cv_data(error_model)
        self.prettify_cv_data(error_baseline)
        headers = ["Model"] + [error for error in error_model.keys()]
        contents = [
            [model],
            [baseline]
        ]
        for i in range(1, len(headers)):
            contents[0].append(error_model[headers[i]])
        for i in range(1, len(headers)):
            contents[1].append(error_baseline[headers[i]])
            headers[i] = headers[i].upper()
        HTML = """
<!DOCTYPE html>
<html>
<head>
    <style>
        table {
            width:100%;
        }
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 15px;
            text-align: left;
        }
        tr:nth-child(even) {
            background-color: #eee;
        }
        tr:nth-child(odd) {
            background-color: #fff;
        }
    </style>
</head>
<body>

<h1>Cross-validation results</h1>

<table>
"""
        HTML += self.get_html_table_row(headers, True)
        HTML += self.get_html_table_row(contents[0])
        HTML += self.get_html_table_row(contents[1])
        HTML += """
</table>

</body>
</html>
        """
        self.ui.webView.setHtml(HTML)
        

    def handle_errors(self):
        flag_correct = True

        for le in self.lineEdits:
            if not self.check_correct(le, le.text()):
                flag_correct = False
        
        for cb in self.comboBoxes_general:
            if not self.check_correct(cb, cb.currentText()):
                flag_correct = False

        dates = [
            self.ui.dateEdit_start.date(), 
            self.ui.dateEdit_end.date(), 
            self.ui.dateEdit_forecast.date()
        ]
        cur = QtCore.QDate.currentDate()
        
        flag_start = dates[0] <= cur and dates[0] not in dates[1:]
        flag_end = dates[1] <= cur and dates[1] not in [dates[0], dates[2]]
        flag_forecast = dates[2] not in dates[:2]

        flag_start &= (dates[0] < dates[1]) and (dates[0] < dates[2])
        flag_end &= (dates[1] > dates[0]) and (dates[1] < dates[2])
        flag_forecast &= (dates[2] > dates[1]) and (dates[2] > dates[0])

        self.check_correct(self.ui.dateEdit_start, flag_start)
        self.check_correct(self.ui.dateEdit_end, flag_end)
        self.check_correct(self.ui.dateEdit_forecast, flag_forecast)

        flag_correct &= flag_start & flag_end & flag_forecast

        if self.ui.checkBox_cv.isChecked():
            for cb in self.comboBoxes_cv:
                if not self.check_correct(cb, cb.currentText()):
                    flag_correct = False

            for sb in self.spinBoxes:
                if not self.check_correct(sb, sb.value()):
                    flag_correct = False

        return flag_correct

    def predict_series(self):
        if not self.handle_errors():
            print("WARNING: Incorrect input!")
            return

        params = hlp.PredictParams(
            self.ui.lineEdit_series.text(),
            ui_cfg.TRANSLATE.Model.value[self.ui.comboBox_model.currentText()],
            [self.ui.listWidget.item(i).text() for i in range(self.ui.listWidget.count())],
            ui_cfg.TRANSLATE.Metrics.value[self.ui.comboBox_metric.currentText()],
            ui_cfg.TRANSLATE.Method.value[self.ui.comboBox_method.currentText()],
            ui_cfg.TRANSLATE.Type.value[self.ui.comboBox_type.currentText()],
            self.ui.dateEdit_start.date().toString("yyyy-MM-dd"),
            self.ui.dateEdit_end.date().toString("yyyy-MM-dd"),
            self.ui.dateEdit_forecast.date().toString("yyyy-MM-dd"),
            ui_cfg.TRANSLATE.Offset.value[self.ui.comboBox_offset.currentText()],
            self.ui.spinBox_shift.value(),
            self.ui.spinBox_period.value(),
            self.ui.spinBox_preddays.value()
        )

        print(params.__dict__)
        if self.ui.checkBox_cv.isChecked():
            data_cur = self.process_request(params, "cross-validate")
            data_baseline = self.process_request(params, "cross-validate")
            print(data_cur)
            print(data_baseline)
            if not data_cur or not data_baseline:
                return
            self.print_cv(
                self.ui.comboBox_model.currentText(),
                data_cur['data'],
                "Наивная модель",
                data_baseline['data']
            )

    def process_request(self, params: hlp.PredictParams, request: str) -> any:
        headers = {'Content-type': 'application/json'}
        req_res = send_request(
            method='POST', 
            url='http://158.101.168.149:8080/' + request, 
            headers=headers,
            data=json.dumps(params.__dict__, cls=hlp.EnumEncoder)
        )
        while not req_res.get('success', False):
            req_res = send_request(
                method='POST', 
                url='http://158.101.168.149:8080/' + request, 
                headers=headers,
                data=json.dumps(params.__dict__, cls=hlp.EnumEncoder)
            )
            time.sleep(1)
        data = self.get_request(req_res['id'])
        if data.get('status', None) is not cfg.Status.ready:
            print(data)
            return None
        else:
            return data

    @staticmethod
    def get_request(uid):
        params = {
            'id': uid
        }
        res = send_request(method='GET', url='http://158.101.168.149:8080/get', params=params)
        while res.get('status', cfg.Status.fail) in [cfg.Status.wait, cfg.Status.process]:
            res = send_request(method='GET', url='http://158.101.168.149:8080/get', params=params)
            time.sleep(1)
        return res


if __name__ == '__main__':
    test = False
    if len(sys.argv) > 1:
        test = (sys.argv[1] == '--test')
    app = QtWidgets.QApplication([])
    application = GUI(test)
    application.show()

    sys.exit(app.exec())
