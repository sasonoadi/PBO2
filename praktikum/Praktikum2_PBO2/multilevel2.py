class Plant:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} speak")

class Flower(Plant):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def Color(self):
        print(f'{self.name} Colored {self.color}')

class Rose(Flower):
    def __init__(self, name, color, origin):
        super().__init__(name, color)
        self.origin = origin

    def Origin(self):
        print(f"{self.name} Origin Form {self.origin} ")

rose = Rose("Rose", 'Read', "China, Middle East & eastern europe")
rose.Color() 
rose.Origin() 
