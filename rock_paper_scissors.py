import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie! 🤝")

    elif player == "rock" and computer == "scissors":
        print("Rock smashes scissors! Player wins! ✅")

    elif player == "paper" and computer == "rock":
        print("Paper covers rock! Player wins! ✅")

    elif player == "scissors" and computer == "paper":
        print("Scissors cuts paper! Player wins! ✅")

    else:
        print("Computer wins! ❌")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
