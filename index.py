import pyttsx3

engine = pyttsx3.init()

# Voice rate
engine.setProperty('rate', 180)

# Volumn 0 to mute, 1 to unmute
engine.getProperty('volume')
engine.setProperty('volume', 1)

# Voice 0 for Male, 1 for Female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Pitch (default 50) to 75 out of 100
engine.setProperty('pitch', 75)

text = """
Yeah-yeah
Baby, baby, you're my sun and moon
Girl, you're everything between
A lot of pretty faces could waste my time
But you're my dream girl
"""

# Save as a file
# engine.save_to_file(text, 'test.mp3')

engine.say(text)
engine.runAndWait()
engine.stop()


# while True:
#     textto = input("Type something to say: ")
#     engine.say(textto)
#     engine.runAndWait()
#     engine.stop()