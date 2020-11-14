import glob
import os
import zipfile
import datetime

from flask import Flask, render_template, redirect, send_file

from YoutubeDownloader import YoutubeDownloader
from YoutubePlaylist import YoutubePlaylist
from download_form import DownloadForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
DOWNLOAD_PATH = '/Users/Diana/Repos/youtube-downloader/youtube_downloads/'
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
        print("Form data: url: {}, is_playlist: {}, is_video: {}, highest_resolution: {}".format(
            download_form.url.data,
            download_form.is_playlist.data,
            download_form.is_video.data,
            download_form.highest_resolution.data))
        is_playlist = download_form.is_playlist.data
        url = download_form.url.data
        is_video = download_form.is_video.data
        highest_resolution = download_form.highest_resolution.data

        if is_playlist:
            youtube_playlist = YoutubePlaylist(url)
            youtube_urls = youtube_playlist.get_playlist_urls()
        else:
            youtube_urls = [url]

        file_list = get_file_list(DOWNLOAD_PATH + '*')
        remove_files(file_list)
        YoutubeDownloader.download(youtube_urls, is_video, highest_resolution, download_location='youtube_downloads')
        file_list = get_file_list(DOWNLOAD_PATH + '*')
        
        if is_playlist:
            youtube_playlist_zip = "youtube_playlist_{}.zip".format(datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
            zip_file = zipfile.ZipFile(DOWNLOAD_PATH + youtube_playlist_zip, mode='w')
            for file in file_list:
                file_dir_path = os.path.dirname(os.path.abspath(file))
                arc_file_name = file[len(file_dir_path) + 1:]
                zip_file.write(file, arc_file_name)
            zip_file.close()
            return send_file(DOWNLOAD_PATH + youtube_playlist_zip, mimetype='zip', as_attachment=True)
        else:
            try:
                return send_file(file_list[0], as_attachment=True)
            except Exception as e:
                print(e)
                return redirect('/')
    return render_template('download_form.html', download_form=download_form)
