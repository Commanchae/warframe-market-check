from bs4 import BeautifulSoup
import requests
from os import system
import json

# Inventory
inventory = []

def getOrderPrice(order):
    return order["platinum"]


URL = '''https://warframe.market/items/'''
def checkWarframeMarket(itemName):
    itemNameSplit = itemName.split()
    jSON = {}
    onlineBuyers = []
    onlineSellers = []
    URL_CHECK = URL
    for index, item in enumerate(itemNameSplit):
        if (index != len(itemNameSplit)-1):
            URL_CHECK += item.lower() + "_"
        else:
            URL_CHECK += item.lower()
    page = requests.get(URL_CHECK)
    soup = BeautifulSoup(page.text, 'html.parser')
    jSON = json.loads(soup.find('script', id = "application-state").text)
    for order in jSON["payload"]["orders"]:
        if (order["user"]["status"] == "ingame"):
            if (order["order_type"] == "buy"):
                onlineBuyers.append(order)
            elif (order["order_type"] == "sell"):
                onlineSellers.append(order)   
    onlineBuyers.sort(key = getOrderPrice, reverse = True)
    onlineSellers.sort(key = getOrderPrice)

    print("BUYERS:")
    for order in onlineBuyers:
        if order["order_type"] == "buy":
            print(order['user']['ingame_name'] + ": " + str(order['platinum']) + " PLAT x " + str(order['quantity']) + " AMT(s)")

system("cls")
checkWarframeMarket("Ankyros Prime Blade")
exit()
         






system("cls")
while True: 
    playerInput = input("What would you like to do? \n\t [1] Enter item \n\t [2] Remove Item \n\t [3] Check Market\n\n")
    if (playerInput == "1"):
        system("cls")
        done = False
        while (not done):
            itemToAdd = input("Add item or DONE for done.: ")
            if itemToAdd != "DONE":
                inventory.append(itemToAdd)
            else:
                done = True
    elif (playerInput == "2"):
        system("cls")
        done = False
        while (not done):
            for index, item in enumerate(inventory):
                print(f"[{index+1}] {item}")
            inputIndex = int(input("Input index (input 99 to finish)): "))
            try:
                inventory.pop(inputIndex-1)
            except:
                print("Index error.")
                done = True
            if (inputIndex == 99):
                done = True
            system("cls")
    elif (playerInput == "DONE"):
        exit()
    elif playerInput== "3":
        pass
