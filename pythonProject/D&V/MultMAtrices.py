"""
Multiplicacion normal de matrices
import numpy as np
def mat_mult(A, B):
    # A has shape (M,N)
    # B has shape (N,L)
    M = len(A)
    N = len(A[0])


    assert N == len(B)
    L = len(B[0])
    result = np.zeros((M, L))

    for i in range(M):
        for j in range(L):
            cell = 0
            for k in range(N):
                cell += A[i][k] * B[k][j]
            result[i][j] = cell
    return result

"""
import time
import numpy as np


def rand_mat(exp):
    return np.random.randint(30, size=(2 ** exp, 2 ** exp))


def mat_mult_DaC(A, B):
    if len(A) == 16:
        return mat_mult(A, B)

    # Cuatro caudrantes de A
    a11 = A[:(len(A) // 2), :(len(A) // 2)]
    a12 = A[:(len(A) // 2), (len(A) // 2):]
    a21 = A[(len(A) // 2):, :(len(A) // 2)]
    a22 = A[(len(A) // 2):, (len(A) // 2):]

    # Cuatro cuadrantes de B
    b11 = B[:(len(B) // 2), :(len(B) // 2)]
    b12 = B[:(len(B) // 2), (len(B) // 2):]
    b21 = B[(len(B) // 2):, :(len(B) // 2)]
    b22 = B[(len(B) // 2):, (len(B) // 2):]

    Ac = np.array([[a11, a12], [a21, a22]])
    Bc = np.array([[b11, b12], [b21, b22]])

    Cc = []

    for i in range(2):
        row = []
        for j in range(2):
            Cij = mat_mult_DaC(Ac[i][0], Bc[0][j]) + mat_mult_DaC(Ac[i][1], Bc[1][j])
            row.append(Cij)
        Cc.append(row)

    result = np.vstack((np.hstack(Cc[0][0], Cc[0][1]) ,np.hstack(Cc[1][0],Cc[1][1])))
    return result


def mat_mult(A, B):
    # A has shape (M,N)
    # B has shape (N,L)
    M = len(A)
    N = len(A[0])

    assert N == len(B)
    L = len(B[0])
    result = np.zeros((M, L))

    for i in range(M):
        for j in range(L):
            cell = 0
            for k in range(N):
                cell += A[i][k] * B[k][j]
            result[i][j] = cell
    return result


def test_random():
    A = rand_mat(9)
    print(A)
    B = rand_mat(9)

    tini = time.time()
    # C = A.dot(B)
    mat_mult(A, B)
    #mat_mult_strassen(A, B)
    mat_mult_DaC(A, B)
    elapsed = time.time() - tini
    print(str("{0:.4f}".format(elapsed)))


test_random()
