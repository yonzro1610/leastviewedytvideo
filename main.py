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
        'force_generic_extractor': False
    }
    
    videos = []
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
            
        if 'entries' not in info:
            raise Exception("Failed to retrieve channel videos")
            
        video_urls = [entry.get('webpage_url') for entry in info['entries'] if entry.get('webpage_url')]
            
        all_videos_info = []
        for video_url in video_urls:
            video_info = ydl.extract_info(video_url, download=False)
            all_videos_info.append(video_info)

        # Now, all_videos_info contains information for all videos
        index = 0
        for video_info in all_videos_info:
            index = index + 1
            if video_info:
                video_data = {
                    'title': video_info['title'],
                    'url': video_info['webpage_url'],
                    'views': video_info.get('view_count', 'N/A')
                }
                print(f"Video Scraped: {video_data['title']} | Index {index}")
                videos.append(video_data)
                return videos

# Validate URL
regex = re.compile(r"https:\/\/www\.youtube\.com\/channel\/\S+")
valid = regex.match(providedLink)
if valid:
    os.system('cls')
    print("Valid link! Starting scraping process...")
    time.sleep(1)
    os.system('cls')
    print("This will take a while.")
    vids = scrapeVideos(providedLink)
    time.sleep(0.3)
    print("Scraping done! Sorting by views...")
    LOWEST = 99999999999999999999999999999999999
    for vid in vids:
        if vid['views'] <= LOWEST:
            LOWEST = vid['views']
    
    for vid in vids:
        if vid['views'] == LOWEST:
            os.system('cls')
            print(f"Least viewed video on channel found. ({vid['views']} views)")
            print(f"Title: {vid['title']}\nURL: {vid['url']}")
else:
    print("Invalid link.")
    
print(color.END)