# Function
import datetime
from Speak import say


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
        result = wikipedia.summary(name, sentences=2)
        say("According to Wikipedia")
        say(result)
        say("That's all for Now. Thank you.")

    elif "google" in tag:
        query = str(query).replace("google", "")
        query = query.replace("search", "")
        import pywhatkit
        pywhatkit.search(query)
