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
   
just_fix_windows_console()

# Clean console
os.system('cls'); os.system('title YCLVV')

# Get URL
providedLink = input(f"{color.BLUE}{color.UNDERLINE}Enter Channel URL > ")

# Functions
def scrapeVideos(url):
    ydl_opts = {
        'extract_flat': True,
        'skip_download': True,
        'quiet': True
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel_url, download=False)
    
    videos = []
    
    if 'entries' in result:
        for entry in result['entries']:
            if 'url' in entry:
                vurl = entry['url']
                vinfo = ydl.extract_info(vurl, download=False)
                vdetails = {
                    'title': vinfo.get('title'),
                    'views': vinfo.get('views'),
                    'url': vurl,
                    'upload_date': vinfo.get('upload_date')
                }
                videos.append(vdetails)
        
        return videos
    else:
        print("This channe has no videos.")

# Validate URL
regex = re.compile(r"https:\/\/www\.youtube\.com\/channel\/\S+")
valid = regex.match(providedLink)
if valid:
    print("Link valid!")
    
else:
    print("Invalid link.")

print(color.END)