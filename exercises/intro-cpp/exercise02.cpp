// =================================================================
//
// File: exercise02.cpp
// Author(s): Esteban Padilla Cerdio - A01703068
//            Hilda Olivia Beltrán Acosta - A01251916
// Description: This file contains the code that performs the sum of
//				all prime numbers less than or equal to MAXIMUM. The
//				time this implementation takes will be used as the
//				basis to calculate the improvement obtained with
//				parallel technologies.
//
// Copyright (c) 2022 by Tecnologico de Monterrey.
// All Rights Reserved. May be reproduced for any non-commercial
// purpose.
//
// =================================================================

#include "utils.h"
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>

#define MAXIMUM 1000000 // 1e6

using namespace std;

// implement your code here

int main(int argc, char *argv[])
{
	int i;
	double ms;

	cout << "Starting..." << endl;
	ms = 0;

	long long result;

	for (int i = 0; i < N; i++)
	{
		start_timer();

		result = 0;

		for (int i = 2; i <= MAXIMUM; i++)
		{
			bool isPrime = true;
			for (int j = 2; j <= sqrt(i); j++)
			{
				if (i % j == 0)
				{
					isPrime = false;
					break;
				}
			}
			if (isPrime)
			{
				result += i;
			}
		}

		ms += stop_timer();
	}

	cout << "result = " << result << "\n";
	cout << "avg time = " << (ms / N) << " ms" << endl;

	return 0;
}
