import numpy as np
import pylab as pl
import time
# %matplotlib inline


def print_matrix(matrix):
    for row in matrix:
        print(row)


def create_matrix(size, value):
    # Normal:
    """m = []
    for i in range(size):
        m.append([])
        for j in range(size):
            m[i].append(value)"""
    # Pythonic:
    m = [[value for col in range(size)] for row in range(size)]
    return m


def multiply_matrices(A, B):
    result = [[0 for row in range(len(B[0]))] for col in range(len(A))]

    for i in range(len(A)):    # Filas de A
        for j in range(len(B[0])): # Columnas de B
            for k in range(len(A[0])): # Columnas de A
                result[i][j] += A[i][k] * B[k][j]
    return result

test = 10   # Cantidad de pruebas que se haran por tamaño
max = 100   # Cantidad maxima de tamaños para matrices cuadradas que se multiplicaran
times = []  # Lista para manejar los tiempos

for n in range(2, max+1):    # n = size
    m1 = create_matrix(n, 1)
    m2 = create_matrix(n, 2)

    sum = 0
    for t in range(test):
        t0 = time.clock()
        mult = multiply_matrices(m1, m2)
        tf = time.clock()
        aux = (tf-t0) / (2*(n**3))
        sum += aux

    times.append(sum/test)  # Avg
    print("Matrix {}: {}".format(n, times[n-2]))

arange = np.arange(1, max+1)
pl.ylabel("Tiempo")
pl.xlabel("Tamaño de la matriz")
pl.plot(arange, times)
pl.show()

""" ULTIMAS 11 MATRICES:
Matrix 90: 2.153654385129391e-07
Matrix 91: 2.078683319282993e-07
Matrix 92: 2.0674274013042759e-07
Matrix 93: 2.0739707843361772e-07
Matrix 94: 2.0808728015355274e-07
Matrix 95: 2.0656738416048568e-07
Matrix 96: 2.0539704752681887e-07
Matrix 97: 2.0647072020185035e-07
Matrix 98: 2.0892018833611126e-07
Matrix 99: 2.1130385913786829e-07
Matrix 100: 2.088838468833458e-07
"""