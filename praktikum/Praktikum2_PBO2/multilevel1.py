class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name\t   : {self.name}\nAge\t   : {self.age}")

class BussinessMan(Person):
    def __init__(self, name, age, business, income):
        super().__init__(name, age) 
        self.business = business
        self.income = income

    def get_details(self):
        super().get_details()
        print(f"Business   : {self.business}\nIncome\t   : {self.income}")

class Manager(BussinessMan):
    def __init__(self, name, age, business, income, position):
        super().__init__(name, age, business, income) 
        self.position = position

    def get_details(self): 
        super().get_details()
        print(f"Position   : {self.position}")


manager = Manager('Adi', '35th', 'Packaging','Rp.200jt', 'Director')
manager.get_details()
