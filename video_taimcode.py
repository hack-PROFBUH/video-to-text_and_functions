from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip

link = input("sslka: ")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
ys.download(filename="my_video.mp4")

path = "my_video.mp4"
start_time = 5
end_time = 15

clip = VideoFileClip(path).subclip(start_time, end_time)

clip.write_videofile("my_video_trimmed.mp4")
