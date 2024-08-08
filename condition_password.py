password = input("Enter your password: ")

special_characters = "!@#$%^&*()-+?_=,<>/"

# Initialize flags
case1  = False
case2 = False

# Check each character in the password
for char in password:
    if char in special_characters:
        case1 = True
    if char.isdigit():
        case2 = True

# Validate the password
if case1 and case2:
    print("The password is valid.")
else:
    print("The password is invalid.")
