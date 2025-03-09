import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice=[]
total=0

def rollDice(times):
    for i in range(times):
      dice.append(random.randint(1,6))
    return dice

def showDice():
    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end=" ")
        print()
        
def showTotalPoints(dice):
    return sum(dice)

    
while True:
    try:
        num_dice = int(input("How many dice do you wanna roll? (1-5): "))
        if 1 <= num_dice <= 5:
            break
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

dice = rollDice(num_dice)
showDice()
total = showTotalPoints(dice)

print(f"Total: {total}")