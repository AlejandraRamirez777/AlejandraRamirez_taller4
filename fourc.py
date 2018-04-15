import numpy as np
from scipy import fftpack

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
