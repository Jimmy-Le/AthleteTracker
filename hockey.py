from athlete import Athlete 
from enum import Enum
#import x from y

class HockeyPosition(Enum):
    Forward = "Forward"
    Defenseman = "Defenseman"
    Goalie = "Goalie"


class HockeyPlayer(Athlete):


    def __init__( self, name, age, country = None, salary = None, position = None, goals = None, brand = None, size = None):
        super().__init__(name, age, country, salary)

        self.position = position
        self.goals_scored = goals
        self.stick_brand = brand
        self.skates_size = size 
    
    def __str__(self):
        text = f"HockeyPlayer: {self.name}, {self.age}, {self.country}, {self.salary}, {self.goals_scored}, {self.stick_brand}, {self.skates_size}"
        return text
    
    def printStats(self):
        print(self.goals_scored, self.name)
        


    @staticmethod
    def parse(text):
    
        newPlayer = HockeyPlayer(None, None)

        for index, field in enumerate(text):
            try:
            
                if(index == 0):
                    newPlayer.name = field
                elif (index == 1):
                    newPlayer.age = int(field)
                elif (index == 2):
                    newPlayer.country = field
                elif (index == 3): 
                    newPlayer.salary = float(field)
                elif (index == 4): 
                    newPlayer.position = HockeyPosition(field)
                elif (index == 5): 
                    newPlayer.goals_scored = int(field)
                elif (index == 6): 
                    newPlayer.stick_brand = field
                elif (index == 7): 
                    newPlayer.skates_size = int(field)

            except:
                pass

        return newPlayer

