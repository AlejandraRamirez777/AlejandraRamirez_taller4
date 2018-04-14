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
(YY, XX, capas) = np.shape(arr)

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

#Fourier para gausiana 2d
#Param: gausiana a transformar, dimensiones Y y X de esta
#Return: transformada de Fourier para gausiana
def fouG(arrGA,Y,X):
    #Array donde se guardara info fourierizados
    sol = np.zeros((Y,X,4), dtype = complex)
    # num of samples
    for n in range(Y):
        for o in range(X):
            #Contador de suma
            g = 0.0
            #Sumatorias
            for k in range(Y):
                for p in range(X):
                    GG = arrGA[k][p]

                    wy = (float(n*k)/float(Y))
                    wx = (float(o*p)/float(X))
                    ee = np.exp(-1j*2.0*np.pi*(wy+wx))
                    #aplicacion formula a suma de gauss
                    g += GG*ee

            sol[n][o][0] = g
            sol[n][o][1] = g
            sol[n][o][2] = g
            sol[n][o][3] = g

    return sol

#Fourier 2d de imagen
#Param: array de imagen PNG a transformar, dimensiones Y y X de esta
#Return: transformada de fourier de imagen
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

                    wy = (float(n*k)/float(Y))
                    wx = (float(o*p)/float(X))
                    ee = np.exp(-1j*2.0*np.pi*(wy+wx))
                    #aplicacion formula a suma
                    sR += ee*R
                    sG += ee*G
                    sB += ee*B
                    sf += ee*f

            sol[n][o][0] = sR
            sol[n][o][1] = sG
            sol[n][o][2] = sB
            sol[n][o][3] = sf
    return sol

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

#Aplicar trans Fourier a gausiana
fGA = fouG(ga,YY,XX)

#Aplicar transformada de Fourier a imagen
fIM = fou(arr,YY,XX)

#Convolucion - Multiplicacion de transformadas (gausiana e imagen)
conv = fGA*fIM

#Transformada de Fourier inversa 2d
#Param:array fourierizado, dimensiones Y y X de este
#Return:transformada inversa de Fourier
def ifouG(FT,Y,X):
    #Array donde se guardara info fourierizados
    sol = np.zeros((Y,X,4), dtype = int)
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
                    (R,G,B,f) = FT[k][p][:]

                    wy = (float(n*k)/float(Y))
                    wx = (float(o*p)/float(X))
                    ee = np.exp(1j*2.0*np.pi*(wy+wx))
                    
                    sR += ee*R
                    sG += ee*G
                    sB += ee*B
                    sf += ee*f

            sol[n][o][0] = int((sR.real/float(X)/float(Y))+0.5)
            sol[n][o][1] = int((sG.real/float(X)/float(Y))+0.5)
            sol[n][o][2] = int((sB.real/float(X)/float(Y))+0.5)
            sol[n][o][3] = int((sf.real/float(X)/float(Y))+0.5)

    return sol

#Inversa de Convolucion
invC = ifouG(conv,YY,XX)

#Reubicacion de array resultante
final = trans(invC,YY,XX,cc[0],cc[1])

#Save image
#Se utiliza cmap para que imshow lea imagen como escala de grises
plt.imshow(final, cmap = plt.get_cmap('gray'))
plt.savefig("suaveColor.png")
