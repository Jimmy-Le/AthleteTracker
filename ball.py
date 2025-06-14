from athlete import Athlete


class BallPlayer(Athlete):
    def __init__(self, name, age, team, jersey, country, salary,  endorsement):
        super().__init__(name, age, country, salary)
        
        self.team_name = team
        self.jersey_number = jersey
        self.endorsement = endorsement

    def printEndorsement(self):
        print("Endorsement:", self.endorsement)


class BasketballPlayer(BallPlayer):
    def __init__(self, name, age, team, jersey, country = None, salary = None, endorsement = None,  pct = None, rebounds = None):
        super().__init__(name, age, team, jersey, country, salary, endorsement)
        
        self.three_point_pct = pct
        self.rebounds = rebounds

    def printStats(self):
        # Use Dictionary to keep track
        print(self.endorsement)
    
    def __str__(self):
        text = f"BasketballPlayer: {self.name}, {self.age}, {self.team_name}, {self.jersey_number}, {self.country}, {self.salary}, {self.endorsement}, {self.three_point_pct}, {self.rebounds}"
        return text

    @staticmethod
    def parse(text):
        newPlayer = BasketballPlayer(None, None, None, None)

        for index, field in enumerate(text):
            try:
            
                if(index == 0):
                    newPlayer.name = field
                elif (index == 1):
                    newPlayer.age = int(field)
                elif (index == 2):
                    newPlayer.team_name = field
                elif (index == 3):
                    newPlayer.jersey_number = int(field)
                elif (index == 4):
                    newPlayer.country = field
                elif (index == 5): 
                    newPlayer.salary = float(field)
                elif (index == 6): 
                    newPlayer.endorsement = field
                elif (index == 7): 
                    newPlayer.three_point_pct = float(field)
                elif (index == 8): 
                    newPlayer.rebounds = int(field)

            except:
                pass

        return newPlayer
    

class FootballPlayer(BallPlayer):
    def __init__(self, name, age, team, jersey, country = None, salary = None,  endorsement = None, touchdowns = None, yards = None):
        super().__init__(name, age, team, jersey, country, salary,  endorsement)
        
        self.touchdowns = touchdowns
        self.passing_yards = yards

    def printStats(self):
        print(self.touchdowns, self.name)

    def __str__(self):
        text = f"FootballPlayer: {self.name}, {self.age}, {self.team_name}, {self.jersey_number}, {self.country}, {self.salary}, {self.endorsement}, {self.touchdowns}, {self.passing_yards}"
        return text

    @staticmethod
    def parse(text):
        newPlayer = FootballPlayer(None, None, None, None)

        for index, field in enumerate(text):
            try:
            
                if(index == 0):
                    newPlayer.name = field
                elif (index == 1):
                    newPlayer.age = int(field)
                elif (index == 2):
                    newPlayer.team_name = field
                elif (index == 3):
                    newPlayer.jersey_number = int(field)
                elif (index == 4):
                    newPlayer.country = field
                elif (index == 5): 
                    newPlayer.salary = float(field)
                elif (index == 6): 
                    newPlayer.endorsement = field
                elif (index == 7): 
                    newPlayer.touchdowns = int(field)
                elif (index == 8): 
                    newPlayer.passing_yards = int(field)

            except:
                pass

        return newPlayer