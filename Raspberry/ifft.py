from __future__ import print_function
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fourier
import numpy as np
from matplotlib import pyplot as plt
# NOTA   OCTAVA0              OCTAVA1  ............
# DO     261.63                523.25
# RE     293.66                587.33
# MI     329.63                659.26
# FA     349.23                698.46
# SOL    392.0 (SOL# 415.3)    783.99 (830.61)
# LA     440.0                 880
fs_rate, signal = wavfile.read("doremifasollasi.wav")
print("Frequency sampling", fs_rate)
l_audio = len(signal.shape)
print("Channels", l_audio)
if l_audio == 2:
    signal = signal.sum(axis=1) / 2
N = signal.shape[0]
print("Complete Samplings N", N)
secs = N / float(fs_rate)
print("secs", secs)
Ts = 1.0/fs_rate  # sampling interval in time
print("Timestep between samples Ts", Ts)
t = np.arange(0, secs, Ts)  # time vector as scipy arange field / numpy.ndarray
FFT = abs(fourier.fft(signal))
FFT_side = FFT[range(N//2)]  # one side FFT range
freqs = fourier.fftfreq(signal.size, t[1]-t[0])
fft_freqs = np.array(freqs)
freqs_side = freqs[range(N//2)]  # one side frequency
range
fft_freqs_side = np.array(freqs_side)
plt.subplot(311)
p1 = plt.plot(t, signal, "g")  # plotting the signal
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(312)
p2 = plt.plot(freqs, FFT, "r")  # plotting the complete fft spectrum
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count dbl-sided')
plt.subplot(313)
# plotting the positive fft spectrum
p3 = plt.plot(freqs_side, abs(FFT_side), "b")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count single-sided')
plt.show()
# Apply inverse Fourier
FFT = fourier.fft(signal)
inverseFFT = fourier.ifft(FFT)
plt.plot(inverseFFT[:100000])
plt.show()
