#!/usr/bin/python3
"""!/Program notes:
This is a simple game that is made to simulate a life of crime much as gta does
but is massively simpler. I do hope it is enjoyed. Sorry online compilers smoke crack and hate this, but Having tested it on Ubuntu, I am confident in saying it will <u>Likely</u> work on anything that is at least Debian based and has the latest python3 Interpreter installed. (perhaps some older ones)
It is not really anything fancy and does not warrant my time as far as update, I was just bored and wanted a game like this to play and that is why I made it. I do have other games I am working on that I am more hopeful of their longevity / multi-platform use.
 
(29/06/2018) Note:
 
I may end up adding to this after all as I did get a little bit further with making this a bit more oop and thus making it a have a bit more depth to it. But at the moment, most of my time at a terminal is being spent learning Java and doing some dabbling with wireless router security.
 
(I would not expect much even if it is done, but feel free to do whatever yourself)
 
"""
import random
#--comment-space---
def name():
    print("Hello welcome to the crime game, a text game where the goal is to become the most prolific: \n'crime lord'\n'gangster'\n'drug dealer'\netc\nThere are a few ways to do this; you can type 'help' in the command issuer.")
    print("Please make a username first.\n")
    i=input("Username: "); return i
def listnpc():
    for each in npclist:
        print("List-ID: %i; Name: %s; Job-Title: %s; weed: %i; coke: %i; mdma: %i; cash: %s"%(each["ID"],each["name"],each["job"],each["weed"],each["coke"],each["mdma"],each["cash"]))
class market:
    def selectnpc():
        listnpc()
        print("from the information at hand please pick the list ID of the npc you would like to trade with.\n")
        i=(int(input("SELECT ID: "))); return i
    def ddeal(user,npc):
        print("Hello "+user["name"]+", my name is "+npc["name"]+". What would you like to buy or sell?")
        bos=input("%s@%s$ "%(user["name"],npc["name"]))
    def buy(obj,sel,am):
        if sel == "weed":
            for x in range(int(am)):
                obj["cash"] -= 5
                obj["weed"] += 1
            print("You buy %i gram(s) of weed,\nYou now have %s grams of weed"%(am,obj["weed"]))
        elif sel =="coke":
            for x in range(int(am)):
                obj["cash"] -= 40
                obj["coke"] += 1
            print("You buy %i gram(s) of coke.\nYou now have %s grams of coke"%(am,obj["coke"]))
        elif sel == "mdma":
            for x in range(int(am)):
                obj["cash"] -= 40
                obj["mdma"] += 1
            print("You buy %i gram(s) of mdma.\nYou now have %s grams of mdma."%(am,obj["mdma"]))
        else:
            print("Sorry an error has taken place and the program has now closed.")
    def sell(obj,sel,am):
        if sel == "weed":
            if obj["weed"] == 0:
                print("You have no weed to sell!")
            for x in range(int(am)):
                obj["cash"] += 10
                obj["weed"] -= 1
            print("You sell %i gram(s) of weed.\nYou now have %i grams of weed."%(am,obj["weed"]))
        elif sel =="coke":
            if obj["coke"] == 0:
                print("You have no coke to sell!")
            for x in range(int(am)):
                obj["cash"] += 50
                obj["coke"] -= 1
            print("You sell %i gram(s) of coke.\nYou now have %s grams of coke."%(am,obj["coke"]))
        elif sel == "mdma":
            if obj["mdma"] == 0:
                print("you have no mdma to sell. :(")
            for x in range(int(am)):
                obj["cash"] -= 50
                obj["mdma"] += 1
            print("You sell %i gram of mdma.\nYou now have %s grams of mdma."%(am,obj["mdma"]))
def _play_():
    def pstats():
        print("Hello %s.\nYou have $%i\n%i g(s) weed\n%i g(s) coke \n%i g(s) mdma"%(player["name"],player["cash"],player["weed"],player["coke"],player["mdma"]))
    pstats()
    cmd=input("Command: ")
    commands = [
        "'buy':used to buy a product or service.\n",
        "'sell':used to sell a product or service.\n",
        "'help':used to bring up this help menu.\n",
        "'lnpc': used to list all the npc's, so you may pick one\n",
    ]
    if cmd == "sell":
        sw=input("Sell what? :")
        if sw == "weed":
            market.sell(player,"weed",int(input("amount in grams: ")))
        elif sw == "coke":
            market.sell(player,"coke",int(input("amount in grams: ")))
        elif sw == "mdma":
            market.sell(player,"mdma",int(input("amount in grams:" )))
        elif sw != "weed" or "coke" or "mdma":
            print("Try again!")
    elif cmd == "buy":
        bw=input("buy what? :")
        if bw == "weed":
            market.buy(player,"weed",int(input("amount in grams: ")))
        elif bw == "coke":
            market.buy(player,"coke",int(input("amount in grams: ")))
        elif bw == "mdma":
            market.buy(player,"mdma",int(input("amount in grams: ")))
        elif bw != "weed" or "coke" or "mdma":
            print("try again!")
    elif cmd == "help":
        for each in commands:
            print("%s"%(each))
    elif cmd == "lnpc":
        listnpc()
    elif cmd == "ddeal":
        market.ddeal(player,npclist[market.selectnpc()])
def main():
    while player["cash"] > 0:
        _play_()
    if player["cash"] < 0:
        print("You are out of money!\nGame Over!\n")
if __name__ == "__main__":
    main()
