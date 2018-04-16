import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

a = np.linspace(0,9,10)
print a
b = np.fft.fft(a)
print b
c = fftpack.fft(a)
print c

def fourier(func,N):
    G = np.array(list())
    for n in range(N):
        g = 0
        for k in range(N):
            w = (n/float(N))
            m = np.exp(-1j*2*np.pi*k*w)
            g += func[k]*m

        G = np.append(G,g)

    return G

print fourier(a,10)

signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)
fourier = np.fft.fft(signal)
print fourier
n = signal.size
print n
timestep = 0.1
freq = np.fft.fftfreq(9, d=timestep)
print  freq
plt.scatter(freq,abs(fourier))
plt.show()
