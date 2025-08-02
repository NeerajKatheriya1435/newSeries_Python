
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showDetail(self):
        print(f"My name is {self.name} and age is {self.age}")


# newObj1=Employee("Mridul",18)
# newObj1.showDetail()

# newObj2=Employee("Ayush",27)
# newObj2.showDetail()

newObj3=Employee("Shubham",67)
newObj3.showDetail()
