from tropical import *
from copy import *
import numpy as np

def mul(a, b):
    return np.matmul(a, b)

def identity(n):
    def id_(i, j):
        return 0 if i == j else -np.infty
    return [[tropical(id_(i,j)) for j in range(n)] for i in range(n)]

def matr_tropical(matr):
    matr = [[tropical(x) for x in r] for r in matr]
    return np.array(matr, dtype=object)

def eig(A, k):
    A_star = identity(A.shape[0])
    A_ = deepcopy(A)
    for _ in range(k):
        A_star = A_star + A_
        A_ = mul(A_, A)
    return A_star

e = -np.infty
matr = [[e, 15, e], [e, e, 14], [10, e, 12]]
matr = matr_tropical(matr)

print(eig(matr, 1))
