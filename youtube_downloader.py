from YoutubeDownloader import YoutubeDownloader
from os import path

url = str(input('Please specify youtube video URL:'))
download_location = str(input("Specify download directory(full path). Press Enter to download in current directory:"))
if download_location != '' and not path.exists(download_location):
    print('Please enter a valid path!')
    exit(1)
highest_resolution = False
audio_only = False

while True:
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

urls = [url]

YoutubeDownloader.download(urls, audio_only, highest_resolution, download_location)
