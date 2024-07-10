import random



m1=0
m2=0



while(True):
    a = input("Enter choice :\n1.Paper \n2.Scissors \n3.Rock \n")
    list = ["rock", "paper", "scissors"]
    bot = random.choice(list)

    print("Your choice : " + a)
    print("Computer's choice : " + bot)

    if (a == bot):
        print("Same choice!!!! \n\n")
    elif (a == "rock" and bot == "scissors"):
        print("\nYou got 1 point")
        m1 = m1 + 1
    elif (a == "rock" and bot == "paper"):
        print("\nComputer got 1 point")
        m2 = m2 + 1
    elif (a == "paper" and bot == "scissors"):
        print("\nComputer got 1 point")
        m2 = m2 + 1
    elif (a == "paper" and bot == "rock"):
        print("\nYou got 1 point")
        m1 = m1 + 1
    elif (a == "scissors" and bot == "paper"):
        print("\nYou got 1 point")
        m1 = m1 + 1
    elif (a == "scissors" and bot == "rock"):
        print("\nComputer got 1 point")
    else:
        print("!!!!!!!!!!!!    wrong choice    !!!!!!!!!!!!!")
        m2 = m2 + 1
    print("      SCORE    ")
    print("You      : ",m1)
    print("Computer : ",m2)
    if(m1==5 or m2==5):
        break

if(m1==5):
    print("  *******  You win   *********")
else:
    print("  *******  Computer win   *********")




