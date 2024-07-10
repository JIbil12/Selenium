import pyttsx3

engine = pyttsx3.init()

token_number = 0
txt = "token number "

while True:
    print("\nOptions \n1.Generate \n2.Exit \n3.Reset")
    try:
        a = int(input("Enter your choice: "))
        if a == 1:
            token_number += 1
            engine.say(txt + str(token_number))
            engine.runAndWait()
        elif a == 2:
            break
        elif a == 3:
            token_number=0
            engine.say("Reset successful")
            engine.runAndWait()
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
