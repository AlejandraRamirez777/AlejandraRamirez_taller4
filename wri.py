import numpy as np
import matplotlib.pyplot as plt

def func(x):
    y = x*x
    return y

a = np.zeros(10)
b = np.zeros(10)

for i in range(10):
    a[i] = i*i*0.1*i
    #b[i] = func(i)
    #b[i] = func(i- np.random.random(1))
    #print str(i*i*0.1*i) + " " + str(int(func(i+ np.random.random(1))))

print str(1101.0) + " " + str(25.113)
print str(911.3) + " " + str(30.131)
print str(636.0) + " " + str(40.120)
print str(451.1) + " " + str(50.128)

#plt.plot(a,b)
#plt.show()
