import random

goat = random.randint(1, 3)
poop = 0

choice = int(input("Choose a door (1-3): ").strip())

while choice < 1 or choice > 3:
    choice = int(input("Choose a door (1-3): ").strip())

if choice == goat:
    if goat == 1:
        poop = random.choice([2, 3])
    elif goat == 2:
        poop = random.choice([1, 3])
    else:
        poop = random.choice([1, 2])
else:
    if goat == 1 and choice == 2 or goat == 2 and choice == 1:
        poop = 3
    elif goat == 2 and choice == 3 or goat == 3 and choice == 2:
        poop = 1
    else:
        poop = 2

print(f"Poop is at {poop}")

switch = input("Do you want to switch? (y/n): ").strip().lower()

while switch != "y" and switch != "n":
    switch = input("Do you want to switch? (y/n): ").strip().lower()

if switch == "y":
    if goat == 1 and choice == 2 or goat == 2 and choice == 1:
        choice = 3
    elif goat == 2 and choice == 3 or goat == 3 and choice == 2:
        choice = 1
    else:
        choice = 2

if choice == goat:
    print("You won")
else:
    print("You got poop")