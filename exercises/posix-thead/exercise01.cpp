// =================================================================
//
// File: exercise01.cpp
// Author(s): Esteban Padilla Cerdio - A01703068
//            Hilda Olivia Beltrán Acosta - A01251916
// Description: This file contains the code to count the number of
//				even numbers within an array using pthreads.
//              To compile: g++ exercise01.cpp -lpthread
//
// Copyright (c) 2020 by Tecnologico de Monterrey.
// All Rights Reserved. May be reproduced for any non-commercial
// purpose.
//
// =================================================================

#include "utils.h"
#include <algorithm>
#include <climits>
#include <iomanip>
#include <iostream>
#include <omp.h>
#include <pthread.h>

using namespace std;

// Se cambió el nombre de la variable porque SIZE ya existe en pthread
const int A_SIZE = 100000000; // 1e9
const int THREADS = 4;

typedef struct
{
	int start, end; // [start, end)
	int *arr;
} Block;

void *countEven(void *param)
{
	int *acum;
	Block *block;
	int i;

	block = (Block *)param;
	acum = new int;
	(*acum) = 0;
	for (i = block->start; i < block->end; i++)
	{
		if (block->arr[i] % 2 == 0)
		{
			(*acum)++;
		}
	}
	return ((void **)acum);
}

// implement your code here

int main(int argc, char *argv[])
{
	int *a, block_size, i, j, result, *acum;
	;
	double ms;
	Block blocks[THREADS];
	pthread_t tids[THREADS];

	a = new int[A_SIZE];
	fill_array(a, A_SIZE);
	display_array("a", a);

	block_size = A_SIZE / THREADS;
	for (i = 0; i < THREADS; i++)
	{
		blocks[i].arr = a;
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
	for (j = 0; j < NUM; j++)
	{
		start_timer();

		result = 0;
		for (i = 0; i < THREADS; i++)
		{
			pthread_create(&tids[i], NULL, countEven, (void *)&blocks[i]);
		}
		for (i = 0; i < THREADS; i++)
		{
			pthread_join(tids[i], (void **)&acum);
			result += (*acum);
			delete acum;
		}

		ms += stop_timer();
	}

	cout << "result = " << fixed << setprecision(0) << result << "\n";
	cout << "avg time = " << fixed << setprecision(5) << (ms / NUM) << " ms" << endl;

	delete[] a;
	return 0;
}
