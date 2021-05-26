# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(290, 0))
        self.horizontalFrame.setMaximumSize(QtCore.QSize(280, 16777215))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_series_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.lineEdit_series_wrapper.setObjectName("lineEdit_series_wrapper")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.lineEdit_series_wrapper)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_series = QtWidgets.QLineEdit(self.lineEdit_series_wrapper)
        self.lineEdit_series.setObjectName("lineEdit_series")
        self.verticalLayout_3.addWidget(self.lineEdit_series)
        self.verticalLayout_2.addWidget(self.lineEdit_series_wrapper)
        self.label_2 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_model_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.comboBox_model_wrapper.setObjectName("comboBox_model_wrapper")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.comboBox_model_wrapper)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_model = QtWidgets.QComboBox(self.comboBox_model_wrapper)
        self.comboBox_model.setObjectName("comboBox_model")
        self.verticalLayout_4.addWidget(self.comboBox_model)
        self.verticalLayout_2.addWidget(self.comboBox_model_wrapper)
        self.exogenous_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.exogenous_wrapper.setObjectName("exogenous_wrapper")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.exogenous_wrapper)
        self.verticalLayout_9.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.exogenous_wrapper)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_exogenous = QtWidgets.QLineEdit(self.exogenous_wrapper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_exogenous.sizePolicy().hasHeightForWidth())
        self.lineEdit_exogenous.setSizePolicy(sizePolicy)
        self.lineEdit_exogenous.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_exogenous.setObjectName("lineEdit_exogenous")
        self.horizontalLayout_5.addWidget(self.lineEdit_exogenous)
        self.pushButton_add_ex = QtWidgets.QPushButton(self.exogenous_wrapper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add_ex.sizePolicy().hasHeightForWidth())
        self.pushButton_add_ex.setSizePolicy(sizePolicy)
        self.pushButton_add_ex.setMinimumSize(QtCore.QSize(55, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add_ex.setIcon(icon)
        self.pushButton_add_ex.setObjectName("pushButton_add_ex")
        self.horizontalLayout_5.addWidget(self.pushButton_add_ex)
        self.pushButton_del_ex = QtWidgets.QPushButton(self.exogenous_wrapper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_del_ex.sizePolicy().hasHeightForWidth())
        self.pushButton_del_ex.setSizePolicy(sizePolicy)
        self.pushButton_del_ex.setMinimumSize(QtCore.QSize(55, 0))
        self.pushButton_del_ex.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_del_ex.setIcon(icon1)
        self.pushButton_del_ex.setObjectName("pushButton_del_ex")
        self.horizontalLayout_5.addWidget(self.pushButton_del_ex)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.listWidget = QtWidgets.QListWidget(self.exogenous_wrapper)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_9.addWidget(self.listWidget)
        self.verticalLayout_2.addWidget(self.exogenous_wrapper)
        self.ets_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.ets_wrapper.setObjectName("ets_wrapper")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.ets_wrapper)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(3)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.widget_3 = QtWidgets.QWidget(self.ets_wrapper)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_17.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_17.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_trend = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_trend.setObjectName("comboBox_trend")
        self.verticalLayout_17.addWidget(self.comboBox_trend)
        self.checkBox_dumped = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_dumped.setObjectName("checkBox_dumped")
        self.verticalLayout_17.addWidget(self.checkBox_dumped)
        self.checkBox_seasonality = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_seasonality.setObjectName("checkBox_seasonality")
        self.verticalLayout_17.addWidget(self.checkBox_seasonality)
        self.verticalLayout_16.addWidget(self.widget_3)
        self.horizontalWidget_seasonality = QtWidgets.QWidget(self.ets_wrapper)
        self.horizontalWidget_seasonality.setObjectName("horizontalWidget_seasonality")
        self.horizontalLayout_seasonality = QtWidgets.QHBoxLayout(self.horizontalWidget_seasonality)
        self.horizontalLayout_seasonality.setContentsMargins(2, 1, 1, -1)
        self.horizontalLayout_seasonality.setSpacing(3)
        self.horizontalLayout_seasonality.setObjectName("horizontalLayout_seasonality")
        self.label_15 = QtWidgets.QLabel(self.horizontalWidget_seasonality)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_seasonality.addWidget(self.label_15)
        self.spinBox_seasonality_wrapper = QtWidgets.QWidget(self.horizontalWidget_seasonality)
        self.spinBox_seasonality_wrapper.setMaximumSize(QtCore.QSize(74, 16777215))
        self.spinBox_seasonality_wrapper.setObjectName("spinBox_seasonality_wrapper")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.spinBox_seasonality_wrapper)
        self.horizontalLayout_14.setContentsMargins(2, 1, 2, 1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.spinBox_seasonality = QtWidgets.QSpinBox(self.spinBox_seasonality_wrapper)
        self.spinBox_seasonality.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBox_seasonality.setObjectName("spinBox_seasonality")
        self.horizontalLayout_14.addWidget(self.spinBox_seasonality)
        self.horizontalLayout_seasonality.addWidget(self.spinBox_seasonality_wrapper)
        self.verticalLayout_16.addWidget(self.horizontalWidget_seasonality)
        self.verticalLayout_2.addWidget(self.ets_wrapper)
        self.label_5 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_method_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.comboBox_method_wrapper.setObjectName("comboBox_method_wrapper")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.comboBox_method_wrapper)
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.comboBox_method = QtWidgets.QComboBox(self.comboBox_method_wrapper)
        self.comboBox_method.setObjectName("comboBox_method")
        self.verticalLayout_7.addWidget(self.comboBox_method)
        self.verticalLayout_2.addWidget(self.comboBox_method_wrapper)
        self.label_6 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_type_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.comboBox_type_wrapper.setObjectName("comboBox_type_wrapper")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.comboBox_type_wrapper)
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.comboBox_type = QtWidgets.QComboBox(self.comboBox_type_wrapper)
        self.comboBox_type.setObjectName("comboBox_type")
        self.verticalLayout_8.addWidget(self.comboBox_type)
        self.verticalLayout_2.addWidget(self.comboBox_type_wrapper)
        self.label_10 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_offset_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.comboBox_offset_wrapper.setObjectName("comboBox_offset_wrapper")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.comboBox_offset_wrapper)
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.comboBox_offset = QtWidgets.QComboBox(self.comboBox_offset_wrapper)
        self.comboBox_offset.setObjectName("comboBox_offset")
        self.verticalLayout_10.addWidget(self.comboBox_offset)
        self.verticalLayout_2.addWidget(self.comboBox_offset_wrapper)
        self.widget = QtWidgets.QWidget(self.horizontalFrame)
        self.widget.setObjectName("widget")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_15.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.checkBox_cv = QtWidgets.QCheckBox(self.widget)
        self.checkBox_cv.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.checkBox_cv.setObjectName("checkBox_cv")
        self.verticalLayout_15.addWidget(self.checkBox_cv)
        self.verticalLayout_2.addWidget(self.widget)
        self.cv_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.cv_wrapper.setObjectName("cv_wrapper")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.cv_wrapper)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(2, 0, 0, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.cv_wrapper)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.spinBox_period_wrapper = QtWidgets.QWidget(self.cv_wrapper)
        self.spinBox_period_wrapper.setMaximumSize(QtCore.QSize(74, 16777215))
        self.spinBox_period_wrapper.setObjectName("spinBox_period_wrapper")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.spinBox_period_wrapper)
        self.verticalLayout_11.setContentsMargins(2, 1, 2, 1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.spinBox_period = QtWidgets.QSpinBox(self.spinBox_period_wrapper)
        self.spinBox_period.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBox_period.setObjectName("spinBox_period")
        self.verticalLayout_11.addWidget(self.spinBox_period)
        self.horizontalLayout_11.addWidget(self.spinBox_period_wrapper)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(2, -1, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.cv_wrapper)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.spinBox_shift_wrapper = QtWidgets.QWidget(self.cv_wrapper)
        self.spinBox_shift_wrapper.setMaximumSize(QtCore.QSize(74, 16777215))
        self.spinBox_shift_wrapper.setObjectName("spinBox_shift_wrapper")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.spinBox_shift_wrapper)
        self.verticalLayout_12.setContentsMargins(2, 1, 2, 1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.spinBox_shift = QtWidgets.QSpinBox(self.spinBox_shift_wrapper)
        self.spinBox_shift.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBox_shift.setObjectName("spinBox_shift")
        self.verticalLayout_12.addWidget(self.spinBox_shift)
        self.horizontalLayout_12.addWidget(self.spinBox_shift_wrapper)
        self.verticalLayout_14.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(2, -1, -1, -1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.cv_wrapper)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.spinBox_preddays_wrapper = QtWidgets.QWidget(self.cv_wrapper)
        self.spinBox_preddays_wrapper.setMaximumSize(QtCore.QSize(74, 16777215))
        self.spinBox_preddays_wrapper.setObjectName("spinBox_preddays_wrapper")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.spinBox_preddays_wrapper)
        self.verticalLayout_13.setContentsMargins(2, 1, 2, 1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.spinBox_preddays = QtWidgets.QSpinBox(self.spinBox_preddays_wrapper)
        self.spinBox_preddays.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBox_preddays.setObjectName("spinBox_preddays")
        self.verticalLayout_13.addWidget(self.spinBox_preddays)
        self.horizontalLayout_13.addWidget(self.spinBox_preddays_wrapper)
        self.verticalLayout_14.addLayout(self.horizontalLayout_13)
        self.verticalLayout_2.addWidget(self.cv_wrapper)
        self.date_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.date_wrapper.setObjectName("date_wrapper")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.date_wrapper)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(3)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_7 = QtWidgets.QLabel(self.date_wrapper)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_18.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(2, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.date_wrapper)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.dateEdit_start_wrapper = QtWidgets.QWidget(self.date_wrapper)
        self.dateEdit_start_wrapper.setObjectName("dateEdit_start_wrapper")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.dateEdit_start_wrapper)
        self.horizontalLayout_7.setContentsMargins(2, 1, 2, 1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.dateEdit_start = QtWidgets.QDateEdit(self.dateEdit_start_wrapper)
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.horizontalLayout_7.addWidget(self.dateEdit_start)
        self.horizontalLayout_3.addWidget(self.dateEdit_start_wrapper)
        self.verticalLayout_18.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(2, -1, -1, -1)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.date_wrapper)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.dateEdit_end_wrapper = QtWidgets.QWidget(self.date_wrapper)
        self.dateEdit_end_wrapper.setObjectName("dateEdit_end_wrapper")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.dateEdit_end_wrapper)
        self.horizontalLayout_8.setContentsMargins(2, 1, 2, 1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.dateEdit_end = QtWidgets.QDateEdit(self.dateEdit_end_wrapper)
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.horizontalLayout_8.addWidget(self.dateEdit_end)
        self.horizontalLayout_6.addWidget(self.dateEdit_end_wrapper)
        self.verticalLayout_18.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addWidget(self.date_wrapper)
        self.forecast_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.forecast_wrapper.setObjectName("forecast_wrapper")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.forecast_wrapper)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(2, -1, -1, -1)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.forecast_wrapper)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.dateEdit_forecast_wrapper = QtWidgets.QWidget(self.forecast_wrapper)
        self.dateEdit_forecast_wrapper.setObjectName("dateEdit_forecast_wrapper")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.dateEdit_forecast_wrapper)
        self.horizontalLayout_9.setContentsMargins(2, 1, 2, 1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.dateEdit_forecast = QtWidgets.QDateEdit(self.dateEdit_forecast_wrapper)
        self.dateEdit_forecast.setObjectName("dateEdit_forecast")
        self.horizontalLayout_9.addWidget(self.dateEdit_forecast)
        self.horizontalLayout_4.addWidget(self.dateEdit_forecast_wrapper)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.forecast_wrapper)
        self.pushButton_forecast_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.pushButton_forecast_wrapper.setObjectName("pushButton_forecast_wrapper")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pushButton_forecast_wrapper)
        self.verticalLayout_5.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_forecast = QtWidgets.QPushButton(self.pushButton_forecast_wrapper)
        self.pushButton_forecast.setFlat(False)
        self.pushButton_forecast.setObjectName("pushButton_forecast")
        self.verticalLayout_5.addWidget(self.pushButton_forecast)
        self.verticalLayout_2.addWidget(self.pushButton_forecast_wrapper)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addWidget(self.horizontalFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Прогнозный ряд"))
        self.lineEdit_series.setPlaceholderText(_translate("MainWindow", "TICKER"))
        self.label_2.setText(_translate("MainWindow", "Модель прогнозирования"))
        self.label_3.setText(_translate("MainWindow", "Внешние переменные"))
        self.lineEdit_exogenous.setPlaceholderText(_translate("MainWindow", "EXOGENOUS"))
        self.label_4.setText(_translate("MainWindow", "Тренд"))
        self.checkBox_dumped.setText(_translate("MainWindow", "Тренд с затуханием"))
        self.checkBox_seasonality.setText(_translate("MainWindow", "Сезонность"))
        self.label_15.setText(_translate("MainWindow", "Сезонность, дн."))
        self.label_5.setText(_translate("MainWindow", "Метод прогнозирования"))
        self.label_6.setText(_translate("MainWindow", "Тип прогнозирования"))
        self.label_10.setText(_translate("MainWindow", "Периодичность"))
        self.checkBox_cv.setText(_translate("MainWindow", "Кросс-валидация"))
        self.label_11.setText(_translate("MainWindow", "Ширина окна, дн."))
        self.label_13.setText(_translate("MainWindow", "Сдвиг окна, дн."))
        self.label_14.setText(_translate("MainWindow", "Размер тест. выборки, дн."))
        self.label_7.setText(_translate("MainWindow", "Даты начала и конца периода"))
        self.label_8.setText(_translate("MainWindow", "Начало:"))
        self.label_9.setText(_translate("MainWindow", "Конец:"))
        self.label_12.setText(_translate("MainWindow", "Конец прогноза:"))
        self.pushButton_forecast.setText(_translate("MainWindow", "Спрогнозировать"))


from PyQt5 import QtWebEngineWidgets
import source.client.resources_rc
