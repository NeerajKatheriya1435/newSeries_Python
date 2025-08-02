# lst1=[8,7,5,4]
# sum=sum(lst1)
# sum1=sum1(lst1)
# print(sum)

# problem add two number

# a=8
# b=6
# sum=a+b

# a1=8
# b1=5
# print(sum)

# print(a1+b1)

# def sumTwoNum(a,b):
#     print(a+b)

# sumTwoNum(5,3)
# sumTwoNum(2,3)

# lst1=[7,4,8,5]
# sum=0
# for i in range(len(lst1)):
#     sum+=lst1[i]

# print("The sum is",sum)

# print("Shreshtha","Shubham","Harsh",sep="-")
# for i in range(8):
#     print(i,end=" and ")

# print("Mridul")
# print("Mridul")
# print("Mridul")
# print("Mridul")
# print("Mridul")
# print("Mridul")
# print("Mridul")
# print("Mridul")

# inp1=int(input("Enter you number: "))

# for i in range(inp1+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

class Employee:
    name=""
    age=78

    def showDetail(self):
        print(f"My name is {self.name} and age is {self.age}")

obj1=Employee()

obj1.name="Mridul"
obj1.age=18
# print(obj1.age)
# print(obj1.name)
obj1.showDetail()

obj2=Employee()

obj2.name="Harsh"
obj2.age=45
obj2.showDetail()


obj3=Employee()
obj3.showDetail()

# obj1.showDetail()