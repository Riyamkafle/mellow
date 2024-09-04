time = 1
while time ()<100:
    print("your 100")
    time += 1
user= float(input("enter  a number :"))

if user % 2 == 0:
    print("the number is odd")
else:
    print("the number is even")

for i in range (1 ,  51):
    if i % 2 == 0:
        print (f"{i} is even")
    else:
        print (f"{i} is odd")


# loop assignment 
i = 1 
j = 1
while i<=5 :
    print("riyam ", end="" )
    j=1
    while j<=4:
        print("manik ", end="")
        j= j+1

    i= i +1 
    print()
 loop practise 

i = 1
j= 1
while i <= 10:
    print("reeyam", end=" ")
    j = 1
    while j <= 9:
        print("chacha", end=" ")
        i = i +1
        j = j + 1
        
        print()


n = 1 

int (input("enter your number: "))
while n <= 3:
    print(n)
    n= n +1
    # loop practice 2


# sum of first n natural numbers
n= int (input("enter the value of n: "))
sum = 0
while n> 0 :
    sum = sum +n
    n= n-1
    print(f"sum is {sum}")
else :
    print("loop ended here")
    loop practice 3

num = int(input("enter 5 numbers: "))
for i in range(1,5):
    num = i+ num
    print(num)  # loop practice 4

sum = 0 

# for i in range(5):
#     num = int(input("enter your 5 numbers: "))
#     sum = sum + num
#     print(sum)

# colors= ["red","yellow","blue","green"]
# for color in colors:
#     print(colors, end=" ")
#     for i in color:
#         print(i)

for m in range(1,20000):
    print(m+1)
    

