#include <iostream>
#include <stdio.h>
#include <limits.h>

using namespace std;

// short
static short fiboS(short n)
{
	short a = 0;
	short b = 1;
	short aux;
	for (short i = 0; i < n; i++)
	{
		aux = (a + b);
		a = b;
		b = aux;
	}
	return a;
}

// int
static int fiboI(int n)
{
	int a = 0;
	int b = 1;
	int aux;
	for (int i = 0; i < n; i++)
	{
		aux = a + b;
		a = b;
		b = aux;
	}
	return a;
}

// long
static long fiboL(long n)
{
	long a = 0;
	long b = 1;
	long aux;
	for (long i = 0; i < n; i++)
	{
		aux = (long) a + b;
		a = b;
		b = aux;
	}
	return a;
}

// long long
static long fiboLL(long long n)
{
	long long a = 0;
	long long b = 1;
	long long aux;
	for (long long i = 0; i < n; i++)
	{
		aux = a + b;
		a = b;
		b = aux;
	}
	return a;
}




// OF short
static short overflow_short()
{
	short of = 0;
	for (short i = 0; i < SHRT_MAX; i++)
	{
		//printf("fibonacci de %d: ", i);
		short fibo = fiboS(i);
		//printf("%d\n", fibo);
		if (fibo < 0)
		{
			of = i;
			break;
		}
	}
	return of;
}

// OF int
static int overflow_int()
{
	int of = 0;
	for (int i = 0; i < INT_MAX; i++)
	{
		//printf("fibonacci de %d: ", i);
		int fibo = fiboI(i);
		//printf("%d\n", fibo);
		if (fibo < 0)
		{
			of = i;
			break;
		}
	}
	return of;
}

// OF long
static long overflow_long()
{
	long of = 0;
	for (long i = 0; i < LONG_MAX; i++)
	{
		//printf("fibonacci de %ld: ", i);
		long fibo = fiboL(i);
		//printf("%d\n", fibo);
		if (fibo < 0)
		{
			of = i;
			break;
		}
	}
	return of;
}

// OF long long
static long long overflow_llong()
{
	long long of = 0;
	for (long long i = 0; i < LLONG_MAX; i++)
	{
		//printf("fibonacci de %ld: ", i);
		long long fibo = fiboL(i);
		//printf("%d\n", fibo);
		if (fibo < 0)
		{
			of = i;
			break;
		}
	}
	return of;
}

int main()
{
	short of_short = overflow_short();
	printf("OVERFLOW: short n = %d\n", of_short);

	int of_int = overflow_int();
	printf("OVERFLOW: int n = %d\n", of_int);

	long of_long = overflow_long();
	printf("OVERFLOW: long n = %ld\n", of_long);

	long long of_llong = overflow_llong();
	printf("OVERFLOW: long long n = %ld\n", of_llong);

	/* OUTPUT:
	OVERFLOW: short n = 24
	OVERFLOW: int n = 47
	OVERFLOW: long n = 47
	OVERFLOW: long long n = 47
	*/

	// system("pause"); // Descomentar si se compila usando Visual Studio
	return 0;
}
