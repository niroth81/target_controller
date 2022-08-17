# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainMenu(object):
    def setupUi(self, mainMenu):
        mainMenu.setObjectName("mainMenu")
        mainMenu.resize(1023, 600)
        mainMenu.setWindowFlag(QtCore.Qt.FramelessWindowHint) # this will hide the title bar
        mainMenu.setWindowTitle("no title") # set the title
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        mainMenu.setFont(font)
        mainMenu.setAutoFillBackground(False)
        mainMenu.setStyleSheet("QMainWindow#mainMenu {background-image: url(:/images/background.jpg); }")
        self.centralwidget = QtWidgets.QWidget(mainMenu)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: transparent;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 981, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(25, 0, 0, 20)
        self.gridLayout.setHorizontalSpacing(100)
        self.gridLayout.setObjectName("gridLayout")
        
        
        self.setRangeBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.setRangeBtn.setFont(font)
        self.setRangeBtn.setAutoFillBackground(False)
        self.setRangeBtn.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.setRangeBtn.setObjectName("setRangeBtn")
        self.gridLayout.addWidget(self.setRangeBtn, 0, 1, 1, 1)
        
        self.rangeStatus = QtWidgets.QLabel(self.centralwidget)
        self.rangeStatus.setGeometry(QtCore.QRect(0, 10, 1024, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rangeStatus.setFont(font)
        self.rangeStatus.setStyleSheet("color: rgb(0, 0, 0);")
        self.rangeStatus.setText("")
        self.rangeStatus.setObjectName("rangeStatus")
        self.rangeStatus.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.rapidFireBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.rapidFireBtn.setFont(font)
        self.rapidFireBtn.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.rapidFireBtn.setObjectName("rapidFireBtn")
        self.gridLayout.addWidget(self.rapidFireBtn, 2, 0, 1, 1)
        
        
        self.e2Btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.e2Btn.setFont(font)
        self.e2Btn.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.e2Btn.setObjectName("e2Btn")
        self.gridLayout.addWidget(self.e2Btn, 0, 2, 1, 1)
        
        
        self.e3Btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.e3Btn.setFont(font)
        self.e3Btn.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.e3Btn.setObjectName("e3Btn")
        self.gridLayout.addWidget(self.e3Btn, 1, 2, 1, 1)
        
        
        self.bullsEyeBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bullsEyeBtn.setFont(font)
        self.bullsEyeBtn.setAutoFillBackground(False)
        self.bullsEyeBtn.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.bullsEyeBtn.setObjectName("bullsEyeBtn")
        self.gridLayout.addWidget(self.bullsEyeBtn, 0, 0, 1, 1)
        
        
        self.e4Btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.e4Btn.setFont(font)
        self.e4Btn.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.e4Btn.setObjectName("e4Btn")
        self.gridLayout.addWidget(self.e4Btn, 2, 2, 1, 1)
        
        
        self.CenterFireBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.CenterFireBtn.setFont(font)
        self.CenterFireBtn.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.CenterFireBtn.setObjectName("25MCenterFireBtn")
        self.gridLayout.addWidget(self.CenterFireBtn, 3, 0, 1, 1)
        
        
        self.e5Btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.e5Btn.setFont(font)
        self.e5Btn.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.e5Btn.setObjectName("e5Btn")
        self.gridLayout.addWidget(self.e5Btn, 3, 2, 1, 1)
        
        
        self.serviceMatchBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.serviceMatchBtn.setFont(font)
        self.serviceMatchBtn.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.serviceMatchBtn.setObjectName("serviceMatchBtn")
        self.gridLayout.addWidget(self.serviceMatchBtn, 1, 0, 1, 1)
        
        
        mainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainMenu)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1023, 21))
        self.menubar.setObjectName("menubar")
        mainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainMenu)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        mainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(mainMenu)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        _translate = QtCore.QCoreApplication.translate
        mainMenu.setWindowTitle(_translate("mainMenu", "Main Menu"))
        self.setRangeBtn.setText(_translate("mainMenu", "Select Range"))
        self.rapidFireBtn.setText(_translate("mainMenu", "Intl Rapid Fire"))
        self.e2Btn.setText(_translate("mainMenu", "--Empty Slot---"))
        self.e3Btn.setText(_translate("mainMenu", "--Empty Slot---"))
        self.bullsEyeBtn.setText(_translate("mainMenu", "Bullseye"))
        self.e4Btn.setText(_translate("mainMenu", "--Empty Slot---"))
        self.CenterFireBtn.setText(_translate("mainMenu", "25M Center Fire"))
        self.e5Btn.setText(_translate("mainMenu", "--Empty Slot--"))
        self.serviceMatchBtn.setText(_translate("mainMenu", "Service Match"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainMenu = QtWidgets.QMainWindow()
    ui = Ui_mainMenu()
    ui.setupUi(mainMenu)
    mainMenu.show()
    sys.exit(app.exec_())
