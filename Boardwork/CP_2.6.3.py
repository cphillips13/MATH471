"""
Corey Phillips
Started 10/27/22
Last updated 10/27/22
Stored in MATH471 repo on github.com/cphillips13

Question 2.6.3 & 2.6.4
Use Algorithm 2.6 to solve the following system of equations.
     
|6 1 0 0| |x1|   |8 |
|2 4 1 0| |x2| = |13| 
|0 1 4 2| |x3|   |22|
|0 0 1 6| |x4|   |27|
     
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

def __checkSquare(matrixA, shape):
    if(shape[0] == shape[1]):
        print('matrixA is square! It is a ', shape[0],' by ', shape[1], ' matrix!')
        return True
    elif(shape[0] != shape[1]):
        print('matrixA is not square! It is a ', shape[0],' by ', shape[1], ' matrix!')
        return False

matrixA = np.matrix([[6.0,1.0,0,0], [2.0,4.0,1.0,0], [0,1.0,4.0,2.0], [0,0,1.0,6.0]])
solMatrixA = np.matrix([8.0,13.0,22.0,27.0])
shape = np.shape(matrixA)

def checkEdge(matrixA, shape):
    retval = True
    for i in range(int(shape[0]/2)):
        diag = np.diagonal(matrixA,i+2, 0, 1)
        diag2 = np.diagonal(matrixA,i+2, 1, 0)
        if(diag.any() or diag2.any() != 0):
            retval = False                 
    return retval

"""
|a c 0 |
|b a c | 
|0 b a |

|a c 0 0|
|b a c 0| 
|0 b a c|
|0 0 b a| 
"""

def arith(matrixA, shape, solMatrixA):
    #print(matrixA)
    diagA = np.copy(np.diag(matrixA)) #center
    diagB = np.copy(np.diag(matrixA, -1)) #bottom
    diagC = np.copy(np.diag(matrixA, 1)) #top
    solMatrixAFinal = np.copy(solMatrixA)
    retMatrix = matrixA.copy()

    #pass right

    
    for i in range(shape[0]-1):
        temp = diagB[i]
        diagB[i] = diagB[i] - diagA[i] * (temp / diagA[i])
        diagA[i+1] = diagA[i+1] - diagC[i] * (temp / diagA[i])
        solMatrixAFinal[0,i+1] = solMatrixAFinal[0, i+1] - solMatrixAFinal[0,i] * (temp / diagA[i]) 

    print(diagA)
    print(diagC)
    print(solMatrixAFinal)

    for i in range(shape[0]-1):
        temp = diagC[shape[0]-2-i]
        diagC[shape[0]-2-i] = diagC[shape[0]-2-i] - diagA[shape[0]-1-i] * (temp / diagA[shape[0]-1-i])
        solMatrixAFinal[0,shape[0]-2-i] = solMatrixAFinal[0, shape[0]-2-i] - solMatrixAFinal[0, shape[0]-1-i] * (temp / diagA[shape[0]-1-i])
   
    print(diagA)
    print(diagC)
    print(solMatrixAFinal)

    for i in range(shape[0]):
        temp = diagA[i]
        diagA[i] = diagA[i]/temp
        solMatrixAFinal[0,i] = solMatrixAFinal[0, i] / temp 
    

    print(solMatrixAFinal)
    return retMatrix


isSquare = __checkSquare(matrixA, shape)
print(checkEdge(matrixA,shape))
arith(matrixA, shape, solMatrixA)

