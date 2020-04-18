"""
So I put this together to help people with game development, I don't write games (clearly)
but I find them interesting, so this OOP example should help anyone have a base for a really basic text game.

If you open a terminal window in the same directory as the one both files are save in, then just pop python shell you have a 'framework' for basic text game development, well to practice concepts anyhow.

This is just one way to do it but there are a lot...  I think looking at the variables from MAIN  and then coding your own game in the SOURCE file... I may do the same thing myself but that sounds like a lot of development work and I just have so many other things that require my time.
 """
#__________________SOURCE________________
#!/usr/bin/python3
import os,
from dragonslayercopy import *
def main():

if __name__ == "__main__":
    main()
#_______________MAIN_______________
#!/usr/bin/python3
import os, optparse, random
def hitchance():
    return random.random()
def sh(arg):
    i=input(arg); return i
class human:
    name="slayer"
    health=100
    attack=10
    def hitchance():
        return hitchance()
class dragon:
    name="dragon"
    health=100
    attack=10
    def hitchance():
        return hitchance()
class elf:
    name="elf"
    health=100
    attack=10
    def hitchance():
            return hitchance()
class ork:
    name="ork"
    health=100
    attack=10
    def hitchance():
            return hitchance()
def healthchange(a,b):
    if a.hitchance() > b.hitchance():
        b.health -= a.attack
        print("%s "%(b.health))
    else:
        a.health -= b.attack
        print("%s "%(a.health))
def combat(a,b):
    while a.health > 0 and b.health > 0:
        healthchange(a,b)
        if a.health == 0:
            print("You lose!")
        elif b.health == 0:
            print("You win!")
def main():
    combat(human,dragon)
    rematch=input("Rematch? ('y' or 'no')")
    if rematch == "y":
        human.health = 100; dragon.health = 100
        combat(human,dragon)
    elif rematch  == "n":
        print("Bye then!")
        exit()
if __name__ == "__main__":
    main()
#___________________________________________________ 
