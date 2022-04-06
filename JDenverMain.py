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
