// =================================================================
//
// File: exercise01.cpp
// Author(s):
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

namespace CST
{
	const int SIZE = 100000000; // 1e9
}

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

using namespace std;

// implement your code here

int main(int argc, char *argv[])
{
	int *a, block_size, i, j;
	double ms, result, *acum;
	Block blocks[THREADS];
	pthread_t tids[THREADS];

	a = new int[CST::SIZE];
	fill_array(a, CST::SIZE);
	display_array("a", a);

	block_size = CST::SIZE / THREADS;
	for (i = 0; i < THREADS; i++)
	{
		blocks[i].arr = a;
		blocks[i].start = i * block_size;
		if (i != (THREADS - 1))
		{
			blocks[i].end = blocks[i].start + block_size;
		}
		else
		{
			blocks[i].end = CST::SIZE;
		}
	}

	cout << "Starting..." << endl;
	ms = 0;
	for (int i = 0; i < NUM; i++)
	{
		start_timer();

		result = 0;
		for (j = 0; j < THREADS; j++)
		{
			pthread_create(&tids[j], NULL, countEven, (void *)&blocks[j]);
		}

		ms += stop_timer();
	}
	cout << "result = " << fixed << setprecision(0) << result << "\n";
	cout << "avg time = " << fixed << setprecision(5) << (ms / NUM) << " ms" << endl;

	delete[] a;
	return 0;
}
