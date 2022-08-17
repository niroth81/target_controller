import os
from PyQt5 import QtWidgets
from ui.setRangeWindow import Ui_rangeWindow

class setRange(QtWidgets.QMainWindow):

    def __init__(self):
        super(setRange, self).__init__()
        self.ui = Ui_rangeWindow()
        self.ui.setupUi(self)
        self.ipaddressFilePath = os.path.join(os.getcwd(),'IPaddress.txt')
        self.currentIPFilePath = os.path.join(os.getcwd(),'currentIp.txt')
      
        
        
        self.ui.setBtn1.clicked.connect(self.setRangeIntoFile)
        self.ui.setBtn2.clicked.connect(self.setRangeIntoFile)
        self.ui.setBtn3.clicked.connect(self.setRangeIntoFile)
        self.ui.setBtn4.clicked.connect(self.setRangeIntoFile)
        self.ui.setBtn5.clicked.connect(self.setRangeIntoFile)
        self.ui.setBtn6.clicked.connect(self.setRangeIntoFile)

        self.loadIpFile()



   
    def loadIpFile(self):
        try:
            with open(self.ipaddressFilePath) as f:
                self.lines = f.readlines()
                print(self.lines)
        except IOError:
            print("File open error")        

    def setRangeIntoFile(self):

        btnName=self.sender().objectName()
        btnText = self.sender().text()

        if(btnName == "setBtn1"):
            print("range 1 click")
            self.setCurrentIpAddress(self.lines[0],btnText)

        if(btnName == "setBtn2"):
            print("range 2 click")
            self.setCurrentIpAddress(self.lines[1],btnText)

        if(btnName == "setBtn3"):
            print("range 3 click")
            self.setCurrentIpAddress(self.lines[2],btnText)

        if(btnName == "setBtn4"):
            print("range 4 click")
            self.setCurrentIpAddress(self.lines[3],btnText)

        if(btnName == "setBtn5"):
            print("range 5 click")
            self.setCurrentIpAddress(self.lines[4],btnText)

        if(btnName == "setBtn6"):
            print("range 6 click")
            self.setCurrentIpAddress(self.lines[5],btnText)

        from scripts.mainMenuProgram import mainMenu
        self.mainMenuWindow = mainMenu()
        self.mainMenuWindow.show()
        self.close()

    def setCurrentIpAddress(self,ipAddress,range):
        try:
            with open(self.currentIPFilePath,"w") as f:
                f.write(range+","+ipAddress)

        except IOError:
             print ("Error: can\'t find file or read data")



    if __name__ == "__main__":
        print("setRange window")
        pass   
