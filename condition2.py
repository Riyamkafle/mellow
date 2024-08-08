# email = input("Enter your email address: ")

# if "@" in email and "." in email:
#     data1 = email.index("@")
#     data2 = email.rindex(".")
#     data3 = email.index("com")   
#     # Ensure "@" is not the first or last character and there is a "." after "@"
#     if data1 > 0 and data2 > data1 + 1 and data2 < len(email) - 1:
#         print("The email address is valid.")
#     else:
#         print("The email address is invalid.")
# else:
#     print("The email address is invalid.")


percentage = float(input("Enter your marks percentage: "))

# Determine the division based on the percentage
if percentage >= 60:
    print("First Division")
elif 50 <= percentage < 60:
    print("Second Division")
elif 40 <= percentage < 50:
    print("Third Division")
else:
    print("Fail")
# determine the division based on the name of the students snd percentage 
studentsname(input("enter your name here"))
marks_percentage = float (input ("enter your marks percentage "))


