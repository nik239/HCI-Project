import config
import pydub
from pydub.playback import play
#import time
#from threading import Thread
#0import os

first_frequency = config.first_freq
final_frequency = config.final_freq
increment = config.increment

waves = [str for i in range(int((final_frequency-first_frequency)/increment))]

for i in range(len(waves)): 
    waves[i] = str(first_frequency + increment * i) + '.wav'

for wave in waves: 
    f = open('results.' + wave + '.csv','w')
    f.write(wave+':')
    wav_file =  pydub.AudioSegment.from_file(file = wave,format = "wav")
    wav_file = wav_file - 100 # set volume to 0%
    for i in range(0,29,1):
        wav_file = wav_file + 1
        play(wav_file)
        print("Currenty volume is at " + str(i+1) + "%")
        entry = input("Enter 1 if you heard something, enter 0 otherwise!")
        if entry == '1': 
            f.write('Volume: '+str(i+1)+', Audible = 1') 
            f.close()
            break
        else: 
            f.write('Volume: '+str(i+1)+', Audible = 0') 




        