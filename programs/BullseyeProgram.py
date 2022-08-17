
from programs.masterProgram import masterPrograms
import time

class BullseyeProgram(masterPrograms):

    def __init__(self, matchInstructions, Sequencedescription):
        super().__init__(matchInstructions, Sequencedescription)

        self.matchInstructions = matchInstructions
        
        self.ListOfSequences = [
                ["ON:7","OFF:600","ON:3"],
                ["ON:7","OFF:600","ON:3"],
                ["ON:7","OFF:600","ON:3"],
                ["ON:7","OFF:20","ON:3"],
                ["ON:7","OFF:20","ON:3"],
                ["ON:7","OFF:10","ON:3"],
                ["ON:7","OFF:10","ON:3"],
                ["ON:7","OFF:600","ON:3"],
                ["ON:7","OFF:20","ON:3"],
                ["ON:7","OFF:20","ON:3"],
                ["ON:7","OFF:20","ON:3"],
                ["ON:7","OFF:20","ON:3"],
                ["ON:7","OFF:10","ON:3"],
                ["ON:7","OFF:10","ON:3"],
                ["ON:7","OFF:10","ON:3"],
                ["ON:7","OFF:10","ON:3"]

        ];
       

        self.programGroupDescriptons=[
            "Slow Fire: 10 shots in 10 minutes at 50 Yards using NRA B-6 Target",
            "Slow Fire: 10 shots in 10 minutes at 50 Yards using NRA B-6 Target",
            "Slow Fire: 10 shots in 10 minutes at 50 Yards using NRA B-6 Target",
            "Timed Fire: 5 shots in 20 seconds at 25 Yards using NRA B-8 Target",
            "Timed Fire: 5 shots in 20 seconds at 25 Yards using NRA B-8 Target",
            "Rapid Fire: 5 shots in 10 seconds at 25 Yards using NRA B-8 Target",
            "Rapid Fire: 5 shots in 10 seconds at 25 Yards using NRA B-8 Target",
            "Slow Fire: 10 shots in 10 minutes at 50 Yards using NRA B-6 Target",
            "Timed Fire: 5 shots in 20 seconds at 25 Yards using NRA B-8 Target",
            "Timed Fire: 5 shots in 20 seconds at 25 Yards using NRA B-8 Target",
            "Timed Fire: 5 shots in 20 seconds at 25 Yards using NRA B-8 Target",
            "Timed Fire: 5 shots in 20 seconds at 25 Yards using NRA B-8 Target",
            "Rapid Fire: 5 shots in 10 seconds at 25 Yards using NRA B-8 Target",
            "Rapid Fire: 5 shots in 10 seconds at 25 Yards using NRA B-8 Target",
            "Rapid Fire: 5 shots in 10 seconds at 25 Yards using NRA B-8 Target",
            "Rapid Fire: 5 shots in 10 seconds at 25 Yards using NRA B-8 Target"
 
            ];
        
        

    def procedure(self):
        self.relay_1 =super().initilaiseRGPIO();
