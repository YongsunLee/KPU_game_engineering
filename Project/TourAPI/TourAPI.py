# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\creat\Desktop\TourAPI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request
import xml.etree.ElementTree as ET
import comboboxSettingFunc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 10, 491, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.MapLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.MapLayout.setContentsMargins(0, 0, 0, 0)
        self.MapLayout.setObjectName("MapLayout")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 240, 821, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 817, 247))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(800, 0, 16, 241))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 321, 221))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.SearchLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.SearchLayout.setContentsMargins(0, 0, 0, 0)
        self.SearchLayout.setObjectName("SearchLayout")

        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_2.setObjectName("groupBox_2")

        self.label_Service = QtWidgets.QLabel(self.groupBox_2)
        self.label_Service.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label_Service.setObjectName("label_Service")

        self.comboBox_smallService = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_smallService.setGeometry(QtCore.QRect(80, 60, 231, 21))
        self.comboBox_smallService.setObjectName("comboBox_smallService")

        self.comboBox_smallService.addItem("중분류 선택")

        self.label_City = QtWidgets.QLabel(self.groupBox_2)
        self.label_City.setGeometry(QtCore.QRect(40, 140, 41, 21))
        self.label_City.setObjectName("label_City")

        self.comboBox_Area = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_Area.setGeometry(QtCore.QRect(80, 100, 231, 21))
        self.comboBox_Area.setObjectName("comboBox_Area")

        self.comboBox_Area.addItem("지역", 0)
        self.comboBox_Area.addItem("서울", 1)
        self.comboBox_Area.addItem("인천", 2)
        self.comboBox_Area.addItem("대전", 3)
        self.comboBox_Area.addItem("대구", 4)
        self.comboBox_Area.addItem("광주", 5)
        self.comboBox_Area.addItem("부산", 6)
        self.comboBox_Area.addItem("울산", 7)
        self.comboBox_Area.addItem("세종특별자치시", 8)
        self.comboBox_Area.addItem("경기도", 31)
        self.comboBox_Area.addItem("강원도", 32)
        self.comboBox_Area.addItem("충청북도", 33)
        self.comboBox_Area.addItem("충청남도", 34)
        self.comboBox_Area.addItem("경상북도", 35)
        self.comboBox_Area.addItem("경상남도", 36)
        self.comboBox_Area.addItem("전라북도", 37)
        self.comboBox_Area.addItem("전라남도", 38)
        self.comboBox_Area.addItem("제주도", 39)

        def on_comboBox_currentIndexChanged_Area():
            Area = self.comboBox_Area.currentData()
            self.comboBox_City.clear()
            comboboxSettingFunc.CitycomboboxSettingFunc(Area, self.comboBox_City)

        self.comboBox_Area.currentIndexChanged.connect(on_comboBox_currentIndexChanged_Area)

        self.comboBox_Service = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_Service.setGeometry(QtCore.QRect(80, 20, 151, 21))
        self.comboBox_Service.setAcceptDrops(False)
        self.comboBox_Service.setObjectName("comboBox_Service")

        self.comboBox_Service.addItem("서비스 선택")
        self.comboBox_Service.addItem("관광지", 12)
        self.comboBox_Service.addItem("숙박", 32)

        def on_comboBox_currentIndexChanged():
            Service = self.comboBox_Service.currentData()
            self.comboBox_smallService.clear()
            comboboxSettingFunc.smallServicecomboboxSettingFunc(Service, self.comboBox_smallService)

        self.comboBox_Service.currentIndexChanged.connect(on_comboBox_currentIndexChanged)

        self.label_Area = QtWidgets.QLabel(self.groupBox_2)
        self.label_Area.setGeometry(QtCore.QRect(50, 100, 31, 21))
        self.label_Area.setObjectName("label_Area")

        self.comboBox_City = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_City.setGeometry(QtCore.QRect(80, 140, 231, 21))
        self.comboBox_City.setObjectName("comboBox_City")

        self.comboBox_City.addItem("시군구")

        self.label_smallService = QtWidgets.QLabel(self.groupBox_2)
        self.label_smallService.setGeometry(QtCore.QRect(40, 60, 41, 21))
        self.label_smallService.setObjectName("label_smallService")

        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(210, 172, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.SearchLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Search"))
        self.label_Service.setText(_translate("MainWindow", "서비스 분류"))
        self.label_City.setText(_translate("MainWindow", "시군구"))
        self.label_Area.setText(_translate("MainWindow", "지역"))
        self.label_smallService.setText(_translate("MainWindow", "소분류"))
        self.pushButton.setText(_translate("MainWindow", "검색"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

