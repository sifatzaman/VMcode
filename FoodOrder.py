from word2number import w2n
from Speak import say
from Listen import listen, listen_s
from Task import take_objection
from VMServer import server_update
from VMServer import server_fetch
from VMServer import admin_update
import time
file = open("Conversation.txt", "w")

def match_server(food, Quantity):
    items = server_fetch()
    sum = 0
    j = 0
    for item in food:
        for pieces in items:
            if item == pieces[1]:
                if int(Quantity[j]) <= int(pieces[2]):
                    sum = sum + int(Quantity[j])* int(pieces[3])
                    pieces[2] = int(pieces[2]) - int(Quantity[j])
                else:
                    say(f"Sorry Sir, I don't have {Quantity[j]} {item}. I am serving the rest of the foods.")
                    food = food.__delitem__(j)
                    Quantity = Quantity.__delitem__(j)
                    match_server(food, Quantity)
        j = j + 1
    admin_update(items)
    return sum, food, Quantity

def makeint(num):
    try:
        if num == "a":
            return 1

        if num == "tu" or num == "to" or num == "too":
            return 2

        else:
            res = w2n.word_to_num(num)
            # print("The string after performing replace : " + str(res))
            return res
    except:
        say("Sorry Sir, again not clear, Quantity is  ")
        s1 = listen_s()
        s1 = s1.lower()
        makeint(s1)

def Retake(foods):

    quantity = []

    say("Sorry Sir, Quantity is not clear. Please tell me again.")

    for items in foods:
        say(f"What is the Quantity of {items}")
        q1 = listen_s()
        q1 = q1.lower()
        q2 = makeint(q1)
        quantity.append(q2)
    return quantity

def OrderProcess(food, quantity):

    say("Thanks for your order. Your Order is: ")
    x = 0
    for item in food:
        say(f"{quantity[x]} pieces of {item}")
        x = x+1

    say("Is that okay?")
    confirmation = listen_s()
    confirmation = confirmation.lower()

    if confirmation == "ok" or confirmation == "okay" or confirmation == "yes":
        final_output = match_server(food,quantity)
        food = final_output[1]
        quantity = final_output[2]
        Total_price = final_output[0]

        say(f"Total Price is: {Total_price} Taka ")

        say("Here is your food")

        x = 0
        for item in food:
            i = 1

            while i <= quantity[x]:
                print(item)
                i = i+1
            x = x+1

    else:

        say("The Order Process is Collapsed. I am cancelling your order. Please re-order.")
        say("What should I serve you?")

    objection = take_objection()
    q = 0
    for item in food:
        server_update(item, quantity[q], "Male", "Nagad", objection)
        time.sleep(1.5)
        q = q+1

    file.write("\n -------------------------------------------------------------------------- ")

def TakeOrder(sentence):

    food = []
    quantity = []
    for items in sentence:

        if items == "cake":
            food.append("cake")

        if items == "coca" or items == "coca-cola":
            food.append("coca-cola")

        if items == "due":
            food.append("mountain-due")

        if items == "chocolate":
            food.append("chocolate")

        if items == "a":
            quantity.append(1)

        if items == "tu" or items == "to" or items == "too":
            quantity.append(2)

        try:
            res = w2n.word_to_num(items)
            # print("The string after performing replace : " + str(res))
            quantity.append(res)
        except:
            continue

    print(food)
    print(quantity)

    if len(food) != len(quantity):
        quantity = Retake(food)
        OrderProcess(food, quantity)

    else:
        OrderProcess(food,quantity)




