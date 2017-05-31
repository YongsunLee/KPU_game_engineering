# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\creat\Desktop\TourAPI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json

class City:
    def __init__(self):
        self.cityName = " "
        self.indexNum = 0

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

        self.label_City = QtWidgets.QLabel(self.groupBox_2)
        self.label_City.setGeometry(QtCore.QRect(40, 140, 41, 21))
        self.label_City.setObjectName("label_City")

        self.comboBox_Area = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_Area.setGeometry(QtCore.QRect(80, 100, 231, 21))
        self.comboBox_Area.setObjectName("comboBox_Area")

        self.comboBox_Area.addItem("서울")
        self.comboBox_Area.addItem("인천")
        self.comboBox_Area.addItem("대전")
        self.comboBox_Area.addItem("대구")
        self.comboBox_Area.addItem("광주")
        self.comboBox_Area.addItem("부산")
        self.comboBox_Area.addItem("울산")
        self.comboBox_Area.addItem("세종특별자치시")
        self.comboBox_Area.addItem("경기도")
        self.comboBox_Area.addItem("강원도")
        self.comboBox_Area.addItem("충청북도")
        self.comboBox_Area.addItem("충청남도")
        self.comboBox_Area.addItem("경상북도")
        self.comboBox_Area.addItem("경상남도")
        self.comboBox_Area.addItem("전라북도")
        self.comboBox_Area.addItem("전라남도")
        self.comboBox_Area.addItem("제주도")

        def on_comboBox_currentIndexChanged_Area():
            global city
            Area = self.comboBox_Area.currentText()
            city = City()
            if (str(Area) == "서울"):
                f = open("city_seoul.txt", "r")
                cityData = json.load(f)
                print(cityData)
                for i in cityData:
                    self.comboBox_City.addItem()
                f.close()
            #elif (str(Area) == "인천"):
            #elif (str(Area) == "대전"):
            #elif (str(Area) == "대구"):

        self.comboBox_Area.currentIndexChanged.connect(on_comboBox_currentIndexChanged_Area)

        self.comboBox_Service = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_Service.setGeometry(QtCore.QRect(80, 20, 151, 21))
        self.comboBox_Service.setAcceptDrops(False)
        self.comboBox_Service.setObjectName("comboBox_Service")

        self.comboBox_Service.addItem("서비스 선택")
        self.comboBox_Service.addItem("관광지", 12)
        self.comboBox_Service.addItem("숙박", 32)

        def on_comboBox_currentIndexChanged():
            Service = self.comboBox_Service.currentText()
            if (str(Service) == "관광지"):
                self.comboBox_smallService.clear()
                self.comboBox_smallService.addItem("국립공원", 1010100)
                self.comboBox_smallService.addItem("도립공원", 1010200)
                self.comboBox_smallService.addItem("군립공원", 1010300)
                self.comboBox_smallService.addItem("산", 1010400)
                self.comboBox_smallService.addItem("자연생태관광지", 1010500)
                self.comboBox_smallService.addItem("자연휴양림", 1010600)
                self.comboBox_smallService.addItem("수목원", 1010700)
                self.comboBox_smallService.addItem("폭포", 1010800)
                self.comboBox_smallService.addItem("계곡", 1010900)
                self.comboBox_smallService.addItem("약수터",1011000)
                self.comboBox_smallService.addItem("해안절경", 1011100)
                self.comboBox_smallService.addItem("해수욕장", 1011200)
                self.comboBox_smallService.addItem("섬", 1011300)
                self.comboBox_smallService.addItem("항구/포구", 1011400)
                self.comboBox_smallService.addItem("어촌", 1011500)
                self.comboBox_smallService.addItem("등대", 1011600)
                self.comboBox_smallService.addItem("호수", 1011700)
                self.comboBox_smallService.addItem("강", 1011800)
                self.comboBox_smallService.addItem("동굴", 1011900)
            elif (str(Service) == "숙박"):
                self.comboBox_smallService.clear()
                self.comboBox_smallService.addItem("관광호텔", 2010100)
                self.comboBox_smallService.addItem("수상관광호텔", 2010200)
                self.comboBox_smallService.addItem("전통호텔", 2010300)
                self.comboBox_smallService.addItem("가족호텔", 2010400)
                self.comboBox_smallService.addItem("콘도미니엄", 2010500)
                self.comboBox_smallService.addItem("유스호스텔", 2010600)
                self.comboBox_smallService.addItem("펜션", 2010700)
                self.comboBox_smallService.addItem("여관", 2010800)
                self.comboBox_smallService.addItem("모텔", 2010900)
                self.comboBox_smallService.addItem("민박", 2011000)
                self.comboBox_smallService.addItem("게스트하우스", 2011100)
                self.comboBox_smallService.addItem("홈스테이", 2011200)
                self.comboBox_smallService.addItem("서비스드레지던스", 2011300)
                self.comboBox_smallService.addItem("의료관광호텔", 2011400)
                self.comboBox_smallService.addItem("소형호텔", 2011500)
                self.comboBox_smallService.addItem("한옥스테이", 2011600)
            elif (str(Service) == "서비스 선택"):
                self.comboBox_smallService.clear()
                self.comboBox_smallService.addItem("중분류 선택")

        self.comboBox_Service.currentIndexChanged.connect(on_comboBox_currentIndexChanged)

        self.label_Area = QtWidgets.QLabel(self.groupBox_2)
        self.label_Area.setGeometry(QtCore.QRect(50, 100, 31, 21))
        self.label_Area.setObjectName("label_Area")

        self.comboBox_City = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_City.setGeometry(QtCore.QRect(80, 140, 231, 21))
        self.comboBox_City.setObjectName("comboBox_City")

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

