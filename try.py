from pytube import YouTube
from moviepy.editor import *
import speech_recognition as sr

###
link = input("sslka: ")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
ys.download(filename="my_video.mp4")
###

###
video_path = "my_video.mp4"
video = VideoFileClip(video_path)
audio = video.audio
audio_path = "audio.wav"
audio.write_audiofile(audio_path)
###

###
r = sr.Recognizer()
file_path = "audio.wav"
with sr.AudioFile(file_path) as source:
    audio_text = r.record(source)

text = r.recognize_google(audio_text, language="ru-RU")
print(text)
