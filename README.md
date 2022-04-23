# CS530-Project
This will be used to create/manage our CS530 project

Our goal is to create a language translator to convert English to any given language

Although we are focusing on converting from English, we are able to make it universal, we just only know English so for the sake of the project, we will keep it to English input

Requirements and how to use:
Our project is based in Python 3.X and uses the libraries googletrans 3.1.0a0,
gTTS 2.2.4, playsound 1.2.2, PyAudio 0.2.11, and SpeechRecognition 3.8.1

Our source code is structured so that it has the dictionary of languages, followed by a way to speak and get audio from an input. This can be changed to typing with a device that does not take audio input. We then have a translation and a way to search the dictionary for a language input and returns a sorry message if not found. Finally, a bulk of the code is in the introduction which guides the user how to use.

To use, simply clone the repository from github and run the script. After that, the user is walked through on how to use the translator.

EDIT: Can now take any input language
