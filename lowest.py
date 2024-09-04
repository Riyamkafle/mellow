# # data = int (input("enter your numbers "))

# # lowest_digit = 9

# # for digit in data:
# #     if int(digit) < lowest_digit:
# #         lowest_digit = int(digit)
        
# # print(f"The lowest digit in {data} is {lowest_digit}")

# # Get the number of inputs from the user
# num_values = int(input("Enter the number of values you want to input: "))

# # Initialize an empty list to store the values
# values = []

# # Collect the values from the user
# for _ in range(num_values):
#     value = float(input("Enter a value: "))
#     values.append(value)

# # Find the lowest and highest values
# lowest_value = min(values)
# highest_value = max(values)

# # Print the results
# print(f"The lowest value is: {lowest_value}")
# print(f"The highest value is: {highest_value}")


#count the word
# word= input("enter the word")
# count = 0
# for letter in word:
#     if letter == " ":
#         count += 1
#         print(count)


# program that takes a positive integer as input and calculates the sum of its digits.
# data = int(input("enter the number"))
# sum = 0
# for digit in str(data):
#     sum += int(digit)

# print (sum)

#write a program that takes a string as input and prints the strings in reverse oreder 
# word = input("enter a word")
# print(word[::-1])
# print (word[::-1])
#write a program that checks the given word is palindrome (reads the same forward and backward)
word = input("enter a word: ")
if print(word == word[::-1]):
    print("the word is palindrome")
else:
    print("the word is not palindrome")

