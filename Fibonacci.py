# Programa para comparar tiempos que toma calcular numeros de Fibonacci de manera iterativa y recursiva

import numpy as np
import pylab as pl
import time

def fiboRec(n):
    """
    Recursive
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fiboRec(n-1) + fiboRec(n-2)

def fiboIte(n):
    """
    Iterative
    """
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b


ns = np.arange(0,36)
listR = []
listI = []

for i in ns:
    t0 = time.clock()
    k = fiboRec(i)
    tf = time.clock()
    print("fiboRec({}): {}, time: {} seconds process time".format(i, k, tf - t0))
    listR.append(tf - t0)

    t0 = time.clock()
    k = fiboIte(i)
    tf = time.clock()
    print("fiboIte({}): {}, time: {} seconds process time".format(i, k, tf - t0))
    listI.append(tf - t0)
    print("......")

pl.ylabel("Tiempo")
pl.xlabel('Tamaño')
pl.plot(ns, listR, ns, listI)
pl.savefig("Figura_final.png")
pl.show()