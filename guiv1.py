# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets


class Ui_I23Cams(object):
    def setupUi(self, I23Cams):
        I23Cams.setObjectName("I23Cams")
        I23Cams.resize(1151, 1156)
        I23Cams.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(I23Cams)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setSizeIncrement(QtCore.QSize(1, 1))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.maincams = QtWidgets.QWidget()
        self.maincams.setObjectName("maincams")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.maincams)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.maincams)
        self.webEngineView.setUrl(QtCore.QUrl("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM6.mjpg.mjpg"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout.addWidget(self.webEngineView)
        self.webEngineView_2 = QtWebEngineWidgets.QWebEngineView(self.maincams)
        self.webEngineView_2.setUrl(QtCore.QUrl("http://bl23i-di-serv-01.diamond.ac.uk:8080/ECAM10.mjpg.mjpg"))
        self.webEngineView_2.setObjectName("webEngineView_2")
        self.verticalLayout.addWidget(self.webEngineView_2)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.maincams, "")
        self.extracams = QtWidgets.QWidget()
        self.extracams.setObjectName("extracams")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.extracams)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.webEngineView_4 = QtWebEngineWidgets.QWebEngineView(self.extracams)
        self.webEngineView_4.setUrl(QtCore.QUrl("http://bl23i-di-serv-01.diamond.ac.uk:8080/ECAM9.mjpg.mjpg"))
        self.webEngineView_4.setObjectName("webEngineView_4")
        self.gridLayout.addWidget(self.webEngineView_4, 1, 1, 1, 1)
        self.webEngineView_6 = QtWebEngineWidgets.QWebEngineView(self.extracams)
        self.webEngineView_6.setUrl(QtCore.QUrl("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM7.mjpg.mjpg"))
        self.webEngineView_6.setObjectName("webEngineView_6")
        self.gridLayout.addWidget(self.webEngineView_6, 1, 0, 1, 1)
        self.webEngineView_5 = QtWebEngineWidgets.QWebEngineView(self.extracams)
        self.webEngineView_5.setUrl(QtCore.QUrl("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM3.mjpg.mjpg"))
        self.webEngineView_5.setObjectName("webEngineView_5")
        self.gridLayout.addWidget(self.webEngineView_5, 0, 0, 1, 1)
        self.webEngineView_3 = QtWebEngineWidgets.QWebEngineView(self.extracams)
        self.webEngineView_3.setUrl(QtCore.QUrl("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM5.mjpg.mjpg"))
        self.webEngineView_3.setObjectName("webEngineView_3")
        self.gridLayout.addWidget(self.webEngineView_3, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.extracams, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        I23Cams.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(I23Cams)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setObjectName("statusbar")
        I23Cams.setStatusBar(self.statusbar)

        self.retranslateUi(I23Cams)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(I23Cams)

    def retranslateUi(self, I23Cams):
        _translate = QtCore.QCoreApplication.translate
        I23Cams.setWindowTitle(_translate("I23Cams", "I23 Cam Viewer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.maincams), _translate("I23Cams", "Main Cams"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.extracams), _translate("I23Cams", "Extra Cams"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_I23Cams()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())

