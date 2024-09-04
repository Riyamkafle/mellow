user= float(input("enter  a number :"))

if user % 2 == 0:
    print("the number is odd")
else:
    print("the number is even")


num= int(input("enter your number:"))

# assumption
is_prime = True

#now check the number is less than 2 or not
if num < 2 :
    print("the number is neither a prime nor a composite")
elif num == 2 or num == 3 :
    result = "prime"
elif num % 2 == 0 or num % 3 == 0:
    result="composite"
else :
    result = "prime "

# # now outputing the  results 
# print(f"{num} is a {resuli 

# run = int(input("enter a number"))
# for i in range (run ):
#     b= run-i

#     print(b)  # prints: 50 49 48 47 46 45
#     if b==5:
#         break


    


# i= 1 
# while i<=50:
#     if i % 2 == 0:
#         print("the number is even",i)
#     else:
#         print("the number is odd",i)


data = "1,2,3,4,5,6,7,8"
