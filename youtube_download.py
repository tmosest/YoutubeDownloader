from __future__ import unicode_literals
import youtube_dl

youtube_link = 'http://www.youtube.com/watch?v=dK7EMl2xNCE';

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([youtube_link])
