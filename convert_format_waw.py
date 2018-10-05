import os

#Parameters
#==========
#path = "/home/usuario/Escritorio/abel/"

#All type of format can be change to wav
def get_format(carpeta):
	for archivo in os.listdir(carpeta):
		name_file = archivo.split('.')
		os.system("ffmpeg -i '"+path+archivo+"' -acodec pcm_s16le -ac 1 -ar 16000 '"+path+name_file[0]+"_next.wav'")
		#os.system("rm '"+path+archivo+"'")


#Function principal
def main():
	get_format(path)
	
def audio(path):
	os.system("ffmpeg -i '"+path+"' -acodec pcm_s16le -ac 1 -ar 16000 '"+"conversion_"+path+"'")
	#os.system("rm '"+path+archivo+"'")
	return("conversion_"+path)


if __name__ == "__main__":
	main()
	