import numpy as np

def func(x):
    y = x*x
    return y

a = np.linspace(0,14,15)
b = np.zeros(15)

for i in a:
    b[i] = func(i)
    #print str(a[i]) + " " + str(b[i])

c = np.genfromtxt("result.txt")

d = np.fft.fft(c)
e = np.fft.fftfreq(12,1.27273)

print d
print e
