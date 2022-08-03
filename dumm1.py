# import requests
# from bs4 import BeautifulSoup
#
# url="https://www.google.com/search?&q= Weather+in+Rajshahi"
# r=requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")
# update = soup.find("div", class_="BNeawe").text

import datetime
import calendar

#
# list1 = [["AB", 2, 5], ["cd", 3, 6]]
# list1[0][2] = 8
# print(list1[0][2])
#
# list1.__delitem__(0)
# print(list1)

from VMServer import admin_update
from VMServer import server_fetch
from Speak import say

food = ["next", "catbery"]
quant = [ 4, 3]


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


golu = match_server(food, quant)
print("golu:\n")
print(golu)
print(golu[0])
print(golu[1])
print(golu[2])
















