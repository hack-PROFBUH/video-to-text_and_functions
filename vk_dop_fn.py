import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     ydl.download(['https://vk.com/video-30316056_456326877'])
