from gtts import gTTS

from playsound import playsound

n=int(input("Enter number"))
txt = "ടോക്കൺ നമ്പർ "+str(n)

obj = gTTS(txt,lang='ml')
obj.save("token.mp3")
playsound("token.mp3")



