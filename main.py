from gtts import gTTS
import os

myText = """
Yeah-yeah
Baby, baby, you're my sun and moon
Girl, you're everything between
A lot of pretty faces could waste my time
But you're my dream girl
"""

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")