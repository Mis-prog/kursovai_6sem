# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1092, 800)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        self.treewidget_all_signals = QtWidgets.QTreeWidget(parent=self.tab)
        self.treewidget_all_signals.setObjectName("treewidget_all_signals")
        self.gridLayout_4.addWidget(self.treewidget_all_signals, 0, 0, 8, 1)
        self.open_dialog = QtWidgets.QPushButton(parent=self.tab)
        self.open_dialog.setObjectName("open_dialog")
        self.gridLayout_4.addWidget(self.open_dialog, 1, 1, 1, 1)
        self.signal_name = QtWidgets.QLineEdit(parent=self.tab)
        self.signal_name.setObjectName("signal_name")
        self.gridLayout_4.addWidget(self.signal_name, 3, 1, 1, 1)
        self.set_signal = QtWidgets.QPushButton(parent=self.tab)
        self.set_signal.setObjectName("set_signal")
        self.gridLayout_4.addWidget(self.set_signal, 4, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.tab)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 5, 1, 1, 1)
        self.tablewidget_buffer_signals = QtWidgets.QTableWidget(parent=self.tab)
        self.tablewidget_buffer_signals.setDefaultDropAction(QtCore.Qt.DropAction.IgnoreAction)
        self.tablewidget_buffer_signals.setObjectName("tablewidget_buffer_signals")
        self.tablewidget_buffer_signals.setColumnCount(1)
        self.tablewidget_buffer_signals.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_buffer_signals.setHorizontalHeaderItem(0, item)
        self.gridLayout_4.addWidget(self.tablewidget_buffer_signals, 6, 1, 1, 1)
        self.save_file = QtWidgets.QPushButton(parent=self.tab)
        self.save_file.setObjectName("save_file")
        self.gridLayout_4.addWidget(self.save_file, 7, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.tab)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.smoothing_widget = QtWidgets.QWidget(parent=self.tab_2)
        self.smoothing_widget.setGeometry(QtCore.QRect(9, 79, 1041, 621))
        self.smoothing_widget.setObjectName("smoothing_widget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 11, 720, 53))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.smoothing_window_value_widget = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.smoothing_window_value_widget.setMaximum(1000)
        self.smoothing_window_value_widget.setProperty("value", 0)
        self.smoothing_window_value_widget.setDisplayIntegerBase(10)
        self.smoothing_window_value_widget.setObjectName("smoothing_window_value_widget")
        self.gridLayout_3.addWidget(self.smoothing_window_value_widget, 1, 2, 1, 1)
        self.smoothing_window_widget = QtWidgets.QLabel(parent=self.layoutWidget)
        self.smoothing_window_widget.setObjectName("smoothing_window_widget")
        self.gridLayout_3.addWidget(self.smoothing_window_widget, 0, 2, 1, 1)
        self.smoothing_param_value_widget = QtWidgets.QDoubleSpinBox(parent=self.layoutWidget)
        self.smoothing_param_value_widget.setMaximum(100.0)
        self.smoothing_param_value_widget.setSingleStep(0.01)
        self.smoothing_param_value_widget.setObjectName("smoothing_param_value_widget")
        self.gridLayout_3.addWidget(self.smoothing_param_value_widget, 1, 3, 1, 1)
        self.smoothing_param_window = QtWidgets.QLabel(parent=self.layoutWidget)
        self.smoothing_param_window.setObjectName("smoothing_param_window")
        self.gridLayout_3.addWidget(self.smoothing_param_window, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.run_smoothing_widget = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.run_smoothing_widget.setObjectName("run_smoothing_widget")
        self.gridLayout_3.addWidget(self.run_smoothing_widget, 1, 1, 1, 1)
        self.list_filter_smoothing_widget = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.list_filter_smoothing_widget.setObjectName("list_filter_smoothing_widget")
        self.list_filter_smoothing_widget.addItem("")
        self.list_filter_smoothing_widget.addItem("")
        self.list_filter_smoothing_widget.addItem("")
        self.list_filter_smoothing_widget.addItem("")
        self.list_filter_smoothing_widget.addItem("")
        self.gridLayout_3.addWidget(self.list_filter_smoothing_widget, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.eliminating_gaps_widget = QtWidgets.QWidget(parent=self.tab_4)
        self.eliminating_gaps_widget.setGeometry(QtCore.QRect(11, 65, 631, 646))
        self.eliminating_gaps_widget.setObjectName("eliminating_gaps_widget")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(660, 60, 381, 651))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.tab_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 12, 369, 55))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.layoutWidget1)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_4, 0, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_6.addWidget(self.pushButton_8, 0, 1, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_6.addWidget(self.pushButton_26, 0, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_19 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_13.addWidget(self.label_19, 2, 3, 1, 1)
        self.search_anomaly_widget = QtWidgets.QWidget(parent=self.tab_3)
        self.search_anomaly_widget.setObjectName("search_anomaly_widget")
        self.gridLayout_13.addWidget(self.search_anomaly_widget, 3, 0, 2, 3)
        self.tablewidget_intervals_anomaly = QtWidgets.QTableWidget(parent=self.tab_3)
        self.tablewidget_intervals_anomaly.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tablewidget_intervals_anomaly.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablewidget_intervals_anomaly.setObjectName("tablewidget_intervals_anomaly")
        self.tablewidget_intervals_anomaly.setColumnCount(2)
        self.tablewidget_intervals_anomaly.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_intervals_anomaly.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_intervals_anomaly.setHorizontalHeaderItem(1, item)
        self.gridLayout_13.addWidget(self.tablewidget_intervals_anomaly, 4, 3, 1, 2)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 1)
        self.list_method_search_anomaly = QtWidgets.QComboBox(parent=self.tab_3)
        self.list_method_search_anomaly.setObjectName("list_method_search_anomaly")
        self.list_method_search_anomaly.addItem("")
        self.list_method_search_anomaly.addItem("")
        self.gridLayout_11.addWidget(self.list_method_search_anomaly, 1, 0, 1, 1)
        self.run_analysis_signals = QtWidgets.QPushButton(parent=self.tab_3)
        self.run_analysis_signals.setObjectName("run_analysis_signals")
        self.gridLayout_11.addWidget(self.run_analysis_signals, 1, 1, 1, 1)
        self.cut_intervals_anomaly = QtWidgets.QPushButton(parent=self.tab_3)
        self.cut_intervals_anomaly.setObjectName("cut_intervals_anomaly")
        self.gridLayout_11.addWidget(self.cut_intervals_anomaly, 1, 2, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_11, 0, 0, 2, 1)
        self.append_interval = QtWidgets.QPushButton(parent=self.tab_3)
        self.append_interval.setObjectName("append_interval")
        self.gridLayout_13.addWidget(self.append_interval, 2, 4, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " Файл с коротажной прямой"))
        self.treewidget_all_signals.headerItem().setText(0, _translate("MainWindow", "Название листа:"))
        self.open_dialog.setText(_translate("MainWindow", "Выбрать файл"))
        self.set_signal.setText(_translate("MainWindow", "Добавить"))
        self.label_14.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Выбранные сигналы:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        item = self.tablewidget_buffer_signals.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Сигналы:"))
        self.save_file.setText(_translate("MainWindow", "Сохранить"))
        self.label_13.setText(_translate("MainWindow", "Текущий сигнал:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Данные"))
        self.smoothing_window_widget.setText(_translate("MainWindow", "Ширина окна:"))
        self.smoothing_param_window.setText(_translate("MainWindow", "Подбор параметра:"))
        self.label_2.setText(_translate("MainWindow", "Метод сглаживание:"))
        self.run_smoothing_widget.setText(_translate("MainWindow", "Выполнить "))
        self.list_filter_smoothing_widget.setItemText(0, _translate("MainWindow", "Метод скользящего среднего "))
        self.list_filter_smoothing_widget.setItemText(1, _translate("MainWindow", "Медианный фильтр "))
        self.list_filter_smoothing_widget.setItemText(2, _translate("MainWindow", "Экспонитациональный фильтр"))
        self.list_filter_smoothing_widget.setItemText(3, _translate("MainWindow", "Окно Хэмминга"))
        self.list_filter_smoothing_widget.setItemText(4, _translate("MainWindow", "Окно Гаусса"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Сглаживание данных"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Промежутки \n"
"аномалий:"))
        self.label_6.setText(_translate("MainWindow", "Метод  востановления разрыва :"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Сплайнами"))
        self.pushButton_8.setText(_translate("MainWindow", "Выполнить "))
        self.pushButton_26.setText(_translate("MainWindow", "Применить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Устранение разрывов"))
        self.label_19.setText(_translate("MainWindow", "Промежутки аномалий:"))
        item = self.tablewidget_intervals_anomaly.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "От:"))
        item = self.tablewidget_intervals_anomaly.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "До:"))
        self.label_5.setText(_translate("MainWindow", "Метод  поиска аномалий:"))
        self.list_method_search_anomaly.setItemText(0, _translate("MainWindow", "Скользящего среднего"))
        self.list_method_search_anomaly.setItemText(1, _translate("MainWindow", "Окно Хэмминга"))
        self.run_analysis_signals.setText(_translate("MainWindow", "Анализ"))
        self.cut_intervals_anomaly.setText(_translate("MainWindow", "Вырезать"))
        self.append_interval.setText(_translate("MainWindow", "Добавить интервал"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Устранение аномалий"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Python"))
        self.comboBox.setItemText(1, _translate("MainWindow", "C++"))
        self.comboBox.setItemText(2, _translate("MainWindow", "C++(OpenMP)"))
