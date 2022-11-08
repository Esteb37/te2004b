from __future__ import print_function
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fourier
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
from scipy.signal import chirp, stft
import os

fs_rate_p1, signal_p1 = wavfile.read(
    os.path.join(os.getcwd(), "Raspberry/doremifasollasi.wav").replace("\\", "/"))
print("Frequency sampling P1", fs_rate_p1)
print("signal_p1 data type ", signal_p1.dtype)


signal_p1 = signal_p1[44000:len(signal_p1)]
l_audio_p1 = len(signal_p1.shape)
print("Channels P1", l_audio_p1)
if l_audio_p1 == 2:
    signal_p1 = signal_p1.sum(axis=1) / 2

N_p1 = signal_p1.shape[0]
print("Complete Samplings N P1", N_p1)
secs_p1 = N_p1 / float(fs_rate_p1)
print("secs P1", secs_p1)
Ts_p1 = 1.0/fs_rate_p1  # sampling interval in time
print("Timestep between samples Ts P1", Ts_p1)


# time vector as scipy arange field / numpy.ndarray
t_p1 = np.arange(0, secs_p1, Ts_p1)
FFT_p1_real = fourier.rfft(signal_p1)
freq_p1_real = fourier.rfftfreq(signal_p1.size, Ts_p1)
FFT_p1 = abs(fourier.fft(signal_p1))
FFT_side_p1 = FFT_p1[range(N_p1//2)]  # one side FFT range
freqs_p1 = fourier.fftfreq(signal_p1.size, t_p1[1]-t_p1[0])
fft_freqs_p1 = np.array(freqs_p1)
freqs_side_p1 = freqs_p1[range(N_p1//2)]  # one side frequency range
fft_freqs_side_p1 = np.array(freqs_side_p1)
plt.subplot(2, 1, 1)
p1 = plt.plot(t_p1, signal_p1, "g")  # plotting the signal
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(2, 1, 2)

# plotting the positive fft spectrum

p2 = plt.plot(freqs_side_p1, abs(FFT_side_p1), "b")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count single-sided')

# size error t_p2 is one element larger
for i, f in enumerate(freq_p1_real):
    if f < 62 and f > 58:  # (1)
        FFT_p1_real[i] = 0.0
    if f < 21 or f > 20000:  # (2)
        FFT_p1_real[i] = 0.0


noiseless_signal = fourier.irfft(FFT_p1_real)
noiseless_signal = np.int16(noiseless_signal *
                            (32767/noiseless_signal.max()))

wavfile.write("noiseless_p1_amealco.wav", fs_rate_p1,
              noiseless_signal)
print("writing file")
fs_rate_p4, signal_p4 = wavfile.read(
    os.path.join(os.getcwd(), "Raspberry/p1p2p3_amealco.wav"))
print("Frequency sampling P1", fs_rate_p4)
print("signal_p4 data type ", signal_p4.dtype)
signal_p4 = signal_p4[24000:len(signal_p4)]
l_audio_p4 = len(signal_p4.shape)
if l_audio_p4 == 2:
    signal_p4 = signal_p4.sum(axis=1) / 2
N_p4 = signal_p4.shape[0]
print("Complete Samplings N P4", N_p4)
secs_p4 = N_p4 / float(fs_rate_p4)
print("secs P4", secs_p4)
Ts_p4 = 1.0/fs_rate_p4  # sampling interval in time
print("Timestep between samples Ts P4 ", Ts_p4)

# time vector as scipy arange field / numpy.ndarray
t_p4 = np.arange(0, secs_p4, Ts_p4)
FFT_p4_real = fourier.rfft(signal_p4)
freq_p4_real = fourier.rfftfreq(signal_p4.size, Ts_p4)


FFT_p4 = abs(fourier.fft(signal_p4))
FFT_side_p4 = FFT_p4[range(N_p4//2)]  # one side FFT range
freqs_p4 = fourier.fftfreq(signal_p4.size, t_p4[1]-t_p4[0])
fft_freqs_p4 = np.array(freqs_p4)
freqs_side_p4 = freqs_p4[range(N_p4//2)]  # one side frequency range

fft_freqs_side_p4 = np.array(freqs_side_p4)
plt.subplot(2, 2, 1)
p1 = plt.plot(t_p1, signal_p1, "g")  # plotting the signal
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(2, 2, 2)

# plotting the positive fft spectrum
p2 = plt.plot(freqs_side_p1, abs(FFT_side_p1), "b")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count single-sided')
plt.subplot(2, 2, 3)

p3 = plt.plot(t_p4, signal_p4, "g")  # plotting the signal
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(2, 2, 4)

# plotting the positive fft spectrum
p4 = plt.plot(freqs_side_p4, abs(FFT_side_p4), "b")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count single-sided')
plt.show()
f, t, Zxx = signal.stft(signal_p1,
                        fs_rate_p1, nperseg=2048)
plt.figure(1)
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0,
               vmax=1, shading='gouraud')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.grid()
f, t, Zxx = signal.stft(signal_p4,
                        fs_rate_p4, nperseg=2048)
plt.figure(2)
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0,
               vmax=1, shading='gouraud')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.grid()
plt.show()
