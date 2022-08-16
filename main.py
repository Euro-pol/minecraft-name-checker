import httpx
import time
from colorama import Fore

client = httpx.Client()
delay = float(input("Delay between checks (seconds): "))

def add_name(name):
    with open("names.txt", "a") as f:
        f.write(f"{name}\n")

def check(name):
    r = client.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
    if r.status_code == 204:
        return True
    elif r.status_code == 200:
        return False    
    else:
        return False

def checkWord():
    word = client.get("https://random-word-api.herokuapp.com/word").json()[0]
    if(check(word)):
        print(Fore.GREEN + f"{word} is available!")
        add_name(word)
    else:
        print(Fore.RED + f"{word} is not available!")


while True:
    checkWord()
    time.sleep(delay)