// =================================================================
//
// File: exercise01.cpp
// Author(s): Esteban Padilla Cerdio - A01703068
//            Hilda Olivia Beltrán Acosta - A01251916
// Description: This file contains the code to count the number of
//				even numbers within an array. The time this implementation
//				takes will be used as the basis to calculate the
//				improvement obtained with parallel technologies.
//
// Copyright (c) 2022 by Tecnologico de Monterrey.
// All Rights Reserved. May be reproduced for any non-commercial
// purpose.
//
// =================================================================

#include "utils.h"
#include <algorithm>
#include <climits>
#include <iomanip>
#include <iostream>

const int SIZE = 100000000; // 1e8

using namespace std;

// implement your code here

int main(int argc, char *argv[])
{
	int *a;
	long result = 0;
	double ms;

	a = new int[SIZE];
	fill_array(a, SIZE);
	display_array("a", a);

	cout << "Starting..." << endl;
	ms = 0;
	for (int i = 0; i < N; i++)
	{
		start_timer();

		for (int j = 0; j < SIZE; j++)
		{
			// Sum true (1) when even, false (0) when odd
			result += *(a + i) % 2 == 0;
		}

		ms += stop_timer();
	}
	cout << "result = " << setprecision(5) << result << "\n";
	cout << "avg time = " << setprecision(5) << (ms / N) << " ms" << endl;

	delete[] a;
	return 0;
}
