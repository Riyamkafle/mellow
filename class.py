# #make a calculator using class


# class calculator:
#     def add(self, a,b):
#         return a + b
#     def subtract(self , a, b):
#         return a-b
#     def Division(self , a , b ):
#         if b==0:
#             return "error!"
#         return a / b

#     def multiply(self, a , b ):
#         return a * b
# calc = calculator()
# print("Addition:", calc.add(5, 3))
# print("Subtraction:", calc.subtract(10, 4))
# print("Multiplication:", calc.multiply(6, 7))
# print("Division:", calc.Division(15, 3))


class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed"

def main():
    calculator = Calculator()

    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    operation = input(''' 
Please type in the math operation you would like to complete: 
+ for addition 
- for subtraction 
* for multiplication 
/ for division 
''')

    if operation == '+':
        print(num1, "+", num2, "=", calculator.add(num1, num2))

    elif operation == '-':
        print(num1, "-", num2, "=", calculator.subtract(num1, num2))

    elif operation == '*':
        print(num1, "*", num2, "=", calculator.multiply(num1, num2))

    elif operation == '/':
        print(num1, "/", num2, "=", calculator.divide(num1, num2))

    else:
        print('You have not typed a valid operator, please run the program again.')

if __name__ == "__main__":
    main()
