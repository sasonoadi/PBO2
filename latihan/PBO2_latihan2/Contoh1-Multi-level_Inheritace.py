class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} speak")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def Breed(self):
        print(f'{self.name} descendant of {self.breed} Breed')

class Bulldog(Dog):
    def __init__(self, name, breed, origin):
        super().__init__(name, breed)
        self.origin = origin

    def Origin(self):
        print(f"{self.name} is a {self.breed} Britania")

buldog = Bulldog("Black Key", 'Mastiff Combat', "Britania")
buldog.Breed() 
buldog.Origin() 
