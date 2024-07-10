# Multiplication Table
import pyttsx3

engine=pyttsx3.init()


n = input("Enter a number")

dict = {
    "1": "Ones",
    "2": "twos",
    "3": "threes",
    "4": "fours",
    "5": "fives",
    "6": "sixs",
    "7": "sevens",
    "8": "eights",
    "9": "nines",
    "10": "tens"
}

txt = ""

for i in range(1, 11):
    mul = i * int(n)
    txt += str(i) + " " + dict[n] + " are " + str(mul) + "\n"
print(txt)

engine.say(txt)
engine.runAndWait()
