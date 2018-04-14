import numpy as np
import matplotlib.pyplot as plt
import sys

#Info input by user en forma de lista
#[0] nombre del .py - [1] nombre imagen - [2] ancho de gausiana
inn = sys.argv
name = inn[1]
des = inn[2]

# covertir imagen del input a un array
arr = plt.imread(name)

#Dimensiones imagen
(YY, XX, capas) = np.shape(arr)

#Transformar imagen a grayscale
#Param: array de imagen para convertir a grayscale
#Return: array de imagen en grayscale
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

#array de imagen en grayscale
arrg = rgb2gray(arr)

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

#Funcion para reubicar los resultados de transformada de fourier
#Param: array para reubicar contenido, dimensiones Y y X de este, centro del Array
#Return: mismo array con sus 4 cuadrantes reubicados diagonalmente
def trans(arra,Y,X,cy,cx):
    a = np.copy(arra)
    r = np.copy(arra)
    ccy = cy-1
    ccx = cx-1

    if(Y%2 == 0 and X%2 ==0):

        s1 = a[:cy,:cx]
        s2 = a[:cy,cx:X]
        s3 = a[cy:Y,:cx]
        s4 = a[cy:Y,cx:X]

        r[cy:Y,:cx] = s2
        r[:cy,:cx] = s4
        r[cy:Y,cx:X] = s1
        r[:cy,cx:X] = s3

    elif(Y%2 != 0 and X%2 !=0):
        s1 = a[:cy,:cx]
        s2 = a[:cy,cx:X]
        s3 = a[cy:Y,:cx]
        s4 = a[cy:Y,cx:X]

        r[ccy:Y,:ccx] = s2
        r[:ccy,:ccx] = s4
        r[ccy:Y,ccx:X] = s1
        r[:ccy,ccx:X] = s3

    elif(Y%2 != 0 and X%2 ==0):

        s1 = a[:cy,:cx]
        s2 = a[:cy,cx:X]
        s3 = a[cy:Y,:cx]
        s4 = a[cy:Y,cx:X]

        r[ccy:Y,:cx] = s2
        r[:ccy,:cx] = s4
        r[ccy:Y,cx:X] = s1
        r[:ccy,cx:X] = s3

    elif(Y%2 == 0 and X%2 !=0):

        s1 = a[:cy,:cx]
        s2 = a[:cy,cx:X]
        s3 = a[cy:Y,:cx]
        s4 = a[cy:Y,cx:X]

        r[cy:Y,:ccx] = s2
        r[:cy,:ccx] = s4
        r[cy:Y,ccx:X] = s1
        r[:cy,ccx:X] = s3

    return r

#Fourier 2d de imagen
#Param: array de imagen grayscale a transformar, dimensiones Y y X de esta
#Return: transformada de fourier de imagen
def fou(arr,Y,X):
    #Array donde se guardara info de color de pixeles fourierizados
    sol = np.zeros((Y,X), dtype = complex)
    # num of samples
    for n in range(Y):
        for o in range(X):
            #Suma
            sV = 0.0
            #Sumatorias
            for k in range(Y):
                for p in range(X):
                    #Se extrae pixel
                    V = arr[k][p]

                    wy = (float(n*k)/float(Y))
                    wx = (float(o*p)/float(X))
                    ee = np.exp(-1j*2.0*np.pi*(wy+wx))
                    #aplicacion formula a suma
                    sV += ee*V

            sol[n][o] = sV
    return sol

#Aplicar transformada de Fourier a imagen
fIM = fou(arrg,YY,XX)

#print np.max(fIM)
#print np.min(fIM)
#print np.mean(fIM)

#Deja pasar altas
def highS(FT,Y,X):
    for i in range(Y):
        for j in range(X):
            if(FT[i][j]<1):
                FT[i][j] = 0.0
            else:
                FT[i][j] = FT[i][j]
    return FT

#Deja pasar bajas
def lowS(FT,Y,X):
    for i in range(Y):
        for j in range(X):
            if(FT[i][j]>1):
                FT[i][j] = 0.0
            else:
                FT[i][j] = FT[i][j]
    return FT


#Transformada de Fourier inversa 2d
#Param:array fourierizado, dimensiones Y y X de este
#Return:transformada inversa de Fourier
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

                    sV += ee*V

            sol[n][o] = (sV/float(X)/float(Y)).real

    return sol

if(des == "altas" or des == "alto"):
    High = highS(fIM,YY,XX)
    invH = ifouG(High,YY,XX)
    #Save image
    #Se utiliza cmap para que imshow lea imagen como escala de grises
    plt.imshow(invH, cmap = plt.get_cmap('gray'))
    #plt.savefig("altas.png")
    plt.show()

if(des == "bajas" or des == "bajo"):
    Low = lowS(fIM,YY,XX)
    invL = ifouG(Low,YY,XX)
    #Save image
    #Se utiliza cmap para que imshow lea imagen como escala de grises
    plt.imshow(invL, cmap = plt.get_cmap('gray'))
    #plt.savefig("altas.png")
    plt.show()

#Reubicacion de array resultante
#final = trans(inv,YY,XX,cc[0],cc[1])

#Save image
#Se utiliza cmap para que imshow lea imagen como escala de grises
#plt.imshow(inv, cmap = plt.get_cmap('gray'))
#plt.savefig("suave.png")
#plt.show()
