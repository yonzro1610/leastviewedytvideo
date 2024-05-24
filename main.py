from colorama import Fore, Back, init
import os

init()

os.system('cls')

print(f"{Fore.WHITE}{Back.RED}Youtube Channel Least Viewed Video Getter{Fore.RESET}{Back.RESET}")

channelLink = input(f"{Fore.RED}{Back.WHITE}Enter Channel Link > ")

print("Checking for valid URL...")