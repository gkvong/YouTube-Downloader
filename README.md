# YouTube Downloader
This python script takes a list of YouTube (or SoundCloud) links in a text document and downloads them as mp3 files. I made this script because I had hundreds of bookmarked YouTube songs and downloading them manually would take forever. This script uses [youtube-dl](https://github.com/ytdl-org/youtube-dl) which has neat documentation so the code can be readily modified to suit your needs (e.g. downloading mp4 or parts of videos).

## Getting Started

### Prerequisties
* [Python version 3.6 or higher](https://www.python.org/downloads/) is required.
* Install [FFmpeg](https://www.ffmpeg.org/).
* Install the youtube-dl python package. Using shell or command prompt execute the following command:
  ```
  python -m pip install -U youtube-dl
  ```
  
### Installation
Download or clone the respository
```
git clone https://github.com/gkvong/YouTube-Downloader
```

## Usage
Enter each YouTube/SoundCloud link on a new line in *songs.txt* and save the file. A sample *songs.txt* file is included. If the links are bookmarked on Google Chrome, you can open bookmark manager to simply copy and paste the links.

To download the links in the *songs.txt* file, run the *dl.py* python script:
```
python dl.py
```
The mp3 files will be downloaded into a folder in the same directory called *Downloads*.

## Errors
If the script fails to download a link, a *failed.txt* file will be created containing a list of all the links that it failed to download.

Sometimes the script can stall on a link, you can stop and restart it. Provided that you don't change the downloaded file names, it shouldn't download the same mp3 file twice.

### Download Checker
The repository also contains another script *check.py* that you can run:
```
python check.py
```
*check.py* takes links in the *checker.txt** file and outputs the links that don't have corresponding mp3 files in the *Downloads* folder. A sample *checker.txt* file is also included.

## License
[MIT License](LICENSE)