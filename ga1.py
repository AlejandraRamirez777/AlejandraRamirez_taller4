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

#Dimensiones imagen
#(y,x,capas)
print(np.shape(arr))
(YY, XX, capas) = np.shape(arr)
print YY
print XX
print(np.shape(arr))

def gaussx(x,anc,cx):
    c = anc
    #normalizacion
    a = 1/float(c*np.sqrt(2*np.pi))

    ux = (x-cx)*(x-cx)
    #uy = (y-cy)*(y-cy)

    ff = ux/float(2*c*c)
    #gg = uy/float(2*c*c)

    ee = np.exp(-ff)
    sol = a*ee
    return sol

def cen(Y,X):
    sol = list()
    cx = 0.0
    cy = 0.0
    if(Y%2 != 0):
        cy = int((Y/2.0) + 1)
    if(Y%2 == 0):
        cy = int((Y/2.0))
    if(X%2 != 0):
        cx = int((X/2.0) + 1)
    if(X%2 == 0):
        cx = int((X/2.0))
    sol.append(float(cy))
    sol.append(float(cx))
    return sol

#Calcular centro de imagen
cc = cen(YY,XX)
print cc

xx = np.linspace(0,35-1,35)
yyy = np.linspace(0,35-1,35)
print xx

for i in range(35):
    print i
    yyy[i] = gaussx(i,wd,cc[1])

print yyy

plt.plot(xx,yyy)
plt.show()
