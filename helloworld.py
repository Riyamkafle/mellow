print ("hello_world")


# the student's information
name = input("Enter the name of the student: ")
total_marks = int(input("Enter the total marks obtained: "))
total_subjects = int(input("Enter the number of subjects: "))

# Calculating total subject  percentage
percentage = (total_marks / (total_subjects * 100)) * 100

#  division using if-else conditions
if percentage >= 60:
    division = "First Division"
elif percentage >= 45:
    division = "Second Division"
elif percentage >= 33:
    division = "Third Division"
else:
    division = "Fail"


print(f"\nStudent Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Division: {division}")