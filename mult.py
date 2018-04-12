import numpy as np
import matplotlib.pyplot as plt
import sys

#Info input by user en forma de lista
#[0] nombre del .py - [1] nombre imagen - [2] ancho de gausiana
inn = sys.argv
name = inn[1]
wd = float(inn[2])

# covertir imagen del input a un array
arr = plt.imread(name)
print(np.shape(arr))

#Dimensiones imagen
#(y,x,capas)
(YY, XX, capas) = np.shape(arr)
print YY
print XX

a = np.ones((YY,XX,4))*2

c = arr*a
d = a*arr

'''
for i in range(YY):
    for j in range(XX):
        print "OK"
        print arr[i][j]
        print c[i][j]
        print d[i][j]
'''

print np.shape(arr[:][0][0])        
