import random

low = 1
high = 100
guesses = 1
number = random.randint( low, high)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
while True:
    guess = int(input(f"Take a guess between {low} - {high}: "))
    guesses += 1 
    if guess > number :
        print(f" {guess}Too high!")
    elif guess < number:
        print(f" {guess}Too low!")
    else: 
        print(f"Yay, you found the number in {guesses} guesses!")
        break
print(f"this round took you {guesses} guesses")


