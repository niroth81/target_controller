
from programs.masterProgram import masterPrograms
import time

class IntlRapidProgram(masterPrograms):

    def __init__(self, matchInstructions, Sequencedescription):
        super().__init__(matchInstructions, Sequencedescription)

        self.matchInstructions = matchInstructions
        
        self.ListOfSequences = [
                ["ON:3","OFF:8","ON:3"],
                ["ON:3","OFF:8","ON:3"],
                ["ON:3","OFF:6","ON:3"],
                ["ON:3","OFF:6","ON:3"],
                ["ON:3","OFF:4","ON:3"],
                ["ON:3","OFF:4","ON:3"],
                ["ON:3","OFF:8","ON:3"],
                ["ON:3","OFF:8","ON:3"],
                ["ON:3","OFF:6","ON:3"],
                ["ON:3","OFF:6","ON:3"],
                ["ON:3","OFF:4","ON:3"],
                ["ON:3","OFF:4","ON:3"]
        ];
       

        self.programGroupDescriptons=[
            "5 shots in 8 seconds at 25 Yards using ISSF Rapid Fire Target",
            "5 shots in 8 seconds at 25 Yards using ISSF Rapid Fire Target",
            "5 shots in 6 seconds at 25 Yards using ISSF Rapid Fire Target",
            "5 shots in 6 seconds at 25 Yards using ISSF Rapid Fire Target",
            "5 shots in 4 seconds at 25 Yards using ISSF Rapid Fire Target",
            "5 shots in 4 seconds at 25 Yards using ISSF Rapid Fire Target",
            "5 shots in 8 seconds at 25 Yards using ISSF Rapid Fire Target",
            "5 shots in 8 seconds at 25 Yards using ISSF Rapid Fire Target",
            "5 shots in 6 seconds at 25 Yards using ISSF Rapid Fire Target",
            "5 shots in 6 seconds at 25 Yards using ISSF Rapid Fire Target",
            "5 shots in 4 seconds at 25 Yards using ISSF Rapid Fire Target",
            "5 shots in 4 seconds at 25 Yards using ISSF Rapid Fire Target"
             ];
        
        

    def procedure(self):
        self.relay_1 =super().initilaiseRGPIO();
