from pytube import YouTube
from pprint import pprint

yt = YouTube('https://www.youtube.com/watch?v=vzhJixCzOc4a')
for i in yt.streams.filter(audio_codec='mp4a.40.2'):
    print(i)
    video_hd = i

# print(video_hd.dowload())
# print(video_hd)
# print(type(video_hd))
# video_hd.download()
# YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams[2].download()
