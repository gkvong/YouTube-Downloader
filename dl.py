#!/usr/bin/python

import youtube_dl
       
ydl_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'outtmpl': 'Downloads/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with open('songs.txt') as f:
    song_lines = f.readlines()

for line in song_lines:
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading {line.strip()}")
            info_dict = ydl.extract_info(line.strip())
            video_title = info_dict.get('title', None)
            print(f"Downloaded {video_title} {line.strip()}\n")
            
    except:
        print(f"Failed to download {line}")
        f = open('failed.txt','a')
        f.write(f"{line.strip()}\n")
        f.close()
