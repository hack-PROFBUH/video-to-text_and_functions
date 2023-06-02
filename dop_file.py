
'''
from pytube import YouTube
import speech_recognition as sr


link = input("sslka: ")

yt = YouTube(link)

ys = yt.streams.get_highest_resolution()

#print(f"Заголовок: {yt.title}")

ys.download()
print("Загрузка завершена")

'''

##############################################


import speech_recognition as sr

r = sr.Recognizer()
file_path = "13.wav"

with sr.AudioFile(file_path) as source:
    audio_text = r.record(source)

text = r.recognize_google(audio_text, language="ru-RU")
print(text)


##########################################################
