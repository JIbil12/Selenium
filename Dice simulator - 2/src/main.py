import random


dice_art = {
    1: ("┌─────────┐\n"
        "│         │\n"
        "│    ●    │\n"
        "│         │\n"
        "└─────────┘\n"),
    2: ("┌─────────┐\n"
        "│  ●      │\n"
        "│         │\n"
        "│      ●  │\n"
        "└─────────┘\n"),
    3: ("┌─────────┐\n"
        "│  ●      │\n"
        "│    ●    │\n"
        "│      ●  │\n"
        "└─────────┘\n"),
    4: ("┌─────────┐\n"
        "│  ●   ●  │\n"
        "│         │\n"
        "│  ●   ●  │\n"
        "└─────────┘\n"),
    5: ("┌─────────┐\n"
        "│  ●   ●  │\n"
        "│    ●    │\n"
        "│  ●   ●  │\n"
        "└─────────┘\n"),
    6: ("┌─────────┐\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "└─────────┘\n")
}

while True:
    a=random.randint(1,6)
    match a:
        case 1 : print(dice_art[1])
        case 2 : print(dice_art[2])
        case 3 : print(dice_art[3])
        case 4 : print(dice_art[4])
        case 5 : print(dice_art[5])
        case 6 : print(dice_art[6])
        case _:print("Wrong choice")
    a=input("Do you want to roll again !")
    if(a.lower()=="no"):
        break