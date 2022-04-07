#Main Branch
from fnmatch import translate
import os
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

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("You may now give an input", "en")
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

def getLanguage(fullname):
    match fullname:
        case "Spanish":
            return 'es'
        case _:
            return 'es'

def introduction():
    speak("Hello! Welcome to Team 12's final project: an English to world-wide language translator!", "en")
    speak("What language would you like to translate into?", "en")
    newLang = get_audio()
    newLang = getLanguage(newLang)
    speak("What would you like to translate?", "en")
    text = get_audio()
    translatedSentence = translation(text, newLang)
    speak(translatedSentence, newLang)

introduction()
