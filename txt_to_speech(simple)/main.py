import pyttsx3

engine = pyttsx3.init()
engine.say("Hello how are you")
engine.runAndWait()

# Advanced-------------->

# Changing the audio to female


#
# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here
# engine.say('Hello World')
# engine.runAndWait()
