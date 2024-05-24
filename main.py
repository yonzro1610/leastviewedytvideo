# Libraries
from colorama import just_fix_windows_console
import yt_dlp
import json
import re
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Clean console
os.system('cls'); os.system('title YCLVV')

# Get URL
providedLink = input(f"{color.BLUE}{color.UNDERLINE}Enter Channel URL > "); print(color.END)