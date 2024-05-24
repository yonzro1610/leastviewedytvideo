from colorama import Fore, Back, init
import os

init()

os.system('cls')

print(f"{Fore.WHITE}{Back.RED}Youtube Channel Least Viewed Video Getter{Fore.RESET}{Back.RESET}")

channelLink = input(f"\n{Fore.WHITE}{Back.RED}Enter Channel Link > ")
print(f"{Fore.RESET}{Back.RESET}")

os.system('cls')

print(f"{Fore.WHITE}{Back.RED}Checking for valid URL...{Fore.RESET}{Back.RESET}")