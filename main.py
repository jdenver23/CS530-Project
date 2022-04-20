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

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese simplified',
    'zh-tw': 'chinese traditional',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish kurmanji',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar burmese',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'}

def speak(text, language):
    tts = gTTS(text=text, lang=language)
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def get_audio(sent):
    speak(sent, "en")
    said = input()
#    r = sr.Recognizer()
#    with sr.Microphone() as source:
#        speak(sent, "en")
#        audio = r.listen(source)
#        said = ""
#
#       try:
#            said = r.recognize_google(audio)
#            print(said)
#        except Exception as e:
#            print("Exception: " + str(e))
    return said

def translation(text, newLang, source):
    translator = Translator()
    return translator.translate(text, dest = newLang, src = source).text

def didNotGetLanguage():
    speak("I am sorry, I did not get that, let's try all of this again","en")
    os.execl(sys.executable, sys.executable, *sys.argv)

def getLanguage(fullname):
    try:
        new_dict = dict([(value, key) for key, value in LANGUAGES.items()])
        return new_dict[fullname.lower()]
    except:
        didNotGetLanguage()

def introduction():
    speak("Hello! Welcome to Team 12's final project: a world-wide language translator!", "en")
    oldLang = get_audio("What language would you like to translate from?")
    oldLang = getLanguage(oldLang)
    newLang = get_audio("What language would you like to translate into?")
    longLang = newLang
    newLang = getLanguage(newLang)
    text = get_audio("What would you like to translate?")
    translatedSentence = translation(text, newLang, oldLang)
    try:
        speak(translatedSentence, newLang)
        speak(" is " + text + " in " + longLang, 'en')
    except:
        speak("Some languages, such as the chosen language, do not support text to speech, although I can print the translation", "en")
    print(translatedSentence + " is " + text + " in " + longLang)

def startAgain():
    answerToStartingAgain = get_audio("Would you like to start again?")
    if(answerToStartingAgain.__contains__("yes") or answerToStartingAgain.__contains__("Yes")): os.execl(sys.executable, sys.executable, *sys.argv)
    else: speak("Thank you, take care!", "en")

introduction()
startAgain()