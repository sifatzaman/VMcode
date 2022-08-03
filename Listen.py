import speech_recognition as sr
from Speak import say

file = open("Conversation.txt", "w")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\tListening... ")
        r.energy_threshold = 400
        r.pause_threshold = 1
        audio = r.listen(source, 0, 5)

    command = ""
    try:
        command = r.recognize_google(audio, language="en-in")
        print("Your Command: \n" + command)
        file.write("\nCustomer: " + command)
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
        file.write("Customer: " + command)
    except sr.UnknownValueError:
        say("I couldn't Understand your command")

    return command