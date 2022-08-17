from abc import ABC, abstractmethod, abstractstaticmethod
from distutils.log import error
from logging import raiseExceptions
from pickle import FALSE
import sys
import gpiozero
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from PyQt5 import QtWidgets

class masterPrograms(ABC):

    def __init__ (self,matchInstructions,Sequencedescription):
        
        self.matchInstructions = matchInstructions
        self.Sequencedescription =Sequencedescription
        self.remoteIPaddress = "192.168.1.63"
        self.relay_1=None

	
    @abstractmethod
    def procedure(self):
        pass
  

    def initilaiseRGPIO(self):

        RELAY_1_pin = 10
       

        try:
            factory = PiGPIOFactory(host='192.168.1.63')

            self.relay_1 = gpiozero.OutputDevice(RELAY_1_pin,pin_factory=factory, active_high=False, initial_value=False)
            
            return self.relay_1

        except:
              
            print("remote connection error")
		


    if __name__ == "__main__":
        pass
