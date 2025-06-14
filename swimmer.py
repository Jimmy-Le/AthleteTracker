from athlete import Athlete


class Swimmer(Athlete):
    def __init__(self, name, age, style, country = None, salary = None, time = None):
        super().__init__(name, age, country, salary)
        self.stroke_style = style
        self.personal_best_time = time

    def __str__(self):
        text = f"Swimmer: {self.name},{self.age},{self.stroke_style},{self.country if self.country is not None else ""},{self.salary if self.salary is not None else ""},{self.personal_best_time if self.personal_best_time is not None else ""}\n"
        return text

    @staticmethod
    def parse(text):
        newPlayer = Swimmer(None, None, None)

        for index, field in enumerate(text):
            try:
            
                if(index == 0):
                    newPlayer.name = field
                elif (index == 1):
                    newPlayer.age = int(field)
                elif (index == 2):
                    newPlayer.stroke_style = field
                elif (index == 3): 
                    newPlayer.country = field
                elif (index == 4): 
                    newPlayer.salary = float(field)
                elif (index == 5): 
                    newPlayer.personal_best_time = float(field)
            except:
                pass

        return newPlayer
    

