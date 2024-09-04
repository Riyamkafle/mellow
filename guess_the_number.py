import random

num_lists = random.sample(range(100, 200), 15)

selected_number = random.choice(num_lists)

user_input = int(input("Enter your number: "))

if user_input > selected_number:
    print("Computer number:", selected_number)
    print("Your guess is too high.")
elif user_input < selected_number:
    print("Computer number:", selected_number)
    print("Your guess is too low.")
else:
    print("Computer number:", selected_number)
    print("Your guess is correct!")
