import speech_recognition as sr
from Speak import say


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\tListening... ")
        audio = r.listen(source, 0, 3)

    command = ""
    try:
        command = r.recognize_google(audio, language="en-in")
        print("Your Command: \n" + command)
    except sr.UnknownValueError:
        say("I couldn't Understand your command")

    return command
