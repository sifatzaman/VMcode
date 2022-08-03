import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import requests
from bs4 import BeautifulSoup

Scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("/home/sifat/Documents/Trainning/VMcode/secret_key.json")
file = gspread.authorize(creds)
workbook = file.open("Vend_server")
inventory = workbook.sheet1

url="https://www.google.com/search?&q= Weather+in+Rajshahi"
r=requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
Temperature = soup.find("div", class_="BNeawe").text


def server_fetch():
    items = []
    p = 2
    while (p < 6):
        items.append(inventory.row_values(p))
        p = p + 1
    return items
item = server_fetch()
print(item)

def server_update(food, Qty, gender, paymethod, obj):
    mytime = datetime.datetime.now().strftime("%H:%M")
    mydate = str(datetime.date.today())
    myday = datetime.datetime.now().strftime("%A")
    temp = Temperature

    inventory.update("H2:P2", [[mytime, mydate, myday, temp, food, Qty, gender, paymethod, obj]])



def admin_update(num):
    inventory.update("C2", num[0][2])
    inventory.update("C3", num[1][2])
    inventory.update("C4", num[2][2])
    inventory.update("C5", num[3][2])



