import re

from django import forms
from django.core.exceptions import ValidationError
from pytube import YouTube
from pytube.exceptions import RegexMatchError

from .models import Post


class Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={"class": "form-control",
                                          "placeholder": "Enter your link here",
                                          "rows": 1,
                                          "style": "resize:none;white-space: nowrap;",
                                          "required": True}), }
        labels = {
            'text': '',
        }

    def clean_text(self):
        data = self.cleaned_data['text']
        if self.youtube_url_validation(data) is None:
            raise ValidationError("Check your link. Something go wrong")
        try:
            check_youtube_video = YouTube(data).title
        except RegexMatchError:
            raise ValidationError("Check your link. I can't download it!")

        return data

    @staticmethod
    def youtube_url_validation(url):
        youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

        youtube_regex_match = re.match(youtube_regex, url)
        if youtube_regex_match:
            return True
