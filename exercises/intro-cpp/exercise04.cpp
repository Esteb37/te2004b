// =================================================================
//
// File: exercise04.cpp
// Author(s): Esteban Padilla Cerdio - A01703068
//            Hilda Olivia Beltrán Acosta - A01251916
// Description: This file implements the PI approximation using the
//				series proposed by Euler.
//				pi = sqrt ( 6 * sumatoria(i = 1-N) (1 / i^2) )
//				The time this implementation takes will be used as
//				the basis to calculate the improvement obtained with
//				parallel technologies.
//
// Copyright (c) 2022 by Tecnologico de Monterrey.
// All Rights Reserved. May be reproduced for any non-commercial
// purpose.
//
// =================================================================

#include "utils.h"
#include <cmath>
#include <iomanip>
#include <iostream>

const int LIMIT = 1000000; // 1e6

using namespace std;

// implement your code here

int main(int argc, char *argv[])
{
	long double result;
	double ms;

	cout << "Starting..." << endl;
	ms = 0;
	for (int i = 0; i < N; i++)
	{
		start_timer();

		result = 0;

		// pi = sqrt ( 6 * sum(i = 1-N) (1 / i^2) )
		for (long long j = 1; j <= LIMIT; j++)
		{
			result += 1.0 / (j * j);
		}

		result = sqrt(6 * result);

		ms += stop_timer();
	}
<<<<<<< HEAD
	cout << "result = " << setprecision(10) << result << "\n";
	cout << "avg time = " << setprecision(10) << (ms / N) << " ms" << endl;
	== == == =
				 cout << "result = " << fixed << setprecision(10) << result << "\n";
	cout << "avg time = " << setprecision(5) << (ms / N) << " ms" << endl;
>>>>>>> 7518a1397c1d2682a3780a9d66fad3a64f4d9ff8

	return 0;
}
