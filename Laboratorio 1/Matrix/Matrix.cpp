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
	Matrix 2: +3.12500e-08
	Matrix 3: +5.55556e-09
	Matrix 4: +3.90625e-09
	Matrix 5: +2.80000e-09
	Matrix 6: +1.62037e-09
	Matrix 7: +1.02041e-09
	Matrix 8: +1.07422e-09
	Matrix 9: +8.91632e-10
	Matrix 10: +1.05000e-09
	Matrix 11: +8.26446e-10
	Matrix 12: +7.52315e-10
	Matrix 13: +6.82749e-10
	Matrix 14: +6.92420e-10
	Matrix 15: +6.51852e-10
	Matrix 16: +6.22559e-10
	Matrix 17: +6.30979e-10
	Matrix 18: +6.00137e-10
	Matrix 19: +5.75886e-10
	Matrix 20: +5.68750e-10
	Matrix 21: +5.66893e-10
	Matrix 22: +5.58790e-10
	Matrix 23: +5.46560e-10
	Matrix 24: +5.49769e-10
	Matrix 25: +5.98400e-10
	Matrix 26: +5.09217e-10
	Matrix 27: +5.15673e-10
	Matrix 28: +5.10204e-10
	Matrix 29: +5.16626e-10
	Matrix 30: +5.05556e-10
	Matrix 31: +4.96794e-10
	Matrix 32: +4.92859e-10
	Matrix 33: +4.92529e-10
	Matrix 34: +4.92316e-10
	Matrix 35: +6.09913e-10
	Matrix 36: +5.25120e-10
	Matrix 37: +5.27116e-10
	Matrix 38: +5.32148e-10
	Matrix 39: +5.29341e-10
	Matrix 40: +5.55469e-10
	Matrix 41: +4.81711e-10
	Matrix 42: +5.44623e-10
	Matrix 43: +4.75430e-10
	Matrix 44: +5.08898e-10
	Matrix 45: +5.10288e-10
	Matrix 46: +5.06493e-10
	Matrix 47: +5.36972e-10
	Matrix 48: +5.17216e-10
	Matrix 49: +5.12967e-10
	Matrix 50: +5.16800e-10
	Matrix 51: +5.02823e-10
	Matrix 52: +5.11706e-10
	Matrix 53: +5.13511e-10
	Matrix 54: +5.04877e-10
	Matrix 55: +5.02780e-10
	Matrix 56: +4.88851e-10
	Matrix 57: +4.83010e-10
	Matrix 58: +4.81006e-10
	Matrix 59: +4.84227e-10
	Matrix 60: +4.83796e-10
	Matrix 61: +4.81979e-10
	Matrix 62: +4.69521e-10
	Matrix 63: +4.58314e-10
	Matrix 64: +4.56238e-10
	Matrix 65: +4.56805e-10
	Matrix 66: +4.54963e-10
	Matrix 67: +4.42209e-10
	Matrix 68: +4.37774e-10
	Matrix 69: +4.38192e-10
	Matrix 70: +4.37026e-10
	Matrix 71: +4.27341e-10
	Matrix 72: +4.21436e-10
	Matrix 73: +4.21190e-10
	Matrix 74: +4.20508e-10
	Matrix 75: +4.10904e-10
	Matrix 76: +4.10273e-10
	Matrix 77: +4.09280e-10
	Matrix 78: +3.99535e-10
	Matrix 79: +3.92464e-10
	Matrix 80: +3.91895e-10
	Matrix 81: +3.83392e-10
	Matrix 82: +3.79057e-10
	Matrix 83: +3.78725e-10
	Matrix 84: +3.69746e-10
	Matrix 85: +3.31447e-10
	Matrix 86: +3.44073e-10
	Matrix 87: +3.31661e-10
	Matrix 88: +3.30388e-10
	Matrix 89: +3.43774e-10
	Matrix 90: +3.40809e-10
	Matrix 91: +3.35536e-10
	Matrix 92: +3.32418e-10
	Matrix 93: +3.32937e-10
	Matrix 94: +3.28203e-10
	Matrix 95: +3.19172e-10
	Matrix 96: +3.18852e-10
	Matrix 97: +3.19720e-10
	Matrix 98: +3.18107e-10
	Matrix 99: +3.18871e-10
	Matrix 100: +3.21000e-10
	*/

	
	// system("pause"); // Descomentar si se compila en Visual Studio
	return 0;
}
