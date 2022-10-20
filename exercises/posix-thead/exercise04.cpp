// =================================================================
//
// File: exercise04.cpp
// Author(s): Esteban Padilla Cerdio - A01703068
//            Hilda Olivia Beltrán Acosta - A01251916
// Description: This file implements the PI approximation using the
//				series proposed by Euler using using pthreads.
//              To compile: g++ exercise04.cpp -lpthread
//
// Copyright (c) 2020 by Tecnologico de Monterrey.
// All Rights Reserved. May be reproduced for any non-commercial
// purpose.
//
// =================================================================

#include "utils.h"
#include <cmath>
#include <iomanip>
#include <iostream>
#include <omp.h>
#include <pthread.h>

const int LIMIT = 1000000; // 1e6

using namespace std;

const int THREADS = 20;

// implement your code here

typedef struct
{
	long double start, end; // [start, end)
} Block;

void *calcPI(void *param)
{
	long double *acum;
	Block *block;

	block = (Block *)param;
	acum = new long double;
	(*acum) = 0;
	for (long double i = block->start; i < block->end; i++)
	{
		(*acum) += 1.0 / (i * i);
	}

	return ((void **)acum);
}

int main(int argc, char *argv[])
{
	int block_size, i, j;
	double ms;
	long double result, *acum;
	Block blocks[THREADS];
	pthread_t tids[THREADS];

	block_size = LIMIT / THREADS;

	for (i = 0; i < THREADS; i++)
	{
		blocks[i].start = i * block_size + 1;
		if (i != (THREADS - 1))
		{
			blocks[i].end = (i + 1) * block_size;
		}
		else
		{
			blocks[i].end = LIMIT;
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
			pthread_create(&tids[i], NULL, calcPI, (void *)&blocks[i]);
		}
		for (i = 0; i < THREADS; i++)
		{
			pthread_join(tids[i], (void **)&acum);
			result += (*acum);
			delete acum;
		}

		result = sqrt(6.0 * result);
		ms += stop_timer();
	}

	cout << "result = " << fixed << setprecision(10) << result << "\n";
	cout << "avg time = " << setprecision(5) << (ms / NUM) << " ms" << endl;

	return 0;
}
