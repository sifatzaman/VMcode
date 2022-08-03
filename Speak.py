from gtts import gTTS
import playsound

file = open("Conversation.txt", "w")

def say(text):
    file.write("\nVendor: " + text)
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)





### Unig OS
# def listenme():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Say something loudly and clearly: ")
#         audio = r.listen(source, 0, 2)
#
#     command = ""
#     try:
#         command = r.recognize_google(audio)
#         print("Your Command: \n" + command)
#     except sr.UnknownValueError:
#         print("I couldn't Understand your command.")
#
#     return command
#
#
# def sayme(text):
#     os.system("play " + text + " tempo 1.9")
#     print(f"Caption: {text}")
#
#
# text = "I can speak now"
# sayme(text)