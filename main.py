#Main Branch
from fnmatch import translate
import os
import sys
import time
from playsound import playsound
from pathlib import Path
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator


def speak(text, language):
    tts = gTTS(text=text, lang=language)
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def get_audio(sent):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak(sent, "en")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

def translation(text, newLang):
    translator = Translator()
    return translator.translate(text, dest = newLang, src = 'en').text

def didNotGetLanguage():
    speak("I am sorry, I did not get that, let's try all of this again","en")
    os.execl(sys.executable, sys.executable, *sys.argv)

def getLanguage(fullname):
    match fullname:
        case "Spanish":
            return 'es'
        case _:
            return didNotGetLanguage()

def introduction():
    speak("Hello! Welcome to Team 12's final project: an English to world-wide language translator!", "en")
    newLang = get_audio("What language would you like to translate into?")
    longLang = newLang
    newLang = getLanguage(newLang)
    text = get_audio("What would you like to translate?")
    translatedSentence = translation(text, newLang)
    speak(text + " in " + longLang + " is " + translatedSentence, newLang)

introduction()
