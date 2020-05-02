import logging

from django.http import FileResponse
from django.shortcuts import render
from pytube import YouTube
from hurry.filesize import size

from .forms import Form
from .models import Post

# Create your views here.

logger = logging.getLogger(__name__)


def main_site(request):
    if request.method == 'POST':
        form = Form(request.POST)

        if 'checkForm' in request.POST:
            if form.is_valid():
                context = check_form(form)
                return render(request, 'main/base_page.html', context=context)
            else:
                return render(request, 'main/base_page.html', context={'form': form})

        elif 'downloadForm' in request.POST:
            if form.is_valid():
                video = get_video(form)
                return FileResponse(video, as_attachment=True)
            else:
                return render(request, 'main/base_page.html', context={'form': form})

    else:
        form = Form()
        return render(request, 'main/base_page.html', {'form': form})


def check_form(form):
    link = form.cleaned_data['text']
    video = YouTube(link).streams.filter(progressive=True).get_highest_resolution()

    video_filesize = size(video.filesize)
    video_title = video.title
    video_expiration = video.expiration
    video_resolution = video.resolution

    context = {'form': form, 'title': video_title,
               'expiration': video_expiration,
               'filesize': video_filesize,
               'resolution': video_resolution}
    return context


def get_video(form):
    link = form.cleaned_data['text']
    post = Post()
    post.text = link
    post.file_video = YouTube(link).streams[0].download(output_path='media')
    post.save()
    return post.file_video
