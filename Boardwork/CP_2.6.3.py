"""
Corey Phillips
Started 10/27/22
Last updated 10/27/22
Stored in MATH471 repo on github.com/cphillips13

Question 2.6.3 & 2.6.4
Use Algorithm 2.6 to solve the following system of equations.
     
|6 1 0 0| |x1|   |pi/9     |
|2 4 1 0| |x2| = |sqrt(3)/2| 
|0 1 4 2| |x3|   |sqrt(3)/2|
|0 0 1 6| |x4|   |-pi/9    |
     
You should get the solution x = (1,2,3,4)^T

Algorithm 2.6:

a11x1 + a12x2 + ... + a1nxn = f1
a21x1 + a22x2 + ... + a2nxn = f2
.                     .        .
.                     .        .
.                     .        .
an1x1 + an2x2 + ... + annxn = fn

"""

import numpy as np
import math

matrixA = np.matrix([[6,1,0,0, np.pi/9], [2,4,1,0, np.sqrt(3)/2], [0,1,4,2, np.sqrt(3)/2], [0,0,1,6, np.pi/-9]])
shape = np.shape(matrixA)

def __checkSquare(matrixA, shape):
    if(shape[0] == shape[1]-1):
        print('matrixA is square! It is a ', shape[0],' by ', shape[1]-1 , ' matrix!')
        return True
    elif(shape[0] != shape[1]-1):
        print('matrixA is not square! It is a ', shape[0],' by ', shape[1], ' matrix!')
        return False

def checkUpperCorner(matrixA, shape):
    x = __checkSquare(matrixA,shape)
    if(x == True):
        for i in range(int(shape[0]/2)):
            for j in range(int(shape[0]/2)):
                print(matrixA[i, j + i + 2])
        print('yes')
        return 0
    elif(x == False):
        print('no')
        return 0

checkUpperCorner(matrixA, shape)
#use np.matrix
#np.linalg.solve