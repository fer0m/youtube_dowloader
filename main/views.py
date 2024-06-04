import logging

from asgiref.sync import sync_to_async
from django.http import FileResponse
from django.shortcuts import render
from pytube import YouTube
from hurry.filesize import size

from .forms import Form
from .models import Post

logger = logging.getLogger(__name__)

from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
async def main_site(request):
    form = Form(request.POST)
    if 'checkForm' in request.POST:
        if form.is_valid():
            context = await check_form(form)
            return render(request, 'main/base_page.html', context=context)
        else:
            return render(request, 'main/base_page.html', {'form': form})

    elif 'downloadForm' in request.POST:
        if form.is_valid():
            video = await get_video(form)
            return FileResponse(video, as_attachment=True)
        else:
            return render(request, 'main/base_page.html', {'VideoForm': form})

    else:
        form = Form()
        return render(request, 'main/base_page.html', {'form': form})


async def check_form(form):
    link = form.cleaned_data['text']
    video_info = await get_video_info(link)
    context = {'form': form, **video_info}
    return context


@sync_to_async
def get_video_info(link):
    video = YouTube(link).streams.filter(progressive=True).get_highest_resolution()
    print(video)
    return {
        'filesize': size(video.filesize),
        'title': video.title,
        'expiration': video.expiration,
        'resolution': video.resolution
    }


@sync_to_async
def get_video(form):
    link = form.cleaned_data['text']
    post = Post()
    post.text = link
    post.file_video = YouTube(link).streams[0].download(output_path='media')
    post.save()
    return post.file_video
