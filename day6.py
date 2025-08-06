class Student:
    def __init__(self,name):
        self.name=name

class Result(Student):
    def __init__(self, name,physics,chemistry):
        super().__init__(name)
        self.physics=physics
        self.chemistry=chemistry
    
    def showMarks(self):
        print(f"The marks in physics: {self.physics}")
        print(f"The marks in chemistry: {self.chemistry}")

class AverageMarks(Result):
    def __init__(self, name, physics, chemistry):
        super().__init__(name, physics, chemistry)
        self.average=(physics+chemistry)/2
    
    def showResult(self):
        print(f"My name is: {self.name}")
        print(f"The average is: {self.average}")

obj1=AverageMarks("Mridul",70,72)
obj1.showResult()


# heracrical iheritance -->a,b,c---d
# hybrid inheritance -->combination of single level multilevel multipule