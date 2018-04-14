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
print(np.shape(arr))

#Dimensiones imagen
#(y,x,capas)
(YY, XX, capas) = np.shape(arr)
print YY
print XX

#Transformar imagen a grayscale
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

arrg = rgb2gray(arr)

#print np.shape(arrg)

def fou(arr,Y,X):
    #Array donde se guardara info de color de pixeles fourierizados
    sol = np.zeros((Y,X), dtype = complex)
    # num of samples
    for n in range(Y):
        for o in range(X):
            #Sumas
            sV = 0.0
            #Sumatorias
            for k in range(Y):
                for p in range(X):
                    #Se extrae pixel
                    V = arr[k][p]
                    #este se multiplicaria por sr ?
                    wy = (float(n*k)/float(Y))
                    wx = (float(o*p)/float(X))
                    ee = np.exp(-1j*2.0*np.pi*(wy+wx))
                    #aplicacion formula a suma
                    sV += ee*V
            #normalizacion ?
            sol[n][o] = sV
    return sol

fIMG = fou(arrg,YY,XX)
#go1 = np.fft.fft2(arrg)

'''
for i in range(YY):
    for j in range(XX):
        print "OK"
        print fIMG[i][j]
        print go1[i][j]
'''

def ifouG(FT,Y,X):
    #Array donde se guardara info fourierizados
    sol = np.zeros((Y,X))
    # num of samples
    for n in range(Y):
        for o in range(X):
            #Sumas de cada color de pixel
            sV = 0.0
            #Sumatorias
            for k in range(Y):
                for p in range(X):
                    #Se extraen colores de pixel
                    V = FT[k][p]

                    wy = (float(n*k)/float(Y))
                    wx = (float(o*p)/float(X))
                    ee = np.exp(1j*2.0*np.pi*(wy+wx))
                    #aplicacion formula a suma de gauss
                    sV += ee*V

            sol[n][o] = (sV/float(X)/float(Y)).real

    return sol

okk = ifouG(fIMG,YY,XX)
gi = np.fft.ifft2(fIMG)
'''
for i in range(YY):
    for j in range(XX):
        print "OK"
        print okk[i][j]
        print gi[i][j]
'''

#Display image
#plt.imshow(okk, cmap = plt.get_cmap('gray'))
plt.imshow(okk)
plt.savefig("OKK.png")
plt.imshow(arrg)
#plt.show()
plt.savefig("ARRG.png")
