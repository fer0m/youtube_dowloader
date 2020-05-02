from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    text = models.TextField(max_length=150)
    file_video = models.FileField(verbose_name="Видео", default="", upload_to='documents')
    time_now = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.time_now)