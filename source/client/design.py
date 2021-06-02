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
        MainWindow.resize(800, 700)
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
        self.widget_2 = QtWidgets.QWidget(self.horizontalFrame)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.checkBox_upload = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_upload.setObjectName("checkBox_upload")
        self.verticalLayout_8.addWidget(self.checkBox_upload)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.lineEdit_series_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.lineEdit_series_wrapper.setObjectName("lineEdit_series_wrapper")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.lineEdit_series_wrapper)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_series = QtWidgets.QLineEdit(self.lineEdit_series_wrapper)
        self.lineEdit_series.setObjectName("lineEdit_series")
        self.verticalLayout_3.addWidget(self.lineEdit_series)
        self.verticalLayout_2.addWidget(self.lineEdit_series_wrapper)
        self.horizontalWidget_series_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.horizontalWidget_series_wrapper.setObjectName("horizontalWidget_series_wrapper")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.horizontalWidget_series_wrapper)
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalWidget_series = QtWidgets.QWidget(self.horizontalWidget_series_wrapper)
        self.horizontalWidget_series.setObjectName("horizontalWidget_series")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalWidget_series)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_upload = QtWidgets.QLabel(self.horizontalWidget_series)
        self.label_upload.setObjectName("label_upload")
        self.horizontalLayout_10.addWidget(self.label_upload)
        self.pushButton_upload = QtWidgets.QPushButton(self.horizontalWidget_series)
        self.pushButton_upload.setMinimumSize(QtCore.QSize(119, 0))
        self.pushButton_upload.setMaximumSize(QtCore.QSize(119, 16777215))
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.horizontalLayout_10.addWidget(self.pushButton_upload)
        self.verticalLayout_7.addWidget(self.horizontalWidget_series)
        self.verticalLayout_2.addWidget(self.horizontalWidget_series_wrapper)
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
        self.horizontalWidget_exogenous = QtWidgets.QWidget(self.exogenous_wrapper)
        self.horizontalWidget_exogenous.setObjectName("horizontalWidget_exogenous")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalWidget_exogenous)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_exogenous = QtWidgets.QLineEdit(self.horizontalWidget_exogenous)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_exogenous.sizePolicy().hasHeightForWidth())
        self.lineEdit_exogenous.setSizePolicy(sizePolicy)
        self.lineEdit_exogenous.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_exogenous.setObjectName("lineEdit_exogenous")
        self.horizontalLayout_5.addWidget(self.lineEdit_exogenous)
        self.pushButton_add_ex = QtWidgets.QPushButton(self.horizontalWidget_exogenous)
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
        self.pushButton_del_ex = QtWidgets.QPushButton(self.horizontalWidget_exogenous)
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
        self.verticalLayout_9.addWidget(self.horizontalWidget_exogenous)
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
        self.label_4 = QtWidgets.QLabel(self.ets_wrapper)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_16.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_trend_wrapper = QtWidgets.QWidget(self.ets_wrapper)
        self.comboBox_trend_wrapper.setObjectName("comboBox_trend_wrapper")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.comboBox_trend_wrapper)
        self.verticalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.comboBox_trend = QtWidgets.QComboBox(self.comboBox_trend_wrapper)
        self.comboBox_trend.setObjectName("comboBox_trend")
        self.verticalLayout_17.addWidget(self.comboBox_trend)
        self.verticalLayout_16.addWidget(self.comboBox_trend_wrapper)
        self.widget_3 = QtWidgets.QWidget(self.ets_wrapper)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_19.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.checkBox_dumped = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_dumped.setObjectName("checkBox_dumped")
        self.verticalLayout_19.addWidget(self.checkBox_dumped)
        self.verticalLayout_16.addWidget(self.widget_3)
        self.verticalLayout_2.addWidget(self.ets_wrapper)
        self.metric_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.metric_wrapper.setObjectName("metric_wrapper")
        self.verticalLayout_71 = QtWidgets.QVBoxLayout(self.metric_wrapper)
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_71.setSpacing(3)
        self.verticalLayout_71.setObjectName("verticalLayout_71")
        self.label_6 = QtWidgets.QLabel(self.metric_wrapper)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_71.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_metric_wrapper = QtWidgets.QWidget(self.metric_wrapper)
        self.comboBox_metric_wrapper.setObjectName("comboBox_metric_wrapper")
        self.verticalLayout_81 = QtWidgets.QVBoxLayout(self.comboBox_metric_wrapper)
        self.verticalLayout_81.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_81.setObjectName("verticalLayout_81")
        self.comboBox_metric = QtWidgets.QComboBox(self.comboBox_metric_wrapper)
        self.comboBox_metric.setObjectName("comboBox_metric")
        self.verticalLayout_81.addWidget(self.comboBox_metric)
        self.verticalLayout_71.addWidget(self.comboBox_metric_wrapper)
        self.verticalLayout_2.addWidget(self.metric_wrapper)
        self.loss_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.loss_wrapper.setObjectName("loss_wrapper")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.loss_wrapper)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(3)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_17 = QtWidgets.QLabel(self.loss_wrapper)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_20.addWidget(self.label_17, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_loss_wrapper = QtWidgets.QWidget(self.loss_wrapper)
        self.comboBox_loss_wrapper.setObjectName("comboBox_loss_wrapper")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.comboBox_loss_wrapper)
        self.verticalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.comboBox_loss = QtWidgets.QComboBox(self.comboBox_loss_wrapper)
        self.comboBox_loss.setObjectName("comboBox_loss")
        self.verticalLayout_21.addWidget(self.comboBox_loss)
        self.verticalLayout_20.addWidget(self.comboBox_loss_wrapper)
        self.widget_alpha = QtWidgets.QWidget(self.loss_wrapper)
        self.widget_alpha.setObjectName("widget_alpha")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_alpha)
        self.horizontalLayout_16.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_18 = QtWidgets.QLabel(self.widget_alpha)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_16.addWidget(self.label_18)
        self.doubleSpinBox_alpha = QtWidgets.QDoubleSpinBox(self.widget_alpha)
        self.doubleSpinBox_alpha.setMinimumSize(QtCore.QSize(70, 0))
        self.doubleSpinBox_alpha.setMaximumSize(QtCore.QSize(70, 16777215))
        self.doubleSpinBox_alpha.setObjectName("doubleSpinBox_alpha")
        self.horizontalLayout_16.addWidget(self.doubleSpinBox_alpha)
        self.verticalLayout_20.addWidget(self.widget_alpha)
        self.verticalLayout_2.addWidget(self.loss_wrapper)
        self.learning_rate_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.learning_rate_wrapper.setObjectName("learning_rate_wrapper")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.learning_rate_wrapper)
        self.horizontalLayout_17.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_19 = QtWidgets.QLabel(self.learning_rate_wrapper)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_17.addWidget(self.label_19)
        self.doubleSpinBox_learnrate = QtWidgets.QDoubleSpinBox(self.learning_rate_wrapper)
        self.doubleSpinBox_learnrate.setMinimumSize(QtCore.QSize(70, 0))
        self.doubleSpinBox_learnrate.setMaximumSize(QtCore.QSize(70, 16777215))
        self.doubleSpinBox_learnrate.setObjectName("doubleSpinBox_learnrate")
        self.horizontalLayout_17.addWidget(self.doubleSpinBox_learnrate)
        self.verticalLayout_2.addWidget(self.learning_rate_wrapper)
        self.estimators_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.estimators_wrapper.setObjectName("estimators_wrapper")
        self.horizontalLayout_101 = QtWidgets.QHBoxLayout(self.estimators_wrapper)
        self.horizontalLayout_101.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_101.setObjectName("horizontalLayout_101")
        self.label_5 = QtWidgets.QLabel(self.estimators_wrapper)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_101.addWidget(self.label_5)
        self.spinBox_estimators = QtWidgets.QSpinBox(self.estimators_wrapper)
        self.spinBox_estimators.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_estimators.setMaximumSize(QtCore.QSize(70, 16777215))
        self.spinBox_estimators.setObjectName("spinBox_estimators")
        self.horizontalLayout_101.addWidget(self.spinBox_estimators)
        self.verticalLayout_2.addWidget(self.estimators_wrapper)
        self.min_samples_leaf_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.min_samples_leaf_wrapper.setObjectName("min_samples_leaf_wrapper")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.min_samples_leaf_wrapper)
        self.horizontalLayout_14.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(self.min_samples_leaf_wrapper)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.doubleSpinBox_leaf = QtWidgets.QDoubleSpinBox(self.min_samples_leaf_wrapper)
        self.doubleSpinBox_leaf.setMinimumSize(QtCore.QSize(70, 0))
        self.doubleSpinBox_leaf.setMaximumSize(QtCore.QSize(70, 16777215))
        self.doubleSpinBox_leaf.setObjectName("doubleSpinBox_leaf")
        self.horizontalLayout_14.addWidget(self.doubleSpinBox_leaf)
        self.verticalLayout_2.addWidget(self.min_samples_leaf_wrapper)
        self.max_samples_wrapper = QtWidgets.QWidget(self.horizontalFrame)
        self.max_samples_wrapper.setObjectName("max_samples_wrapper")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.max_samples_wrapper)
        self.horizontalLayout_15.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.max_samples_wrapper)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16)
        self.doubleSpinBox_samples = QtWidgets.QDoubleSpinBox(self.max_samples_wrapper)
        self.doubleSpinBox_samples.setMinimumSize(QtCore.QSize(70, 0))
        self.doubleSpinBox_samples.setMaximumSize(QtCore.QSize(70, 16777215))
        self.doubleSpinBox_samples.setObjectName("doubleSpinBox_samples")
        self.horizontalLayout_15.addWidget(self.doubleSpinBox_samples)
        self.verticalLayout_2.addWidget(self.max_samples_wrapper)
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
        self.label.setText(_translate("MainWindow", "Forecast series"))
        self.checkBox_upload.setText(_translate("MainWindow", "Upload .csv series from PC"))
        self.lineEdit_series.setPlaceholderText(_translate("MainWindow", "TICKER"))
        self.label_upload.setText(_translate("MainWindow", "Upload series"))
        self.pushButton_upload.setText(_translate("MainWindow", "Search..."))
        self.label_2.setText(_translate("MainWindow", "Model"))
        self.label_3.setText(_translate("MainWindow", "Exogenous variables"))
        self.lineEdit_exogenous.setPlaceholderText(_translate("MainWindow", "EXOGENOUS"))
        self.label_4.setText(_translate("MainWindow", "Trend"))
        self.checkBox_dumped.setText(_translate("MainWindow", "Dumped trend"))
        self.label_6.setText(_translate("MainWindow", "Criterion"))
        self.label_17.setText(_translate("MainWindow", "Loss function"))
        self.label_18.setText(_translate("MainWindow", "Alpha parameter"))
        self.label_19.setText(_translate("MainWindow", "Learning rate"))
        self.label_5.setText(_translate("MainWindow", "Number of estimators"))
        self.label_15.setText(_translate("MainWindow", "Min. % of samples in a leaf"))
        self.label_16.setText(_translate("MainWindow", "% of samples to learn from"))
        self.label_10.setText(_translate("MainWindow", "Periodicity"))
        self.checkBox_cv.setText(_translate("MainWindow", "Cross-validation"))
        self.label_11.setText(_translate("MainWindow", "Window size"))
        self.label_13.setText(_translate("MainWindow", "Shift"))
        self.label_14.setText(_translate("MainWindow", "Test sample size"))
        self.label_7.setText(_translate("MainWindow", "Dates"))
        self.label_8.setText(_translate("MainWindow", "Start"))
        self.label_9.setText(_translate("MainWindow", "End"))
        self.label_12.setText(_translate("MainWindow", "Forecast end"))
        self.pushButton_forecast.setText(_translate("MainWindow", "Forecast"))


from PyQt5 import QtWebEngineWidgets
import source.client.resources_rc
