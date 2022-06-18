import speech_recognition as sr
from Speak import say


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\tListening... ")
        r.pause_threshold = 2
        audio = r.listen(source, 0, 10)

    command = ""
    try:
        command = r.recognize_google(audio, language="en-in")
        print("Your Command: \n" + command)
    except sr.UnknownValueError:
        say("I couldn't Understand your command")

    return command

def listen_s():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\tListening... ")
        r.pause_threshold = 2
        audio = r.listen(source, 0, 5)

    command = ""
    try:
        command = r.recognize_google(audio, language="en-in")
        print("Your Command: \n" + command)
    except sr.UnknownValueError:
        say("I couldn't Understand your command")

    return command