import numpy as np
import matplotlib.pyplot as plt

def func(x):
    y = x*x
    return y

a = np.zeros(10)
b = np.zeros(10)

for i in range(10):
    a[i] = i*i*0.1*i
    b[i] = func(i+ np.random.random(1))
    #print str(a[i]) + " " + str(b[i]))

'''
print str(1101.0) + " " + str(25.113)
print str(911.3) + " " + str(30.131)
print str(636.0) + " " + str(40.120)
print str(451.1) + " " + str(50.128)
'''

inter = np.genfromtxt("result.txt")
#Desde 0 hasta 73
xinter = np.linspace(0,73,74)

orix = np.genfromtxt("datos.txt", usecols=0)
oriy = np.genfromtxt("datos.txt", usecols=1)

plt.plot(orix,oriy)
plt.plot(xinter,inter, c = "g")
plt.show()
