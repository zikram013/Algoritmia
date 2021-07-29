import time
import numpy as np


# Complexity: O(M*N*L) = O(n^3) assuming M=N=L
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


def mat_mult_DaC(A, B):
    if len(A) <= 16:
        return mat_mult(A, B)
    else:
        assert len(A) == len(B)
        assert len(A) % 2 == 0
        # A cuadrants
        a11 = A[:(len(A) // 2), :(len(A) // 2)]
        a12 = A[:(len(A) // 2), (len(A) // 2):]
        a21 = A[(len(A) // 2):, :(len(A) // 2)]
        a22 = A[(len(A) // 2):, (len(A) // 2):]

        # B cuadrants
        b11 = B[:(len(B) // 2), :(len(B) // 2)]
        b12 = B[:(len(B) // 2), (len(B) // 2):]
        b21 = B[(len(B) // 2):, :(len(B) // 2)]
        b22 = B[(len(B) // 2):, (len(B) // 2):]

        Ac = np.array([[a11, a12], [a21, a22]])
        Bc = np.array([[b11, b12], [b21, b22]])

        # C11 = A11*B11 + A12*B21
        Cc = []
        for i in range(2):
            row = []
            for j in range(2):
                Cij = mat_mult_DaC(Ac[i][0], Bc[0][j]) \
                      + mat_mult_DaC(Ac[i][1], Bc[1][j])
                row.append(Cij)
            Cc.append(row)

        # result = C11 C12
        #          C21 C22
        result = np.vstack((np.hstack((Cc[0][0], Cc[0][1])),
                            np.hstack((Cc[1][0], Cc[1][1]))))

        return result





def mat_mult_strassen(A, B):
    if len(A) <= 16:
        return mat_mult(A, B)
    else:
        assert len(A) == len(B)
        assert len(A) % 2 == 0
        # A cuadrants
        a11 = A[:(len(A) // 2), :(len(A) // 2)]
        a12 = A[:(len(A) // 2), (len(A) // 2):]
        a21 = A[(len(A) // 2):, :(len(A) // 2)]
        a22 = A[(len(A) // 2):, (len(A) // 2):]

        # B cuadrants
        b11 = B[:(len(B) // 2), :(len(B) // 2)]
        b12 = B[:(len(B) // 2), (len(B) // 2):]
        b21 = B[(len(B) // 2):, :(len(B) // 2)]
        b22 = B[(len(B) // 2):, (len(B) // 2):]

        # m1 = mat_mult_strassen((a11+a22), (b11+b22))
        #
        # m2 = mat_mult_strassen(a21+a22, b11)
        #
        # m3 = mat_mult_strassen(a11, b12-b22)
        #
        # m4 = mat_mult_strassen(a22, b21-b11)
        m1 = mat_mult_strassen(add_mat(a11, a22),
                               add_mat(b11, b22))

        m2 = mat_mult_strassen(add_mat(a21, a22),
                               b11)
        m3 = mat_mult_strassen(a11,
                               subtract_mat(b12, b22))
        m4 = mat_mult_strassen(a22,
                               subtract_mat(b21, b11))
        m5 = mat_mult_strassen(add_mat(a11, a12),
                               b22)
        m6 = mat_mult_strassen(subtract_mat(a21, a11),
                               add_mat(b11, b12))
        m7 = mat_mult_strassen(subtract_mat(a12, a22),
                               add_mat(b21, b22))

        C11 = add_mat(add_mat(m1, m4),
                      subtract_mat(m7, m5))
        C12 = add_mat(m3, m5)
        C21 = add_mat(m2, m4)
        C22 = add_mat(subtract_mat(m1, m2),
                      add_mat(m3, m6))

        # result = C11 C12
        #          C21 C22
        result = np.vstack((np.hstack((C11, C12)),
                            np.hstack((C21, C22))
                            ))

        return result


# mat = A + B
def add_mat(A, B):
    assert len(A) == len(B) == len(B[0]) == len(A[0])
    N = len(A)
    mat = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            mat[i][j] = A[i][j] + B[i][j]
    return mat


# mat = A - B
def subtract_mat(A, B):
    assert len(A) == len(B) == len(B[0]) == len(A[0])
    N = len(A)
    mat = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            mat[i][j] = A[i][j] - B[i][j]
    return mat

def rand_mat(exp):
    return np.random.randint(30, size=(2 ** exp, 2 ** exp))


def test():
    A = np.matrix([[1, 2], [3, 4]])
    B = np.matrix([[2, 1], [4, 3]])

    tini = time.time()
    # print(mat_mult(A, B))
    print(mat_mult_DaC(A, B))
    elapsed = time.time() - tini
    print(str("{0:.4f}".forcmat(elapsed)))


def test_random():
    A = rand_mat(9)
    B = rand_mat(9)

    tini = time.time()
    # C = A.dot(B)
    mat_mult(A, B)
    #mat_mult_strassen(A, B)
    mat_mult_DaC(A, B)
    elapsed = time.time() - tini
    print(str("{0:.4f}".format(elapsed)))


test_random()

# test(), n=5
# N^3:      0.0266
# DaC (v2): 0.5592
# NP.dot:   0.0000
# test(), n=8
# N^3:      12.265
# DaC (v2): 12.740
# NP.dot:    0.024