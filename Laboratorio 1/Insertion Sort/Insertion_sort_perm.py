import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations

def insertion_sort(arr):
    """
    Retorna una tupla con la cantidad de instrucciones, comparaciones y swaps (intercambios)
    """
    ins = 0  # instrucciones
    comp = 0  # comparaciones
    swaps = 0  # swaps (intercambios)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        ins += 3    # i = ; key =; j = ;
        comp += 1    # key < arr[j];
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]   # Desplaza hacia la derecha el valor
            swaps += 1
            j -= 1
            ins += 3    # arr[j+1] =; j =; j >=;
        arr[j+1] = key; ins += 1
    return ins, comp, swaps


instructions = []   # Lista para manejar las instrucciones
comparisons = []    # Lista para manejar las comparaciones
swaps = []      # Lista para manejar los swaps
max = 9    # Cantidad maxima de permutaciones, mediante experimentacion el maximo no deberia ser mayor a 10

print("N \tNumber of permutations")
for n in range(1, max):

    # Lista que guarda todas las permutaciones, cada permutacion es una tupla
    permut = list(permutations(range(n)))
    #print(permut)
    print("{}\t{}".format(n, len(permut)))
    i_aux = []
    c_aux = []
    s_aux = []
    for p in permut:
        p = list(p)
        #print(p)
        i, c, s = insertion_sort(p)
        #print("i: {}, c: {}, s: {}".format(i, c, s))
        i_aux.append(i)
        c_aux.append(c)
        s_aux.append(s)

    instructions.append(i_aux)
    comparisons.append(c_aux)
    swaps.append(s_aux)


def means(seq):
    """
    Retorna una lista con las medias de cada lista dentro de la secuencia
    """
    return [np.mean(s) for s in seq]


fig = plt.figure()
ax = plt.subplot(111)
x_axe = np.arange(1, max)
w = 0.2     # width

ins_means = means(instructions)
print()
ax.bar(x_axe, ins_means, w, color="r")

comp_means = means(comparisons)
ax.bar(x_axe+w, comp_means, w, color="g")

swaps_means = means(swaps)
ax.bar(x_axe+2*w, swaps_means, w, color="b")

ax.set_xticks(x_axe+w)
ax.set_xticklabels(x_axe)
ax.legend(["instructions", "comparisons", "swaps"])
ax.set_xlabel("Permutacion de N")

print(ins_means)
print(comp_means)
print(swaps_means)

plt.show()