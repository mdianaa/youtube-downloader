import bs4
import re
import requests


class YoutubePlaylist:

    def __init__(self, youtube_playlist_url):
        self.youtube_playlist_url = youtube_playlist_url

    def get_playlist_urls(self):
        youtube_playlist_html = requests.get(self.youtube_playlist_url)
        soup_html_object = bs4.BeautifulSoup(youtube_playlist_html.text, 'html.parser')
        youtube_playlist_data_pattern = re.compile(r"ytInitialData")
        youtube_playlist_script_match = soup_html_object.find("script", text=youtube_playlist_data_pattern)
        youtube_playlist_video_urls = re.findall(r"/watch\?v=[0-9A-Za-z-_&=\\]+index=[0-9]",
                                         youtube_playlist_script_match.string.split('window["ytInitialPlayerResponse"]')[
                                             0].replace(
                                             "\\u0026", '&'))
        return list(set(youtube_playlist_video_urls))
