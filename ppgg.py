import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import fftpack

import matplotlib.image as mpimg


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

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

gray = rgb2gray(arr)




#Funcion para hacer Fourier 2d
#Param: array al que se le hara fourier (png)
#Return: array de array (png) fourierizado


def fou(arr,Y,X):
    #Array donde se guardara info de color de pixeles fourierizados
    sol = np.zeros((Y,X,4), dtype = complex)
    # num of samples
    for n in range(Y):
        for o in range(X):
            #Sumas de cada color de pixel
            sR = 0.0
            sG = 0.0
            sB = 0.0
            sf = 0.0
            #Sumatorias
            for k in range(Y):
                for p in range(X):
                    #Se extraen colores de pixel
                    (R,G,B,f) = arr[k][p][:]
                    #este se multiplicaria por sr ?
                    wy = (float(n*k)/float(Y))
                    wx = (float(o*p)/float(X))
                    ee = np.exp(-1j*2.0*np.pi*(wy+wx))
                    #aplicacion formula a suma
                    sR += ee*R
                    sG += ee*G
                    sB += ee*B
                    sf += ee*f
            #normalizacion ?
            sol[n][o][0] = sR
            sol[n][o][1] = sG
            sol[n][o][2] = sB
            sol[n][o][3] = sf
    return sol

go1 = np.fft.fft2(gray)
print go1
print np.shape(go1)
#print type(go1)

go3 = fou(arr,YY,XX)
gray3 = rgb2gray(go3)
print gray3
print np.shape(gray3)







#plt.imshow(gray, cmap = plt.get_cmap('gray'))



#plt.show()
