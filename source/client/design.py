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
        MainWindow.resize(800, 600)
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
        self.horizontalFrame.setMaximumWidth(260)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_series = QtWidgets.QComboBox(self.horizontalFrame)
        self.comboBox_series.setObjectName("comboBox_series")
        self.verticalLayout_2.addWidget(self.comboBox_series)
        self.label_2 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_model = QtWidgets.QComboBox(self.horizontalFrame)
        self.comboBox_model.setObjectName("comboBox_model")
        self.verticalLayout_2.addWidget(self.comboBox_model)
        self.label_3 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.listWidget = QtWidgets.QListWidget(self.horizontalFrame)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.label_4 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_metric = QtWidgets.QComboBox(self.horizontalFrame)
        self.comboBox_metric.setObjectName("comboBox_metric")
        self.verticalLayout_2.addWidget(self.comboBox_metric)
        self.label_5 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_method = QtWidgets.QComboBox(self.horizontalFrame)
        self.comboBox_method.setObjectName("comboBox_method")
        self.verticalLayout_2.addWidget(self.comboBox_method)
        self.label_6 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_type = QtWidgets.QComboBox(self.horizontalFrame)
        self.comboBox_type.setObjectName("comboBox_type")
        self.verticalLayout_2.addWidget(self.comboBox_type)
        self.label_7 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.dateEdit_start = QtWidgets.QDateEdit(self.horizontalFrame)
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.horizontalLayout_3.addWidget(self.dateEdit_start)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.dateEdit_end = QtWidgets.QDateEdit(self.horizontalFrame)
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.horizontalLayout_6.addWidget(self.dateEdit_end)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.dateEdit_forecast = QtWidgets.QDateEdit(self.horizontalFrame)
        self.dateEdit_forecast.setObjectName("dateEdit_forecast")
        self.horizontalLayout_4.addWidget(self.dateEdit_forecast)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_10 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_offset = QtWidgets.QComboBox(self.horizontalFrame)
        self.comboBox_offset.setObjectName("comboBox_offset")
        self.verticalLayout_2.addWidget(self.comboBox_offset)
        self.pushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
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
        self.label_2.setText(_translate("MainWindow", "Модель прогнозирования"))
        self.label_3.setText(_translate("MainWindow", "Внешние переменные"))
        self.label_4.setText(_translate("MainWindow", "Метрика"))
        self.label_5.setText(_translate("MainWindow", "Метод прогнозирования"))
        self.label_6.setText(_translate("MainWindow", "Тип прогнозирования"))
        self.label_7.setText(_translate("MainWindow", "Даты начала и конца периода"))
        self.label_8.setText(_translate("MainWindow", "Начало:"))
        self.label_9.setText(_translate("MainWindow", "Конец:"))
        self.label_12.setText(_translate("MainWindow", "Конец прогноза:"))
        self.label_10.setText(_translate("MainWindow", "Периодичность"))
        self.pushButton.setText(_translate("MainWindow", "Спрогнозировать"))
from PyQt5 import QtWebEngineWidgets
