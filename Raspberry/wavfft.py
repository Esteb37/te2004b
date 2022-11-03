import numpy as np
import scipy.fftpack as fourier
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
# tiempo y frecuencia de muestreo
Ts = 0.0001
Fs = 1/Ts
# frecuencia de 60Hz y 223 Hz
w1 = 2*np.pi*60
w2 = 2*np.pi*223
n = Ts*np.arange(0, 1000)
sin1 = 3*np.sin(w1*n)
sin2 = 2.3*np.sin(w2*n)
# mix sin1 and sin2
sinMix = sin1+sin2
# add noise
noise = np.random.random(len(n))
sinMixNoise = sinMix+noise
plt.subplot(411)
p1 = plt.plot(n, sin1, '.-')
plt.xlabel('Tiempo (s) ', fontsize='14')
plt.ylabel('Amplitud ', fontsize='14')
plt.subplot(412)
p2 = plt.plot(n, sin2, '.-')
plt.xlabel('Tiempo (s) ', fontsize='14')
plt.ylabel('Amplitud ', fontsize='14')
plt.subplot(413)
p2 = plt.plot(n, sinMix, '.-')
plt.xlabel('Tiempo (s) ', fontsize='14')
plt.ylabel('Amplitud ', fontsize='14')
plt.subplot(414)
p2 = plt.plot(n, sinMixNoise, '.-')
plt.xlabel('Tiempo (s) ', fontsize='14')
plt.ylabel('Amplitud ', fontsize='14')
plt.show()
# compute Fourier
gk = fourier.fft(sinMixNoise)
M_gk = abs(gk)
# vector de frecuencias
F = Fs*np.arange(0, len(n))/len(n)
plt.plot(F, M_gk)
plt.xlabel('Frecuencia (Hz) ', fontsize='14')
plt.ylabel('Amplitud FFT ', fontsize='14')
plt.show()
