#!/usr/bin/python

import sys
from pathlib import Path
import youtube_dl

with open('checker.txt') as f:
    check_lines = f.readlines()
    
ydl_opts = {'quiet': True}

for line in check_lines:
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(line.strip(),download=False)
                video_title = info_dict.get('title', None)
                video_title = video_title.replace(":"," -").replace("\"","\'").replace("\\","_").replace("/","_")
        mp3_file = Path(f"Downloads/{video_title}.mp3")
        if mp3_file.exists():
            pass
        else:
            print(f"MISSING/BAD NAME: {video_title}.mp3 {line.strip()}\n")
    except:
        print (f"{line.strip()} is an invalid url.\n")

print('Done.')
sys.exit()
