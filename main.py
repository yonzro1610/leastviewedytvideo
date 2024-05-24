# Libraries
from colorama import just_fix_windows_console
import yt_dlp
import json
import time
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
   
just_fix_windows_console()

# Clean console
os.system('cls'); os.system('title YCLVV')

# Get URL
providedLink = input(f"{color.BLUE}Enter Channel URL > {color.UNDERLINE}"); print(color.END)
print(f"{color.BLUE}")

# Functions
def scrapeVideos(channel_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,  # Do not download the videos
        'force_generic_extractor': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        
        if 'entries' not in info:
            raise Exception("Failed to retrieve channel videos")
        
        videos = []
        for i, entry in enumerate(info['entries']):
            video_info = ydl.extract_info(entry['url'], download=False)
            video_data = {
                'title': video_info['title'],
                'url': video_info['webpage_url'],
                'views': video_info.get('view_count', 'N/A')
            }
            videos.append(video_data)
            print(i + 1)
        
        return videos

# Validate URL
regex = re.compile(r"https:\/\/www\.youtube\.com\/channel\/\S+")
valid = regex.match(providedLink)
if valid:
    os.system('cls')
    print("Link valid! Scraping beginning...")
    time.sleep(1)
    os.system('cls')
    vids = scrapeVideos(providedLink)
else:
    print("Invalid link.")
    
print(color.END)