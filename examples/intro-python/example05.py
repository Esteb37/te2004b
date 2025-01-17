## =================================================================
##
## File: example05.py
## Author: Pedro Perez
## Description: This file contains the code that implements the
##				bubble sort algorithm. The time this implementation takes
##				will be used as the basis to calculate the improvement
##				obtained with parallel technologies.
##
## Copyright (c) 2022 by Tecnologico de Monterrey.
## All Rights Reserved. May be reproduced for any non-commercial
## purpose.
##
## =================================================================
import utils
import time

SIZE = 10000 ##1e4

def swap(array, i, j):
    aux = array[i]
    array[i] = array[j]
    array[j] = aux

def oddEvenSort(array):
	aux = array.copy()
	for step in range(len(aux)):
		if step % 2 == 0:
			for i in range (0, len(aux) - 1, 2):
				if aux[i] > aux[i + 1]:
					swap(aux, i, i + 1)
		else:
			for i in range (1, len(aux) - 1, 2):
				if aux[i] > aux[i + 1]:
					swap(aux, i, i + 1)
	return aux


if __name__ == "__main__":
    array = [0] * SIZE

    utils.randomArray(array)
    utils.displayArray("array", array)

    print("Starting...")
    startTime = endTime = ms = 0
    for i in range(utils.N):
        startTime = time.time() * 1000

        result = oddEvenSort(array)

        endTime = time.time() * 1000

        ms = ms + (endTime - startTime)

    utils.displayArray("array", result)
    print("avg time = ", (ms / utils.N), " ms")