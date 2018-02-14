# Programa que suma y multiplica matrices de 500x500 y calcula el tiempo del proceso.

import time
import random

def print_matrix(matrix):
    for row in matrix:
        print(row)


n_rows = 500
n_cols = 500
X = []
num_rand = random.randint(0, 100)
for i in range(n_rows):
    X.append([]) # agrega filas
    for j in range(n_cols):
        X[i].append(num_rand) # agrega valor
        num_rand = random.randint(0, 100)

#print("X:")
#print_matrix(X)


"""n_rows = 10
n_cols = 10"""
Y = []
num_rand = random.randint(0, 100)
for i in range(n_rows):
    Y.append([]) # agrega filas
    for j in range(n_cols):
        Y[i].append(num_rand) # agrega valor en
        num_rand = random.randint(0, 100)

#print("Y:")
#print_matrix(Y)

result = []
for i in range(len(X)):
    result.append([]) # agrega filas
    for j in range(len(Y[0])):
        result[i].append(0) # agrega un 0

#print("result:")
#print_matrix(result)

#print("-------------------------------------------------------------------------------")

t0 = time.clock()
for row in range(len(X)):
    for col in range(len(X[0])):
        result[row][col] = X[row][col] + Y[row][col]
tf = time.clock()

print("Add:")
#print_matrix(result)
print("time: {} seconds process time".format(tf - t0))


print("-------------------------------------------------------------------------------")

t0 = time.clock()
# Filas X
for i in range(len(X)):
    # Columnas Y
    for j in range(len(Y[0])):
        # Filas Y, sumando
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
tf = time.clock()

print("Multiplication:")
#print_matrix(result)
print("time: {} seconds process time".format(tf - t0))