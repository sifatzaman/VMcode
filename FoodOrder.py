from word2number import w2n
from Speak import say
from Listen import listen, listen_s

def makeint(num):
    if num == "a":
        return 1

    if num == "tu" or num == "to" or num == "too":
        return 2

    else:
        res = w2n.word_to_num(num)
        # print("The string after performing replace : " + str(res))
        return res

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

    if confirmation == "ok" or confirmation == "okay":
        say("Thanks Sir. Here is the Qr code: ")

        say("Here is your food")

        x = 0
        for item in food:
            i = 1

            while i <= quantity[x]:
                print(item)
                i = i+1
            x = x+1

    elif confirmation == "no":
        say("The Order Process is Collapsed. I am cancelling your order. Please re-order.")
        say("What should I serve you?")



def TakeOrder(sentence):

    food = []
    quantity = []
    for items in sentence:

        if items == "pepsi":
            food.append("pepsi")

        if items == "coca":
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




