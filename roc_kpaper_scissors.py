import random 




riyam = input("Riyam, please choose rock, paper, or scissors: ").lower()
manik = input("Manik, please choose rock, paper, or scissors: ").lower()

# Icons for winning and losing
win_icon = "🏆"
lose_icon = "💔"     

# Determine the winner using if-else conditions
if riyam == manik:
    print("It's a tie!")
elif riyam == "rock" and manik == "scissors":
    print(f"{win_icon} Bingo! Riyam wins {lose_icon}")
elif riyam == "scissors" and manik == "paper":
    print(f"{win_icon} Riyam wins! {lose_icon}")
elif riyam == "paper" and manik == "rock":
    print(f"{win_icon} Riyam wins! {lose_icon}")
elif manik == "rock" and riyam == "scissors":
    print(f"{win_icon} Manik wins! {lose_icon}")
elif manik == "scissors" and riyam == "paper":
    print(f"{win_icon} Manik wins! {lose_icon}")
elif manik == "paper" and riyam == "rock":
    print(f"{win_icon} Manik wins! {lose_icon}")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")
