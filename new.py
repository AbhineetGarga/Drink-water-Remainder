# pip install pyttsx3

import os
import time
import ctypes
import speech_recognition as sr
import pyttsx3


# language = "en"
REPEAT_INTERVAL = 3 # Repeat frequency in seconds


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def display_message():
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'Hey Harry, Drink water', 'Reminder', 0x40 | 0x1)


while True:
    display_message()
    if __name__ == '__main__':
        tosay = say(f"Hey Harry, Drink water")
        say(tosay)
    time.sleep(REPEAT_INTERVAL)
