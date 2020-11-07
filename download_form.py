from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import Regexp


class DownloadForm(FlaskForm):
    url = StringField('Youtube Url: ', validators=[Regexp('https:\/\/www\.youtube\.com\/watch', message="Please enter a valid Youtube video url.")])
    is_playlist = BooleanField('Are you downloading a playlist?')
    audio_only = BooleanField('Do you want to download only the audio of the video?')
    highest_resolution = BooleanField('Do you want do download the video with the highest resolution?')
    submit = SubmitField('Download')
