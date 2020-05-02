from django.core.management.base import BaseCommand
from django.utils import timezone
from pytube import YouTube
from hurry.filesize import size
import json

class Command(BaseCommand):
    help = '''Write youtube link for test. For example:
           ./manage.py check_link https://www.youtube.com/watch?v=9bZkp7q19f0'''

    def add_arguments(self, parser):
        parser.add_argument('youtube_link', help=u'Enter here youtube link')

    def handle(self, *args, **kwargs):
        link = kwargs['youtube_link']
        try:
            video = YouTube(link).streams.filter(progressive=True).get_highest_resolution()
            video_filesize = size(video.filesize)
            video_title = video.title
            video_resolution = video.resolution

            context = {'title': video_title,
                       'filesize': video_filesize,
                       'resolution': video_resolution}
            text_to_console = ''

            for key, value in context.items():
                text_to_console += f'{key} : {value}. '
            self.stdout.write(self.style.SUCCESS(text_to_console))

        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
