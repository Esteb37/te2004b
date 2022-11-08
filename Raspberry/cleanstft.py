import numpy as np
from scipy.fft import fft, fftfreq
from matplotlib import pyplot as plt
from scipy import signal

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


# Generate a 2 hertz sine wave that lasts for 5 seconds
x, y1 = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, y2 = generate_sine_wave(2000, SAMPLE_RATE, DURATION)

aux1 = len(y1)//2
aux2 = len(y2)
newY1 = y1[:aux1]
newY2 = y2[aux1:aux2]
mixed_tone = np.concatenate([newY1, newY2])

normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

plt.plot(normalized_tone)
plt.show()

# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION

yf = fft(normalized_tone)
xf = fftfreq(N, 1 / SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.show()

f, t, Zxx = signal.stft(normalized_tone, SAMPLE_RATE, nperseg=4096)
plt.figure(1)
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=1, shading='gouraud')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.grid()
plt.show()
