import os
import cut
import audiospeed
import convert_format_waw
from pydub import AudioSegment

#path inicial
path="test_next.wav"
#file name
s_extension=path.split(".")
#path_destino of slow audio
dst=s_extension[0]+"_slowly_0.5.wav"

#convert_format_wav
name=convert_format_waw.audio(path)

#separate audio in part of 30 seconds
cut.separate_audio(name)

#sound
sound = AudioSegment.from_file(name)

#slow audio in 0.5
audiospeed.speed_change(sound,0.50,dst)
