# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matchWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_matchWindow(object):
    def setupUi(self, matchWindow):
        matchWindow.setObjectName("matchWindow")
        matchWindow.resize(1024, 600)
        matchWindow.setStyleSheet("background-color: rgb(70, 70, 70);")
        matchWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint) # this will hide the title bar
        matchWindow.setWindowTitle("no title") # set the title
        self.centralwidget = QtWidgets.QWidget(matchWindow)
        self.centralwidget.setStyleSheet("background-color: transparent;")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 40, 1001, 251))
        self.frame.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 2, 601, 61))
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.descriptionLabel = QtWidgets.QLabel(self.frame)
        self.descriptionLabel.setGeometry(QtCore.QRect(20, 60, 941, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.thisSequenceDesriptionLbl = QtWidgets.QLabel(self.frame)
        self.thisSequenceDesriptionLbl.setGeometry(QtCore.QRect(20, 170, 961, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.thisSequenceDesriptionLbl.setFont(font)
        self.thisSequenceDesriptionLbl.setObjectName("thisSequenceDesriptionLbl")
        self.nextSequenceDescriptionLbl = QtWidgets.QLabel(self.frame)
        self.nextSequenceDescriptionLbl.setGeometry(QtCore.QRect(20, 210, 961, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nextSequenceDescriptionLbl.setFont(font)
        self.nextSequenceDescriptionLbl.setObjectName("nextSequenceDescriptionLbl")
        self.beginSeqBtn = QtWidgets.QPushButton(self.centralwidget)
        self.beginSeqBtn.setGeometry(QtCore.QRect(20, 480, 220, 80))
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.beginSeqBtn.setFont(font)
        self.beginSeqBtn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.beginSeqBtn.setObjectName("beginSeqBtn")
        self.endSeqBtn = QtWidgets.QPushButton(self.centralwidget)
        self.endSeqBtn.setGeometry(QtCore.QRect(280, 480, 220, 80))
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.endSeqBtn.setFont(font)
        self.endSeqBtn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.endSeqBtn.setObjectName("endSeqBtn")
        self.continueBtn = QtWidgets.QPushButton(self.centralwidget)
        self.continueBtn.setGeometry(QtCore.QRect(530, 480, 220, 80))
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.continueBtn.setFont(font)
        self.continueBtn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.continueBtn.setObjectName("continueBtn")
        self.notificationLabel = QtWidgets.QLabel(self.centralwidget)
        self.notificationLabel.setEnabled(False)
        self.notificationLabel.setGeometry(QtCore.QRect(12, 3, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.notificationLabel.setFont(font)
        self.notificationLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.notificationLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.notificationLabel.setText("")
        self.notificationLabel.setObjectName("notificationLabel")
        self.quitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.quitBtn.setGeometry(QtCore.QRect(780, 480, 220, 80))
        font = QtGui.QFont()
        font.setFamily("SerpentineEF")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.quitBtn.setFont(font)
        self.quitBtn.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.quitBtn.setObjectName("quitBtn")
        self.relayStatusLbl = QtWidgets.QLabel(self.centralwidget)
        self.relayStatusLbl.setGeometry(QtCore.QRect(690, 3, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.relayStatusLbl.setFont(font)
        self.relayStatusLbl.setStyleSheet("color: rgb(0, 255, 0);")
        self.relayStatusLbl.setText("")
        self.relayStatusLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.relayStatusLbl.setObjectName("relayStatusLbl")
        self.notificationLabel.raise_()
        self.frame.raise_()
        self.beginSeqBtn.raise_()
        self.endSeqBtn.raise_()
        self.continueBtn.raise_()
        self.quitBtn.raise_()
        self.relayStatusLbl.raise_()
        matchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(matchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        matchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(matchWindow)
        self.statusbar.setObjectName("statusbar")
        matchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(matchWindow)
        QtCore.QMetaObject.connectSlotsByName(matchWindow)

    def retranslateUi(self, matchWindow):
        _translate = QtCore.QCoreApplication.translate
        matchWindow.setWindowTitle(_translate("matchWindow", "MainWindow"))
        self.label.setText(_translate("matchWindow", "Match Information"))
        self.descriptionLabel.setText(_translate("matchWindow", "All details about the specific sequence will go in here"))
        self.thisSequenceDesriptionLbl.setText(_translate("matchWindow", "<html><head/><body><p>This Sequence:10 shots in 10 minutes</p><p><br/></p></body></html>"))
        self.nextSequenceDescriptionLbl.setText(_translate("matchWindow", "<html><head/><body><p>Next Sequence:5 shots in 20 seconds</p><p><br/></p></body></html>"))
        self.beginSeqBtn.setText(_translate("matchWindow", "Start Match"))
        self.endSeqBtn.setText(_translate("matchWindow", "Finish String"))
        self.continueBtn.setText(_translate("matchWindow", "Next String"))
        self.quitBtn.setText(_translate("matchWindow", "Main menu"))
import resources_rc