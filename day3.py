# def addTwoNum(num1,num2):
#     print("The sum is :",num1+num2)


# def greetFunc(func):
#     print("----------------")
#     func(8,8)
#     print("----------------")

# greetFunc(addTwoNum)

def decorator(addTwoNum):
    def mfx():
        print("Good Morning")
        addTwoNum()
        print("BBye Byye")
    return mfx

@decorator
def addTwoNum():
    print("Shivam")

addTwoNum()
