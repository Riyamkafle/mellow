# Get input from the user
num = int(input("Enter a number: "))

# Initial assumption
is_prime = True

# Check if the number is less than 2
if num < 2:
    result = "neither prime nor composite"
elif num == 2 or num == 3:
    result = "prime"
elif num % 2 == 0 or num % 3 == 0:
    result = "composite"
else:
    result = "prime"

# Output the result
print(f"{num} is {result}.")

