"""
Corey Phillips
Started 10/27/22
Last updated 11/01/22
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

#Checks if the matrix is n x n, takes in np.matrix and np.shape
def __checkSquare(shape):
    retval = False
    #If n = m, the matrix is square
    if(shape[0] == shape[1]):
        print('matrixA is square! It is a ', shape[0],' by ', shape[1], ' matrix!')
        retval = True
    #If n != m, the matrix cannot be square.
    else:
        print('matrixA is not square! It is a ', shape[0],' by ', shape[1], ' matrix!')
    return retval

#Checks the corners of our matrix and checks if they are zeros. Takes in np.matrix and np.shape
def checkEdge(matrixA, shape):
    retval = True
    #Checks the diagonals that aren't on the main.
    for i in range(int(shape[0]/2)):
        diag = np.diagonal(matrixA,i+2, 0, 1)
        diag2 = np.diagonal(matrixA,i+2, 1, 0)
        if(diag.any() or diag2.any() != 0):
            retval = False                 
    return retval

def diagDominant(matrixA, shape):
    diagA = np.copy(np.diag(matrixA)) #center
    diagB = np.copy(np.diag(matrixA, -1)) #bottom
    diagC = np.copy(np.diag(matrixA, 1)) #top
    
    retval = True
    if((abs(diagC[0]) >= abs(diagA[0])) or (abs(diagB[shape[0]-2]) >= abs(diagA[shape[0]-1]))):
        retval = False
    for i in range(shape[0] - 2):
        if(abs(diagA[i+1]) <= abs(diagB[i+1]) + abs(diagC[i+1])):
            retval = False
    return retval

#Perform the arithmetic for passing right on a matrix, makes the entries of diagB zero.
def __passRight(diagA, diagB, diagC, solMatrixAFinal, shape):
    for i in range(shape[0]-1):
        temp = diagB[i]
        diagB[i] = diagB[i] - diagA[i] * (temp / diagA[i])
        diagA[i+1] = diagA[i+1] - diagC[i] * (temp / diagA[i])
        solMatrixAFinal[0,i+1] = solMatrixAFinal[0, i+1] - solMatrixAFinal[0,i] * (temp / diagA[i]) 

#Perform the arithmetic for passing right on a matrix, makes the entries of diagC zero.
def __passLeft(diagA, diagC, solMatrixAFinal, shape):
    for i in range(shape[0]-1):
        temp = diagC[shape[0]-2-i]
        diagC[shape[0]-2-i] = diagC[shape[0]-2-i] - diagA[shape[0]-1-i] * (temp / diagA[shape[0]-1-i])
        solMatrixAFinal[0,shape[0]-2-i] = solMatrixAFinal[0, shape[0]-2-i] - solMatrixAFinal[0, shape[0]-1-i] * (temp / diagA[shape[0]-1-i])

#This scales diagA so that it will be 1 on all entries. 
def __scale(diagA, solMatrixAFinal, shape):
    for i in range(shape[0]):
        temp = diagA[i]
        diagA[i] = diagA[i]/temp
        solMatrixAFinal[0,i] = solMatrixAFinal[0, i] / temp 

#Takes in given matrix, the augmented side of the matrix, and its shape to solve matrix.    
def arith(matrixA, shape, solMatrixA):
    diagA = np.copy(np.diag(matrixA)) #center
    diagB = np.copy(np.diag(matrixA, -1)) #bottom
    diagC = np.copy(np.diag(matrixA, 1)) #top
    solMatrixAFinal = np.copy(solMatrixA)
    __passRight(diagA, diagB, diagC, solMatrixAFinal, shape)
    __passLeft(diagA, diagC, solMatrixAFinal, shape)
    __scale(diagA, solMatrixAFinal, shape)
    return solMatrixAFinal

matrixA = np.matrix([[6.0,1.0,0,0], [2.0,4.0,1.0,0], [0,1.0,4.0,2.0], [0,0,1.0,6.0]])
solMatrixA = np.matrix([8.0,13.0,22.0,27.0])


print("Matrix: \n", matrixA)
print("Augmeneted side of matrix: \n", solMatrixA)
shape = np.shape(matrixA)
isSquare = __checkSquare(shape)
isDiagDom = diagDominant(matrixA, shape)
print("Is matrixA diagonally domninant?: ", isDiagDom)
checkEdgeZeros = checkEdge(matrixA, shape)

if(isSquare == True and checkEdgeZeros == True and isDiagDom == True):
    print("Here is the solution of the matrix: \n" , arith(matrixA, shape, solMatrixA))
else:
    print('Matrix is not square or the corners are not zero. Check again.')