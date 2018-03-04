import numpy as np
import pylab as pl
import time
# %matplotlib inline


test = 10   # Cantidad de pruebas que se haran por tamaño
max = 100   # Cantidad maxima de tamaños para matrices cuadradas que se multiplicaran
times = []  # Lista para manejar los tiempos

for n in range(2, max+1):    # n = size
    m1 = np.full((n,n), 1)
    m2 = np.full((n,n), 2)

    sum = 0
    for t in range(test):
        t0 = time.clock()
        mult = np.matmul(m1, m2)
        tf = time.clock()
        aux = (tf - t0) / (2 * (n ** 3))
        sum += aux

    times.append(sum / test)  # Avg
    print("Matrix {}: {}".format(n, times[n - 2]))

arange = np.arange(1, max)
pl.ylabel("Tiempo")
pl.xlabel("Tamaño de la matriz")
pl.plot(arange, times)
pl.show()

""" ULTIMAS 11 MATRICES:
Matrix 90: 4.046785617496968e-10
Matrix 91: 4.077658970147291e-10
Matrix 92: 4.0939537358203187e-10
Matrix 93: 4.059218825129e-10
Matrix 94: 4.1733823586877676e-10
Matrix 95: 4.01545261251485e-10
Matrix 96: 4.0777305401093424e-10
Matrix 97: 3.9619034275247184e-10
Matrix 98: 4.300312817240802e-10
Matrix 99: 4.3508439504840573e-10
Matrix 100: 4.5503210893030184e-10
"""