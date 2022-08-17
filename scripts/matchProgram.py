from PyQt5 import QtWidgets,QtCore,Qt
from PyQt5.QtCore import pyqtSignal,QTimer
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory
from ui.matchWindow import Ui_matchWindow
import socket

class fakeRelay():
    def on(self):
        print("relay on");
    def off(self):
        print("relay off");


class matchProgram(QtWidgets.QMainWindow):
        
    
    def __init__(self,program):
        super(matchProgram, self).__init__()
        
        self.recivedProgram = program

        self.ui = Ui_matchWindow()
        self.ui.setupUi(self)

        self.seqObjsList = program.ListOfSequences;
        self.Ipaddress = program.remoteIPaddress
        self.descriptionList = program.programGroupDescriptons;
        self.matchInstructions = program.matchInstructions
        
       #currently running program index
        self.howmanyBlocks =len(self.seqObjsList)
        self.currentBlock = 0
        self.currentRunningProgramIndex = 0;
        self.sequenceFinished = False

        #set intial values for labesl

        self.ui.descriptionLabel.setText(self.matchInstructions)
        self.ui.thisSequenceDesriptionLbl.setText("Now: "+self.descriptionList[0])
        self.ui.nextSequenceDescriptionLbl.setText("Next: "+self.descriptionList[1])

        #add button click handlers

        self.ui.beginSeqBtn.clicked.connect(self.beginbtnClicked);
        self.ui.endSeqBtn.clicked.connect(self.endBtnClicked);
        self.ui.continueBtn.clicked.connect(self.continueBtnClicked)
        self.ui.quitBtn.clicked.connect(self.closeWithoutRemote)
        
        #hide continue and end buttons
        
        self.ui.continueBtn.setEnabled(False)
        self.ui.endSeqBtn.setEnabled(False)

     
        #check ip address availability
         
        if(not self.checkPort(self.Ipaddress)):
            self.ui.beginSeqBtn.setEnabled(False)
            self.ui.notificationLabel.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(255,0, 0);")
            self.ui.notificationLabel.setText(f"Failed to Connect ...verify remote device is turned on at {self.Ipaddress} ..[error]")
            self.ui.notificationLabel.setVisible(True)
         

        else:
            try:
                factory = PiGPIOFactory(host='192.168.1.63')

                self.relay_1 = gpiozero.OutputDevice(10,pin_factory=factory, active_high=True, initial_value=False)
                
                
                self.ui.notificationLabel.setStyleSheet("color: rgb(0, 255, 0);")
                self.ui.notificationLabel.setText("Remote Device connected......OK")
                self.ui.notificationLabel.setVisible(True)
            except:
                self.ui.beginSeqBtn.setEnabled(False)
                self.ui.notificationLabel.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(255,0, 0);")
                self.ui.notificationLabel.setText(f"Failed to Connect to relay......[ERROR]")
                self.ui.notificationLabel.setVisible(True)
                print("remote Device connection error")
            
