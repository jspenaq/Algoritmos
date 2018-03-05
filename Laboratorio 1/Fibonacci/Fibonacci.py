# Programa para comparar tiempos que toma calcular numeros de Fibonacci de manera iterativa y recursiva

import numpy as np
import pylab as pl
import time
import matplotlib as plt

def fiboIte(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b


timesI = []      # Lista para guardar los tiempos
max = 500       # Numero maximo de fibonacci que se calculará

for i in range(max+1):
    t0 = time.clock()
    k = fiboIte(i)
    tf = time.clock()
    print("fiboIte({}): {}, time: {} seconds process time".format(i, k, tf - t0))
    timesI.append(tf - t0)

arange = np.arange(1, max+1)
pl.ylabel("Tiempo")
pl.xlabel('Tamaño')
pl.plot(arange, timesI)
pl.show()
