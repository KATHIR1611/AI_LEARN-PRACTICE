class Calc:
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b


Number_1 = int(input("Enter the first number : "))
Number_2 = int(input("Enter the second number :"))
Operation = input("Specify your operation like Addition(+) , Subtraction(-), Multiplication(*), Division(/) : ")

c=Calc(Number_1,Number_2)
if Operation =="+":
    print(c.add())
elif Operation =="-":
    print(c.sub())
elif Operation =="*":
    print(c.mul())
elif Operation =="/":
    print(c.div())
else:
    print("Select a valid Operation")


