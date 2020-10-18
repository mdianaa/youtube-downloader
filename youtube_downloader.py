from YoutubeDownloader import YoutubeDownloader
from YoutubePlaylist import YoutubePlaylist
from os import path
from flask import Flask

# url = str(input('Please specify youtube video URL:'))
url = 'https://www.youtube.com/watch?v=iP6XpLQM2Cs&list=PLJatGb3hWsyhUwI8SGxCo7OV4iCB0yFEW&index=1'
#url = 'https://www.youtube.com/watch?v=Q97c5szTgIA'

download_location = str(input("Specify download directory(full path). Press Enter to download in current directory:"))
if download_location != '' and not path.exists(download_location):
    print('Please enter a valid path!')
    exit(1)
highest_resolution = False
audio_only = False
is_playlist = False

while True:
    while True:
        is_playlist_user_answer = str(input('Are you downloading a playlist?')).lower()
        if is_playlist_user_answer == 'yes':
            is_playlist = True
            break
        elif is_playlist_user_answer == 'no':
            is_playlist = False
            break
        else:
            print("Please enter either Yes or No. You entered {}".format(is_playlist_user_answer))
    audio_only_user_answer = str(input("Do you want to download only the audio of the video?")).lower()
    if audio_only_user_answer == 'yes':
        audio_only = True
        break
    elif audio_only_user_answer == 'no':
        audio_only = False
        while True:
            highest_resolution_user_answer = str(
                input("Do you want to download the video with the highest resolution?")).lower()
            if highest_resolution_user_answer == 'yes':
                highest_resolution = True
                break
            elif highest_resolution_user_answer == 'no':
                highest_resolution = False
                break
            else:
                print("Please enter either Yes or No. You entered {}".format(highest_resolution_user_answer))
        break
    else:
        print("Please enter either Yes or No. You entered {}".format(audio_only_user_answer))

youtube_urls = ''
if is_playlist:
    youtube_playlist = YoutubePlaylist(url)
    youtube_urls = youtube_playlist.get_playlist_urls()
else:
    youtube_urls = [url]

YoutubeDownloader.download(youtube_urls, audio_only, highest_resolution, download_location)
