from pytube import YouTube

class YoutubeDownloader:

    @staticmethod
    def download(urls, audio_only, highest_resolution, download_location):
        for url in urls:
            try:
                youtube = YouTube(url)
                video_title = youtube.title
                print("Downloading:\nSong Title: {}".format(video_title))
                if audio_only:
                    stream = youtube.streams.filter(only_audio=True).first()
                else:
                    if highest_resolution:
                        stream = youtube.streams.get_highest_resolution()
                    else:
                        stream = youtube.streams.first()
                if download_location == '':
                    stream.download()
                else:
                    stream.download(download_location)
                print("{} successfully downloaded.".format(video_title))

            except Exception as e:
                print(e)
                print("Something went wrong")
