
from programs.masterProgram import masterPrograms
import time

class CenterFireProgram(masterPrograms):

    def __init__(self, matchInstructions, Sequencedescription):
        super().__init__(matchInstructions, Sequencedescription)

        self.matchInstructions = matchInstructions
        
        self.ListOfSequences = [
                ["ON:7","OFF:300","ON:3"],
                ["ON:7","OFF:300","ON:3"],
                ["ON:7","OFF:300","ON:3"],
                ["ON:7","OFF:300","ON:3"],
                ["ON:7","OFF:300","ON:3"],
                ["ON:7","OFF:300","ON:3"],
                
                ["ON:3","OFF:3","ON:7"],
                ["ON:3","OFF:3","ON:7"],
                ["ON:3","OFF:3","ON:7"],
                ["ON:3","OFF:3","ON:7"],
                ["ON:3","OFF:3","ON:7"],
                ["ON:3","OFF:3","ON:7"]


        ];
       

        self.programGroupDescriptons=[
            "Precision Stage: 5 shots in 5 minutes at 25 Yards using ISSF 25Yd Precision Target",
            "Precision Stage: 5 shots in 5 minutes at 25 Yards using ISSF 25Yd Precision Target",
            "Precision Stage: 5 shots in 5 minutes at 25 Yards using ISSF 25Yd Precision Target",
            "Precision Stage: 5 shots in 5 minutes at 25 Yards using ISSF 25Yd Precision Target",
            "Precision Stage: 5 shots in 5 minutes at 25 Yards using ISSF 25Yd Precision Target",
            "Precision Stage: 5 shots in 5 minutes at 25 Yards using ISSF 25Yd Precision Target",
            "Rapid Fire: 5 shots in 3 seconds at 25 Yards using ISSF Large Dueling Target",
            "Rapid Fire: 5 shots in 3 seconds at 25 Yards using ISSF Large Dueling Target",
            "Rapid Fire: 5 shots in 3 seconds at 25 Yards using ISSF Large Dueling Target",
            "Rapid Fire: 5 shots in 3 seconds at 25 Yards using ISSF Large Dueling Target",
            "Rapid Fire: 5 shots in 3 seconds at 25 Yards using ISSF Large Dueling Target",
            "Rapid Fire: 5 shots in 3 seconds at 25 Yards using ISSF Large Dueling Target"
 
            ];
        
        

    def procedure(self):
        self.relay_1 =super().initilaiseRGPIO();
