from PyQt5 import QtWidgets,QtCore

from PyQt5.QtGui import QFont

from ui.matchInstructionsWindow import Ui_matchInstructionsWindow

class matchInstructions(QtWidgets.QMainWindow):
    backSignal = QtCore.pyqtSignal()

    def __init__(self,program):
        super(matchInstructions, self).__init__()
        self.ui = Ui_matchInstructionsWindow()
        self.ui.setupUi(self)
        self.program = program
        self.matchInstructions = program.matchInstructions
        self.ui.matchDescriptionLabel.setFont(QFont('Arial', 16))
        self.ui.matchDescriptionLabel.setText(self.matchInstructions)

        self.ui.mainMenuBtn.clicked.connect(self.mainMenuBtnClickHandler)
        self.ui.startBtn.clicked.connect(self.startMatchClickHandler)

    def mainMenuBtnClickHandler(self):
        from scripts.mainMenuProgram import mainMenu
        self.mainMenuWindow = mainMenu()
        self.mainMenuWindow.show()
        self.close()
        

    def startMatchClickHandler(self):

        from scripts.matchProgram import matchProgram
        self.mprogram = matchProgram(self.program)
        self.mprogram.show()
        self.close()
       
        
    if __name__ == "__main__":
        pass    
        
        