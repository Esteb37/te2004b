// =================================================================
//
// File: exercise02.cpp
// Author(s):
// Description: This file contains the code that performs the sum of
//				all prime numbers less than or equal to MAXIMUM using
//				pthreads.
//              To compile: g++ exercise02.cpp -lpthread
//
// Copyright (c) 2020 by Tecnologico de Monterrey.
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
#include <omp.h>
#include <pthread.h>

#define MAXIMUM 1000000 // 1e6

using namespace std;

const int THREADS = 4;

typedef struct
{
	int start, end; // [start, end)
} Block;

void *sumPrimes(void *param)
{
	int *acum;
	Block *block;
	int i, j, limit;

	block = (Block *)param;
	acum = new int;
	(*acum) = 0;
	for (i = block->start; i < block->end; i++)
	{
		limit = (int)sqrt(i);
		for (j = 2; j <= limit; j++)
		{
			if (i % j == 0)
			{
				break;
			}
		}
		if (j > limit)
		{
			(*acum) += i;
		}
	}
	return ((void **)acum);
}

int main(int argc, char *argv[])
{
	int block_size, i, j;
	double ms, result, *acum;
	Block blocks[THREADS];
	pthread_t tids[THREADS];

	cout << "Starting..." << endl;
	ms = 0;

	block_size = MAXIMUM / THREADS;

	for (i = 0; i < THREADS; i++)
	{
		blocks[i].start = i * block_size;
		if (i != (THREADS - 1))
		{
			blocks[i].end = blocks[i].start + block_size;
		}
		else
		{
			blocks[i].end = MAXIMUM;
		}
	}

	for (int i = 0; i < NUM; i++)
	{
		start_timer();

		result = 0;
		for (j = 0; j < THREADS; j++)
		{
			pthread_create(&tids[j], NULL, sumPrimes, (void *)&blocks[j]);
		}

		ms += stop_timer();
	}
	cout << "result = " << fixed << setprecision(0) << result << "\n";
	cout << "avg time = " << fixed << setprecision(5) << (ms / NUM) << " ms" << endl;

	return 0;
}
