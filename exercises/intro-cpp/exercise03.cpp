// =================================================================
//
// File: exercise03.cpp
// Author(s): Esteban Padilla Cerdio - A01703068
//            Hilda Olivia Beltrán Acosta - A01251916
// Description: This file contains the code that implements the
//				enumeration sort algorithm. The time this implementation
//				takes ill be used as the basis to calculate the
//				improvement obtained with parallel technologies.
//
// Copyright (c) 2022 by Tecnologico de Monterrey.
// All Rights Reserved. May be reproduced for any non-commercial
// purpose.
//
// =================================================================

#include "utils.h"
#include <cstring>
#include <iomanip>
#include <iostream>

const int SIZE = 10000; // 1e4

using namespace std;

// implement your code here

int main(int argc, char *argv[])
{
	int *a, *b;
	double ms;

	a = new int[SIZE];
	b = new int[SIZE];

	random_array(a, SIZE);
	display_array("before", a);

	cout << "Starting..." << endl;
	ms = 0;

	for (int i = 0; i < N; i++)
	{
		start_timer();

		// For each element in the array
		for (int j = 0; j < SIZE; j++)
		{
			// Asume it is the biggest
			int count = SIZE - 1;

			// Subtract how many elements are bigger than it
			for (int k = 0; k < SIZE; k++)
			{
				if (a[j] < a[k] || (a[j] == a[k] && j < k))
				{
					count--;
				}
			}

			// Place it in the position according to the count
			b[count] = a[j];
		}

		ms += stop_timer();
	}

	display_array("after", b);

	// Check that the array is sorted
	bool sorted = true;
	for (int i = 0; i < SIZE - 1; i++)
	{
		if (b[i] > b[i + 1])
		{
			sorted = false;
			break;
		}
	}

	if (sorted)
	{
		cout << "The array is sorted" << endl;
	}
	else
	{
		cout << "The array is not sorted" << endl;
	}

	cout << "avg time = " << setprecision(5) << (ms / N) << " ms" << endl;

	delete[] a;
	delete[] b;
	return 0;
}
