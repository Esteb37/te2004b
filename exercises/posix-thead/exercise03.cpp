// =================================================================
//
// File: exercise03.cpp
// Author(s): Esteban Padilla Cerdio - A01703068
//            Hilda Olivia Beltrán Acosta - A01251916
// Description: This file contains the code that implements the
//				enumeration sort algorithm using pthreads.
//              To compile: g++ exercise03.cpp -lpthread
//
// Copyright (c) 2020 by Tecnologico de Monterrey.
// All Rights Reserved. May be reproduced for any non-commercial
// purpose.
//
// =================================================================

#include "utils.h"
#include <cstring>
#include <iomanip>
#include <iostream>
#include <omp.h>
#include <pthread.h>

const int A_SIZE = 50000; // 5e4
const int THREADS = 1;

using namespace std;

typedef struct
{
	int start, end; // [start, end)
	int *arr_a, *arr_b;
} Block;

void *enumerationSort(void *param)
{

	Block *block;
	int j, k;

	block = (Block *)param;

	for (j = block->start; j < block->end; j++)
	{

		// Asume it is the biggest
		int count = A_SIZE - 1;

		// Subtract how many elements are bigger than it
		for (int k = 0; k < A_SIZE; k++)
		{
			if (block->arr_a[j] < block->arr_a[k] || (block->arr_a[j] == block->arr_a[k] && j < k))
			{
				count--;
			}
		}

		// Place it in the position according to the count
		block->arr_b[count] = block->arr_a[j];
	}

	return ((void **)block->arr_b);
}

// implement your code here

int main(int argc, char *argv[])
{

	int *a, *b;

	a = new int[A_SIZE];
	b = new int[A_SIZE];

	random_array(a, A_SIZE);
	display_array("before", a);

	int block_size, i, j;

	double ms;
	Block blocks[THREADS];
	pthread_t tids[THREADS];

	block_size = A_SIZE / THREADS;
	for (i = 0; i < THREADS; i++)
	{
		blocks[i].arr_a = a;
		blocks[i].arr_b = b;
		blocks[i].start = i * block_size;
		if (i != (THREADS - 1))
		{
			blocks[i].end = (i + 1) * block_size;
		}
		else
		{
			blocks[i].end = A_SIZE;
		}
	}

	cout << "Starting..." << endl;
	ms = 0;

	for (int j = 0; j < NUM; j++)
	{
		start_timer();

		b = new int[A_SIZE];

		for (i = 0; i < THREADS; i++)
		{
			pthread_create(&tids[i], NULL, enumerationSort, (void *)&blocks[i]);
		}

		for (i = 0; i < THREADS; i++)
		{
			pthread_join(tids[i], (void **)&b);
		}

		ms += stop_timer();

		if (j != NUM - 1)
		{
			delete[] b;
		}
	}

	display_array("after", b);

	cout << "avg time = " << fixed << setprecision(5) << (ms / NUM) << " ms" << endl;

	delete[] a;
	delete[] b;
	return 0;
}
