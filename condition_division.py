# information of the students
name= input("enter the students name here!:  ")
total_marks= float(input("enter the total marks of you lad:  "))
total_subjects= float(input("enetr the total subjects here!:  "))
science= float(input("enetr your science marks "))
math= float(input("enetr your math marks "))
english= float(input("enetr your english marks "))
social= float (input("enter your sicial marks"))
computer= float(input("enetr your computer marks "))

#now we calculate the percentage of the studnets 
percentage = (total_marks / (total_subjects * 100)) * 100

#division using the if and else condition 
if percentage >=80 :
    division= "{percentage} Distinction \n good job{name}" 
elif percentage >= 60:
    division="First division"
elif percentage >= 45:
    division="Second division "
elif percentage >= 33:
    division="third division" 
else: 
    division="failed!"
    

# now displaying the results below:
print(f"\n students Name: {name} ") 
print(f"total marks: {total_marks}" )    
print(f"percentage : {percentage:.2f}%" )
print(f"division:  {division}")

