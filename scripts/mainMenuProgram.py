import os
from PyQt5 import QtWidgets
from ui.mainMenu import Ui_mainMenu

from scripts.matchProgram import matchProgram

from programs.BullseyeProgram import BullseyeProgram
from programs.serviceProgram import serviceProcedure
from programs.CenterFireProgram import CenterFireProgram
from programs.IntlRapidProgram import IntlRapidProgram

class mainMenu(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainMenu, self).__init__()
        self.ui = Ui_mainMenu()
        self.ui.setupUi(self)
        
        self.ui.setRangeBtn.clicked.connect(self.setRangebtnClickHandler);
        self.ui.bullsEyeBtn.clicked.connect(self.bullsEyeClickedHandler);
        self.ui.serviceMatchBtn.clicked.connect(self.serviceMatchClickedHandler);
        self.ui.CenterFireBtn.clicked.connect(self.CenterFireClickedHandler);
        self.ui.rapidFireBtn.clicked.connect(self.rapidFireClickedHandler);


        self.currentIPFilePath = os.path.join(os.getcwd(),'currentIp.txt')
        self.loadCurrentIPaddress()


        self.program1 = BullseyeProgram("The Bullseye 900 Match contains the National Match with additional strings to make up a match of 90 shots. 3x 10 shot strings from 50 Meters with the remaining 60 shots to be taken from 25 meters. This match usually takes about 40 minutes to complete.","The Bullseye 900 Match contains the National Match with additional strings to make up a match of 90 shots. 3x 10 shot strings from 50 Meters with the remaining 60 shots to be taken from 25 meters. This match usually takes about 40 minutes to complete.");
        
        self.program2 = serviceProcedure("match instruction service","service match sequence description");
  
        self.program3 = CenterFireProgram("25 meter center-fire pistol is one of the ISSF shooting events. Its origin lies in competitions with military-style service pistols, and as such its history dates back to the 19th century.","25 meter center-fire pistol is one of the ISSF shooting events. Its origin lies in competitions with military-style service pistols, and as such its history dates back to the 19th century.");  

        self.program4 = IntlRapidProgram("25 meter rapid fire pistol is one of the ISSF shooting events and is shot with .22 LR pistols. The event has been a part of the Olympic program ever since the beginning in 1896","25 meter rapid fire pistol is one of the ISSF shooting events and is shot with .22 LR pistols. The event has been a part of the Olympic program ever since the beginning in 1896");  



    def loadCurrentIPaddress(self):
        try:
            with open(self.currentIPFilePath) as f:
                line = f.readline() 
                if(line != ""):
                    print(line)
                    rangeName,ipaddress = line.split(",")
                    #self.ui.rangeStatus.setText(f"Currently Set to {rangeName} @ {ipaddress}")
                    self.ui.rangeStatus.setText(f"Currently Set to {rangeName}")
                else:
                    self.ui.rangeStatus.setText("Not Set")

        except IOError:
            self.ui.rangeStatus.setText("File read error")
            print("Current ip address open error");



    def setRangebtnClickHandler(self):
        from scripts.setRangeWindowProgram import setRange
        self.setRangeWindow =  setRange()
        self.setRangeWindow.show()
        self.close()

    def bullsEyeClickedHandler(self):   
        #local import to remove cyclic import error
        from scripts.matchInstructProgram import matchInstructions
        self.test = matchInstructions(self.program1)
        self.test.show()
        self.close()
    
    def serviceMatchClickedHandler(self):
        #local import to remove cyclic import error
        from scripts.matchInstructProgram import matchInstructions
        self.test = matchInstructions(self.program2)
        self.test.show()
        self.close()

    def CenterFireClickedHandler(self):
        #local import to remove cyclic import error
        from scripts.matchInstructProgram import matchInstructions
        self.test = matchInstructions(self.program3)
        self.test.show()
        self.close()   

    def rapidFireClickedHandler(self):
        #local import to remove cyclic import error
        from scripts.matchInstructProgram import matchInstructions
        self.test = matchInstructions(self.program4)
        self.test.show()
        self.close()   


    if __name__ == "__main__":
        print("mainmenu")
        pass
            
