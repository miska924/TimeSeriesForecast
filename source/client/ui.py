import json
import time
import sys
from functools import partial
from typing import List
import csv

from PyQt5 import QtWidgets, QtCore

import plotly
import plotly.graph_objs as go

import source._helpers as hlp
from source._helpers import send_request
import source.client.config as ui_cfg
import source.config as cfg
from source.client.design import Ui_MainWindow
import source.client.custom_widgets as cw
from source.client.multithreading import Worker
import source.client.helpers as ui_hlp


class GUI(QtWidgets.QMainWindow):
    def __init__(self, test):
        super(GUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("TimeSeries Forecast")
        self.test_flag = test

        self.comboBoxes_general = [self.ui.comboBox_model, self.ui.comboBox_offset]
        self.spinBoxes = [self.ui.spinBox_period, self.ui.spinBox_shift, self.ui.spinBox_preddays]

        self.ui.horizontalWidget_series_wrapper.hide()
        self.filename = "Upload series"
        self.uploaded_data = []
        if test:
            self.home_loc = ""
        else:
            self.home_loc = QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.HomeLocation)[0]

        if not test:
            for cb in self.comboBoxes_general:
                cb.addItem("")            
            self.ui.comboBox_trend.addItem("") 
            self.ui.comboBox_loss.addItem("")

        self.ui.comboBox_model.addItems(ui_cfg.TRANSLATE.Model.keys())
        self.ui.comboBox_offset.addItems(ui_cfg.TRANSLATE.Offset.keys())
        self.ui.comboBox_trend.addItems(ui_cfg.TRANSLATE.ETSTrend.keys())
        self.ui.comboBox_loss.addItems(ui_cfg.TRANSLATE.GBLoss.keys())

        self.ui.spinBox_estimators.setMinimum(1)
        self.ui.spinBox_estimators.setMaximum(1000)
        self.ui.doubleSpinBox_leaf.setMinimum(0.01)
        self.ui.doubleSpinBox_leaf.setMaximum(50)
        self.ui.doubleSpinBox_samples.setMinimum(0.01)
        self.ui.doubleSpinBox_samples.setMaximum(100)
        self.ui.doubleSpinBox_alpha.setMinimum(0.01)
        self.ui.doubleSpinBox_alpha.setMaximum(0.99)

        if test:
            self.ui.spinBox_estimators.setValue(50)
            self.ui.doubleSpinBox_leaf.setValue(10)
            self.ui.doubleSpinBox_samples.setValue(100)
            self.ui.doubleSpinBox_alpha.setValue(0.5)
            self.ui.doubleSpinBox_learnrate.setValue(0.1)

        cur = QtCore.QDate.currentDate()
        self.ui.dateEdit_forecast.setDate(cur)
        cur = cur.addDays(-30 if test else -7)
        self.ui.dateEdit_end.setDate(cur)
        cur = cur.addYears(-2)
        self.ui.dateEdit_start.setDate(cur)

        self.ui.listWidget.__class__ = cw.List

        for model in ui_cfg.TRANSLATE.Model.values():
            for widget in model.widgets:
                curr = self.ui.centralwidget.findChild(QtWidgets.QWidget, widget)
                curr.hide()
        if not test:
            self.ui.checkBox_dumped.hide()
        self.ui.widget_alpha.hide()

        if test:
            self.change_model(self.ui.comboBox_model.currentText())

        self.ui.cv_wrapper.hide()
        self.ui.spinBox_shift.setMaximum(10000)
        self.ui.spinBox_period.setMaximum(10000)
        self.ui.spinBox_preddays.setMaximum(10000)

        if test:
            self.ui.spinBox_period.setValue(120)
            self.ui.spinBox_shift.setValue(15)
            self.ui.spinBox_preddays.setValue(2)

        self.threadpool = QtCore.QThreadPool()
        print("Max number of threads which will be used=%d" % self.threadpool.maxThreadCount())

        threadtest = QtCore.QThread(self)
        idealthreadcount = threadtest.idealThreadCount()
        print("Your machine can handle {} threads optimally.".format(idealthreadcount))

        self.mutex = QtCore.QMutex()

        self.ui.checkBox_upload.stateChanged.connect(self.show_upload_series)
        self.ui.pushButton_upload.clicked.connect(self.upload_series)
        self.ui.comboBox_model.currentTextChanged.connect(self.change_model)
        self.ui.comboBox_trend.currentTextChanged.connect(self.update_ets_trend)
        self.ui.lineEdit_exogenous.returnPressed.connect(self.add_exogenous)
        self.ui.pushButton_add_ex.clicked.connect(self.add_exogenous)
        self.ui.pushButton_del_ex.clicked.connect(self.del_exogenous)
        self.ui.listWidget.delete.connect(self.del_exogenous)
        self.ui.comboBox_loss.currentTextChanged.connect(self.update_loss)
        self.ui.checkBox_cv.stateChanged.connect(self.update_cv)
        self.ui.pushButton_forecast.clicked.connect(self.predict_handler)

    def update_uploaded(self) -> List[str]:
        with open(self.filename, newline='') as f:
            reader = csv.reader(f)
            self.uploaded_data = list(reader)
            return self.uploaded_data[0][1:]

    def show_upload_series(self, state):
        self.ui.listWidget.clear()
        self.ui.lineEdit_series.clear()
        if state:
            self.ui.horizontalWidget_exogenous.hide()
            self.ui.lineEdit_series.setReadOnly(True)
            self.ui.listWidget.delete.disconnect()
            if self.filename != "Upload series":
                headers = self.update_uploaded()
                self.ui.listWidget.addItems(headers[1:])
                self.ui.lineEdit_series.setText(headers[0])
            self.ui.horizontalWidget_series_wrapper.show()
        else:
            self.ui.horizontalWidget_series_wrapper.hide()
            self.ui.listWidget.delete.connect(self.del_exogenous)
            self.ui.lineEdit_series.setReadOnly(False)
            self.ui.horizontalWidget_exogenous.show()
            
    def upload_series(self):
        tmp_filename = QtWidgets.QFileDialog.getOpenFileName(
            parent=None,
            caption="Select series",
            directory=self.home_loc,
            filter="*.csv"
        )[0]
        if not tmp_filename:
            return
        self.filename = tmp_filename
        headers = self.update_uploaded()
        self.ui.lineEdit_series.setText(headers[0])
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(headers[1:])
        short_name = self.filename if '/' not in self.filename else self.filename[self.filename.rfind('/') + 1:]
        self.ui.label_upload.setText(short_name)

    def add_exogenous(self):
        if self.ui.lineEdit_exogenous.text():
            self.ui.listWidget.insertItem(0, self.ui.lineEdit_exogenous.text())
        self.ui.lineEdit_exogenous.clear()

    def del_exogenous(self):
        selected = self.ui.listWidget.selectedItems()
        for item in selected:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def update_ets_trend(self, trend_name):
        if trend_name and trend_name != "No trend":
            self.ui.checkBox_dumped.show()
        else:
            self.ui.checkBox_dumped.hide()

    def update_loss(self, loss_name):
        if loss_name and (loss_name == "Huber" or loss_name == "Quantile"):
            self.ui.widget_alpha.show()
        else:
            self.ui.widget_alpha.hide()

    def change_model(self, model_name):
        for model in ui_cfg.TRANSLATE.Model.values():
            for widget in model.widgets:
                curr = self.ui.centralwidget.findChild(QtWidgets.QWidget, widget)
                curr.hide()
        self.ui.comboBox_metric.clear()
        if model_name:
            model = ui_cfg.TRANSLATE.Model[model_name]
            for widget in model.widgets:
                curr = self.ui.centralwidget.findChild(QtWidgets.QWidget, widget)
                curr.show()
            if not self.test_flag:
                self.ui.comboBox_metric.addItem("")
            self.ui.comboBox_metric.addItems(ui_cfg.TRANSLATE.Model[model_name].metrics.keys())

    def update_cv(self, state):
        if state:
            self.ui.forecast_wrapper.hide()
            self.ui.cv_wrapper.show()
        else:
            self.ui.cv_wrapper.hide()
            self.ui.forecast_wrapper.show()

    def paint_widget(self, widget, color: str):
        widget_name = widget.objectName() + "_wrapper"
        widget = self.ui.centralwidget.findChild(QtWidgets.QWidget, widget_name)
        widget.setStyleSheet(ui_hlp.style_sheet_text(widget_name, color))

    def check_correct(self, widget, data):
        if not data:
            self.paint_widget(widget, ui_cfg.error_color)
            return False
        else:
            self.paint_widget(widget, ui_cfg.correct_color)
            return True

    def print_predict(self, result):
        if result["cv_flag"]:
            self.print_cv(
                result["cur_model"],
                result["cur_data"],
                result["baseline_model"],
                result["baseline_data"]
            )
        else:
            self.plot(result["data"], result["ticker"])

    def plot(self, data, ticker):
        x, y, x_pred, y_pred = data["X"], data["Y"], data["PredictedX"], data["PredictedY"]

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Known values'))
        fig.add_trace(go.Scatter(x=x_pred, y=y_pred, mode='lines', name='Forecast'))
        fig.update_layout(
            title={
                'text': ticker,
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

    def print_cv(self, model: str, error_model, baseline: str, error_baseline):
        ui_hlp.prettify_cv_data(error_model)
        ui_hlp.prettify_cv_data(error_baseline)
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
        self.ui.webView.setHtml(ui_hlp.get_table_html(headers, contents))
        

    def handle_errors(self):
        flag_correct = True

        if self.ui.checkBox_upload.isChecked():
            if not self.check_correct(self.ui.horizontalWidget_series, self.filename != "Upload series"):
                flag_correct = False
        elif not self.check_correct(self.ui.lineEdit_series, self.ui.lineEdit_series.text()):
                flag_correct = False
        
        for cb in self.comboBoxes_general:
            if not self.check_correct(cb, cb.currentText()):
                flag_correct = False

        if self.ui.comboBox_model.currentText() and \
             "ets_wrapper" in ui_cfg.TRANSLATE.Model[self.ui.comboBox_model.currentText()].widgets:
            if not self.check_correct(self.ui.comboBox_trend, self.ui.comboBox_trend.currentText()):
                flag_correct = False
        
        if self.ui.comboBox_model.currentText() and \
             "metric_wrapper" in ui_cfg.TRANSLATE.Model[self.ui.comboBox_model.currentText()].widgets:
            if not self.check_correct(self.ui.comboBox_metric, self.ui.comboBox_metric.currentText()):
                flag_correct = False
        
        if self.ui.comboBox_model.currentText() and \
             "loss_wrapper" in ui_cfg.TRANSLATE.Model[self.ui.comboBox_model.currentText()].widgets:
            if not self.check_correct(self.ui.comboBox_loss, self.ui.comboBox_loss.currentText()):
                flag_correct = False
        
        dates = [
            self.ui.dateEdit_start.date(), 
            self.ui.dateEdit_end.date(), 
            self.ui.dateEdit_forecast.date()
        ]
        cur = QtCore.QDate.currentDate()
        
        flag_start = dates[0] <= cur and dates[0] not in dates[1:]
        flag_end = dates[1] <= cur and dates[1] not in [dates[0], dates[2]]

        flag_start &= (dates[0] < dates[1]) and (dates[0] < dates[2])
        flag_end &= (dates[1] > dates[0]) and (dates[1] < dates[2])

        self.check_correct(self.ui.dateEdit_start, flag_start)
        self.check_correct(self.ui.dateEdit_end, flag_end)

        flag_correct &= flag_start & flag_end

        if not self.ui.checkBox_cv.isChecked():
            flag_forecast = dates[2] not in dates[:2]
            flag_forecast &= (dates[2] > dates[1]) and (dates[2] > dates[0])
            self.check_correct(self.ui.dateEdit_forecast, flag_forecast)
            flag_correct &= flag_forecast

        if self.ui.checkBox_cv.isChecked():
            for sb in self.spinBoxes[1:]:
                if not self.check_correct(sb, sb.value()):
                    flag_correct = False
        
            days = dates[0].daysTo(dates[1])
            if not self.check_correct(self.ui.spinBox_period, self.ui.spinBox_period.value() < days and self.ui.spinBox_period.value() > 0):
                flag_correct = False

        return flag_correct

    def predict_handler(self):
        if not self.handle_errors():
            print("WARNING: Incorrect input!")
            return

        self.ui.pushButton_forecast.setEnabled(False)

        all_params = {
            "exogenous_variables":
                [self.ui.listWidget.item(i).text() for i in range(self.ui.listWidget.count())],
            "trend": ui_cfg.TRANSLATE.ETSTrend[self.ui.comboBox_trend.currentText()] 
                if self.ui.comboBox_trend.currentText() else None,
            "dumped": self.ui.checkBox_dumped.isChecked(),
            "n_estimators": self.ui.spinBox_estimators.value(),
            "criterion": ui_cfg.TRANSLATE.Model[self.ui.comboBox_model.currentText()].metrics[self.ui.comboBox_metric.currentText()]
                if self.ui.comboBox_metric.currentText() else None,
            "min_samples_leaf": self.ui.doubleSpinBox_leaf.value(),
            "max_samples": self.ui.doubleSpinBox_samples.value(),
            "loss": ui_cfg.TRANSLATE.GBLoss[self.ui.comboBox_loss.currentText()] 
                if self.ui.comboBox_loss.currentText() else None,
            "learning_rate": self.ui.doubleSpinBox_learnrate.value(),
            "alpha": self.ui.doubleSpinBox_alpha.value()
        }

        curr_params = { key: all_params[key]
            for key in ui_cfg.TRANSLATE.Model[self.ui.comboBox_model.currentText()].params }

        params = hlp.PredictParams(
            ticker=self.ui.lineEdit_series.text(),
            model=ui_cfg.TRANSLATE.Model[self.ui.comboBox_model.currentText()].backend,
            start_date=self.ui.dateEdit_start.date().toString("yyyy-MM-dd"),
            end_date=self.ui.dateEdit_end.date().toString("yyyy-MM-dd"),
            forecast_date=self.ui.dateEdit_forecast.date().toString("yyyy-MM-dd"),
            offset=ui_cfg.TRANSLATE.Offset[self.ui.comboBox_offset.currentText()],
            cv_shift=self.ui.spinBox_shift.value(),
            cv_period=self.ui.spinBox_period.value(),
            cv_predict_days=self.ui.spinBox_preddays.value(),
            params=curr_params,
            upload=self.ui.checkBox_upload.isChecked(),
            uploaded_data=self.uploaded_data if self.ui.checkBox_upload.isChecked() else []
        )

        self.worker = Worker(partial(self.predict_series, params, self.ui.checkBox_cv.isChecked()))
        self.worker.signals.result.connect(self.print_predict)
        self.worker.signals.finish.connect(partial(self.ui.pushButton_forecast.setEnabled, True))
        self.threadpool.start(self.worker)
    
    def predict_series(self, params, cv_flag):

        print(params.__dict__)
        if cv_flag:
            cur_model = ""
            for key in ui_cfg.TRANSLATE.Model.keys():
                if ui_cfg.TRANSLATE.Model[key].backend == params.model:
                    cur_model = key
            data_cur = self.process_request(params, "cross-validate")
            params.model = cfg.Model.naive
            data_baseline = self.process_request(params, "cross-validate")
            print(data_cur)
            print(data_baseline)
            self.mutex.lock()
            if not data_cur or not data_baseline or self.worker.stop:
                self.mutex.unlock()
                return None
            self.mutex.unlock()
            print("CROSS-VALIDATION REQUEST")
            return {
                "cur_model": cur_model,
                "cur_data": data_cur['data'],
                "baseline_model": "Naive model",
                "baseline_data": data_baseline['data'],
                "cv_flag": True
            }
        else:
            data = self.process_request(params, 'predict')
            self.mutex.lock()
            if not data or self.worker.stop:
                self.mutex.unlock()
                return None
            self.mutex.unlock()
            print("PREDICT REQUEST")
            return {
                "ticker": params.ticker,
                "data": data['data'],
                "cv_flag": False
            }

    def process_request(self, params: hlp.PredictParams, request: str) -> any:
        headers = {'Content-type': 'application/json'}
        self.mutex.lock()
        if self.worker.stop:
            self.mutex.unlock()
            return None
        self.mutex.unlock()
        req_res = send_request(
            method='POST', 
            url='http://158.101.168.149:8080/' + request, 
            headers=headers,
            data=json.dumps(params.__dict__, cls=hlp.EnumEncoder)
        )
        while not req_res.get('success', False):
            self.mutex.lock()
            if self.worker.stop:
                self.mutex.unlock()
                return None
            self.mutex.unlock()
            req_res = send_request(
                method='POST', 
                url='http://158.101.168.149:8080/' + request, 
                headers=headers,
                data=json.dumps(params.__dict__, cls=hlp.EnumEncoder)
            )
            time.sleep(0.1)
        data = self.get_request(req_res['id'])
        if not data or data.get('status', None) is not cfg.Status.ready:
            print(data)
            return None
        else:
            return data

    def get_request(self, uid):
        params = {
            'id': uid
        }
        self.mutex.lock()
        if self.worker.stop:
            self.mutex.unlock()
            return None
        self.mutex.unlock()
        res = send_request(method='GET', url='http://158.101.168.149:8080/get', params=params)
        while res.get('status', cfg.Status.fail) in [cfg.Status.wait, cfg.Status.process]:
            self.mutex.lock()
            if self.worker.stop:
                self.mutex.unlock()
                return None
            self.mutex.unlock()
            res = send_request(method='GET', url='http://158.101.168.149:8080/get', params=params)
            time.sleep(0.1)
        return res

    # потоки или процессы должны быть завершены    ###
    def closeEvent(self, event):
        # закрыть поток Worker(QRunnable)
        self.mutex.lock()
        if hasattr(self, "worker"):
            self.worker.stop = True
        self.mutex.unlock()
        self.threadpool.waitForDone(-1)
        super(GUI, self).closeEvent(event)

if __name__ == '__main__':
    test = False
    if len(sys.argv) > 1:
        test = (sys.argv[1] == '--test')
    app = QtWidgets.QApplication([])
    application = GUI(test)
    application.show()

    sys.exit(app.exec())
