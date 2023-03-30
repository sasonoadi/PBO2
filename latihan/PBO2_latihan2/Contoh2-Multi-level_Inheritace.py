class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name\t   : {self.name}\nAge\t   : {self.age}")

class Employee(Person):
    def __init__(self, name, age, id, salary):
        super().__init__(name, age) 
        self.id = id
        self.salary = salary

    def get_details(self):
        super().get_details()
        print(f"ID\t   : {self.id}\nSalary\t   : {self.salary}")

class Manager(Employee):
    def __init__(self, name, age, id, salary, department):
        super().__init__(name, age, id, salary) 
        self.department = department

    def get_details(self): 
        super().get_details()
        print(f"Department : {self.department}")


manager = Manager('Adi', '27th', '160202','Rp.70jt', 'IT')
manager.get_details()