#     def connectRelay(self):
#         try:
#             factory = PiGPIOFactory(host='192.168.1.63')
# 
#             self.relay_1 = gpiozero.OutputDevice(10,pin_factory=factory, active_high=True, initial_value=False)
#             
#             self.ui.notificationLabel.setStyleSheet("color: rgb(0, 255, 0);")
#             self.ui.notificationLabel.setText("Remote Device connected......[OK]")
#             self.ui.notificationLabel.setVisible(True)
#                     
# 
# 
#         except:
#             self.ui.beginSeqBtn.setEnabled(False)
#             self.ui.notificationLabel.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(255,0, 0);")
#             self.ui.notificationLabel.setText(f"Failed to Connect to relay......[ERROR]")
#             self.ui.notificationLabel.setVisible(True)
#             print("remote Device connection error")
        


    def checkPort(self,ipaddress):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)                                      #2 Second Timeout
        result = sock.connect_ex((ipaddress,8888))
        if result == 0:
          print ('port OPEN')
          return True
        else:
          print ('port CLOSED, connect_ex returned: '+str(result))
          return False

        
    def beginbtnClicked(self):
        
        self.updateNotificationLabel(1);
        self.setupTheTimer();
                
        
    def setupTheTimer(self):


        if(self.currentBlock > self.howmanyBlocks-1):
            print("Full procedure over")
            self.timer1.stop()
            self.relay_1.off()
            self.updateNotificationLabel(4)
            self.currentBlock =0
            self.currentRunningProgramIndex=0
            
        else:
            self.updateShortDescriptions()

            if(self.currentRunningProgramIndex > len(self.seqObjsList[self.currentBlock])-1):
                print("sequence inside block over")
                self.timer1.stop()
                self.relay_1.off()
                self.updateNotificationLabel(2) 
                
            else:
                print(self.seqObjsList[self.currentBlock])       

                command = self.seqObjsList[self.currentBlock][self.currentRunningProgramIndex].split(":")[0]
                timeToWait = self.seqObjsList[self.currentBlock][self.currentRunningProgramIndex].split(":")[1]

                self.timer1 = QTimer()
                self.timer1.setSingleShot(True)

                if(command == "ON"):
                    self.relay_1.on()
                    print(f"command:={command}")
                    self.ui.relayStatusLbl.setText(f"Hide Targets for {timeToWait} Seconds ")
                    print("forward to off relay")
                    self.timer1.timeout.connect(self.relayOff)
                else:
                    self.relay_1.off()
                    print(f"command:={command}")
                    self.ui.relayStatusLbl.setText(f"Show Targets for {timeToWait} Seconds ")
                    print("forward to ON relay")
                    self.timer1.timeout.connect(self.relayOn)

                self.currentRunningProgramIndex+=1
                self.timer1.start(int(timeToWait)*1000)

    
    def relayOff(self):
        self.relay_1.off()
        self.setupTheTimer()
        


    def relayOn(self):
        self.relay_1.on() 
        self.setupTheTimer()   
        


    def updateShortDescriptions(self):
        if(self.currentBlock >= len(self.seqObjsList)-1):

            self.ui.thisSequenceDesriptionLbl.setText(f"Now: {self.descriptionList[self.currentBlock]}") 
            self.ui.nextSequenceDescriptionLbl.setText("Next: Match Finished")
        else:
            self.ui.thisSequenceDesriptionLbl.setText(f"Now: {self.descriptionList[self.currentBlock]}") 
            self.ui.nextSequenceDescriptionLbl.setText(f"Next: {self.descriptionList[self.currentBlock+1]}")

    def endBtnClicked(self):
        
        #if total block is over
        if(self.currentBlock >= len(self.seqObjsList)-1):
            print("blocks over")
            self.relay_1.off()
            self.currentBlock=0
            self.currentRunningProgramIndex=0  
            self.updateNotificationLabel(3)  
            self.timer1.stop()
            
            
        #if we have more blocks ahead  
        else:
            self.ui.relayStatusLbl.setText(f"")
            self.relay_1.off()
            self.timer1.stop()
            print("========end btn============================")
            self.currentRunningProgramIndex=0
            self.updateNotificationLabel(2)
            
            
            
            

    def continueBtnClicked(self):
        self.updateNotificationLabel(1)
        self.ui.continueBtn.setEnabled(False)
       
        print("=================continue==========================")
      
        self.currentBlock+=1
        self.currentRunningProgramIndex=0
        self.setupTheTimer()



    def updateNotificationLabel(self,state):
        
        #state processing the sequnce
        if(state ==1):
            
            self.ui.beginSeqBtn.setEnabled(False)
            self.ui.continueBtn.setEnabled(False)
            self.ui.endSeqBtn.setEnabled(True)
            self.ui.notificationLabel.setGeometry(QtCore.QRect(12, 3, 661, 31))
            self.ui.notificationLabel.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.ui.notificationLabel.setStyleSheet("color: rgb(0,255,0);")
            self.ui.notificationLabel.setText(f"Running String......")
            #self.ui.notificationLabel.setText(f"Running String...... {self.seqObjsList[self.currentBlock]}")
            self.ui.notificationLabel.setVisible(True)
            
            
        #state waiting for user confirmation
        if(state == 2):
            self.ui.beginSeqBtn.setEnabled(False)
            self.ui.continueBtn.setEnabled(True)
            self.ui.endSeqBtn.setEnabled(False)
            self.ui.notificationLabel.setGeometry(11, 3, 999, 31)
            self.ui.notificationLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            self.ui.notificationLabel.setStyleSheet("background-color: rgb(1, 122, 255);color: rgb(255,255,255);")
            self.ui.notificationLabel.setText(f"Score and patch, then press next string to continue")
            self.ui.notificationLabel.setVisible(True)
            self.ui.relayStatusLbl.setText(f"")
        #completed sequence    
        if(state ==3):
            self.ui.beginSeqBtn.setEnabled(True)
            self.ui.continueBtn.setEnabled(False)
            self.ui.endSeqBtn.setEnabled(False)
            self.ui.notificationLabel.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(0, 255, 0);")
            self.ui.notificationLabel.setText("String Completed")
            self.ui.notificationLabel.setVisible(True)
            self.ui.relayStatusLbl.setText(f"")

        #completed procedure
        if(state ==4):
            self.ui.beginSeqBtn.setEnabled(True)
            self.ui.continueBtn.setEnabled(False)
            self.ui.endSeqBtn.setEnabled(False)
            self.ui.notificationLabel.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(0, 255, 0);")
            self.ui.notificationLabel.setText("Match Completed")
            self.ui.notificationLabel.setVisible(True)
            self.ui.relayStatusLbl.setText(f"")
     


    def closeWithoutRemote(self):
        self.relay_1.off()
        from scripts.mainMenuProgram import mainMenu

        self.window1 =mainMenu()
        self.window1.show()
        self.close()
      
        print("end")

     
        