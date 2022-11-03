import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt32
CHANNELS = 1
RATE = 16000
file = wave.open('archivo.wav', 'rb')
sample_freq = file.getframerate()
frames = file.getnframes()
signal_wave = file.readframes(-1)
file.close()
time = frames / sample_freq
# if one channel use int16, if 2 use int32
audio_array = np.frombuffer(signal_wave, dtype=np.int32)
times = np.linspace(0, time, num=frames)
plt.figure(figsize=(15, 5))
plt.plot(times, audio_array)
plt.ylabel('Signal Wave')
plt.xlabel('Time (s)')
plt.xlim(0, time)
plt.title('The Thing I Just Recorded!!')
plt.show()
