import config
import wave
import numpy as np

first_frequency = config.first_freq
final_frequency = config.final_freq
increment = config.increment


def generate_waves(frequency):
    samplerate = 44100
    seconds = 1

    project_directory = "/Users/nikitaivanov/Desktop/HCI project/"
    soundname = project_directory+str(frequency)+".wav"

    t = np.linspace(0, seconds, samplerate)
    left_channel = 0.5 * np.sin(2 * np.pi * frequency * t)
    right_channel = left_channel

    # Put the channels together with shape (2, 44100).
    audio = np.array([left_channel, right_channel]).T

    # Convert to (little-endian) 16 bit integers.
    audio = (audio * (2 ** 15 - 1)).astype("<h")

    with wave.open(soundname, "w") as f:
        # 2 Channels.
        f.setnchannels(2)
        # 2 bytes per sample.
        f.setsampwidth(2)
        f.setframerate(samplerate)
        f.writeframes(audio.tobytes())

for i in range(first_frequency, final_frequency + increment, increment):
    generate_waves(i)
