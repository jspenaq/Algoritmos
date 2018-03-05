import numpy as np
import pylab as pl
import time
import matplotlib as plt

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

arange = np.arange(1, max)
pl.ylabel("Tiempo")
pl.xlabel("Tamaño de la matriz")
pl.plot(arange, times)
pl.show()

""" OUTPUT:
Matrix 2: 8.463757268059197e-07
Matrix 3: 4.544401208798563e-07
Matrix 4: 3.40473871919654e-07
Matrix 5: 2.897169760605961e-07
Matrix 6: 2.549576263464746e-07
Matrix 7: 2.356901043283207e-07
Matrix 8: 2.181260928505977e-07
Matrix 9: 4.1906100333086693e-07
Matrix 10: 8.07103893082125e-07
Matrix 11: 3.806734912960476e-07
Matrix 12: 2.8615051403333087e-07
Matrix 13: 2.242152626767251e-07
Matrix 14: 1.8484325440977416e-07
Matrix 15: 1.8945441454152456e-07
Matrix 16: 1.838723214260065e-07
Matrix 17: 1.8478073155340664e-07
Matrix 18: 1.8240158605084975e-07
Matrix 19: 3.671408565666605e-07
Matrix 20: 1.9274283596807523e-07
Matrix 21: 2.8504810530807497e-07
Matrix 22: 1.9630644717488858e-07
Matrix 23: 2.5848850249146154e-07
Matrix 24: 1.83188455656987e-07
Matrix 25: 2.553356962091804e-07
Matrix 26: 1.8356410537015546e-07
Matrix 27: 1.7302712063559398e-07
Matrix 28: 2.4564169276734204e-07
Matrix 29: 2.250254799705944e-07
Matrix 30: 2.1525415050117583e-07
Matrix 31: 2.4936179435476747e-07
Matrix 32: 2.2539149409802892e-07
Matrix 33: 2.1772060855900416e-07
Matrix 34: 2.3350727891035017e-07
Matrix 35: 1.6726244758193767e-07
Matrix 36: 2.0809595162758563e-07
Matrix 37: 2.018385158436632e-07
Matrix 38: 2.1398202545984455e-07
Matrix 39: 2.0763820122840716e-07
Matrix 40: 2.2701944991938422e-07
Matrix 41: 2.044064700880022e-07
Matrix 42: 2.264958528553037e-07
Matrix 43: 2.0758538013396196e-07
Matrix 44: 2.056179675761769e-07
Matrix 45: 2.1852462202142822e-07
Matrix 46: 2.027089164224459e-07
Matrix 47: 1.9849430601360849e-07
Matrix 48: 2.0498681619243755e-07
Matrix 49: 2.1824852735471685e-07
Matrix 50: 2.0549863123091507e-07
Matrix 51: 2.192366616899828e-07
Matrix 52: 1.9633588485203004e-07
Matrix 53: 2.1495548600535483e-07
Matrix 54: 2.175353410436923e-07
Matrix 55: 2.0836513634976652e-07
Matrix 56: 2.1097785762146978e-07
Matrix 57: 2.1251320698670696e-07
Matrix 58: 2.1628396059577295e-07
Matrix 59: 2.1015012422415e-07
Matrix 60: 2.1532767404916067e-07
Matrix 61: 2.137508224337275e-07
Matrix 62: 2.133542173783771e-07
Matrix 63: 2.0601233291398944e-07
Matrix 64: 2.0413778471113428e-07
Matrix 65: 2.135551381586592e-07
Matrix 66: 2.0866756754112842e-07
Matrix 67: 2.1620840406494907e-07
Matrix 68: 1.9985080716449382e-07
Matrix 69: 2.0218529507573546e-07
Matrix 70: 2.087107657615392e-07
Matrix 71: 2.0424835613740022e-07
Matrix 72: 2.112524454646955e-07
Matrix 73: 2.062084924414339e-07
Matrix 74: 2.1589087783444184e-07
Matrix 75: 2.0763877974346894e-07
Matrix 76: 2.0677109661622867e-07
Matrix 77: 2.152218371399138e-07
Matrix 78: 2.0876902142955204e-07
Matrix 79: 2.1039241408882087e-07
Matrix 80: 2.0725565498247513e-07
Matrix 81: 2.105080524202e-07
Matrix 82: 2.0858570498711396e-07
Matrix 83: 2.072573652136753e-07
Matrix 84: 2.0979961394210095e-07
Matrix 85: 2.024009744141609e-07
Matrix 86: 2.0622523360426574e-07
Matrix 87: 2.0677000541790653e-07
Matrix 88: 2.0671599979950323e-07
Matrix 89: 2.1122372017489457e-07
Matrix 90: 2.061136726183265e-07
Matrix 91: 2.1201686527277333e-07
Matrix 92: 2.1032269016202746e-07
Matrix 93: 2.0284301397291624e-07
Matrix 94: 2.146553796453551e-07
Matrix 95: 2.1219313402188551e-07
Matrix 96: 2.1384184356818295e-07
Matrix 97: 2.0728252484786874e-07
Matrix 98: 2.0737926107678866e-07
Matrix 99: 2.135841031469502e-07
Matrix 100: 2.097194710736467e-07
"""
