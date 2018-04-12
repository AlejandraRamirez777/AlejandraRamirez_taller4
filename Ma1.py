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

#Calcula el centro de la imagen
#Param: dimensiones de la imagen Y,X
#Return: lista con los centros (cy,cx)
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

#Array donde se guardara gausiana
ga = np.zeros((YY,XX))

#Generar gausiana en base a imagen
for h in range(YY):
    for j in range(XX):
        ga[h][j] = gauss(j,h,wd,cc[1],cc[0])

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

#Aplicar transformada de Fourier a imagen
#fIMG = fou(arr,YY,XX)
#print fIMG
#print np.shape(fIMG)

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
#fouGA = fouG(YY,XX)

go4 = np.fft.fft2(ga)


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

'''
go9 = ifouG(fouGA,YY,XX)

for i in range(16):
    for j in range(16):
        print "GOR"
        print go7[i][j]
        print "GOM"
        print go9[i][j]
'''



#Display image
#plt.imshow(img)
#plt.show()
