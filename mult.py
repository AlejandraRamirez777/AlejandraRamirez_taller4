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

#Transformar imagen a grayscale
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

arrg = rgb2gray(arr)

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

hh = trans(arrg,YY,XX,cc[0],cc[1])

plt.imshow(hh, cmap = plt.get_cmap('gray'))
plt.show()
