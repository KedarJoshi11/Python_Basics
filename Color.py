from termcolor import colored
from pyfiglet import figlet_format
import colorama
colorama.init()
msg = input("What would you like to print? ")

while True:
    paint = input("What color? ")
    colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    if paint in colors:
        art = figlet_format(msg)
        final_art = colored(art, color=paint)
        print(final_art)
        break
    else:
        print("Please choose another color, this isn't available. Options are: red, green, yellow, blue, magenta, cyan, white")


# text = colored("What the hell is up, man!", color = "cyan", on_color = "on_yellow", attrs=["bold"])
