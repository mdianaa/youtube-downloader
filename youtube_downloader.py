from pytube import YouTube

url = str(input("Please specify video URL:"))

try:
    youtube = YouTube(url)
    print("Downloading the following song:\n")
    print("Song Title: {}\nSong Description: {}".format(youtube.title,
                                                        youtube.description))
    stream = youtube.streams.first()
    stream.download()
    print("Songs successfully downloaded.")

except Exception as e:
    print(e)
    print("Something went wrong")


# # python3.6 youtube_downloader.py