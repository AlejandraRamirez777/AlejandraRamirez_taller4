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
#Param:coordenada x, y y el ancho
#Return:punto de gausiana resultante
def gauss(x,y,anc):
    c = anc
    a = 1/float(c*c*2*np.pi)
    ff = x*x/float(2*c*c)
    gg = y*y/float(2*c*c)
    ee = np.exp(-(ff+gg))
    sol = a*ee
    return sol

#Array donde se guardara gausiana
ga = np.zeros((YY,XX))
#print ga

#Generar gausiana en base a imagen
for h in range(YY):
    for j in range(XX):
        ga[h][j] = gauss(h,j,wd)

#print ga


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

#go1 = np.fft.fft2(arr)
#print go1
#print np.shape(go1)
#print type(go1)

#go2 = fftpack.fft2(arr)
#print go1
#print np.shape(go2)
#print type(go1)

#go3 = fou(arr,YY,XX)
#print np.shape(go3)
#print type(go3)
#print go3

'''
for i in range(16):
    for j in range(16):
        print "Img"
        print arr[i][j]
        print "GO1"
        print go1[i][j]
        print "GO3"
        print go3[i][j]
'''





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
            for k in range(Y-1):
                for p in range(X-1):
                    #este se multiplicaria por sr
                    wy = (float(n*k)/float(Y))
                    wx = (float(o*p)/float(X))
                    ee = np.exp(-1j*2*np.pi*(wy+wx))
                    #aplicacion formula a suma de gauss
                    g+=gauss(p,k,wd)*ee

            sol[n][o] = g

    return sol

#Array de valores para la gausiana correspondiente
gin = np.zeros((YY,XX))

for i in range(YY):
    for j in range(XX):
        gin[i][j] = gauss(i,j,wd)

#Aplicar trans Fourier a gausiana
fouGA = fouG(XX,YY)


#print gin
#print np.shape(gin)

go4 = np.fft.fft2(gin)
#print go4
#print np.shape(go4)
#print type(go1)

#go5 = fouG(XX,YY)
#print go5
#print np.shape(go5)


#Fourier Inversa para gauss
def ifouG(FT,Y,X):
    #Array donde se guardara info fourierizados
    sol = np.zeros((Y,X), dtype = complex)
    # num of samples
    for n in range(Y):
        for o in range(X):
            #Contador de suma
            g = 0.0
            #Sumatorias
            for k in range(Y-1):
                for p in range(X-1):
                    #este se multiplicaria por sr
                    wy = (float(n*k)/float(Y))
                    wx = (float(o*p)/float(X))
                    ee = np.exp(1j*2*np.pi*(wy+wx))
                    #aplicacion formula a suma de gauss
                    g += FT[k][p]*ee

            sol[n][o] = g

    return sol

go7 = np.fft.ifft2(go4)
go9 = ifouG(fouGA,YY,XX)

for i in range(16):
    for j in range(16):
        print "GOR"
        print go7[i][j]
        print "GOM"
        print go9[i][j]


#Display image
#plt.imshow(img)
#plt.show()
