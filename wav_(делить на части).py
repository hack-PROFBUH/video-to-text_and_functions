from pydub import AudioSegment

sound = AudioSegment.from_wav("all.wav")

a = 5000

for i, part in enumerate(sound[::a]):
    part.export(f"part_{i}.wav", format="wav")
