import random

again=True
while again:
    print(random.randint(1,6))
    a = input("Do you want to roll again !")
    if (a.lower() == "no"):
        break
    else:
        again = "True"



