import sys

# Set
s = set()
s.add(5)
s.add(3)
s.add(2)
s.add(9)
s.add(3)

# OOP
class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            print("Error: Cannot divide by 0")
            sys.exit(1)


# try:
#     x = int(input("Enter x : "))
#     y = int(input("Enter y : "))
# except ValueError:
#     print("Error: Invalid input")
#     sys.exit(1)

# c = Calculator(x, y)
# print(f"Addition: {c.add()}.  Subtraction: {c.subtract()}.   Multiplication: {c.multiply()}.   Division: {c.divide()}.")

# Decorators

def announce(f):
    def wrapper():
        print("Function starts")
        f()
        print("Function ends")
    return wrapper

@announce
def hello():
    print("Hello, world")

hello()