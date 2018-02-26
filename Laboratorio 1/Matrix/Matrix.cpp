/**
* author: Sebastian Peña
*/
#include <iostream>		// cin, cout
#include <stdio.h>		// printf, scanf
#include <array>		// fill
#include <time.h>		// time_t, clock, CLOCKS_PER_SEC

using namespace std;

const int SIZE = 4;

void printMatrix(int matrix[SIZE][SIZE]) {
	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++) {
			printf("%d ", matrix[i][j]);
		}
		printf("\n");
	}
}

int** createMatrix(int value) {
	int** M = new int*[SIZE];
	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++)
			M[i][j] = value;
	}
	return M;
}


int main() {

	int*[SIZE] m = createMatrix(2);
	printMatrix(matrix);
	system("pause");
	return 0;
}
