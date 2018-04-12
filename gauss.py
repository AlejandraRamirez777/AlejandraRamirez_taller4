import numpy as np
import matplotlib.pyplot as plt
import sys

from scipy import fftpack

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

#Funcion que define gausiana del suavizado
#Param:coordenada x, y y el ancho, centrada en (cx,cy)
#Return:punto de gausiana resultante
def gauss(x,y,anc,cx,cy):
    c = anc
    #normalizacion
    a = 1/float(c*c*2*np.pi)

    ux = (x-cx)*(x-cx)
    uy = (y-cy)*(y-cy)

    ff = ux/float(2*c*c)
    gg = uy/float(2*c*c)

    ee = np.exp(-(ff+gg))
    sol = a*ee
    return sol

#determinar centrado de gausiana en base a imagen
#Param: dimensiones Y,X de la imagen
#return: lista con centro de la imagen (cy,cx)
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

print cen(YY,XX)

#Calcular centro de imagen
cc = cen(YY,XX)

#Array donde se guardara gausiana
ga = np.zeros((YY,XX))
#print ga

#Generar gausiana en base a imagen
for h in range(YY):
    for j in range(XX):
        ga[h][j] = gauss(j,h,wd,cc[1],cc[0])

#Fourier para gauss
def fouG(Y,X):
    #Array donde se guardara info fourierizados
    sol = np.zeros((Y,X), dtype = complex)
    # num of samples
    for n in range(Y):
        for o in range(X):
            #Contador de suma
            g = 0.0
            #Sumatorias
            for k in range(Y):
                for p in range(X):
                    #este se multiplicaria por sr
                    wy = (float(n*k)/float(Y))
                    wx = (float(o*p)/float(X))
                    ee = np.exp(-1j*2.0*np.pi*(wy+wx))
                    #aplicacion formula a suma de gauss
                    g+=gauss(p,k,wd,cc[1],cc[0])*ee

            sol[n][o] = g

    return sol

#Aplicar trans Fourier a gausiana
fouGA = fouG(YY,XX)

go4 = np.fft.fft2(ga)

print np.shape(ga)
print np.shape(fouGA)
print np.shape(go4)



for i in range(YY):
    for j in range(XX):
        print "FOUga"
        print go4[i][j]
        print fouGA[i][j]
