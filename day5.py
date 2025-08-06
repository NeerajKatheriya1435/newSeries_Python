# Multiple inheritance
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def printDetails(self):
        print(f"My name is {self.name} and age is {self.age}")

# obj1=Student("Mridul",23)
# obj1.printDetails()

class Teacher:
    def __init__(self,id,salary):
        self.id=id
        self.salary=salary
    
    def showDetails(self):
        print(f"My id is {self.id} and salary is {self.salary}")
    
# myObj=Teacher(420,30000)
# myObj.showDetails()

class Hacker(Student,Teacher):
    def __init__(self, name, age,id,salary,lang):
        Teacher.__init__(self,id,salary)
        self.lang=lang
        super().__init__(name, age)
    
    def details(self):
        print(f"My name is hacker {self.name}")
        print(f"My age is {self.age}")
        print(f"My salary is {self.salary}")
        print(f"My language is {self.lang}")

# obj1=Hacker("Mridul",12,420,300000,"Python")
# obj1.printDetails()
print(Hacker.mro())
