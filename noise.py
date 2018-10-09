import numpy as np
from scikits.audiolab import wavread, wavwrite

data1, fs1, enc1 = wavread("audioEres_Mi_Sueno_-_Carlo_Supo_Feat_features_slow.wav")
data2, fs2, enc2 = wavread("audioEres_Mi_Sueno_-_Carlo_Supo_Feat_features_slow.wav")

assert fs1 == fs2
assert enc1 == enc2
result = 0.5 * data1 + 0.5 * data2

wavwrite(result, 'result.wav')