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

def __checkSquare(matrixA, shape):
    if(shape[0] == shape[1]):
        print('matrixA is square! It is a ', shape[0],' by ', shape[1], ' matrix!')
        return True
    elif(shape[0] != shape[1]):
        print('matrixA is not square! It is a ', shape[0],' by ', shape[1], ' matrix!')
        return False

def checkUpperCorner(matrixA, shape, isSquare):
    if(isSquare == True):
        for i in range(int(shape[0]/2)):
            for j in range(int(shape[0]/2)):
                if(i+j+2 < shape[0] and matrixA[i, j + i + 2] != 0):
                    return False
        return True
    else:
        return False

def checkLowerCorner(matrixA, shape, isSquare):
    if(isSquare == True):
        for i in range(int(shape[0]/2)):
            for j in range(int(shape[0]/2)):
                if(i+j+2 < shape[0] and matrixA[i+j+2, i] != 0):
                    return False
        return True
    else:
        return False

def run(matrixA, shape, isSquare):
    if(isSquare == True):
        UC = checkUpperCorner(matrixA, shape, isSquare)
        LC = checkLowerCorner(matrixA, shape, isSquare)
        print(LC)
        print(UC)
        matrixACopy = np.copy(matrixA)
        x = 0
        for i in range(shape[0]-1):
            y = matrixACopy[i,x]
            x = x+1
            for j in range(shape[1]):
                if(matrixACopy[i,j] != 0):
                    matrixACopy[i+1,j] = matrixACopy[i+1,j] - matrixACopy[i,j]*(matrixACopy[i+1,j]/y)
                    print(matrixACopy)
        return 1


    return 0 

matrixA = np.matrix([[6,1,0,0], [2,4,1,0], [0,1,4,2], [0,0,1,6]])
solMatrixA = np.matrix([np.pi/9,np.sqrt(3)/2,np.sqrt(3)/2,np.pi/-9])
#matrixA = np.matrix([[6,1,0,0,0, np.pi/9], [2,4,1,0,0, np.sqrt(3)/2], [0,1,4,2,0, np.sqrt(3)/2], [0,0,1,6,0, np.pi/-9]])
diag2 = np.diagonal(matrixA,1,0,1)
diag3 = np.diagonal(matrixA,0,1,0)
print(diag2)
print(diag3)


shape = np.shape(matrixA)
isSquare = __checkSquare(matrixA, shape)
#run(matrixA, shape, isSquare)

def checkEdge(matrixA, shape):
    for i in range(int(shape[0]/2)):
        diag = np.diagonal(matrixA,i+2, 0, 1)
        diag2 = np.diagonal(matrixA,i+2, 1, 0)
        if(diag.any() or diag2.any() != 0):
            return False
    return True

"""
|a c 0 |
|b a c | 
|0 b a |

|a c 0 0|
|b a c 0| 
|0 b a c|
|0 0 b a| 
"""
def arith(matrixA, shape):
    print(matrixA)
    diagA = np.diagonal(matrixA).copy
    diagB = np.diagonal(matrixA, 1, 1, 0).copy
    diagC = np.diagonal(matrixA, 1, 0, 1).copy

    retMatrix = matrixA.copy

    #pass right
    for i in range(int(shape[0]-1)):
        for j in range(int(shape[0]-1)):
            retMatrix[i+1][j] = retMatrix[i+1][j] - retMatrix[i][j]*(retMatrix[i+1][j]/retMatrix[i][j])

    print(retMatrix)




    return 0 
print(checkEdge(matrixA,shape))
arith(matrixA, shape)