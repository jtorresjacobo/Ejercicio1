import pyaudio  
import wave 
import numpy as np

f = wave.open('audioEres_Mi_Sueno_-_Carlo_Supo_Feat_features_slow.wav',"r")  
p = pyaudio.PyAudio()  
# open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
float_array = np.fromstring(f.readframes(10000000), dtype=np.uint16).astype('float32')
output = 0.9 *  float_array
stream.write(output.astype('uint16').tostring())

#sound.export(p,format="wav")



