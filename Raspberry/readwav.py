import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
import sys
wf = wave.open("archivo.wav", 'rb')
print("Number of channels", wf.getnchannels())
print("sample width", wf.getsampwidth())
print("frame rate", wf.getframerate())
print("Number of frames", wf.getnframes())
print("parameters", wf.getparams())
sample_freq = wf.getframerate()
n_samples = wf.getnframes()
# get the time in seconds
duration = n_samples/sample_freq
print("duration ", duration)
signal_wave = wf.readframes(-1)  # read all frames
print(type(signal_wave), type(signal_wave[0]))
# divide by the sampwidth and nchannels values parameter
print(len(signal_wave) / 4)
wf.close()
# Create a new file with the same parameters (copy)
wf_new = wave.open("archivo.wav", "wb")
wf_new.setnchannels(2)
wf_new.setsampwidth(2)
wf_new.setframerate(44100)
wf_new.writeframes(signal_wave)
wf_new.close()
