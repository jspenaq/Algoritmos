/**
* author: Sebastian Peña
*/
#include <iostream>		// cin, cout
#include <stdio.h>		// printf, scanf
#include <time.h>		// time_t, clock, CLOCKS_PER_SEC
#include <math.h>		// pow
#include <vector>		// vector, push_back

using namespace std;


void printMatrix(int** m, int rows, int cols) {
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			printf("%d ", m[i][j]);
		}
		printf("\n");
	}
}

int** createMatrix(int size, int value) {
	int** m;
	m = new int*[size];
	for (int i = 0; i < size; i++)
	{
		m[i] = new int[size];
		for (int j = 0; j < size; j++)
		{
			m[i][j] = value;
		}
	}
	return m;
}

int** multiplyMatrices(int** A, int** B, int rowsA, int colsA, int colsB) {
	int** result;
	result = new int*[rowsA];
	for (int i = 0; i < rowsA; i++)
	{
		result[i] = new int[colsB];
		for (int j = 0; j < colsB; j++)
		{
			int sum = 0;
			for (int k = 0; k < colsA; k++)
			{
				sum += A[i][k] * B[k][j];
			}
			result[i][j] = sum;
		}
	}
	return result;
}

int main() {

	clock_t t0, tf;    // Variables para medir el tiempo en milisegundos
	const int test = 10;  // Cantidad de pruebas que se haran por tamaño
	const int max = 100;   // Cantidad maxima de tamaños para matrices cuadradas que se multiplicaran
	vector<double> times;	// Lista para manejar los tiempos

	for (int n = 2; n < max+1; n++)
	{
		int** m1 = createMatrix(n, 1);
		int** m2 = createMatrix(n, 2);
		int** mult;
		double sum = 0;
		for (int i = 0; i < test; i++) {
			t0 = clock();
			mult = multiplyMatrices(m1, m2, n, n, n);
			tf = clock();
			double aux = ((double)(tf - t0) / CLOCKS_PER_SEC) / (2 * pow(n, 3.0));
			sum += aux;
		}
		times.push_back(sum / test); // Avg
		printf("Matrix %d: %+.5e\n", n, times[n-2]); // floats: %4.2f %+.0e %E \n
	}

	
	/* ULTIMAS 11 MATRICES:
	Matrix 90: +3.70370e-09
	Matrix 91: +2.58768e-09
	Matrix 92: +3.33895e-09
	Matrix 93: +3.10807e-09
	Matrix 94: +3.73231e-09
	Matrix 95: +2.56597e-09
	Matrix 96: +3.33433e-09
	Matrix 97: +2.52007e-09
	Matrix 98: +2.12496e-09
	Matrix 99: +2.16428e-09
	Matrix 100: +2.35000e-09
	*/

	
	system("pause");
	return 0;
}
