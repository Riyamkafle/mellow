# Get choices
riyam = input("Riyam, please choose rock, paper, or scissors: ").lower()
manik = input("Manik, please choose rock, paper, or scissors: ").lower()

# Determine the winner using if-else conditions
if riyam == manik:
    print("It's a tie!")
elif riyam == "rock" and manik == "scissors":
    print("Riyam wins!")
elif riyam == "scissors" and manik == "paper":
    print("Riyam wins!")
elif riyam == "paper" and manik == "rock":
    print("Riyam wins!")
elif manik == "rock" and riyam == "scissors":
    print("Manik wins!")
elif manik == "scissors" and riyam == "paper":
    print("Manik wins!")
elif manik == "paper" and riyam == "rock":
    print("Manik wins!")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")