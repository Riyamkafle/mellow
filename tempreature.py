# tempreture = int(input("enter the temprature"))
# i = 1
# while   i <=tempreture:
#     i +=1
#     print("It's cold")
# else:
#     print("It's not cold")


# i = 1 
# while i<5:
#     temp=int(input("enter the temprature"))
#     i += 1
#     if temp > 20:
#         print("turn on your AC")
#         break
#     else:
#         print("turn off your AC")
    
        
    # else:
    #     print("it's normal")

letter = "abcd"
for i in letter :
    print (i, end=" ,")
    for j in letter :
        print(i+j, end=",")
        for k in letter :
            print(i+j+k, end=",")
            for l in letter :
                print(i+j+k+l, end=",")
                print()  # print a newline to separate the output of each iteration of the outer loop
    