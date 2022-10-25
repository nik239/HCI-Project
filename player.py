import config
import pydub
import csv
from pydub.playback import play

first_frequency = config.first_freq
final_frequency = config.final_freq
increment = config.increment
project_directory = config.project_directory

waves = [str for i in range(int((final_frequency-first_frequency)/increment))]

for i in range(len(waves)): 
    waves[i] = str(first_frequency + increment * i) + '.wav'

file = open('results2.csv','w')
writer = csv.writer(file)
writer.writerow(["frequency", "volume"])

for wave in waves: 
    wav_file =  pydub.AudioSegment.from_file(file = wave,format = "wav")
    wav_file = wav_file - 100 # set volume to 0%
    for i in range(0,29,1):
        wav_file = wav_file + 1
        play(wav_file)
        print("Currently volume is at " + str(i+1) + "%")
        entry = input("Enter 1 if you heard something, enter 0 otherwise!")
        if entry == '1':  
            writer.writerow([wave,str(i+1)])
            break
    
file.close()
