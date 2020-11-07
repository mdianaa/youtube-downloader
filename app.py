import glob
import os

from flask import Flask, render_template, redirect, send_file

from YoutubeDownloader import YoutubeDownloader
from YoutubePlaylist import YoutubePlaylist
from download_form import DownloadForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


def get_file_list(full_directory_path):
    return glob.glob(full_directory_path)


def remove_files(files):
    for file in files:
        os.remove(file)


@app.route('/', methods=['GET', 'POST'])
def youtube_download():
    download_form = DownloadForm()
    if download_form.validate_on_submit():
        print("Form data: url: {}, is_playlist: {}, audio_only: {}, highest_resolution: {}".format(
            download_form.url.data,
            download_form.is_playlist.data,
            download_form.audio_only.data,
            download_form.highest_resolution.data))
        is_playlist = download_form.is_playlist.data
        url = download_form.url.data
        audio_only = download_form.audio_only.data
        highest_resolution = download_form.highest_resolution.data

        if is_playlist:
            youtube_playlist = YoutubePlaylist(url)
            youtube_urls = youtube_playlist.get_playlist_urls()
        else:
            youtube_urls = [url]

        file_list = get_file_list('/Users/Diana/Repos/youtube-downloader/youtube_downloads/*')
        remove_files(file_list)
        YoutubeDownloader.download(youtube_urls, audio_only, highest_resolution, download_location='youtube_downloads')
        file_list = get_file_list('/Users/Diana/Repos/youtube-downloader/youtube_downloads/*')

        try:
            for file in file_list:
                return send_file(file, as_attachment=True)
        except Exception as e:
            print(e)
        return redirect('/')
    return render_template('download_form.html', download_form=download_form)
