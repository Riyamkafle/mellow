
roll_number = input("Enter the student's roll number: ")

# List of 5 subjects
subjects = ["Math", "Science", "English", "History", "Geography"]
marks = []

# Input marks for each subject
for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

# Calculate total marks and percentage
total_marks = sum(marks)
num_subjects = len(subjects)
percentage = total_marks / num_subjects
average= total_marks/num_subjects

# calculate the division
if percentage >= 60:
    division = "First Division"
elif percentage >= 45:
    division = "Second Division"
elif percentage >= 33:
    division = "Third Division /n try harder"
else:
    division = "Fail"

# Print results with formatting methods
print("\n--- Result ---")
print(f"Roll Number: {roll_number}")
for i in range(num_subjects):
    print(f"{subjects[i]}: {marks[i]} marks")

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Division: {division}")
print(f"Average: {average:.2f}%")
# roll_no= int(input("enter your roll no: "))
# marks = []
# for i in range(5):
#     marks.append(int(input(f"enter the marks of subject {i+1}: ")))
#     total = sum(marks)
#     percentage = (total/500)*100
#     # 12
#       # calculate the division
#     if percentage >= 60:
#         division = "First Division"
#     elif percentage >= 45:
#         division = "Second Division"
#     elif percentage >= 33:
#         division = "Third Division /n try harder"
#     else:
#         print(" you're fail")
#         print(f"your percentage is {percentage}%")
#         print(f"your total marks is {total}")
#         print(f"your roll no is {roll_no}")
#         # print(f"your average marks is {average}")
        


