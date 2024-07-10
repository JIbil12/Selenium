from gtts import gTTS
import io

from playsound import playsound



# open("book.txt","r")
fp = io.open("book.txt", mode="r", encoding="utf-8")
book_content = fp.read()


obj = gTTS(book_content, lang='ml')
obj.save("token.mp3")
playsound("token.mp3")
