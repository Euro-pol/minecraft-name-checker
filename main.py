import httpx
import time
from colorama import Fore

client = httpx.Client()
delay = float(input("Delay between checks (seconds): "))
choice = input("What do you want to do? (1) Check random words (2) Check from words.txt: ")

def add_name(name):
    with open("names.txt", "a") as f:
        f.write(f"{name}\n")

def check(name):
    r = client.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
    if r.status_code == 204:
        return True
    elif r.status_code == 200:
        return False    
    elif r.status_code == 429:
        print(Fore.YELLOW + "You are being ratelimited!")
        time.sleep(5)
        return False    
    else:
        return False

def checkWord():
    while True:
        word = client.get("https://random-word-api.herokuapp.com/word").json()[0]
        if(check(word)):
            print(Fore.GREEN + f"{word} is available!")
            add_name(word)
        else:
            print(Fore.RED + f"{word} is not available!")
        time.sleep(delay)    

def checkFile():
    with open("words.txt", "r") as f:
        words = f.read().splitlines()
    for word in words:
        if(check(word)):
            print(Fore.GREEN + f"{word} is available!")
            add_name(word)
        else:
            print(Fore.RED + f"{word} is not available!")
        time.sleep(delay)



if __name__ == "__main__":
    if choice == "1":
        checkWord()
    elif choice == "2":
        checkFile()
    else:
        print("Invalid choice!")
    