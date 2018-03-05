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

	
	/* OUTPUT:
	Matrix 2: +0.00000e+00
	Matrix 3: +0.00000e+00
	Matrix 4: +7.81250e-07
	Matrix 5: +0.00000e+00
	Matrix 6: +0.00000e+00
	Matrix 7: +0.00000e+00
	Matrix 8: +0.00000e+00
	Matrix 9: +0.00000e+00
	Matrix 10: +0.00000e+00
	Matrix 11: +3.75657e-08
	Matrix 12: +0.00000e+00
	Matrix 13: +0.00000e+00
	Matrix 14: +0.00000e+00
	Matrix 15: +1.48148e-08
	Matrix 16: +0.00000e+00
	Matrix 17: +0.00000e+00
	Matrix 18: +8.57339e-09
	Matrix 19: +0.00000e+00
	Matrix 20: +6.25000e-09
	Matrix 21: +0.00000e+00
	Matrix 22: +0.00000e+00
	Matrix 23: +4.10948e-09
	Matrix 24: +3.61690e-09
	Matrix 25: +3.20000e-09
	Matrix 26: +2.84479e-09
	Matrix 27: +2.54026e-09
	Matrix 28: +2.27770e-09
	Matrix 29: +2.05010e-09
	Matrix 30: +3.70370e-09
	Matrix 31: +3.35672e-09
	Matrix 32: +3.05176e-09
	Matrix 33: +2.78265e-09
	Matrix 34: +2.54427e-09
	Matrix 35: +2.33236e-09
	Matrix 36: +3.21502e-09
	Matrix 37: +2.96133e-09
	Matrix 38: +2.73363e-09
	Matrix 39: +2.52870e-09
	Matrix 40: +1.56250e-09
	Matrix 41: +2.17640e-09
	Matrix 42: +2.02462e-09
	Matrix 43: +1.88663e-09
	Matrix 44: +2.34786e-09
	Matrix 45: +2.19479e-09
	Matrix 46: +2.56842e-09
	Matrix 47: +2.40794e-09
	Matrix 48: +2.26056e-09
	Matrix 49: +2.12496e-09
	Matrix 50: +2.40000e-09
	Matrix 51: +2.26157e-09
	Matrix 52: +2.48919e-09
	Matrix 53: +2.68678e-09
	Matrix 54: +2.22273e-09
	Matrix 55: +2.40421e-09
	Matrix 56: +2.27770e-09
	Matrix 57: +2.42990e-09
	Matrix 58: +3.84395e-09
	Matrix 59: +2.67798e-09
	Matrix 60: +2.31481e-09
	Matrix 61: +2.42311e-09
	Matrix 62: +3.56651e-09
	Matrix 63: +2.19959e-09
	Matrix 64: +2.47955e-09
	Matrix 65: +2.18480e-09
	Matrix 66: +2.43482e-09
	Matrix 67: +2.32741e-09
	Matrix 68: +2.38525e-09
	Matrix 69: +2.28304e-09
	Matrix 70: +2.33236e-09
	Matrix 71: +4.19099e-09
	Matrix 72: +3.48294e-09
	Matrix 73: +2.31352e-09
	Matrix 74: +2.22099e-09
	Matrix 75: +3.55556e-09
	Matrix 76: +3.75875e-09
	Matrix 77: +2.95707e-09
	Matrix 78: +4.74131e-09
	Matrix 79: +2.43388e-09
	Matrix 80: +2.63672e-09
	Matrix 81: +3.66927e-09
	Matrix 82: +2.81119e-09
	Matrix 83: +2.18613e-09
	Matrix 84: +2.36206e-09
	Matrix 85: +3.90800e-09
	Matrix 86: +2.51550e-09
	Matrix 87: +3.64463e-09
	Matrix 88: +2.78808e-09
	Matrix 89: +2.41145e-09
	Matrix 90: +3.90947e-09
	Matrix 91: +2.38863e-09
	Matrix 92: +2.44000e-09
	Matrix 93: +2.05133e-09
	Matrix 94: +2.10695e-09
	Matrix 95: +2.15775e-09
	Matrix 96: +2.14753e-09
	Matrix 97: +2.41050e-09
	Matrix 98: +3.34682e-09
	Matrix 99: +2.11275e-09
	Matrix 100: +2.20000e-09
	*/
	
	// system("pause");	// Descomentar si se compila en Visual Studio
	return 0;
}
