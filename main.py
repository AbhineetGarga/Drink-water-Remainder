# pip install pyttsx3

import os
import time
import ctypes
#First install gtts
from gtts import gTTS
from playsound import playsound


language = "en"
REPEAT_INTERVAL = 3600 # Repeat frequency in seconds



def display_message():
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'Hey Harry, Drink water', 'Reminder', 0x40 | 0x1)

while True:
    text = f"Hey drink water"
    speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
    speech.save("textToSpeech.mp3")
    playsound("textToSpeech.mp3")
    display_message()
    time.sleep(REPEAT_INTERVAL)
