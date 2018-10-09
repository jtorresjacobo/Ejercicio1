import os

def audio(path,filename):
	file=filename
	filename=filename.split(".")
	os.system("ffmpeg -i '"+path+"/"+file+"' -acodec pcm_s16le -ac 1 -ar 16000 '"+path+"/"+filename[0]+"_features.wav"+"'")
	#os.system("rm '"+path+archivo+"'")
	return(filename[0]+"_features.wav")


	