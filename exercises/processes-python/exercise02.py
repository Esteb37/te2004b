# =================================================================
##
# File: exercise02.py
# Author(s): Esteban Padilla Cerdio - A01703068
# 			 Hilda Olivia Beltrán Acosta - A01251916
# Description: This file contains the code that performs the sum of
# all prime numbers less than or equal to MAXIMUM
# using processes in Python.
##
# Copyright (c) 2022 by Tecnologico de Monterrey.
# All Rights Reserved. May be reproduced for any non-commercial
# purpose.
##
# =================================================================

import utils
import time
import multiprocessing as mp
import threading

MAXIMUM = 1000000  # 1e6


def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def partialSumPrime(start, end, queue):
    sum = 0
    for i in range(start, end):
        if isPrime(i):
            sum += i
    queue.put(sum)


if __name__ == "__main__":

    print("Starting...")
    startTime = endTime = ms = 0

    CORES = 10
    blockSize = MAXIMUM // CORES

    for i in range(utils.N):

        startTime = time.time() * 1000

        queue = mp.SimpleQueue()
        processes = list()

        for i in range(CORES):
            start = i * blockSize

            if i != (CORES - 1):
                end = (i + 1) * blockSize
            else:
                end = MAXIMUM
            process = mp.Process(target=partialSumPrime,
                                 args=(start, end, queue,))
            processes.append(process)
            process.start()

        result = 0

        for i in range(CORES):
            result += queue.get()

        endTime = time.time() * 1000

        ms = ms + (endTime - startTime)

    print("sum = ", result)
    print("avg time = ", (ms / utils.N), " ms")
