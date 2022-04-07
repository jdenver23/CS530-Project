#Jacob Denver Main Branch
import os
import time
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text, lang):
    tts = gTTS(text=text, lang=lang)
    filename = "voice.mp3"
    tts.save(filename)
    playsound('./' + filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said
    
speak("test", "en")
