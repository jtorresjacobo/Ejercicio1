import os
from os import path
from pydub import AudioSegment
import soundfile as sf


def separate_audio(paths,filename):
	#tiempo total en segundos
	s_extension=path.split(".")
	print(paths+"/"+filename)

	name=filename.split(".")
	f = sf.SoundFile(paths+"/"+filename)
	total=int(format(len(f) / f.samplerate))
	cant=total/30
	sobrante=total-cant*30

	sound=AudioSegment.from_wav(paths+"/"+filename)
	sound=sound.set_channels(1)
	halfway_point=len(sound)

	first_half=sound[:30000]
	first_half.export("t",format="wav")
	i=0
	j=0
	k=30000
	for i in range(0,cant):
		audio=sound[j:k]
		#if i==0:
		#os.system("mkdir "+"Audios_separados")
		audio.export(paths+"/"+"cut_"+name[0]+"_"+str(i),format="wav")
		j=j+30000
		k=k+30000
		i=i+1
		if i==cant and sobrante!=0:
			k=k+30000
			audio=sound[j:halfway_point]
			audio.export(paths+"/"+"cut_"+name[0]+"_"+str(i),format="wav")
