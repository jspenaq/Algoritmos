"""
Contest: https://www.hackerrank.com/contests/cleverly-hidden-floyd-warshall/challenges/30-pointer
https://github.com/prakhar1989/Algorithms/blob/master/dp/floyd.py
http://www.programming-algorithms.net/article/45708/Floyd-Warshall-algorithm
https://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/
"""
inf = float("inf")

"""G = [
    [0, 40, 8, 10, inf, inf, inf, inf, inf, inf],
    [inf, 0, inf, inf, 6, inf, 10, inf, inf, inf],
    [inf, 4, 0, 12, inf, 2, inf, inf, inf, inf],
    [inf, inf, inf, 0, inf, 1, inf, inf, inf, inf],
    [inf, inf, 2, inf, 0, 2, 7, inf, inf, inf],
    [inf, inf, inf, inf, inf, 0, inf, 4, 3, inf],
    [inf, inf, inf, inf, inf, inf, 0, 20, inf, 1],
    [inf, inf, inf, inf, 0, inf, inf, 0, inf, 20],
    [inf, inf, inf, 6, inf, inf, 10, inf, 0, 2],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, 0]
]"""



def floydWarshall(graph):
    n = len(graph)
    D = graph # D is a matrix of lengths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


def printFW(Dist):
    n = len(Dist)
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(n):
        for j in range(n):
            if(Dist[i][j] == inf):
                print("%7s," % ("INF"), end=("   "))
            else:
                print("%7d," % (Dist[i][j]), end=("   "))
            if j == n-1:
                print("")


N = int(input())
D = int(input())

G = [[inf for i in range(N)] for i in range(N)]
for i in range(N):
    line = input()
    j = 0
    for c in line:
        if i == j: G[i][j] = 0
        elif c == "Y": G[i][j] = 1
        else: G[i][j] = inf
        j += 1

# print(G)
mat = floydWarshall(G)
print(mat)
import numpy as np
x = np.matrix(mat)
m = x.max()
print(m*D)

