import math        
import pyaudio  
from  scipy.io import wavfile

#This script is mostly a copy-paste from Stack Exchange

PyAudio = pyaudio.PyAudio     #initialize pyaudio
BITRATE = 100000     #number of frames per second/frameset.    
LENGTH = 1    #seconds to play sound

FREQUENCY = 1000  #Hz, waves per second, 261.63=C4-note.
ENDFREQUENCY = 3000

if FREQUENCY > BITRATE:
   BITRATE = FREQUENCY+100
NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''

#generating waves
for x in range(NUMBEROFFRAMES):
     WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
     FREQUENCY += (ENDFREQUENCY - FREQUENCY)/NUMBEROFFRAMES

for x in range(RESTFRAMES):
    WAVEDATA = WAVEDATA+chr(128)

print(WAVEDATA)
p = PyAudio()
stream = p.open(format = p.get_format_from_width(1),channels = 2,rate = BITRATE,output = True)
stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()