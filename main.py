#Main Branch
import os
import time
from playsound import playsound
from pathlib import Path
import speech_recognition as sr
from gtts import gTTS

def speak(text, language):
    tts = gTTS(text=text, lang=language)
    SCRIPT_DIR = Path(__file__).parent
    filename = SCRIPT_DIR / "voice.mp3"
    tts.save(filename)
    playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What would you like to translate?", "en")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

text = get_audio() 
speak(text, "en")
