from PyQt5 import QtWidgets,QtCore
from ui.lastWindow import Ui_lastWindow


class lastMenu(QtWidgets.QMainWindow):
    

    def __init__(self):
        super(lastMenu, self).__init__()
        self.ui = Ui_lastWindow()
        self.ui.setupUi(self)
        
        self.ui.mainMenuBtn.clicked.connect(self.openMainmenu)


    def openMainmenu(self):
        from scripts.mainMenuProgram import mainMenu
        self.mainMenuWindow = mainMenu()
        self.mainMenuWindow.show()
        self.close()
        
    if __name__ == "__main__":
        pass