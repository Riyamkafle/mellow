import random

# Dice art representation
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●      ●│",
        "│         │",
        "│ ●      ●│",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│●       ●│",
        "│    ●    │",
        "│●       ●│",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│●       ●│",
        "│●       ●│",
        "│●       ●│",
        "└─────────┘"),
}

dice = []
total = 0
number_of_dice = int(input("How many dice? "))

# Rolling the dice
for _ in range(number_of_dice):
    dice.append(random.randint(1, 6))

# Printing the dice art
for i in range(5):  # There are 5 lines in each dice art
    for die in dice:
        print(dice_art[die][i], end=" ")
    print()  # Move to the next line after printing one row of dice

# Calculating the total
for die in dice:
    total += die

print(f"Total: {total}")
