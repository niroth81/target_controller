from programs.masterProgram import masterPrograms
import time

class serviceProcedure(masterPrograms):

    def __init__(self, matchInstructions, Sequencedescription):
        super().__init__(matchInstructions, Sequencedescription)


        self.ListOfSequences = [
                ["ON:7","OFF:10","ON:3"],
                ["ON:7","OFF:10","ON:3"],
                ["ON:7","OFF:10","ON:3"],
                ["ON:7","OFF:10","ON:3"],
                ["ON:7","OFF:10","ON:3"]
        ];
     
        self.programGroupDescriptons = [
        "short Desription program service 1",
        "short Desription program service 2",
        "short Desription program  service3",
        "short Desription program  service4",
        "short Desription program  service5"
        
        ];
        
        

    def procedure(self):
        self.relay_1 =super().initilaiseRGPIO();
     
   