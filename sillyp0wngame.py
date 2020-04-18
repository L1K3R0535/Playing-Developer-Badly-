#!/usr/bin/python3
import random, sys
cia_network = {
    "website": "www.cia.gov",
    "router_pwd": 1000,
}
def y_n():
    i=input("y | n"); return i
def cracker():
    guess=1
    for x in range(int(cia_network["router_pwd"])):
        guess += 1
        print("Bruteforcing...")
        if guess == cia_network["router_pwd"]:
            print("Access granted")
            print("root@cia_router2$ start sox-5 proxy -p 9050 && sox-proxy-to-dns -p 9050")
            print("""Ok so read closely, we needed to use nother computer to hack into the cia, we used yours, we have uploaded a program to your computer to secretly change things.
Such as your mac address, and also put your network through a network of special routers that anonymize traffic through encryption, (yes tor!) you know this?
we need you to do something for us like getting to their secret network... granted you just popped your first shell(a little assisted, but that's not too important).
Anyhow, the CIA, secret network! There are a few steps you will have to take, the first step(s) are; locating the domain admin and placing a rootkit on his CPU,(that special program).
luckily we have (if you have not notest by now), uploaded all the programs you will need to your computer! (via that special program, the rootkit)
So just press enter commands we say,  first one ./admin_hunter.cpp -T -p 9050 -A.
""")
    i=input("root@cia_router2$ ")
    def find_admin():
        for x in range(512):
            print("Transfering file from 88.282.821.34 to 22.11.23.45 over port 9050(sox-proxy-tor)")
        for x in range(2048):
            if x > 0:
                print("Searching for admin...")
            if x > 512:
                print("Admin found!\nExploiting box...")
            if x > 1024:
                print("Setting up rootkit...")
            return 1
    def exit_plan():
        for x in range(9001):
            print("<<<<<<<<ENCRYPTING>>>>>>>>\nYour Data Is being collected and backed-up on one of our servers!\nLast chance!")
        lc=input("root@cia_router2$ ")
        holder.push(lc)
    lc_holder=[]
    if i == "./admin_hunter.cpp -T -p 9050 -A":
        if find_admin() == True:
            cmdshell=input("C://Windows7x64/admin>")
def encrypt():
    for x in range(len(str(sys.platform)) * 10):
            print("******OH DEAR ENCRYPTING!*****",x)
    print("VERY IMPORTANT: DO NOT SWITCH OFF YOUR DEVICE, ALL YOUR DATA WILL BE LOST\n")
    print("Your hardrive has been encrypted with a strong aes 128 bit encryption.\nFollow the instructions for a chance to win your presious data back!")
    try:
        print("Press ANY Key to continue")
    except KeyPress:
            exit()
def cryptogames():
    cpu_=[]
    victim_=[]
    try:
        print("Welcome to the crypto games, you have a chance to win your data back.... ")
        def cpu_num():
            num=random.randint(1,100)
            print("Cpus number is %s"%(num))
            return num
        def victim_num():
            num=random.randint(1,100)
            print("Your number is %s"%(num))
            return num
    except KeyPress:
        for x in range(100):
            cpu=cpu_num(); victim=victim_num()
            if cpu > victim:
                cpu_.append(cpu)
            elif cpu == victim:
                print("Draw!");
                cpu_.append(cpu / 2); victim_.append(victim / 2)
            elif victim > cpu:
                victim_.append(victim)
def main():
    encrypt()
    print("Are you ready for the greatest adventure ever?... It begins!")
    print("run spoitpig -b 8 -r y -ctmrk /home/sh04an5/Documents/custom_scripts/rootkits/fedkit www.cia.com")
    if y_n() == "y":
        cracker()
    else:
        cryptogames()
if __name__ == "__main__":
        main()
