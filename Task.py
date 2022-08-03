# Function
import datetime
from Speak import say
from Listen import listen

# 2 Types

# 1 - Non Input
# eg: Time , Date , Speedtest

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    say(time)


def Date():
    date = datetime.date.today()
    date = str(date)
    say(date)


def Day():
    day = datetime.datetime.now().strftime("%A")
    say(day)


def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()


# 2 - Input
# eg - google search , wikipedia

def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("who is", "").replace("about", "").replace("what is", "").replace("wikipedia", "")
        import wikipedia
        result = "According to wikipedia" + wikipedia.summary(name, sentences=2)
        result = result
        say(result)
        say("That's all for Now. Thank you.")

    elif "google" in tag:
        query = str(query).replace("google", "")
        query = query.replace("search", "")
        import pywhatkit
        pywhatkit.search(query)

def take_objection():
    say("Please tell me any objection about the food or about me sir.")
    any_obj = listen()

    say("Okay sir. Thanks for your feedback")

    return any_obj
