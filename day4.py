class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    
    def displayData(self):
        print(f"The Car is: {self.name}\nModel is: {self.model}")
    
    @property
    def getName(self):
        return self.name
    @getName.setter
    def setName(self,name1):
        self.name=name1

obj1=Car("Yamaha",1101)

# print(obj1.getName) # recommeded way
# print(obj1.name) # comman way to acces data or get data

# obj1.name="Honda" # comman way to set data
obj1.setName="Honda" # recommeded way


obj1.displayData()