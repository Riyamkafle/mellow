# # subjects_marks= {}

# # for i in range (1,6):
# #     subject= input("enter the subjects name: ")
# #     subjects_marks[subject]
# #     marks= int(input("enter the marks: "))
# #     subjects_marks[subject]= marks

# # print ("your data looks like: ", subjects_marks)

# # subjects_marks = {}

# # for i in range (1,6):
# #     subject = input("Enter the subject's name: ")
# #     marks = int(input("Enter the marks: "))
# #     subjects_marks[subject] = marks
# #     subjects_marks= ['division']= "first division"
    

# # print ("Your data looks like: ", subjects_marks)
# # Number of students
# num_students = 10

# # List of 5 subjects
# subjects = ["Math", "Science", "English", "History", "Geography"]

# # Data structure to hold student information
# students = []

# # Input details for each student
# for _ in range(num_students):
#     student_data = {}
    
#     # Input student name and roll number
#     student_data['name'] = input("Enter the student's name: ")
#     student_data['roll_number'] = input("Enter the student's roll number: ")

#     marks = []
    
#     # Input marks for each subject
#     for subject in subjects:
#         mark = int(input(f"Enter marks for {subject}: "))
#         marks.append(mark)
    
#     # Calculate total marks, percentage, and average
#     student_data['marks'] = marks
#     total_marks = sum(marks)
#     student_data['total_marks'] = total_marks
#     percentage = total_marks / len(subjects)
#     student_data['percentage'] = percentage
#     average = total_marks / len(subjects)
#     student_data['average'] = average
    
#     # Determine division
#     if percentage >= 60:
#         division = "First Division"
#     elif percentage >= 45:
#         division = "Second Division"
#     elif percentage >= 33:
#         division = "Third Division \nTry harder"
#     else:
#         division = "Fail"
    
#     student_data['division'] = division
    
#     # Add student data to the list
#     students.append(student_data)
    
#     print("\n")  # Separate each student's input with a blank line

# # Print results for all students
# print("\n--- Results ---\n")
# for student in students:
#     print(f"Name: {student['name']}")
#     print(f"Roll Number: {student['roll_number']}")
#     for i in range(len(subjects)):
#         print(f"{subjects[i]}: {student['marks'][i]} marks")
#     print(f"Total Marks: {student['total_marks']}")
#     print(f"Percentage: {student['percentage']:.2f}%")
#     print(f"Average: {student['average']:.2f}%")
#     print(f"Division: {student['division']}")
#     print("\n")  # Separate each student's result with a blank line
# Number of students
total_subjects= int(input("enter the total number of subjects"))
num_students = int(input("enter the number of students: "))


# Data structure to hold information for all students
students_data = []

# Loop to collect data for each student
for _ in range(num_students):
    student = {}
    
    # Input student's name and roll number
    student['name'] = input("Enter the student's name: ")
    student['roll_number'] = input("Enter the student's roll number: ")

    # Initialize dictionary to store subjects and marks
    subjects_marks = {}
    
    # Loop to collect marks for 5 subjects
    for i in range(total_subjects):
        subject = input(f"Enter the name of subject {i}: ")
        marks = int(input(f"Enter marks for {subject}: "))
        subjects_marks[subject] = marks
    
    # Store subjects and marks in the student dictionary
    student['subjects_marks'] = subjects_marks
    
    # Calculate total marks, percentage, and average
    total_marks = sum(subjects_marks.values())
    student['total_marks'] = total_marks
    num_subjects = len(subjects_marks)
    percentage = total_marks / num_subjects
    student['percentage'] = percentage
    average = total_marks / num_subjects
    student['average'] = average
    
    # Determine division based on percentage
    if percentage >= 60:
        division = "First Division"
    elif percentage >= 45:
        division = "Second Division"
    elif percentage >= 33:
        division = "Third Division \nTry harder"
    else:
        division = "Fail"
    
    student['division'] = division
    
    # Add this student's data to the list of students
    students_data.append(student)
    print("\n")  # Separate each student's input with a blank line

# Print results for all students
print("\n--- Results ---\n")
for student in students_data:
    print(f"Name: {student['name']}")
    print(f"Roll Number: {student['roll_number']}")
    for subject, marks in student['subjects_marks'].items():
        print(f"{subject}: {marks} marks")
    print(f"Total Marks: {student['total_marks']}")
    print(f"Percentage: {student['percentage']:.2f}%")
    print(f"Average: {student['average']:.2f}%")
    print(f"Division: {student['division']}")
    print("\n")  # Separate each student's result with a blank line
