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

#Aplicar trans Fourier a gausiana
fGA = fouG(YY,XX)

#Aplicar transformada de Fourier a imagen
fIM = fou(arrg,YY,XX)

#Convolucion - Multiplicacion de transformadas (gauss e imagen)
conv = fGA*fIM


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

#Inversa de Convolucion
invC = ifouG(conv,YY,XX)


#Display image
plt.imshow(invC, cmap = plt.get_cmap('gray'))
#plt.imshow(arrg)
plt.show()
