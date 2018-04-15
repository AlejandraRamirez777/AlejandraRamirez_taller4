import numpy as np
import matplotlib.pyplot as plt

#pr = np.zeros((4,2))
'''
z = 1
y = 10
for i in range(5):
    for o in range(2):
        #print str(z) + " " +str(y)
        z+=1*(o*2
        y+=10
'''

def func(x):
    y = x*x
    return y

a = np.zeros(10)
b = np.zeros(10)

for i in range(10):
    a[i] = i*i*0.1*i
    #b[i] = func(i)
    #b[i] = func(i- np.random.random(1))
    print str(i*i*0.1*i) + " " + str(int(func(i+ np.random.random(1))))

#plt.plot(a,b)
#plt.show()
