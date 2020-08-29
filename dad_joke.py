import requests
from random import choice
from termcolor import colored
from pyfiglet import figlet_format
import colorama
colorama.init()
msg = figlet_format("Dad Joke 3000")
msg = colored(msg, color="green")
print(msg)

url = "https://icanhazdadjoke.com/search"
user_input = input("What would you like to search for? ")
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()
result = res["results"]
num_jokes = res["total_jokes"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes for the word {user_input}. Here's one:")
    print(choice(result)["joke"])
elif num_jokes == 1:
    print("There is one joke.")
    print(result[0]["joke"])
else:
    print(f"Sorry, couldn't find a joke for the word {user_input}")
