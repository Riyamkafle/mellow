
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Input the operator
operator = input("Enter the operation you want to perform (+, -, *, /): ")

# Perform the operation based on the operator
if operator == "+":
    result = a + b
    print(f"{a} + {b} = {result}")

elif operator == "-":
    result = a - b
    print(f"{a} - {b} = {result}")

elif operator == "*":
    result = a * b
    print(f"{a} * {b} = {result}")

elif operator == "/":
    if b != 0:  # Check to avoid division by zero
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("Error! Division by zero.")
        result = None

else:
    print("Invalid operator")
    result = None

# Display the final result if the operation was valid
if result is not None:
    print(f"The result of the operation is: {result}")
